#!/bin/python
from program import *

class ConversionError(Exception):
    def __init__(self, msg):
        super().__init__(f"Conversion error:\n {msg}")
        
class DeletionError(Exception):
    def __init__(self, msg):
        super().__init__(f"Deletion error:\n {msg}")
    
class ExploreModeError(Exception):
    def __init__(self, msg):
        super().__init__(f"Explore mode error: Expected {','.join(list(ExploreMode.__members__))}. Given '{msg}'")