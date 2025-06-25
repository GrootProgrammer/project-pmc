#!/bin/python
from enum import Enum
from typing import Any

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
    SMT_EXACT = "smt"

class PropertyResultType(Enum):
    NOT_SUPPORTED = "not_supported"
    ERROR = "error"
    TIMEOUT = "timeout"
    FLOAT = "float"
    BOOL = "bool"

class PropertyResult():
    def __init__(self, result_type: PropertyResultType, result: Any, time: float):
        self.result_type = result_type
        self.result = result
        self.time = time

    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            "result_type": self.result_type.value,
            "result": self.result,
            "time": self.time
        }

    @staticmethod
    def from_dict(d):
        result = PropertyResult(PropertyResultType(d["result_type"]), d["result"], d["time"])
        return result

    def __str__(self):
        if self.result_type == PropertyResultType.NOT_SUPPORTED:
            return "not supported"
        if self.result_type == PropertyResultType.ERROR:
            return "error"
        if self.result_type == PropertyResultType.TIMEOUT:
            return "timeout"
        if self.result_type == PropertyResultType.FLOAT:
            return f"{self.result}"
        if self.result_type == PropertyResultType.BOOL:
            return f"{self.result}"
        
        raise ValueError(f"Invalid result type: {self.result_type}")
