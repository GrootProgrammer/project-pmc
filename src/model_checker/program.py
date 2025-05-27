#!/bin/python
from enum import Enum

class ExploreMode(Enum):
    RANDOM = "random"

class PropertyType(Enum):
    REACHABILITY = "reachability"
    REWARD = "reward"

class Algorithm(Enum):
    VALUE_ITERATION = "vi"
    POLICY_ITERATION = "pi"
    INTERVAL_ITERATION = "ii"
    SOUND_VALUE_ITERATION = "svi"