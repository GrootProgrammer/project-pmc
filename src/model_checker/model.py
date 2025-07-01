#!/bin/python
from utils import *
from errors import *
from pwarnings import *
from config import *
import warnings
import logging
from collections import deque

logger = logging.getLogger(__name__)

class Model():
    def __init__(self, network, algo:Algorithm=None):
        self.network = network
        self.algo=algo
        self.transition_labels=self.network.Network().transition_labels
        self.properties=self.network.Network().properties
        # n_prob_properties=sum([1  for p in self.properties if p.exp.op in ["p_min", "p_max"]])
        # if n_prob_properties == 0:
        #     raise Exception #Skip reward for now
        self.init_state,self.mdp, self.target_states=self.explore_mdp_all(
            self.extract_property_ap(self.properties),
        )
        
    def extract_property_ap(self, properties: list[Property]) -> list[int]:
        aps=[]
        for property in properties:
            property_exp=property.exp
            if not property_exp.op in PropertyType.__members__:
                # msg=f"Unsupported property type: Expected {','.join(list(PropertyType.__members__))}. Given '{property_exp.op}"
                # warnings.warn(msg, UnsupportedPropertyTypeError)
                aps.append(None)
                continue
            if property_exp.op in [PropertyType.p_max.value,PropertyType.p_min.value]:
                if len(property_exp.args) > 1 or property_exp.args[0].op != "eventually":
                    # msg=f"Only unbounded probabilistic reachability and cumulative-reward-to-reach-a-target properties are supported. Given {str(property_exp.args[0])}"
                    # warnings.warn(msg,OnlyUnboundedPropertyError)
                    aps.append(None)
                    continue
                main_ap=property_exp.args[0].args[0].args[0]
            elif property_exp.op in [PropertyType.e_max_s.value,PropertyType.e_min_s.value]:
                main_ap=property_exp.args[1].args[0]
            aps.append(main_ap)
        return aps

    def explore_mdp_all(self, aps:list[int]=[]) -> tuple[State,dict[State,dict],list[set[State]] ]:
        network = self.network.Network()
        init_state=network.get_initial_state()
        queue = deque([init_state])
        visited = set()
        mdp = {}
        target_states = [set() for _ in aps]

        while queue:
            state = queue.popleft()
            if state in visited: 
                continue
            visited.add(state)
            
            # Check target states
            for i, ap in enumerate(aps):
                if ap is not None and network.get_expression_value(state, ap):
                    target_states[i].add(state)
            
            # Process transitions
            state_transitions = {}
            for transition in network.get_transitions(state):
                branches = {}
                for branch in network.get_branches(state, transition):
                    target = network.jump(state, transition, branch)
                    branches[target] =  branches.get(target, 0) + branch.probability
                    queue.append(target)
                state_transitions[transition.label] = branches
            
            mdp[state] = state_transitions
        
        return init_state, mdp, target_states
    
    def info(self,):
        pass

    def explore(self, mode: ExploreMode, max_states: int=50):
        pass