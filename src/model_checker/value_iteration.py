import threading     
import sys                                                         

def value_iteration(mmodel):
    opt_model = Model(mmodel)
    print(len(opt_model.opt['states']))
    properties = [Property(opt_model, p) for p in mmodel.network.properties]
    threads = []
    # lets multithread if it is allowed
    if sys._is_gil_enabled():
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
    G = [s for s in S if prop.get_goal_value(s) == 1]

    if prop.is_probability:
        # hack to set to exactly 1 only if goal is satisfied
        _v = {s: 1 if prop.get_goal_value(s) == 1 else 0 for s in S}
    elif prop.is_reward:
        S1 = prop.get_Smin1() if prop.exp.op == "p_max" else prop.getSmax1()

        _v = {s: 0 if s in S1 else float('inf') for s in S}

        for s in G:
            assert s in S1
        
    # these should be parameters
    max_iterations = 1000000
    error = 1e-6

    # actual value iteration here:
    for it in range(max_iterations):
        v = _v
        _v = {}
        for s in v:
            if prop.is_probability:
                if prop.is_reachability and s in G:
                    _v[s] = v[s]
                else:
                    # for some reason there are states with no actions that max and min cannot handle so we just keep repeating the same value (which should be 0 or 1 anyways)
                    if len(prop.get_actions(s)) == 0:
                        _v[s] = v[s]
                    else:
                        _v[s] = prop.get_operation()([sum([probability * v[s_prime] for (s_prime, probability) in prop.get_next_state(s, a).items()]) for a in prop.get_actions(s)])
            else:
                # this should be rewards here
                if s in G:
                    _v[s] = 0
                elif s not in S1:
                    _v[s] = float('inf')
                else:
                    paths = []
                    for a in prop.get_actions(s):
                        r = 0
                        for (s_prime, prob) in prop.get_branches(s, a):
                            r += prob * (v[s_prime])
                        paths.append(r)
                    _v[s] = prop.get_operation()(paths)
        if all(_v[s] == float('inf') or _v[s] == 0 or abs(_v[s] - v[s]) / _v[s] < error for s in v):
            break
    print(f"Checking property: {prop.name}")
    print(prop.exp)
    print(_v[0])
    return

class Model:
    def __init__(self, mmodel):
        # TODO: SHOULD ADD A TEMP LIST THAT IS ALL THE NEW STATES RIGHT NOW THIS IS WORST CASE O(n^n) (I think?), with temp it will be O(n)
        new_model = {}
        new_states = [mmodel.network.get_initial_state()]
        new_model["states"] = []
        new_model["transitions"] = {}
        
        while len(new_states) > 0:
            old_new_states = new_states
            new_states = []
            for s in old_new_states:
                # not sure why this is needed as we guard against it, but it is needed
                if s in new_model["states"]:
                    continue
                new_model["states"].append(s)
                new_model["transitions"][s] = { a: { mmodel.network.jump(s, a, b): b.probability for b in mmodel.network.get_branches(s, a) } for a in mmodel.network.get_transitions(s)}

                for a in mmodel.network.get_transitions(s):
                    for b in mmodel.network.get_branches(s, a):
                        #if len(b.branches) > 1:
                        #    print(b.branches)
                        #    raise Exception("here")
                        jmp = mmodel.network.jump(s, a, b)
                        if jmp not in new_model["states"] and jmp not in new_states:
                            new_states.append(jmp)

        # I had issues with this before, but i think that was because a.label is not unique
        for s in new_model["transitions"].keys():
            assert len(new_model["transitions"][s]) == len(mmodel.network.get_transitions(s))
        # this is just to check that the transition probabilities all sum to 1 (barring floating point errors)
        for s in new_model["transitions"].keys():
            for a in new_model["transitions"][s].keys():
                assert abs(sum([p for p in new_model["transitions"][s][a].values()]) - 1) < 0.0000000000000001

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
        if self.is_reward:
            self.goal_exp = args[1].args[0]
            self.reward_exp = args[0]
        
        assert (self.is_probability or self.is_reward)
        assert (not (self.is_probability and self.is_reward))

        self.model = model
        self.goal_cache = {}
        self.reward_cache = {}

    def get_goal_value(self, s):
        if s not in self.goal_cache:
            self.goal_cache[s] = self.model.old.network.get_expression_value(self.model.rev[s], self.goal_exp)
        return self.goal_cache[s]
    
    def get_states(self):
        return self.model.get_states()

    def get_actions(self, s):
        return self.model.get_actions(s)

    def get_transition_prob(self, s, a, s_prime):
        return self.model.get_transition_prob(s, a, s_prime)

    def get_next_state(self, s, a):
        return self.model.get_next_state(s, a)

    def get_operation(self):
        if self.exp.op == 'p_min':
            return min
        elif self.exp.op == 'p_max':
            return max
        else:
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
                if exists_a and s not in R:
                    R.remove(s)
        return R

    def get_Smax1(self):
        S = self.get_states()
        T = [s for s in S if self.get_goal_value(s) == 1]
        R = s.copy()
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
                            if s_prime not in _R and prob == 0:
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