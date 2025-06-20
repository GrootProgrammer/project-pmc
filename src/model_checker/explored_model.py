
class Model:
    def __init__(self, mmodel):
        def breadth_first_search(mmodel):
            import time
            start_time = time.time()
            
            new_model = {}
            initial_state = mmodel.network.get_initial_state()
            from queue import Queue
            new_states = Queue()
            new_states.put(initial_state)
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
                        if __debug__:
                            assert b.probability > 0
                        jmp = mmodel.network.jump(s, a, b)
                        new_states.put(jmp)
            
            end_time = time.time()
            print(f"Breadth first search took {end_time - start_time} seconds")

            return (new_model, initial_state)

        def check_model(t, r, m):
            # I had issues with this before, but i think that was because a.label is not unique
            for s in m["transitions"].keys():
                assert len(m["transitions"][s]) == len(mmodel.network.get_transitions(r[s]))
            # this is just to check that the transition probabilities all sum to 1 (barring floating point errors)
            for s in m["transitions"].keys():
                for a in new_model["transitions"][s].keys():
                    if abs(sum([p for p in new_model["transitions"][s][a].values()]) - 1) > 0.001:
                        print(f"sum of transition probabilities for {s} and {a} is {sum([p for p in new_model['transitions'][s][a].values()])}")
                    assert abs(sum([p for p in new_model["transitions"][s][a].values()]) - 1) < 0.1
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

        new_model, self.initial_state = breadth_first_search(mmodel)
        if __debug__:
            identity_table = {s: s for s in new_model["states"]}
            check_model(identity_table, identity_table, new_model)
        translation_table, rev_table, new_model = translate_to_index(new_model)
        if __debug__:
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

    def get_goal_value(self, s, g_exp):
        return self.old.network.get_expression_value(self.rev[s], g_exp)

    def is_safe(self, s, safe_exp):
        return self.old.network.get_expression_value(self.rev[s], safe_exp)

    def get_reward(self, s, a, s_prime, reward_exp):
        S = self.rev[s]
        S_prime = self.rev[s_prime]

        branches = self.old.network.get_branches(S, a)
        n = 0
        total = 0
        for b in branches:
            reward = [reward_exp].copy()
            new_state = self.old.network.jump(S, a, b, reward)
            if new_state == S_prime:
                n += 1
                total += b.probability * reward[0]
        if __debug__:
            assert n > 0
        return total / n