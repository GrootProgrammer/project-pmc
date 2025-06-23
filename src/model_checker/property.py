
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
            self.goal_cache[s] = self.model.get_goal_value(s, self.goal_exp)
        return self.goal_cache[s]

    def is_safe(self, s):
        if s not in self.safe_cache:
            if self.safe_exp is None:
                if self.is_reward:
                    if self.exp.op.endswith("_s"):
                        self.safe_cache[s] = not self.get_goal_value(s)
            if s not in self.safe_cache:
                self.safe_cache[s] = self.model.is_safe(s, self.safe_exp)
        return self.safe_cache[s]

    def get_reward(self, s, a, s_prime):
        if self.reward_exp is None:
            return 0
        if s not in self.reward_cache:
            self.reward_cache[(s,a,s_prime)] = self.model.get_reward(s, a, s_prime, self.reward_exp)
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