# this file contains the value iteration algorithm for model checking
# this should work with all properties and gives an estimation to the probability of the property being satisfied
# if the GIL is disabled, it will multithread the value iteration for each property
# made by: Ryan Groot

import threading     
import sys
from queue import Queue

def value_iteration(mmodel):
    mmodel = mmodel.network
    opt_model = Model(mmodel)
    print(len(opt_model.opt['states']))
    properties = [Property(opt_model, p) for p in mmodel.network.properties]
    properties = [p for p in properties if p.is_valid]
    threads = []
    # lets multithread if it is allowed
    if hasattr(sys, "is_gil_enabled") and sys._is_gil_enabled():
        for prop in properties:
            value_iteration_thread(prop)
    else:
        for prop in properties:
            thread = threading.Thread(target=value_iteration_thread, args=(prop,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

def value_iteration_thread(prop):
    # all states
    S = prop.get_states()
    # all states that satisfy the goal
    G = set([s for s in S if prop.get_goal_value(s) == True])
    # all states that are not safe
    S0 = set([s for s in S if prop.is_safe(s) == False])

    if prop.is_probability:
        c = {s: 1 if s in G else 0 for s in S}
    elif prop.is_reward:
        c = {s: 0 for s in S}

    #import sympy as sp
#
    #v = {s: sp.Symbol(f"v_{s}") for s in S}
#
    #sys.setrecursionlimit(15000)
    #eqs = []
    #for s in S:
    #    if s in G:
    #        eqs.append(sp.Eq(v[s], 1.0))
    #    elif s in S0:
    #        eqs.append(sp.Eq(v[s], 0.0))
    #    else:
    #        # For each action, calculate the sum of probabilities * values
    #        action_sums = []
    #        for a in prop.get_actions(s):
    #            tmp = 0
    #            for (s_prime, prob) in prop.get_next_state(s, a).items():
    #                tmp += (v[s_prime] + prop.get_reward(s, a, s_prime)) * prob
    #            action_sums.append(tmp)
    #        
    #        # Take maximum over all action sums by comparing each pair
    #        if len(action_sums) > 0:
    #            max_expr = action_sums[0]
    #            for expr in action_sums[1:]:
    #                max_expr = sp.Max(max_expr, expr)
    #            eqs.append(sp.Eq(v[s], max_expr))
#
    ## Solve system of equations
    #solution = sp.solve(eqs, list(v.values()))
    #if solution:
    #    print(f"{prop.name}={solution[v[0]]}")

     # these should be parameters
    max_iterations = sys.maxsize
    error = 1e-6
#
    # actual value iteration here:
    for _ in range(max_iterations):
        def bellman_update(v):
            _v = {}
            for s in v:
                if s in G:
                    _v[s] = 1
                    continue
                if s in S0:
                    _v[s] = 0
                    continue
                if len(prop.get_actions(s)) == 0:
                    _v[s] = v[s]
                else:
                    argmax = [
                        sum(
                            [
                                probability * (v[s_prime] + prop.get_reward(s, a, s_prime)) for (s_prime, probability) in prop.get_next_state(s, a).items()
                            ]
                        ) for a in prop.get_actions(s)
                    ]
                    _v[s] = prop.get_operation()(argmax)
            return _v
        
        _v = bellman_update(c)
        if all(abs(_v[s] - c[s]) / _v[s] < error for s in c if _v[s] != float('inf') and _v[s] != 0):
            break
        c = _v
    print(f"{prop.name}={_v[0]}")
    return

class Model:
    def __init__(self, mmodel):
        new_model = {}
        new_states = [mmodel.network.get_initial_state()]
        new_model["states"] = []
        new_model["transitions"] = {}
        
        while len(new_states) > 0:
            old_new_states = new_states
            new_states = []
            for s in old_new_states:
                # not sure why this is needed as we guard against it, but it is needed
                if s in new_model["transitions"]:
                    continue
                new_model["states"].append(s)
                new_model["transitions"][s] = { a: { mmodel.network.jump(s, a, b): b.probability for b in mmodel.network.get_branches(s, a) } for a in mmodel.network.get_transitions(s)}

                for a in mmodel.network.get_transitions(s):
                    for b in mmodel.network.get_branches(s, a):
                        # if len(b.branches) > 1:
                        #     print(b.branches)
                        #     raise Exception("here")
                        assert b.probability > 0
                        jmp = mmodel.network.jump(s, a, b)
                        new_states.append(jmp)

        # I had issues with this before, but i think that was because a.label is not unique
        for s in new_model["transitions"].keys():
            assert len(new_model["transitions"][s]) == len(mmodel.network.get_transitions(s))
        # this is just to check that the transition probabilities all sum to 1 (barring floating point errors)
        for s in new_model["transitions"].keys():
            for a in new_model["transitions"][s].keys():
                assert abs(sum([p for p in new_model["transitions"][s][a].values()]) - 1) < 0.0000000000001

        assert all([(s in new_model["states"]) for s in new_model["transitions"].keys()])
        assert all([(s in new_model["transitions"]) for s in new_model["states"]])

        # here we convert all the states to their index representation to hopefully provide a faster lookup in the future and caching possibility
        translation_table = {}
        rev_table = {}
        new_states = []

        for i, s in enumerate(new_model["states"]):
            translation_table[s] = i
            rev_table[i] = s
            new_states.append(i)
        new_model["states"] = new_states
        new_model["transitions"] = {translation_table[s]: { a: { translation_table[s_prime]: p for (s_prime,p) in s_.items() } for (a,s_) in v.items()} for (s,v) in new_model['transitions'].items() }
        
        # I had issues with this before, but i think that was because a.label is not unique
        for s in new_model["transitions"].keys():
            assert len(new_model["transitions"][s]) == len(mmodel.network.get_transitions(rev_table[s]))
        # this is just to check that the transition probabilities all sum to 1 (barring floating point errors)
        for s in new_model["transitions"].keys():
            for a in new_model["transitions"][s].keys():
                assert abs(sum([p for p in new_model["transitions"][s][a].values()]) - 1) < 0.0000000000000001

        assert all([(s in new_model["states"]) for s in new_model["transitions"].keys()])
        assert all([(s in new_model["transitions"]) for s in new_model["states"]])
        
        self.old = mmodel
        self.opt = new_model
        self.trans = translation_table
        self.rev = rev_table

    def get_states(self):
        return self.opt['states']

    def get_actions(self, s):
        return self.opt['transitions'][s].keys()

    def get_transition_prob(self, s, a, s_prime):
        return self.opt['transitions'][s][a][s_prime]

    def get_next_state(self, s, a):
        return self.opt['transitions'][s][a]

class Property:
    def __init__(self, model, prop):
        self.name = prop.name
        self.exp = prop.exp
        op = self.exp.op
        args = self.exp.args
        self.is_probability = op.startswith("p_")
        self.is_reachability = op == "exists" and (args[0].op == 'eventually' and args[0].args[0].op == 'ap' or args[0].op == 'until' and args[0].args[0].op == 'ap' and args[0].args[1].op == 'ap')
        self.is_reward = op.startswith("e_") and args[1].op == 'ap'

        if self.is_probability or self.is_reachability:
            self.safe_exp = args[0].args[0].args[0] if args[0].op == 'until' else None
            self.goal_exp = args[0].args[1].args[0] if args[0].op == 'until' else args[0].args[0].args[0]
            self.reward_exp = None
        if self.is_reward:
            self.goal_exp = args[1].args[0]
            self.reward_exp = args[0]
            self.safe_exp = None        

        # xor assertion
        self.is_valid = (self.is_probability or self.is_reward) and (not (self.is_probability and self.is_reward))

        self.model = model
        self.goal_cache = {}
        self.reward_cache = {}
        self.safe_cache = {}

    def get_goal_value(self, s):
        if s not in self.goal_cache:
            self.goal_cache[s] = self.model.old.network.get_expression_value(self.model.rev[s], self.goal_exp)
        return self.goal_cache[s]

    def is_safe(self, s):
        if self.safe_exp is None:
            return True
        if s not in self.safe_cache:
            self.safe_cache[s] = self.model.old.network.get_expression_value(self.model.rev[s], self.safe_exp)
        return self.safe_cache[s]

    def get_reward(self, s, a, s_prime):
        if self.reward_exp is None:
            return 0
        if s not in self.reward_cache:
            S = self.model.rev[s]
            S_prime = self.model.rev[s_prime]

            branches = self.model.old.network.get_branches(S, a)
            n = 0
            total = 0
            for b in branches:
                reward = [self.reward_exp].copy()
                new_state = self.model.old.network.jump(S, a, b, reward)
                if new_state == S_prime:
                    n += 1
                    total += b.probability * reward[0]
            assert n > 0
            self.reward_cache[(s,a,s_prime)] = total / n
        return self.reward_cache[(s,a,s_prime)]
    
    def get_states(self):
        return self.model.get_states()

    def get_actions(self, s):
        return self.model.get_actions(s)

    def get_transition_prob(self, s, a, s_prime):
        return self.model.get_transition_prob(s, a, s_prime)

    def get_next_state(self, s, a):
        return self.model.get_next_state(s, a)

    def get_operation(self):
        if 'min' in self.exp.op:
            return min
        if 'max' in self.exp.op:
            return max
        
        raise NotImplementedError("Operation not supported yet: " + self.exp.op)
    
    def get_Smin0(self):
        S = self.get_states()
        R = [s for s in S if self.get_goal_value(s) == 1]
        _R = []

        while set(R) != set(_R):
            _R = R.copy()
            for s in S:
                forall_a = True
                for a in self.get_actions(s):
                    exists_delta = False
                    for (s_prime, prob) in self.get_next_state(s, a).items():
                        if s_prime in _R and prob > 0:
                            exists_delta = True
                            break
                    if not exists_delta:
                        forall_a = False
                        break
                if forall_a and s not in R:
                    R.append(s)

        return [s for s in S if s not in R]


    def get_Smin1(self):
        S = self.get_states()
        Smin0 = self.getSmin0()
        R = [s for s in S if s not in Smin0]
        _R = []

        while set(R) != set(_R):
            _R = R.copy()
            for s in R:
                exists_a = False
                for a in self.get_actions(s):
                    exists_delta = False
                    for (s_prime, prob) in self.get_next_state(s, a).items():
                        if s_prime not in _R and prob > 0:
                            exists_delta = True
                            break
                    if not exists_delta:
                        exists_a = True
                        break
                if exists_a and s in R:
                    R.remove(s)
        return R

    def get_Smax0(self):
        S = self.get_states()
        R = [s for s in S if self.get_goal_value(s) == 1]
        _R = []
        while set(R) != set(_R):
            _R = R.copy()
            for s in S:
                exists_a = False
                for a in self.get_actions(s):
                    exists_delta = False
                    for (s_prime, prob) in self.get_next_state(s, a).items():
                        if s_prime in _R and prob > 0:
                            exists_delta = True
                            break
                    if exists_delta:
                        exists_a = True
                        break
                if exists_a and s in R:
                    R.remove(s)
        return [s for s in S if s not in R]

    def get_Smax1(self):
        S = self.get_states()
        T = [s for s in S if self.get_goal_value(s) == 1]
        R = S.copy()
        _R = []
        __R = []

        while set(R) != set(_R):
            _R = R.copy()
            R = T.copy()
            
            while set(R) != set(__R):
                __R = R.copy()
                for s in S:
                    exists_a = False
                    for a in self.get_actions(s):
                        forall_s = True
                        exists_s = False

                        for (s_prime, prob) in self.get_next_state(s,a).items():
                            if s_prime not in _R or prob == 0:
                                forall_s = False
                                break
                            if s_prime in __R and prob > 0:
                                exists_s = True

                        if forall_s and exists_s:
                            exists_a = True
                            break
                    if exists_a and s not in R:
                        R.append(s)
        return R