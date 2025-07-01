# this file contains the sound value iteration algorithm for model checking
# this should work with all properties and gives a *sound* estimation to the probability of the property being satisfied
# made by: Ryan Groot

import time
from property import Property
from explored_model import Model
from program import PropertyResult, PropertyResultType

def sound_value_iteration(mmodel, precision):
    opt_model = Model(mmodel.network)
    properties_ = [Property(opt_model, p) for p in mmodel.network.properties]
    properties = [p for p in properties_ if p.is_valid]
    
    results = {p.name: PropertyResult(PropertyResultType.NOT_SUPPORTED, None, 0) for p in properties_ if not p.is_valid}
    for prop in properties:
        timer = time.time()
        try:
            results[prop.name] = sound_value_iteration_thread(prop, timer, precision)
        except Exception as e:
            results[prop.name] = PropertyResult(PropertyResultType.ERROR, None, time.time() - timer)
    return results

def findAction(prop, x, y, s, u):
    if u != float("inf"):
        return prop.get_operation()(prop.get_actions(s), key=lambda a: sum(prop.get_transition_prob(s, a, s_) * (x[s_] + y[s_] * u) for s_ in prop.get_next_states(s, a)))
    else:
        return prop.get_operation()(prop.get_actions(s), key=lambda a: sum(prop.get_transition_prob(s, a, s_) * (y[s_]) for s_ in prop.get_next_states(s, a)))

def decisionValue(prop, x, y, s, a):
    d = -float("inf")
    for b in prop.get_actions(s):
        if b == a:
            continue
        y_delta = sum((prop.get_transition_prob(s, a, s_) - prop.get_transition_prob(s, b, s_)) * y[s_] for s_ in prop.get_next_states(s, a))
        if y_delta > 0:
            x_delta = sum((prop.get_transition_prob(s, b, s_) - prop.get_transition_prob(s, a, s_)) * x[s_] for s_ in prop.get_next_states(s, a))
            d = max([d, x_delta / y_delta])
    return d

def sound_value_iteration_thread(prop, timer, precision):
    # if prop.is_reward:
    #     return PropertyResult(PropertyResultType.NOT_SUPPORTED, None, 0)
    # if prop.is_min():
    #     return PropertyResult(PropertyResultType.NOT_SUPPORTED, None, 0)
    # i                         
    S = prop.get_states()
    G = set([s for s in S if prop.get_goal_value(s) == True])
    # 1
    S0 = set([s for s in S if prop.is_safe(s) == False or len(prop.get_actions(s)) == 0])
    # 2 
    # assert from the paper, ignore here    
    # 3                                              
    S_q = S - (S0 | G)
    if len(S_q) == 0:
        initial_state = prop.get_initial_state()
        return PropertyResult(PropertyResultType.FLOAT, 1 if initial_state in G else 0, time.time() - timer)                 
    # 4                                                
    x = {s: 1 if s in G else 0 for s in S}                                                
    y = {s: 1 if s in S_q else 0 for s in S}

    # 5
    l = -float("inf")                                                                     
    u = float("inf")                                                                      
    d = -float("inf")
    # 6
    # we do not need to keep track of the iteration count

    # 7
    while True:
        # 8
        # we do not need to keep track of the iteration count
        # 9
        x_ = {}
        for s in G:
            x_[s] = 1
        for s in (S - G):
            x_[s] = 0
        y_ = {}
        for s in S_q:
            y_[s] = 1
        for s in S - S_q:
            y_[s] = 0
        # 10
        d_ = d
        # 11
        for s in S_q:
            # 12
            a = findAction(prop, x, y, s, u)
            # 13
            d_ = max([d_, decisionValue(prop, x, y, s, a)])
            # 14
            x_[s] = sum(prop.get_transition_prob(s, a, s_) * x[s_] + prop.get_reward(s, a, s_) for s_ in prop.get_next_states(s, a))
            # 15
            y_[s] = sum(prop.get_transition_prob(s, a, s_) * y[s_] + prop.get_reward(s, a, s_) for a in prop.get_actions(s) for s_ in prop.get_next_states(s, a))
        if all(y_[s] < 1 for s in S_q):
            l_ = max([l, min([(x_[s]/(1-y_[s])) for s in S_q])])
            u_ = min([u, max(d_, max([(x_[s]/(1-y_[s])) for s in S_q]))])
        # this is just undocumented in the paper. nice!
        else:
            l_ = l
            u_ = u
        if y_[prop.get_initial_state()] * (u_ - l_) < 2 * precision:
            result = x_[prop.get_initial_state()] + y_[prop.get_initial_state()] * ((l_ + u_) / 2)
            return PropertyResult(PropertyResultType.FLOAT, result, time.time() - timer)
        x = x_
        y = y_
        d = d_
        u = u_
        l = l_