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

class GS_Value_Iteration():
    def __init__(self, 
                 model:Model,
                 epsilon:float,
                 max_iter:int=10000):
        self.model = model
        self.mdp=model.mdp
        self.transition_labels=model.transition_labels
        self.init_state=model.init_state
        self.target_states=model.target_states
        self.properties=model.properties
        self.epsilon=epsilon
        self.max_iter=max_iter
    
    def compute_S0_min(self, 
                       mdp,
                       target_states):
        r=target_states
        r_prime=set()
        while r!=r_prime:
            r_prime=r
            to_add=set()
            for s,transitions in mdp.items():
                # s ∈ S | ∀a ∈ A(s).( ∃s′ ∈ R′. δM(s, a)(s′)>0) 
                count=0
                for _, tbranches in transitions.items():
                    exists=False
                    for target, prob in tbranches.items():
                        if target in r_prime:
                            exists=True
                            break 
                    if exists:
                        count+=1
                if count==len(transitions):
                    to_add.add(s)
            r=r_prime.union(to_add)
        return set([k for k in mdp.keys()])-r

    def compute_S1_min(self, 
                       mdp,
                       s0_min):
        s=set([k for k in mdp.keys()])
        r=s-s0_min
        r_prime=set()
        while r!=r_prime:
            r_prime=r
            to_exclude=set()
            #  s ∈ R′ | ∃a ∈ A(s). ∃s′ ∈ S. ( δM(s, a)(s′)>0 ∧ s′ ̸∈ R′ ) 
            for s in r_prime:
                transitions=mdp[s]
                exists=False
                for _, tbranches in transitions.items():
                    for target, prob in tbranches.items():
                        if not(target in r_prime):
                            exists=True
                            break 
                if exists:
                    to_exclude.add(s)
            r=r_prime-to_exclude
        return r

    def compute_S0_max(self, 
                       mdp,
                       target_states):
        r=target_states
        r_prime=set()

        while r!=r_prime:
            r_prime=r
            
            to_add=set()
            # s ∈ S | ∃a ∈ A(s).( ∃s′ ∈ R′. δM(s, a)(s′)>0) 
            for s,transitions in mdp.items():
                exists=False
                for _, tbranches in transitions.items():
                    for target, prob in tbranches.items():
                        if target in r_prime:
                            exists=True
                            break 
                if exists:
                    to_add.add(s)
            r=r_prime.union(to_add)
        return set([k for k in mdp.keys()])-r
    
    def compute_S1_max(self, 
                       mdp,
                       target_states):
        r=set([s for s in mdp.keys()])
        r_prime=set()
        while r!=r_prime:
            r_prime=r
            r=target_states
            r_prime_2=set()
            while r!=r_prime_2:
                r_prime_2=r
                to_add=set()
                # s ∈ S | ∃a ∈ A(s). (∀s′ ∈ S. ( δM(s, a)(s′)>0 → s′ ∈ R′ )) ∧ (∃s′ ∈ R′′. δM(s, a)(s′)>0) ;
                for s,transitions in mdp.items():
                    exists=False
                    for _,branches in transitions.items():
                        p1=1
                        p2=0
                        for target,_ in branches.items():
                            if not target in r_prime:
                                p1=min(p1,0)
                            if target in r_prime_2:
                                p2=max(p2,1)
                        exists = (p1==1) and (p2==1)
                    if exists:
                        to_add.add(s)
                r=r_prime_2.union(to_add)                        
        return r    

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

    def compute_reachability_main(self,
                            mdp,
                            s0,
                            s1,
                            op):
        x={}
        for s in mdp.keys():
            if s in s1:
                x[s]=1
            else:
                x[s]=0
        delta=math.inf
        to_traverse=set([s for s in mdp.keys()])-(s0.union(s1))
        n_iter=0
        while delta > self.epsilon and n_iter<self.max_iter:
            n_iter+=1
            delta=0
            for s in to_traverse:
                x_s_potentials=[
                    self.compute_action_probability(mdp,s,action,x)
                    for action in mdp[s].keys()
                ]
                if op == "p_max":
                    x_s_new=max(x_s_potentials)
                else:
                    x_s_new=min(x_s_potentials)
                delta=max(delta,abs(x_s_new-x[s]))
                x[s]=x_s_new
        return x, n_iter
    
    def compute_reachability(self, 
                             target_states,
                             op):
        # print("Begin",type(target_states))
        if op =="p_max":
            s0=self.compute_S0_max(self.mdp,target_states)
            s1=self.compute_S1_max(self.mdp,target_states)
        else:
            s0=self.compute_S0_min(self.mdp,target_states)
            s1=self.compute_S1_min(self.mdp,s0)

        x,n_iter= self.compute_reachability_main(self.mdp, s0,s1,op)
        return x[self.init_state],n_iter

    def compute_action_reward(self, 
                            mdp,
                            state,
                            action,
                            current_reward,
                            ap):
        """
        Compute the new reward of a state when taking an "action" 
        """
        network=self.model.network.Network()
        new_reward=0
        for target, prob in mdp[state][action].items():
            new_reward+=prob*current_reward[target]
        state_reward = network.get_expression_value(state, ap)
        return state_reward + new_reward

    def compute_reward_main(self, 
                        mdp,
                        to_traverse,
                        x,
                        epsilon,
                        op,
                        ap):
        delta = math.inf
        # Only iterate over non-target finite states
        n_iter = 0
        
        while delta > epsilon and n_iter < self.max_iter:
            n_iter += 1
            delta = 0
            
            for s in to_traverse:
                x_s_potentials = [
                    self.compute_action_reward(mdp, s, action, x, ap)
                    for action in mdp[s].keys()
                ]
                
                if op == 'e_max_s':
                    x_s_new = max(x_s_potentials)
                else:
                    x_s_new = min(x_s_potentials)
                
                delta = max(delta, abs(x_s_new - x[s]))  # Use absolute difference
                x[s] = x_s_new
        
        return x, n_iter

    def compute_reward(self, 
                        target_states,
                        op,
                        ap):
        if op =="e_max_s":
            s0=self.compute_S0_min(self.mdp,target_states)
            s1=self.compute_S1_min(self.mdp,s0)
        else:
            s1=self.compute_S1_max(self.mdp,target_states)
        x={}
        for s in self.mdp.keys():
            if s in s1:
                x[s] = 0 
            else:
                x[s] = math.inf
        to_traverse=set([s for s in x.keys()])-target_states
        return self.compute_optimistic_reward(self.mdp,to_traverse,x,self.epsilon,op,ap)
    
    def compute(self):
        """
        Compute reachability/reward
        """
        result={}
        for i in range(len(self.properties)):
            
            property=self.properties[i]
            property_type=property.exp.op
            ap=property.exp.args[0]
            start = time.time()
            # print(f"Processing {i+1}/{len(self.properties)} propertie(s): {property.name} {property_type}")
            # n_iter=None
            if property_type.startswith("p"):
                value,n_iter=self.compute_reachability(target_states=self.target_states[i],op=property_type)
            else:
                value=self.compute_reward(target_states=self.target_states[i],op=property_type,ap=ap)

            from program import PropertyResult
            result[property.name]=PropertyResult(PropertyResultType.FLOAT, value, time.time()-start)

            # result[property.name]={
            #     "type":property_type,
            #     "exact": value,
            #     "epsilon":self.epsilon,
            # }
            # if n_iter is not None:
            #     result["n_iterations"]=n_iter
        # print("-"*20)
        return result

    def compute_optimistic_reward(self, 
                                  mdp, 
                                  to_traverse,
                                  v,
                                  alpha,
                                  op, 
                                  ap):
        v,_=self.compute_reward_main(mdp,to_traverse,v,alpha,op,ap)
        u={}
        for s in v.keys():
            if s in to_traverse:
                u[s]=v[s]+self.epsilon
            else:
                u[s]=v[s]
        viters=0
        while viters<1/alpha:
            up=True
            down=True
            viters=viters+1
            error=0
            for s in to_traverse:
                v_new_potentials=[
                    self.compute_action_reward(mdp,s,action,v,ap)
                    for action in mdp[s].keys()
                ]
                u_new_potentials=[
                    self.compute_action_reward(mdp,s,action,u,ap)
                    for action in mdp[s].keys()
                ]
                if op == "e_max_s":
                    v_new=max(v_new_potentials)
                    u_new=max(u_new_potentials)
                else:
                    v_new=min(v_new_potentials)
                    u_new=max(u_new_potentials)
                if v_new>0:
                    error = max(error,abs(v_new - v[s]))

                if u_new<u[s]:
                    u[s] = u_new
                    up = False
                elif u_new > u[s]:
                    down = False

                v[s] = v_new 

                if v[s]>u[s]:
                    return self.compute_optimistic_reward(mdp,to_traverse,v,error/2,op,ap)

            if down:
                return (u[self.init_state] + v[self.init_state])/2
            elif up:
                return self.compute_optimistic_reward(mdp,to_traverse,v,error/2,op,ap)
        return self.compute_optimistic_reward(mdp,to_traverse,v,error/2,op,ap)





        