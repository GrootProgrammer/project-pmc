# jani_from_ppddl

from __future__ import annotations
from typing import List, Union, Optional
import math

class ExplorationError(Exception):
	__slots__ = ("message")
	
	def __init__(self, message: str):
		self.message = message

class VariableInfo(object):
	__slots__ = ("name", "component", "type", "minValue", "maxValue")
	
	def __init__(self, name: str, component: Optional[int], type: str, minValue = None, maxValue = None):
		self.name = name
		self.component = component
		self.type = type
		self.minValue = minValue
		self.maxValue = maxValue

# States
class State(object):
	__slots__ = ("var0", "var1", "var2", "aut_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.var0
		elif variable == 1:
			return self.var1
		elif variable == 2:
			return self.var2
		elif variable == 3:
			return self.aut_location
	
	def copy_to(self, other: State):
		other.var0 = self.var0
		other.var1 = self.var1
		other.var2 = self.var2
		other.aut_location = self.aut_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.var0 == other.var0 and self.var1 == other.var1 and self.var2 == other.var2 and self.aut_location == other.aut_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var0)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.aut_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "var0 = " + str(self.var0)
		result += ", var1 = " + str(self.var1)
		result += ", var2 = " + str(self.var2)
		result += ", aut_location = " + str(self.aut_location)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ()
	
	def copy_to(self, other: Transient):
		pass
	
	def __eq__(self, other):
		return isinstance(other, self.__class__)
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		return result
	
	def __str__(self):
		result = "("
		result += ")"
		return result

