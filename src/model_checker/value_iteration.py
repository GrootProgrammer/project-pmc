# this file contains the value iteration algorithm for model checking
# this should work with all properties and gives an estimation to the probability of the property being satisfied
# if the GIL is disabled, it will multithread the value iteration for each property
# made by: Ryan Groot

import threading     
import sys
from property import Property
from explored_model import Model

def value_iteration(mmodel):
    mmodel = mmodel.network
    opt_model = Model(mmodel)
    print(len(opt_model.opt['states']))
    properties = [Property(opt_model, p) for p in mmodel.network.properties]
    properties = [p for p in properties if p.is_valid]
    threads = []
    # lets multithread if it is allowed
    if not hasattr(sys, "is_gil_enabled") or not sys.is_gil_enabled():
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
    if __debug__:
        assert len(G) > 0
    # all states that are not safe
    S0 = set([s for s in S if prop.is_safe(s) == False or len(prop.get_actions(s)) == 0])

    # setting this to 1 for G in the case of reachability properties saves just 1 cycle so -\_(-_-)_/
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
                    _v[s] = 1 if prop.is_probability or prop.is_reachability else 0
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