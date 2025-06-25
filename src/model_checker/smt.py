# this file converts the MDP problem to a SMT problem and solves it using z3
# solves fast for some models, loops for others
# results unsat if the solution cannot be expressed as a fraction (which should always be possible?)
# made by: Ryan Groot

import threading     
import sys
from explored_model import Model
from property import Property
from program import PropertyResult, PropertyResultType
import time

def smt(mmodel):
    mmodel = mmodel.network
    opt_model = Model(mmodel)
    properties = [Property(opt_model, p) for p in mmodel.network.properties]
    properties = [p for p in properties if p.is_valid]
    results = {}
    for prop in properties:
        timer = time.time()
        try:
            results[prop.name] = smt_thread(prop, timer)
        except Exception as e:
            results[prop.name] = PropertyResult(PropertyResultType.ERROR, None, time.time() - timer)
    return results

def smt_thread(prop, timer):
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
    # max_iterations = sys.maxsize
    # error = 1e-6

    import z3

    solver = z3.Solver()

    states = {s: z3.Real(f"c_{s}") for s in S}

    # Return minimum of a vector; error if empty
    def z3min(vs):
      if len(vs) == 0:
        return 0
      m = vs[0]
      for v in vs[1:]:
        m = z3.If(v < m, v, m)
      return m

    def z3max(vs):
        if len(vs) == 0:
            return 0
        m = vs[0]
        for v in vs[1:]:
            m = z3.If(v > m, v, m)
        return m


    for s in S:
        if s in G:
            solver.add(states[s] == (1 if prop.is_probability or prop.is_reachability else 0))
        elif s in S0:
            solver.add(states[s] == 0)
        else:
            argmax = []
            for a in prop.get_actions(s):
                a_sum = sum([prop.get_transition_prob(s, a, s_prime) * (states[s_prime] + prop.get_reward(s,a,s_prime)) for s_prime in prop.get_next_states(s, a)])
                argmax.append(a_sum)
            if prop.is_min():
                solver.add(states[s] == z3min(argmax))
            else:
                solver.add(states[s] == z3max(argmax))

    
    if prop.is_probability:
        for s in S:
            solver.add(states[s] >= 0)
            solver.add(states[s] <= 1)

    solver.set("timeout", 10000)
    has_solved = solver.check()
    if has_solved != z3.sat:
        return PropertyResult(PropertyResultType.TIMEOUT, None, time.time() - timer)
    model = solver.model()
    solution = model.eval(states[prop.get_initial_state()])

    return PropertyResult(PropertyResultType.FLOAT, float(solution.as_fraction()), time.time() - timer)