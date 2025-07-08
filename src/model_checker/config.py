#!/bin/python
from enum import Enum

class ExploreMode(Enum):
    RANDOM = "random"
    ALL = "all"

class PropertyType(Enum):
    p_max="p_max"
    p_min="p_min"
    e_max_s="e_max_s"
    e_min_s="e_min_s"

class ProgramCommand(Enum):
    check="check"
    explore="explore"
    
class Algorithm(Enum):
    VALUE_ITERATION = "VALUE_ITERATION"
    INTERVAL_ITERATION = "INTERVAL_ITERATION"
    GS_VALUE_ITERATION = "GS_VALUE_ITERATION"

