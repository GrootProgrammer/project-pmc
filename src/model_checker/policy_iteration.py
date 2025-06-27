# this file contains the value iteration algorithm for model checking
# this should work with all properties and gives an estimation to the probability of the property being satisfied
# if the GIL is disabled, it will multithread the value iteration for each property
# made by: Ryan Groot

import threading     
import sys
import time
from property import Property
from explored_model import Model
from program import PropertyResult, PropertyResultType

def policy_iteration(mmodel, max_iterations, precision):
    mmodel = mmodel.network
    opt_model = Model(mmodel)
    properties_ = [Property(opt_model, p) for p in mmodel.network.properties]
    properties = [p for p in properties_ if p.is_valid]
    
    results = {p.name: PropertyResult(PropertyResultType.NOT_SUPPORTED, None, 0) for p in properties_ if not p.is_valid}
    for prop in properties:
        timer = time.time()
        #try:
        results[prop.name] = policy_iteration_thread(prop, timer, max_iterations, precision)
        #except Exception as e:
        #    print(e)
        #    results[prop.name] = PropertyResult(PropertyResultType.ERROR, None, time.time() - timer)
    return results

def policy_iteration_thread(prop, timer, max_iterations, precision):
    # all states
    S = prop.get_states()
    # all states that satisfy the goal
    G = set([s for s in S if prop.get_goal_value(s) == True])
    if __debug__:
        assert len(G) > 0
    # all states that are not safe
    S0 = set([s for s in S if prop.is_safe(s) == False or len(prop.get_actions(s)) == 0])

    pi = {s: list(prop.get_actions(s))[0] if len(prop.get_actions(s)) > 0 else None for s in S}
    V = {s: 0 for s in S}

    def policy_evaluation(Vc):
        def loop(Vcc):
            _v = {}
            for s in S:
                if s in G:
                    _v[s] = 1 if prop.is_probability or prop.is_reachability else 0
                    continue
                if s in S0:
                    _v[s] = 0
                    continue
                v_ = 0
                action = pi[s]
                for s_prime in prop.get_next_states(s, action):
                    v_ += prop.get_transition_prob(s, action, s_prime) * (prop.get_reward(s, action, s_prime) + Vcc[s_prime])
                _v[s] = v_
            delta = max([abs(_v[s] - Vcc[s]) for s in S])
            
            return delta, _v
        while True:
            delta, Vc = loop(Vc)
            if delta < precision:
                break
            continue
        return Vc

    def policy_improvement(V, pic):
        policy_stable = True
        for s in S:
            b = pic[s]
            if b is None:
                continue
            
            argmax = b
            max_R = -float("inf") if prop.is_max else float("inf")
            for a in prop.get_actions(s):
                R = 0
                for s_prime in prop.get_next_states(s, a):
                    R += prop.get_transition_prob(s, a, s_prime) * (prop.get_reward(s, a, s_prime) + V[s_prime])
                if prop.get_operation()([R, max_R]) == R:
                    max_R = R
                    argmax = a
            if argmax != b:
                policy_stable = False
            pic[s] = argmax
        return policy_stable, pic
    
    for iteration in range(max_iterations):
        V = policy_evaluation(V)
        policy_stable, pi = policy_improvement(V, pi)
        if policy_stable:
            break

    return PropertyResult(PropertyResultType.FLOAT, V[prop.get_initial_state()], time.time() - timer)