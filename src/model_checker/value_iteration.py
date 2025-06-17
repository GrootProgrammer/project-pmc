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
    if not hasattr(sys, "is_gil_enabled") or not sys._is_gil_enabled():
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
    assert len(G) > 0
    # all states that are not safe
    S0 = set([s for s in S if prop.is_safe(s) == False or len(prop.get_actions(s)) == 0])

    if prop.is_probability:
        c = {s: 1 if s in G else 0 for s in S}
    elif prop.is_reward:
        c = {s: 0 for s in S}

     # these should be parameters
    max_iterations = sys.maxsize
    error = 1e-6

    # actual value iteration here:
    for iteration in range(max_iterations):
        def bellman_update(v):
            _v = {}
            for s in v:
                if s in G:
                    _v[s] = 1 if prop.is_probability else 0
                    continue
                if s in S0:
                    _v[s] = 0
                    continue
                argmax = []
                for a in prop.get_actions(s):
                    a_sum = sum([prop.get_transition_prob(s, a, s_prime) * (v[s_prime] + prop.get_reward(s,a,s_prime)) for s_prime in prop.get_next_states(s, a)])
                    argmax.append(a_sum)
                _v[s] = prop.get_operation()(argmax)
            return _v
        
        _v = bellman_update(c)
        def difference(v1, v2, s):
            return abs(v1[s] - v2[s])
        if all([difference(_v, c, s) < error for s in S]):
            #print(f"true stable: {_v == bellman_update(c)} at iteration {iteration}")
            break
        c = _v
    print(f"{prop.name}={_v[prop.model.trans[prop.model.old.network.get_initial_state()]]}")
    return

class Model:
    def __init__(self, mmodel):
        def breadth_first_search(mmodel):
            new_model = {}
            self.initial_state = mmodel.network.get_initial_state()
            from queue import Queue
            new_states = Queue()
            new_states.put(self.initial_state)
            new_model["states"] = set()
            new_model["transitions"] = {}

            while not new_states.empty():
                s = new_states.get()
                if s in new_model["states"]:
                    continue
                new_model["states"].add(s)
                new_model["transitions"][s] = { a: { mmodel.network.jump(s, a, b): b.probability for b in mmodel.network.get_branches(s, a) } for a in mmodel.network.get_transitions(s)}

                for a in mmodel.network.get_transitions(s):
                    for b in mmodel.network.get_branches(s, a):
                        assert b.probability > 0
                        jmp = mmodel.network.jump(s, a, b)
                        new_states.put(jmp)

            return new_model

        def check_model(t, r, m):
            # I had issues with this before, but i think that was because a.label is not unique
            for s in m["transitions"].keys():
                assert len(m["transitions"][s]) == len(mmodel.network.get_transitions(r[s]))
            # this is just to check that the transition probabilities all sum to 1 (barring floating point errors)
            for s in m["transitions"].keys():
                for a in new_model["transitions"][s].keys():
                    assert abs(sum([p for p in new_model["transitions"][s][a].values()]) - 1) < 0.0000001

            assert all([(s in m["states"]) for s in m["transitions"].keys()])
            assert all([(s in m["transitions"]) for s in m["states"]])

        def translate_to_index(m):
            # here we convert all the states to their index representation to hopefully provide a faster lookup in the future and caching possibility
            translation_table = {}
            rev_table = {}
            new_states = set()

            for i, s in enumerate(m["states"]):
                translation_table[s] = i
                rev_table[i] = s
                new_states.add(i)
            m["states"] = new_states
            m["transitions"] = {translation_table[s]: { a: { translation_table[s_prime]: p for (s_prime,p) in s_.items() } for (a,s_) in v.items()} for (s,v) in m['transitions'].items() }

            return translation_table, rev_table, m

        new_model = breadth_first_search(mmodel)
        identity_table = {s: s for s in new_model["states"]}
        check_model(identity_table, identity_table, new_model)
        translation_table, rev_table, new_model = translate_to_index(new_model)
        check_model(translation_table, rev_table, new_model)
        
        self.old = mmodel
        self.opt = new_model
        self.trans = translation_table
        self.rev = rev_table

    def get_initial_state(self):
        return self.trans[self.old.network.get_initial_state()]

    def get_states(self):
        return self.opt['transitions'].keys()

    def get_actions(self, s):
        return self.opt['transitions'][s].keys()

    def get_transition_prob(self, s, a, s_prime):
        return self.opt['transitions'][s][a][s_prime]

    def get_next_states(self, s, a):
        return self.opt['transitions'][s][a].keys()

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

    def get_next_states(self, s, a):
        return self.model.get_next_states(s, a)

    def is_min(self):
        return 'min' in self.exp.op
    
    def is_max(self):
        return 'max' in self.exp.op

    def get_operation(self):
        if 'min' in self.exp.op:
            return min
        if 'max' in self.exp.op:
            return max
        
        raise NotImplementedError("Operation not supported yet: " + self.exp.op)