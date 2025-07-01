#!/bin/python
from enum import Enum
from typing import Any

class ExploreMode(Enum):
    RANDOM = "random"

class Algorithm(Enum):
    VALUE_ITERATION = "vi"
    POLICY_ITERATION = "pi"
    INTERVAL_ITERATION = "ii"
    SOUND_VALUE_ITERATION = "svi"
    SMT_EXACT = "smt"
    OPTIMISTIC_VALUE_ITERATION = "ovi"
    GAUSS_SEIDEL_VALUE_ITERATION = "gsvi"

class PropertyResultType(Enum):
    NOT_SUPPORTED = "not_supported"
    ERROR = "error"
    TIMEOUT = "timeout"
    FLOAT = "float"
    BOOL = "bool"
    INCORRECT_FLOAT = "incorrect_float"

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
        if self.result_type == PropertyResultType.INCORRECT_FLOAT:
            return f"incorrect: {self.result}"
        
        raise ValueError(f"Invalid result type: {self.result_type}")

    def __repr__(self):
        return self.to_dict().__repr__()