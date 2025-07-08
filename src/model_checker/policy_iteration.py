# this file contains the policy iteration algorithm for model checking
# this should work with all properties and gives an estimation to the probability of the property being satisfied
# made by: Ryan Groot

import threading     
import sys
import time
from property import Property
from explored_model import Model
from program import PropertyResult, PropertyResultType

def policy_iteration(mmodel, max_iterations, precision, dynamic_precision):
    mmodel = mmodel.network
    opt_model = Model(mmodel)
    properties_ = [Property(opt_model, p) for p in mmodel.network.properties]
    properties = [p for p in properties_ if p.is_valid]
    
    results = {p.name: PropertyResult(PropertyResultType.NOT_SUPPORTED, None, 0) for p in properties_ if not p.is_valid}
    for prop in properties:
        timer = time.time()
        try:
            results[prop.name] = policy_iteration_thread(prop, timer, max_iterations, precision, dynamic_precision)
        except Exception as e:
                results[prop.name] = PropertyResult(PropertyResultType.ERROR, None, time.time() - timer)
    return results

def policy_iteration_thread(prop, timer, max_iterations, precision, dynamic_precision):
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

    def policy_evaluation(Vc, err):
        def loop(Vcc):
            _v = {}
            for s in S:
                if s in G:
                    _v[s] = 1 if prop.is_probability or prop.is_reachability else 0
                    continue
                if s in S0:
                    _v[s] = 0
                    continue
                a = pi[s]
                _v[s] = sum(prop.get_transition_prob(s, a, s_) * Vcc[s_] + prop.get_reward(s, a, s_) for s_ in prop.get_next_states(s, a))
            delta = max([abs(_v[s] - Vcc[s]) for s in S])
            
            return delta, _v
        while True:
            delta, Vc = loop(Vc)
            if delta < err:
                break
            continue
        return Vc

    def policy_improvement(V, pic):
        policy_stable = True
        for s in S:
            b = pic[s]
            if b is None:
                continue
            
            argmax = prop.get_operation()(prop.get_actions(s), key=lambda a: sum(prop.get_transition_prob(s, a, s_) * V[s_] + prop.get_reward(s, a, s_) for s_ in prop.get_next_states(s, a)))

            if argmax != b:
                policy_stable = False
            pic[s] = argmax
        return policy_stable, pic
    
    if dynamic_precision:
        e = 1
    else:
        e = precision

    for iteration in range(max_iterations):
        V = policy_evaluation(V, e)
        policy_stable, pi = policy_improvement(V, pi)
        if policy_stable:
            if e <= precision:
                break
            e = e / 10
            continue

    return PropertyResult(PropertyResultType.FLOAT, V[prop.get_initial_state()], time.time() - timer)