# Automaton: aut
class autAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [35, 46, 41, 46, 40]
		self.transition_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
	
	def set_initial_values(self, state: State) -> None:
		state.aut_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.aut_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.aut_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.aut_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.aut_location
		if location == 0:
			if transition == 0:
				return ((((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 1) and (state.var0 == 1))) or ((state.var1 == 3) and (state.var0 == 1)))
			elif transition >= 1 and transition < 4:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 4:
				return (((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition >= 5 and transition < 9:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 9:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition >= 10 and transition < 14:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 14:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition >= 15 and transition < 19:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 19:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 1)))
			elif transition >= 20 and transition < 24:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0)))
			elif transition >= 24 and transition < 29:
				return (((((state.var1 == 1) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 29:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 30:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 31:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 32:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 33:
				return ((((state.var1 == 0) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition == 34:
				return ((state.var1 == 3) and (state.var0 == 1))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return (((((((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 0) and (state.var0 == 1))) or ((state.var1 == 1) and (state.var0 == 1))) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 3) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition == 1:
				return ((((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 1) and (state.var0 == 1))) or ((state.var1 == 3) and (state.var0 == 1)))
			elif transition >= 2 and transition < 4:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 4:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 5:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition >= 6 and transition < 9:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 9 and transition < 14:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 14 and transition < 19:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 19 and transition < 24:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0)))
			elif transition >= 24 and transition < 29:
				return (((((state.var1 == 1) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 29:
				return ((((state.var1 == 0) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition == 30:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 31:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 32:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 33:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 34:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 35:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 36:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 37:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 38:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 39:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 40:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 41:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 42:
				return ((state.var1 == 3) and (state.var0 == 1))
			elif transition == 43:
				return ((((state.var1 == 0) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition >= 44:
				return ((state.var1 == 3) and (state.var0 == 1))
			else:
				raise IndexError
		elif location == 2:
			if transition >= 0 and transition < 2:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 2:
				return ((((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 1) and (state.var0 == 1))) or ((state.var1 == 3) and (state.var0 == 1)))
			elif transition == 3:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 4 and transition < 6:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 6:
				return (((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition >= 7 and transition < 9:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 9 and transition < 11:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 11:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition >= 12 and transition < 14:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 14 and transition < 16:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 16:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition >= 17 and transition < 19:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 19 and transition < 21:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0)))
			elif transition == 21:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 1)))
			elif transition >= 22 and transition < 24:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0)))
			elif transition >= 24 and transition < 29:
				return (((((state.var1 == 1) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 29:
				return ((((state.var1 == 0) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition == 30:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 31:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 32:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 33:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 34:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 35:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 36:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 37:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 38:
				return ((((state.var1 == 0) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition >= 39:
				return ((state.var1 == 3) and (state.var0 == 1))
			else:
				raise IndexError
		elif location == 3:
			if transition >= 0 and transition < 2:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 2:
				return (((((((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 0) and (state.var0 == 1))) or ((state.var1 == 1) and (state.var0 == 1))) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 3) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition == 3:
				return ((((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 1) and (state.var0 == 1))) or ((state.var1 == 3) and (state.var0 == 1)))
			elif transition >= 4 and transition < 7:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 7:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 8:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 9 and transition < 14:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 14 and transition < 19:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 19 and transition < 24:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0)))
			elif transition >= 24 and transition < 29:
				return (((((state.var1 == 1) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 29:
				return ((((state.var1 == 0) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition == 30:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 31:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 32:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 33:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 34:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 35:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 36:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 37:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 38:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 39:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 40:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 41:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 42:
				return ((state.var1 == 3) and (state.var0 == 1))
			elif transition == 43:
				return ((((state.var1 == 0) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition >= 44:
				return ((state.var1 == 3) and (state.var0 == 1))
			else:
				raise IndexError
		elif location == 4:
			if transition >= 0 and transition < 4:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 4 and transition < 8:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 8:
				return ((((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition >= 9 and transition < 14:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 14 and transition < 19:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition >= 19 and transition < 24:
				return (((((state.var1 == 0) and (state.var0 == 0)) or ((state.var1 == 1) and (state.var0 == 0))) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0)))
			elif transition >= 24 and transition < 29:
				return (((((state.var1 == 1) and (state.var0 == 0)) or ((state.var1 == 2) and (state.var0 == 0))) or ((state.var1 == 3) and (state.var0 == 0))) or ((state.var1 == 4) and (state.var0 == 0)))
			elif transition == 29:
				return ((((state.var1 == 0) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1))) or ((state.var1 == 4) and (state.var0 == 1)))
			elif transition == 30:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 31:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 32:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 33:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition == 34:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 35:
				return (((state.var1 == 2) and (state.var0 == 1)) or ((state.var1 == 0) and (state.var0 == 1)))
			elif transition == 36:
				return (((state.var1 == 3) and (state.var0 == 1)) or ((state.var1 == 1) and (state.var0 == 1)))
			elif transition == 37:
				return (((state.var1 == 4) and (state.var0 == 1)) or ((state.var1 == 2) and (state.var0 == 1)))
			elif transition >= 38:
				return ((state.var1 == 3) and (state.var0 == 1))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.aut_location
		if location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.aut_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.aut_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
			elif transition == 11:
				return 1
			elif transition == 12:
				return 1
			elif transition == 13:
				return 1
			elif transition == 14:
				return 1
			elif transition == 15:
				return 1
			elif transition == 16:
				return 1
			elif transition == 17:
				return 1
			elif transition == 18:
				return 1
			elif transition == 19:
				return 1
			elif transition == 20:
				return 1
			elif transition == 21:
				return 1
			elif transition == 22:
				return 1
			elif transition == 23:
				return 1
			elif transition == 24:
				return 1
			elif transition == 25:
				return 1
			elif transition == 26:
				return 1
			elif transition == 27:
				return 1
			elif transition == 28:
				return 1
			elif transition == 29:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 30:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 31:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 32:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 33:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 34:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
			elif transition == 11:
				return 1
			elif transition == 12:
				return 1
			elif transition == 13:
				return 1
			elif transition == 14:
				return 1
			elif transition == 15:
				return 1
			elif transition == 16:
				return 1
			elif transition == 17:
				return 1
			elif transition == 18:
				return 1
			elif transition == 19:
				return 1
			elif transition == 20:
				return 1
			elif transition == 21:
				return 1
			elif transition == 22:
				return 1
			elif transition == 23:
				return 1
			elif transition == 24:
				return 1
			elif transition == 25:
				return 1
			elif transition == 26:
				return 1
			elif transition == 27:
				return 1
			elif transition == 28:
				return 1
			elif transition == 29:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 30:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 31:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 32:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 33:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 34:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 35:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 36:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 37:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 38:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 39:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 40:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 41:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 42:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 43:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 44:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 45:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
			elif transition == 11:
				return 1
			elif transition == 12:
				return 1
			elif transition == 13:
				return 1
			elif transition == 14:
				return 1
			elif transition == 15:
				return 1
			elif transition == 16:
				return 1
			elif transition == 17:
				return 1
			elif transition == 18:
				return 1
			elif transition == 19:
				return 1
			elif transition == 20:
				return 1
			elif transition == 21:
				return 1
			elif transition == 22:
				return 1
			elif transition == 23:
				return 1
			elif transition == 24:
				return 1
			elif transition == 25:
				return 1
			elif transition == 26:
				return 1
			elif transition == 27:
				return 1
			elif transition == 28:
				return 1
			elif transition == 29:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 30:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 31:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 32:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 33:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 34:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 35:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 36:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 37:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 38:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 39:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 40:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
			elif transition == 11:
				return 1
			elif transition == 12:
				return 1
			elif transition == 13:
				return 1
			elif transition == 14:
				return 1
			elif transition == 15:
				return 1
			elif transition == 16:
				return 1
			elif transition == 17:
				return 1
			elif transition == 18:
				return 1
			elif transition == 19:
				return 1
			elif transition == 20:
				return 1
			elif transition == 21:
				return 1
			elif transition == 22:
				return 1
			elif transition == 23:
				return 1
			elif transition == 24:
				return 1
			elif transition == 25:
				return 1
			elif transition == 26:
				return 1
			elif transition == 27:
				return 1
			elif transition == 28:
				return 1
			elif transition == 29:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 30:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 31:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 32:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 33:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 34:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 35:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 36:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 37:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 38:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 39:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 40:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 41:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 42:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 43:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 44:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 45:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
			elif transition == 11:
				return 1
			elif transition == 12:
				return 1
			elif transition == 13:
				return 1
			elif transition == 14:
				return 1
			elif transition == 15:
				return 1
			elif transition == 16:
				return 1
			elif transition == 17:
				return 1
			elif transition == 18:
				return 1
			elif transition == 19:
				return 1
			elif transition == 20:
				return 1
			elif transition == 21:
				return 1
			elif transition == 22:
				return 1
			elif transition == 23:
				return 1
			elif transition == 24:
				return 1
			elif transition == 25:
				return 1
			elif transition == 26:
				return 1
			elif transition == 27:
				return 1
			elif transition == 28:
				return 1
			elif transition == 29:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 30:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 31:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 32:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 33:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 34:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 35:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 36:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 37:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 38:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 39:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.aut_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 4:
					if branch == 0:
						target_state.var1 = 1
						target_state.aut_location = 0
				elif transition == 5:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 6:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 7:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 8:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 9:
					if branch == 0:
						target_state.var1 = 2
						target_state.aut_location = 0
				elif transition == 10:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 11:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 12:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 13:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 14:
					if branch == 0:
						target_state.var1 = 3
						target_state.aut_location = 0
				elif transition == 15:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 16:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 17:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 18:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 19:
					if branch == 0:
						target_state.var1 = 4
						target_state.aut_location = 0
				elif transition == 20:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 21:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 22:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 23:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 24:
					if branch == 0:
						target_state.var1 = 0
						target_state.aut_location = 0
				elif transition == 25:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 26:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 27:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 28:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 29:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 0
				elif transition == 30:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 0
				elif transition == 31:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 0
				elif transition == 32:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 0
				elif transition == 33:
					if branch == 0:
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.aut_location = 0
				elif transition == 34:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 4:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 5:
					if branch == 0:
						target_state.var1 = 1
						target_state.aut_location = 1
				elif transition == 6:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 7:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 8:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 9:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 10:
					if branch == 0:
						target_state.var1 = 2
						target_state.aut_location = 1
				elif transition == 11:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 12:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 13:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 14:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 15:
					if branch == 0:
						target_state.var1 = 3
						target_state.aut_location = 1
				elif transition == 16:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 17:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 18:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 19:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 20:
					if branch == 0:
						target_state.var1 = 4
						target_state.aut_location = 1
				elif transition == 21:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 22:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 23:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 24:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 25:
					if branch == 0:
						target_state.var1 = 0
						target_state.aut_location = 1
				elif transition == 26:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 27:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 28:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 29:
					if branch == 0:
						target_state.var2 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.aut_location = 1
				elif transition == 30:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 31:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 32:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 33:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 34:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 35:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 36:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 37:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 38:
					if branch == 0:
						target_state.var1 = 0
						target_state.aut_location = 1
					elif branch == 1:
						target_state.aut_location = 1
				elif transition == 39:
					if branch == 0:
						target_state.var1 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.aut_location = 1
				elif transition == 40:
					if branch == 0:
						target_state.var1 = 2
						target_state.aut_location = 1
					elif branch == 1:
						target_state.aut_location = 1
				elif transition == 41:
					if branch == 0:
						target_state.var1 = 3
						target_state.aut_location = 1
					elif branch == 1:
						target_state.aut_location = 1
				elif transition == 42:
					if branch == 0:
						target_state.var1 = 4
						target_state.aut_location = 1
					elif branch == 1:
						target_state.aut_location = 1
				elif transition == 43:
					if branch == 0:
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.aut_location = 1
				elif transition == 44:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
				elif transition == 45:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 4:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 5:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 6:
					if branch == 0:
						target_state.var1 = 1
						target_state.aut_location = 2
				elif transition == 7:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 8:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 9:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 10:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 11:
					if branch == 0:
						target_state.var1 = 2
						target_state.aut_location = 2
				elif transition == 12:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 13:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 14:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 15:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 16:
					if branch == 0:
						target_state.var1 = 3
						target_state.aut_location = 2
				elif transition == 17:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 18:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 19:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 20:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 21:
					if branch == 0:
						target_state.var1 = 4
						target_state.aut_location = 2
				elif transition == 22:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 23:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 24:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 25:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 26:
					if branch == 0:
						target_state.var1 = 0
						target_state.aut_location = 2
				elif transition == 27:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 28:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 29:
					if branch == 0:
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.aut_location = 2
				elif transition == 30:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 31:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 32:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 33:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 34:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 35:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 36:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 37:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 38:
					if branch == 0:
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.aut_location = 2
				elif transition == 39:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 1
						target_state.aut_location = 1
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
				elif transition == 40:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 3:
					if branch == 0:
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 4:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 5:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 6:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 7:
					if branch == 0:
						target_state.var1 = 1
						target_state.aut_location = 3
				elif transition == 8:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 9:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 10:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 11:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 12:
					if branch == 0:
						target_state.var1 = 2
						target_state.aut_location = 3
				elif transition == 13:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 14:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 15:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 16:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 17:
					if branch == 0:
						target_state.var1 = 3
						target_state.aut_location = 3
				elif transition == 18:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 19:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 20:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 21:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 22:
					if branch == 0:
						target_state.var1 = 4
						target_state.aut_location = 3
				elif transition == 23:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 24:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 25:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 26:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 27:
					if branch == 0:
						target_state.var1 = 0
						target_state.aut_location = 3
				elif transition == 28:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 4
						target_state.aut_location = 4
				elif transition == 29:
					if branch == 0:
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.aut_location = 3
				elif transition == 30:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 31:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 32:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 33:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 34:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 4
						target_state.aut_location = 4
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 35:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 4
						target_state.aut_location = 4
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 36:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 4
						target_state.aut_location = 4
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 37:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 4
						target_state.aut_location = 4
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 38:
					if branch == 0:
						target_state.var1 = 0
						target_state.aut_location = 3
					elif branch == 1:
						target_state.aut_location = 3
				elif transition == 39:
					if branch == 0:
						target_state.var1 = 1
						target_state.aut_location = 3
					elif branch == 1:
						target_state.aut_location = 3
				elif transition == 40:
					if branch == 0:
						target_state.var1 = 2
						target_state.aut_location = 3
					elif branch == 1:
						target_state.aut_location = 3
				elif transition == 41:
					if branch == 0:
						target_state.var1 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.aut_location = 3
				elif transition == 42:
					if branch == 0:
						target_state.var1 = 4
						target_state.aut_location = 3
					elif branch == 1:
						target_state.aut_location = 3
				elif transition == 43:
					if branch == 0:
						target_state.var2 = 4
						target_state.aut_location = 4
					elif branch == 1:
						target_state.aut_location = 3
				elif transition == 44:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 2
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
				elif transition == 45:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 4
						target_state.aut_location = 4
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 3:
					if branch == 0:
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 4:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 5:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 6:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 7:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 8:
					if branch == 0:
						target_state.var1 = 1
						target_state.aut_location = 4
				elif transition == 9:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 10:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 11:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 12:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 13:
					if branch == 0:
						target_state.var1 = 2
						target_state.aut_location = 4
				elif transition == 14:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 15:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 16:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 17:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 18:
					if branch == 0:
						target_state.var1 = 3
						target_state.aut_location = 4
				elif transition == 19:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 20:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 21:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 22:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 23:
					if branch == 0:
						target_state.var1 = 4
						target_state.aut_location = 4
				elif transition == 24:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 0
						target_state.aut_location = 0
				elif transition == 25:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 1
						target_state.aut_location = 1
				elif transition == 26:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 2
						target_state.aut_location = 2
				elif transition == 27:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 3
						target_state.aut_location = 3
				elif transition == 28:
					if branch == 0:
						target_state.var1 = 0
						target_state.aut_location = 4
				elif transition == 29:
					if branch == 0:
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.aut_location = 4
				elif transition == 30:
					if branch == 0:
						target_state.var1 = 0
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 4
				elif transition == 31:
					if branch == 0:
						target_state.var1 = 1
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 4
				elif transition == 32:
					if branch == 0:
						target_state.var1 = 2
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 4
				elif transition == 33:
					if branch == 0:
						target_state.var1 = 3
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 4
				elif transition == 34:
					if branch == 0:
						target_state.var1 = 0
						target_state.aut_location = 4
					elif branch == 1:
						target_state.aut_location = 4
				elif transition == 35:
					if branch == 0:
						target_state.var1 = 1
						target_state.aut_location = 4
					elif branch == 1:
						target_state.aut_location = 4
				elif transition == 36:
					if branch == 0:
						target_state.var1 = 2
						target_state.aut_location = 4
					elif branch == 1:
						target_state.aut_location = 4
				elif transition == 37:
					if branch == 0:
						target_state.var1 = 3
						target_state.aut_location = 4
					elif branch == 1:
						target_state.aut_location = 4
				elif transition == 38:
					if branch == 0:
						target_state.var1 = 4
						target_state.aut_location = 4
					elif branch == 1:
						target_state.aut_location = 4
				elif transition == 39:
					if branch == 0:
						target_state.var1 = 4
						target_state.var2 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var0 = 0
						target_state.aut_location = 4

class PropertyExpression(object):
	__slots__ = ("op", "args")
	
	def __init__(self, op: str, args: List[Union[int, float, PropertyExpression]]):
		self.op = op
		self.args = args
	
	def __str__(self):
		result = self.op + "("
		needComma = False
		for arg in self.args:
			if needComma:
				result += ", "
			else:
				needComma = True
			result += str(arg)
		return result + ")"

class Property(object):
	__slots__ = ("name", "exp")
	
	def __init__(self, name: str, exp: PropertyExpression):
		self.name = name
		self.exp = exp
	
	def __str__(self):
		return self.name + ": " + str(self.exp)

class Transition(object):
	__slots__ = ("sync_vector", "label", "transitions")
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_aut")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ" }
		self.sync_vectors = [[0, 0]]
		self.properties = [
			Property("goal", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("var0", None, "int", 0, 2),
			VariableInfo("var1", None, "int", 0, 5),
			VariableInfo("var2", None, "int", 0, 5),
			VariableInfo("aut_location", 0, "int", 0, 4)
		]
		self._aut_aut = autAutomaton(self)
		self.components = [self._aut_aut]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.var0 = 1
		state.var1 = 0
		state.var2 = 0
		self._aut_aut.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_aut.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return (((state.var2 == 4) and (state.var1 == 4)) and (state.var0 == 1))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return (((state.var2 == 4) and (state.var1 == 4)) and (state.var0 == 1))
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_aut.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_aut = [[]]
		transition_count = self._aut_aut.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_aut.get_guard_value(state, i):
				trans_aut[self._aut_aut.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1]]
			# aut
			if synced is not None:
				if sv[0] != -1:
					if len(trans_aut[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_aut[sv[0]][0]
						for i in range(1, len(trans_aut[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_aut[sv[0]][i]
			if synced is not None:
				for sync in synced:
					sync[-1] = sv[-1]
					sync.append(svi)
				transitions.extend(filter(lambda s: s[-2] != -1, synced))
		# Convert to Transition instances
		for i in range(len(transitions)):
			transitions[i] = Transition(transitions[i][-1], transitions[i][-2], transitions[i])
			del transitions[i].transitions[-1]
			del transitions[i].transitions[-1]
		# Done
		return transitions
	
	def get_rate(self, state: State, transition: Transition) -> Optional[float]:
		for i in range(len(self.components)):
			if transition.transitions[i] != -1:
				rate = self.components[i].get_rate_value(state, transition.transitions[i])
				if rate is not None:
					for j in range(i + 1, len(self.components)):
						if transition.transitions[j] != -1:
							check_rate = self.components[j].get_rate_value(state, transition)
							if check_rate is not None:
								raise ExplorationError("Invalid MA model: Multiple components specify a rate for the same transition.")
					return rate
		return None
	
	def get_branches(self, state: State, transition: Transition) -> List[Branch]:
		combs = [[-1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_aut.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_aut.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_aut.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		result = list(filter(lambda b: b.probability > 0.0, combs))
		if len(result) == 0:
			raise ExplorationError("Invalid model: All branches of a transition have probability zero.")
		return result
	
	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 1):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self._aut_aut.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
