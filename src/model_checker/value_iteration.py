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

def value_iteration(mmodel, max_iterations, precision):
    mmodel = mmodel.network
    opt_model = Model(mmodel)
    properties_ = [Property(opt_model, p) for p in mmodel.network.properties]
    properties = [p for p in properties_ if p.is_valid]
    
    results = {p.name: PropertyResult(PropertyResultType.NOT_SUPPORTED, None, 0) for p in properties_ if not p.is_valid}
    for prop in properties:
        timer = time.time()
        try:
            results[prop.name] = value_iteration_thread(prop, timer, max_iterations, precision)
        except Exception as e:
            results[prop.name] = PropertyResult(PropertyResultType.ERROR, None, time.time() - timer)
    return results

def value_iteration_thread(prop, timer, max_iterations, precision):
    # all states
    S = prop.get_states()
    # all states that satisfy the goal
    G = set([s for s in S if prop.get_goal_value(s) == True])
    if __debug__:
        assert len(G) > 0
    # all states that are not safe
    S0 = set([s for s in S if prop.is_safe(s) == False or len(prop.get_actions(s)) == 0])

    # setting this to 1 for G in the case of reachability properties saves just 1 cycle so -\_(-_-)_/
    c = {s: 0 for s in S}

    # actual value iteration here:
    for iteration in range(max_iterations):
        def bellman_update(v):
            _v = {}
            for s in v:
                if s in G:
                    _v[s] = 1 if prop.is_probability or prop.is_reachability else 0
                    continue
                if s in S0:
                    _v[s] = 0
                    continue
                argmax = []
                for a in prop.get_actions(s):
                    a_sum = sum([(prop.get_transition_prob(s, a, s_prime) * v[s_prime]) + prop.get_reward(s,a,s_prime) for s_prime in prop.get_next_states(s, a)])
                    argmax.append(a_sum)
                _v[s] = prop.get_operation()(argmax)
            return _v
        
        _v = bellman_update(c)
        def difference(new, old, s):
            # if old[s] == 0:
            #     if new[s] == 0:
            #         return 0
            #     return float("inf")
            # return abs((old[s] - new[s]) / old[s])
            return abs(new[s] - old[s])
        if all((difference(_v, c, s) < precision for s in S)):
            c = _v
            break
        c = _v
    return PropertyResult(PropertyResultType.FLOAT, c[prop.get_initial_state()], time.time() - timer)