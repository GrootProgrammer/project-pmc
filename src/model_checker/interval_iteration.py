#!/bin/python
from enum import Enum
from collections import deque
from utils import list_to_string
from model import *
from errors import *
from fractions import Fraction
from decimal import Decimal
import logging,copy,time
import math
logger = logging.getLogger(__name__)

class Interval_Iteration():
    def __init__(self, 
                 model:Model,
                 epsilon:float=None):
        self.model = model
        self.mdp=model.mdp
        self.transition_labels=model.transition_labels
        self.init_state=model.init_state
        self.target_states=model.target_states
        self.properties=model.properties
        self.s_plus=None
        self.s_minus=None
        if epsilon is not None:
            self.epsilon=epsilon
        else:
            self.epsilon=self.compute_epsilon_alpha()            

    def find_largest_denominator(self, mdp):
        probabilities = set()
        for _, transitions in mdp.items():
            for _, t_branches in transitions.items():
                for _, prob in t_branches.items():
                    probabilities.add(str(prob))
        d=[Fraction(Decimal(str(prob))).limit_denominator(100000).denominator for prob in probabilities]
        return max(d)
        
    
    def compute_epsilon_alpha(self):
        """
        Find the stopping threshold based on theorem 3
        """
        d = self.find_largest_denominator(self.mdp)
        n = len(self.mdp)
        
        # Compute ln(α) using the bound
        ln_alpha = n * math.log(n) + 3 * n**2 * math.log(d)
        
        # ε = 1/(2α) = exp(-ln(2α))
        ln_2alpha = math.log(2) + ln_alpha
        epsilon = math.exp(-ln_2alpha)
        return  epsilon
    
    def set_state_default(self, 
                          state, 
                          location: str):
        variables=self.model.network.Network().variables
        var_dict={}
        var_count={}
        for variable in variables:
            if variable.name in var_count.keys():
                name=f"{variable.name}_{var_count[variable.name]}"
                var_count[variable.name]+=1
            else:
                name=variable.name
                var_count[variable.name]=1
            var_dict[name]=variable.type
        svar=state.__slots__
        for var in svar:
            if var_dict[var] == "bool":
                state.__setattr__(var,False) # Does not matter because the algo will not use this field
            elif  var_dict[var] in ["int","real"]:
                state.__setattr__(var,0)
        state.__setattr__(svar[-1],location)
        return state
    
    def compute_s_plus(self,
                       mdp,
                       target_states):
        """
        Merge all target states to s_plus, an absorbing state.
        """
        if len(self.target_states)<1:
            return 
        s_plus=self.model.network.State()
        s_plus=self.set_state_default(s_plus,"s_plus")
        self.s_plus=s_plus
        mdp[s_plus]={
            "loop_plus":{s_plus:1}
        }
        return self.merge_states(mdp,s_plus,target_states)

    def merge_states(self, 
                     mdp,
                     new_state, 
                     states_to_merge):
        """
        Merge given states to a new_state, an absorbing state.
        """
        if self.init_state in states_to_merge:
            self.init_state = new_state
        merged_mdp={}
        for state,transitions in mdp.items():
            if state in states_to_merge:
                continue
            transitions_merged={}
            for t_label, t_branches in transitions.items():
                t_branches_merged={}
                t_branch_plus_prob=0
                for t_target, t_probability in t_branches.items():
                    if t_target in states_to_merge:
                        t_branch_plus_prob+=t_probability
                    else:
                        t_branches_merged[t_target]=t_probability
                if t_branch_plus_prob>0:
                    t_branches_merged[new_state]=t_branch_plus_prob
                transitions_merged[t_label]=t_branches_merged
            merged_mdp[state]=transitions_merged
        return merged_mdp
    
    def compute_mec(self, mdp):
        """
        Compute MECs of an MDP
        """
        logger.info("Computing MEC")
        sm=[]
        stack=[mdp]
        logger.debug(f"- Initial stack: [{list_to_string(stack[0])}]")

        while stack:
            sub_mdp=stack.pop()
            sub_mdp_locations=[s for s in sub_mdp.keys()]
            logger.debug(f"- Sub MDP: [{list_to_string(sub_mdp)}]")

            processed_sub_mdp={}
            transition_matrix={s:[] for s in sub_mdp_locations}
            for state,transitions in sub_mdp.items():
                processed_neighbors=set()
                processed_sub_mdp[state]={}
                for t_label,t_branches in transitions.items():
                    t_neighbors=set()
                    to_remove=False
                    for target,probability in t_branches.items():
                        if probability > 0 and not target in sub_mdp_locations:
                            to_remove=True
                            break
                        t_neighbors.add(target)
                    if to_remove:
                        # del processed_sub_mdp[state][t_label]
                        pass
                    else:
                        processed_sub_mdp[state][t_label]=t_branches
                        processed_neighbors.update(t_neighbors)
                    
                transition_matrix[state]=list(processed_neighbors)
                
            sccs=self.compute_scc(transition_matrix)

            logger.debug(f"- No. sccs: {len(sccs)}")
            if len(sccs)>1:
                for i in range(len(sccs)):
                    stack.append(
                        {
                            s: processed_sub_mdp[s]
                            for s in sccs[i]
                        }
                    )
            else:
                sm.append({
                            s: processed_sub_mdp[s]
                            for s in sccs[0]
                        })
        return sm
      
    def compute_scc(self,graph):
        """
        Compute Strongly connected component using Tarjan's algorithm
        """
        index = 0
        indices = {}
        lowlinks = {}
        on_stack = set()
        stack = []
        sccs = []
        
        def strongconnect(location: int):
            nonlocal index
            indices[location] = index
            lowlinks[location] = index
            index += 1
            stack.append(location)
            on_stack.add(location)
            
            for w in graph[location]:
                if w not in indices:
                    strongconnect(w)
                    lowlinks[location] = min(lowlinks[location], lowlinks[w])
                elif w in on_stack:
                    lowlinks[location] = min(lowlinks[location], indices[w])
            
            if lowlinks[location] == indices[location]:
                scc = []
                while True:
                    w = stack.pop()
                    on_stack.remove(w)
                    scc.append(w)
                    if w == location:
                        break
                sccs.append(set(scc))
        
        for location in graph.keys():
            if location not in indices:
                strongconnect(location)
        return sccs

    def is_trivial_mec(self, mec):
        """
        Validate if a mec is trivial
        """
        if len(mec) > 1:
            return False
        has_actions=False
        for state, transitions in mec.items():
            if len(transitions)>0:
                has_actions=True
        return not has_actions
    
    def is_bottom_mec(self, 
                      mdp,
                      mec):
        """
        Validate if a mec is bmec
        """
        has_out_going_action=False
        for state, mec_transitions in mec:
            full_transition_labels=set([t for t in mdp[state].keys()])
            mec_transition_labels=set([t for t in mec_transitions.keys()])
            if full_transition_labels != mec_transition_labels:
                has_out_going_action=True
                break
        return not has_out_going_action
    
    def reduce_min(self, 
                   mdp, 
                   mecs):
        """
        Keep trivial mecs
        Merge all non-trivial other than ({s+},{loop+}) to s_.
        """
        to_merge=set()
        for mec in mecs:
            if self.s_plus in mec.keys():
                # s_plus is always in a separate mec with 1 state.
                continue
            if not self.is_trivial_mec(mec):
                to_merge.update([s for s in mec.keys()])
        if len(to_merge)>0:
            s_minus=self.model.network.State()
            s_minus=self.set_state_default(s_minus,"s_minus")
            self.s_minus=s_minus
            mdp[s_minus]={"loop_minus":{s_minus:1}}
            return self.merge_states(mdp,s_minus,to_merge)
        return mdp

    def compute_action_probability(self, 
                                   mdp,
                                   state,
                                   action,
                                   current_prob):
        """
        Compute the new probability of a state when taking an "action" 
        """
        new_probability=0
        for target, prob in mdp[state][action].items():
            new_probability+=prob*current_prob[target]
        return new_probability

    def compute_reachability_min(self, 
                                 target_states):
        """
        Compute minimum reachability 
        """
        # Find target states
        if len(target_states)<1:
            return (0.0,0.0),0
        
        # Compute s+
        s_plus_mdp=self.compute_s_plus(self.mdp,target_states)

        # Compute MECs
        mecs=self.compute_mec(s_plus_mdp)
        
        # Reduce Min
        reduced_mdp=self.reduce_min(s_plus_mdp,mecs)

        # Compute probability
        x = {s:0 for s in reduced_mdp.keys()}
        y = {s:1 for s in reduced_mdp.keys()}

        x[self.s_plus]=1
        y[self.s_plus]=1
        if self.s_minus:
            x[self.s_minus]=0
            y[self.s_minus]=0

        delta=math.inf
        full_states=set([s for s in reduced_mdp.keys()])
        states_to_traverse=full_states-{self.s_plus,self.s_minus}
        n_iter=0
        while delta > self.epsilon:
            n_iter+=1
            x_new=y_new={self.s_plus:1}
            if self.s_minus:
                x_new[self.s_minus]=y_new[self.s_minus]=0
            for s in states_to_traverse:
                x_new[s]=min([
                    self.compute_action_probability(reduced_mdp,s,action,x)
                    for action in reduced_mdp[s].keys()
                ])
                y_new[s]=min([
                    self.compute_action_probability(reduced_mdp,s,action,y)
                    for action in reduced_mdp[s].keys()
                ])
            delta=max([y_new[s]-x_new[s] for s in full_states])
            x=x_new
            y=y_new
        return (x[self.init_state], y[self.init_state]),n_iter

    def collapse_mec(self, 
                     mdp,
                     mec, 
                     new_location):
        """
        Collapse a mec to a single state keeping only out going actions
        Redirect all incoming action to the merged state
        """
        s_k=self.model.network.State()
        s_k=self.set_state_default(s_k,new_location)

        #Extract transitions for the new states
        s_k_transitions={}
        has_out_going_action=0
        for state, mec_transitions in mec.items():
            full_transition_labels=set([t for t in mdp[state].keys()])
            mec_transition_labels=set([t for t in mec_transitions.keys()])
            out_going_actions=full_transition_labels-mec_transition_labels
            has_out_going_action=max(has_out_going_action,int(len(out_going_actions)>0))
            for action in out_going_actions:
                action_transitions=mdp[state][action]
                if action in s_k_transitions.keys():
                    s_k_action_transitions=s_k_transitions[action]
                    for target,probability in action_transitions.items():
                        if target in mec.keys():
                            target=s_k
                        if target in s_k_action_transitions.keys():
                            s_k_action_transitions[target]+=probability
                        else:
                            s_k_action_transitions[target]=probability
                else:
                    s_k_action_transitions={}
                    for target,probability in action_transitions.items():
                        if target in mec.keys():
                            target=s_k
                        s_k_action_transitions[target]=probability
                s_k_transitions[action]=s_k_action_transitions
        mdp[s_k]=s_k_transitions
        # Redirect actions to the new states
        mdp=self.merge_states(mdp,s_k,set([s for s in mec.keys()]))
        return mdp,s_k,has_out_going_action==0

    def reduce_max(self, 
                   mdp,
                   mecs):
        """
        Keep trivial mecs
        Collapse each non-trivial non-bottom mec to a single state keeping only out going actions
        Merge all non-trivial bottom mecs other than ({s+},{loop+}) to s_ 
        """
        to_merge=set()
        counter=0
        for mec in mecs:
            if self.s_plus in mec.keys():
                # s_plus is always in a separate mec with 1 state.
                continue
            if self.is_trivial_mec(mec):
                only_state=[k for k in mec.keys()][0]
                if len(mdp[only_state])>0:
                    continue
            new_location=f"k{counter}"
            counter+=1
            mdp,s_k,is_bmec=self.collapse_mec(mdp,mec,new_location)
            if is_bmec:
                to_merge.add(s_k)

        if len(to_merge)>0:
            s_minus=self.model.network.State()
            s_minus=self.set_state_default(s_minus,"s_minus")
            self.s_minus=s_minus
            mdp[s_minus]={"loop_minus":{s_minus:1}}
            return self.merge_states(mdp,s_minus,to_merge)
        return mdp
        
    def compute_reachability_max(self, target_states):
        """
        Compute maximum reachability loop
        """
        # Find target states
        if len(target_states)<1:
            return (0.0,0.0),0
        
        # Compute s+
        s_plus_mdp=self.compute_s_plus(self.mdp, target_states)

        # Compute MECs
        mecs=self.compute_mec(s_plus_mdp)
        
        # Reduce Max
        reduced_mdp=self.reduce_max(s_plus_mdp,mecs)

        # Compute probability
        (x,y),n_iter=self.compute_reachability_max_main(reduced_mdp)
        return (x[self.init_state], y[self.init_state]),n_iter

    def compute_reachability_max_main(self,
                                     mdp):
        # Compute probability
        x = {s:0 for s in mdp.keys()}
        y = {s:1 for s in mdp.keys()}

        x[self.s_plus]=1
        y[self.s_plus]=1
        if self.s_minus:
            x[self.s_minus]=0
            y[self.s_minus]=0

        delta=math.inf
        full_states=set([s for s in mdp.keys()])
        states_to_traverse=full_states-{self.s_plus,self.s_minus}
        n_iter=0
        init=[(x[self.init_state],y[self.init_state])]
        while delta > self.epsilon:
            n_iter+=1
            x_new = {}
            y_new = {}
            x_new[self.s_plus] = 1
            y_new[self.s_plus] = 1
            if self.s_minus:
                x_new[self.s_minus]=0
                y_new[self.s_minus]=0
            for s in states_to_traverse:
                if len(mdp[s])==0:
                    x_new[s]=0
                    y_new[s]=0
                else:
                    x_new[s]=max([
                        self.compute_action_probability(mdp,s,action,x)
                        for action in mdp[s].keys()
                    ])
                    y_new[s]=max([
                        self.compute_action_probability(mdp,s,action,y)
                        for action in mdp[s].keys()
                    ])
            delta=max([y_new[s]-x_new[s] for s in full_states])
            x=x_new
            y=y_new
        return (x, y),n_iter
    
    def compute(self):
        """
        Compute reachability/reward
        """
        result={}
        for i in range(len(self.properties)):
            property=self.properties[i]
            property_type=property.exp.op
            start = time.time()
            from program import PropertyResult
            try:
                #print(f"Processing {i+1}/{len(self.properties)} propertie(s): {property.name} {property_type}")
                if property_type == PropertyType.p_min.value:
                    bounds,n_iter=self.compute_reachability_min(self.target_states[i])
                elif property_type == PropertyType.p_max.value:
                    bounds,n_iter=self.compute_reachability_max(self.target_states[i])
                else:
                    continue
                exact_value=(bounds[0]+bounds[1])/2
                result[property.name]=PropertyResult(PropertyResultType.FLOAT, exact_value, time.time()-start)
            except Exception as e:
                result[property.name]=PropertyResult(PropertyResultType.ERROR, None, time.time()-start)
                continue
            # result[property.name]={
            #     "type":property_type,
            #     "bounds":bounds,
            #     "exact": exact_value,
            #     "epsilon":self.epsilon,
            #     "n_iterations":n_iter
            # }
        #print("-"*20)
        return result