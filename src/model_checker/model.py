#!/bin/python
import random
#import numpy as np
from utils import *
from program import *
from typing import *

class Model():
    def __init__(self, network):
        self.network=network
    
    def info(self):
        """
        Print general information
        """
        print(f"* Model type: {self.network.model_type}")
        print(f"* No. properties: {len(self.network.properties)}")
        print(f"* No. transition labels (incl. tau): {len(self.network.transition_labels)}")
        initial_state = self.network.get_initial_state()
        print("* Initial state:", str(initial_state))

    def explore(self, mode: ExploreMode, max_steps: int = 100):
        if mode == ExploreMode.RANDOM.value:
            return self.explore_mdp_random(max_steps)

    def explore_mdp_random(self, max_steps: int = 100):
        """
        Explore an MDP using random action selection
        
        Args:
            network: Initialized Network object representing the MDP
            max_steps: Maximum number of steps to simulate
            
        Returns:
            List of visited states in traversal order
        """
        state = self.network.get_initial_state()
        path = [state]  # Store initial state
        
        for _ in range(max_steps):
            # Get all possible transitions from current state
            transitions = self.network.get_transitions(state)
            if not transitions:
                break  # Terminal state reached
                
            # Randomly select a transition (action)
            transition = random.choice(transitions)
            
            # Get possible branches for selected transition
            branches = self.network.get_branches(state, transition)
          
            # Select branch according to probabilities
            probabilities = [b.probability for b in branches]
            selected_branch = np.random.choice(branches, p=probabilities)

            # Transition to next state
            state = self.network.jump(state, transition, selected_branch)
            path.append(state)
            
        return path
