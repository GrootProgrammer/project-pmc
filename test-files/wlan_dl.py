# wlan_dl.0

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
	__slots__ = ("c1", "c2", "x1", "s1", "slot1", "backoff1", "x2", "s2", "slot2", "backoff2", "t", "station1_location", "station2_location")
	
	def udfs_global_free_state(self, free__param__c1, free__param__c2):
		return ((free__param__c1 == 0) and (free__param__c2 == 0))
	
	def udfs_global_free_jump(self, transient, free__param__c1, free__param__c2):
		return ((free__param__c1 == 0) and (free__param__c2 == 0))
	
	def udfs_global_busy_state(self, busy__param__c1, busy__param__c2):
		return ((busy__param__c1 > 0) or (busy__param__c2 > 0))
	
	def udfs_global_busy_jump(self, transient, busy__param__c1, busy__param__c2):
		return ((busy__param__c1 > 0) or (busy__param__c2 > 0))
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.c1
		elif variable == 1:
			return self.c2
		elif variable == 2:
			return self.x1
		elif variable == 3:
			return self.s1
		elif variable == 4:
			return self.slot1
		elif variable == 5:
			return self.backoff1
		elif variable == 6:
			return self.x2
		elif variable == 7:
			return self.s2
		elif variable == 8:
			return self.slot2
		elif variable == 9:
			return self.backoff2
		elif variable == 10:
			return self.t
		elif variable == 11:
			return self.station1_location
		elif variable == 12:
			return self.station2_location
	
	def copy_to(self, other: State):
		other.c1 = self.c1
		other.c2 = self.c2
		other.x1 = self.x1
		other.s1 = self.s1
		other.slot1 = self.slot1
		other.backoff1 = self.backoff1
		other.x2 = self.x2
		other.s2 = self.s2
		other.slot2 = self.slot2
		other.backoff2 = self.backoff2
		other.t = self.t
		other.station1_location = self.station1_location
		other.station2_location = self.station2_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.c1 == other.c1 and self.c2 == other.c2 and self.x1 == other.x1 and self.s1 == other.s1 and self.slot1 == other.slot1 and self.backoff1 == other.backoff1 and self.x2 == other.x2 and self.s2 == other.s2 and self.slot2 == other.slot2 and self.backoff2 == other.backoff2 and self.t == other.t and self.station1_location == other.station1_location and self.station2_location == other.station2_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.s1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.slot1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.backoff1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.s2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.slot2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.backoff2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.t)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.station1_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.station2_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "c1 = " + str(self.c1)
		result += ", c2 = " + str(self.c2)
		result += ", x1 = " + str(self.x1)
		result += ", s1 = " + str(self.s1)
		result += ", slot1 = " + str(self.slot1)
		result += ", backoff1 = " + str(self.backoff1)
		result += ", x2 = " + str(self.x2)
		result += ", s2 = " + str(self.s2)
		result += ", slot2 = " + str(self.slot2)
		result += ", backoff2 = " + str(self.backoff2)
		result += ", t = " + str(self.t)
		result += ", station1_location = " + str(self.station1_location)
		result += ", station2_location = " + str(self.station2_location)
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

# Automaton: medium
class mediumAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [6]
		self.transition_labels = [[1, 2, 3, 3, 4, 4]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		pass
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = 0
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[0]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[0][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = 0
		if location == 0:
			if transition == 0:
				return (state.c1 > 0)
			elif transition == 1:
				return (state.c2 > 0)
			elif transition == 2:
				return ((state.c1 == 0) and (state.c2 == 0))
			elif transition == 3:
				return ((state.c1 == 0) and (state.c2 > 0))
			elif transition == 4:
				return ((state.c2 == 0) and (state.c1 == 0))
			elif transition == 5:
				return ((state.c2 == 0) and (state.c1 > 0))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = 0
		if location == 0:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
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
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.c1 = 0
				elif transition == 1:
					if branch == 0:
						target_state.c2 = 0
				elif transition == 2:
					if branch == 0:
						target_state.c1 = 1
				elif transition == 3:
					if branch == 0:
						target_state.c1 = 2
						target_state.c2 = 2
				elif transition == 4:
					if branch == 0:
						target_state.c2 = 1
				elif transition == 5:
					if branch == 0:
						target_state.c1 = 2
						target_state.c2 = 2

# Automaton: station1
class station1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 3, 1, 5, 2, 3, 2, 3, 4, 3, 1]
		self.transition_labels = [[0, 0, 5], [0, 5], [0, 0, 5], [0], [0, 0, 0, 0, 5], [0, 5], [0, 0, 5], [3, 5], [1, 1, 5], [0, 1, 3, 5], [0, 0, 5], [5]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1, 1], [16], [1, 1, 1, 1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.station1_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.station1_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.station1_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.station1_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.station1_location
		if location == 3 or location == 11:
			return True
		elif location == 0:
			if transition == 0:
				return ((state.x1 == 3) or (state.x1 == 2))
			elif transition == 1:
				return state.udfs_global_busy_state(state.c1, state.c2)
			elif transition == 2:
				return ((state.x1 < 3) and state.udfs_global_free_state(state.c1, state.c2))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return state.udfs_global_free_state(state.c1, state.c2)
			elif transition == 1:
				return state.udfs_global_busy_state(state.c1, state.c2)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return state.udfs_global_busy_state(state.c1, state.c2)
			elif transition == 1:
				return ((state.x1 == 3) or (state.x1 == 2))
			elif transition == 2:
				return ((state.x1 < 3) and state.udfs_global_free_state(state.c1, state.c2))
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return ((state.x1 == 1) and (state.backoff1 > 0))
			elif transition == 1:
				return (((state.slot1 > 0) and (state.x1 == 1)) and (state.backoff1 == 0))
			elif transition == 2:
				return (((state.slot1 == 0) and (state.x1 == 1)) and (state.backoff1 == 0))
			elif transition == 3:
				return state.udfs_global_busy_state(state.c1, state.c2)
			elif transition == 4:
				return ((state.x1 < 1) and state.udfs_global_free_state(state.c1, state.c2))
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return state.udfs_global_free_state(state.c1, state.c2)
			elif transition == 1:
				return state.udfs_global_busy_state(state.c1, state.c2)
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return ((state.x1 == 3) or (state.x1 == 2))
			elif transition == 1:
				return state.udfs_global_busy_state(state.c1, state.c2)
			elif transition == 2:
				return ((state.x1 < 3) and state.udfs_global_free_state(state.c1, state.c2))
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return ((state.x1 == 1) or (state.x1 == 0))
			elif transition == 1:
				return (state.x1 < 1)
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return ((state.x1 >= 4) and (state.c1 == 2))
			elif transition == 1:
				return ((state.x1 >= 4) and (state.c1 == 1))
			elif transition == 2:
				return (state.x1 < 10)
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return ((state.udfs_global_busy_state(state.c1, state.c2) and (state.c1 == 0)) and (state.x1 == 0))
			elif transition == 1:
				return ((state.c1 == 1) and ((state.x1 == 4) or (state.x1 == 3)))
			elif transition == 2:
				return ((state.c1 == 0) and ((state.x1 == 1) or ((state.x1 == 0) and state.udfs_global_free_state(state.c1, state.c2))))
			elif transition == 3:
				return (((state.udfs_global_free_state(state.c1, state.c2) and (state.c1 == 0)) and (state.x1 == 0)) or ((state.c1 == 1) and (state.x1 < 4)))
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return ((state.x1 == 0) and state.udfs_global_busy_state(state.c1, state.c2))
			elif transition == 1:
				return (state.x1 == 6)
			elif transition == 2:
				return (((state.x1 == 0) and state.udfs_global_free_state(state.c1, state.c2)) or ((state.x1 > 0) and (state.x1 < 6)))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.station1_location
		if location == 3 or location == 11:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 8:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.station1_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.station1_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				if True:
					return (1 / 16)
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
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.station1_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 8
						target_state.station1_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 2
						target_state.station1_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 11)
						target_state.station1_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 3
						target_state.station1_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.s1 = 2
						target_state.station1_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 2
						target_state.station1_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 4
						target_state.slot1 = 0
						target_state.station1_location = 3
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 11)
						target_state.station1_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 5
						target_state.backoff1 = 0
						target_state.station1_location = 4
					elif branch == 1:
						target_state.s1 = 5
						target_state.backoff1 = 1
						target_state.station1_location = 4
					elif branch == 2:
						target_state.s1 = 5
						target_state.backoff1 = 2
						target_state.station1_location = 4
					elif branch == 3:
						target_state.s1 = 5
						target_state.backoff1 = 3
						target_state.station1_location = 4
					elif branch == 4:
						target_state.s1 = 5
						target_state.backoff1 = 4
						target_state.station1_location = 4
					elif branch == 5:
						target_state.s1 = 5
						target_state.backoff1 = 5
						target_state.station1_location = 4
					elif branch == 6:
						target_state.s1 = 5
						target_state.backoff1 = 6
						target_state.station1_location = 4
					elif branch == 7:
						target_state.s1 = 5
						target_state.backoff1 = 7
						target_state.station1_location = 4
					elif branch == 8:
						target_state.s1 = 5
						target_state.backoff1 = 8
						target_state.station1_location = 4
					elif branch == 9:
						target_state.s1 = 5
						target_state.backoff1 = 9
						target_state.station1_location = 4
					elif branch == 10:
						target_state.s1 = 5
						target_state.backoff1 = 10
						target_state.station1_location = 4
					elif branch == 11:
						target_state.s1 = 5
						target_state.backoff1 = 11
						target_state.station1_location = 4
					elif branch == 12:
						target_state.s1 = 5
						target_state.backoff1 = 12
						target_state.station1_location = 4
					elif branch == 13:
						target_state.s1 = 5
						target_state.backoff1 = 13
						target_state.station1_location = 4
					elif branch == 14:
						target_state.s1 = 5
						target_state.backoff1 = 14
						target_state.station1_location = 4
					elif branch == 15:
						target_state.s1 = 5
						target_state.backoff1 = 15
						target_state.station1_location = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 5
						target_state.backoff1 = (state.backoff1 - 1)
						if target_state.backoff1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.backoff1) + " is less than the lower bound of 0 for variable \"backoff1\".")
						target_state.station1_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 5
						target_state.slot1 = (state.slot1 - 1)
						if target_state.slot1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.slot1) + " is less than the lower bound of 0 for variable \"slot1\".")
						target_state.backoff1 = 15
						target_state.station1_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 8
						target_state.station1_location = 7
				elif transition == 3:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 6
						target_state.station1_location = 5
				elif transition == 4:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 11)
						target_state.station1_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 7
						target_state.station1_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.s1 = 6
						target_state.station1_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 5
						target_state.station1_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 6
						target_state.station1_location = 5
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 11)
						target_state.station1_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 9
						target_state.station1_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 11)
						target_state.station1_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 11
						target_state.station1_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 10
						target_state.station1_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 11)
						target_state.station1_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 2
						target_state.station1_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 12
						target_state.station1_location = 11
				elif transition == 2:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 10
						target_state.station1_location = 9
				elif transition == 3:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 11)
						target_state.station1_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 2
						target_state.station1_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 3
						target_state.station1_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 11)
						target_state.station1_location = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 12
						target_state.station1_location = 11

# Automaton: station2
class station2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 3, 1, 5, 2, 3, 2, 3, 4, 3, 1]
		self.transition_labels = [[0, 0, 5], [0, 5], [0, 0, 5], [0], [0, 0, 0, 0, 5], [0, 5], [0, 0, 5], [4, 5], [2, 2, 5], [0, 2, 4, 5], [0, 0, 5], [5]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1, 1], [16], [1, 1, 1, 1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.station2_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.station2_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.station2_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.station2_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.station2_location
		if location == 3 or location == 11:
			return True
		elif location == 0:
			if transition == 0:
				return ((state.x2 == 3) or (state.x2 == 2))
			elif transition == 1:
				return state.udfs_global_busy_state(state.c2, state.c1)
			elif transition == 2:
				return ((state.x2 < 3) and state.udfs_global_free_state(state.c2, state.c1))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return state.udfs_global_free_state(state.c2, state.c1)
			elif transition == 1:
				return state.udfs_global_busy_state(state.c2, state.c1)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return state.udfs_global_busy_state(state.c2, state.c1)
			elif transition == 1:
				return ((state.x2 == 3) or (state.x2 == 2))
			elif transition == 2:
				return ((state.x2 < 3) and state.udfs_global_free_state(state.c2, state.c1))
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return ((state.x2 == 1) and (state.backoff2 > 0))
			elif transition == 1:
				return (((state.slot2 > 0) and (state.x2 == 1)) and (state.backoff2 == 0))
			elif transition == 2:
				return (((state.slot2 == 0) and (state.x2 == 1)) and (state.backoff2 == 0))
			elif transition == 3:
				return state.udfs_global_busy_state(state.c2, state.c1)
			elif transition == 4:
				return ((state.x2 < 1) and state.udfs_global_free_state(state.c2, state.c1))
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return state.udfs_global_free_state(state.c2, state.c1)
			elif transition == 1:
				return state.udfs_global_busy_state(state.c2, state.c1)
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return ((state.x2 == 3) or (state.x2 == 2))
			elif transition == 1:
				return state.udfs_global_busy_state(state.c2, state.c1)
			elif transition == 2:
				return ((state.x2 < 3) and state.udfs_global_free_state(state.c2, state.c1))
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return ((state.x2 == 1) or (state.x2 == 0))
			elif transition == 1:
				return (state.x2 < 1)
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return ((state.x2 >= 4) and (state.c2 == 2))
			elif transition == 1:
				return ((state.x2 >= 4) and (state.c2 == 1))
			elif transition == 2:
				return (state.x2 < 10)
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return ((state.udfs_global_busy_state(state.c2, state.c1) and (state.c2 == 0)) and (state.x2 == 0))
			elif transition == 1:
				return ((state.c2 == 1) and ((state.x2 == 4) or (state.x2 == 3)))
			elif transition == 2:
				return ((state.c2 == 0) and ((state.x2 == 1) or ((state.x2 == 0) and state.udfs_global_free_state(state.c2, state.c1))))
			elif transition == 3:
				return (((state.udfs_global_free_state(state.c2, state.c1) and (state.c2 == 0)) and (state.x2 == 0)) or ((state.c2 == 1) and (state.x2 < 4)))
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return ((state.x2 == 0) and state.udfs_global_busy_state(state.c2, state.c1))
			elif transition == 1:
				return (state.x2 == 6)
			elif transition == 2:
				return (((state.x2 == 0) and state.udfs_global_free_state(state.c2, state.c1)) or ((state.x2 > 0) and (state.x2 < 6)))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.station2_location
		if location == 3 or location == 11:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 8:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.station2_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.station2_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				if True:
					return (1 / 16)
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
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.station2_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 8
						target_state.station2_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 2
						target_state.station2_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 11)
						target_state.station2_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 3
						target_state.station2_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.s2 = 2
						target_state.station2_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 2
						target_state.station2_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 4
						target_state.slot2 = 0
						target_state.station2_location = 3
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 11)
						target_state.station2_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 5
						target_state.backoff2 = 0
						target_state.station2_location = 4
					elif branch == 1:
						target_state.s2 = 5
						target_state.backoff2 = 1
						target_state.station2_location = 4
					elif branch == 2:
						target_state.s2 = 5
						target_state.backoff2 = 2
						target_state.station2_location = 4
					elif branch == 3:
						target_state.s2 = 5
						target_state.backoff2 = 3
						target_state.station2_location = 4
					elif branch == 4:
						target_state.s2 = 5
						target_state.backoff2 = 4
						target_state.station2_location = 4
					elif branch == 5:
						target_state.s2 = 5
						target_state.backoff2 = 5
						target_state.station2_location = 4
					elif branch == 6:
						target_state.s2 = 5
						target_state.backoff2 = 6
						target_state.station2_location = 4
					elif branch == 7:
						target_state.s2 = 5
						target_state.backoff2 = 7
						target_state.station2_location = 4
					elif branch == 8:
						target_state.s2 = 5
						target_state.backoff2 = 8
						target_state.station2_location = 4
					elif branch == 9:
						target_state.s2 = 5
						target_state.backoff2 = 9
						target_state.station2_location = 4
					elif branch == 10:
						target_state.s2 = 5
						target_state.backoff2 = 10
						target_state.station2_location = 4
					elif branch == 11:
						target_state.s2 = 5
						target_state.backoff2 = 11
						target_state.station2_location = 4
					elif branch == 12:
						target_state.s2 = 5
						target_state.backoff2 = 12
						target_state.station2_location = 4
					elif branch == 13:
						target_state.s2 = 5
						target_state.backoff2 = 13
						target_state.station2_location = 4
					elif branch == 14:
						target_state.s2 = 5
						target_state.backoff2 = 14
						target_state.station2_location = 4
					elif branch == 15:
						target_state.s2 = 5
						target_state.backoff2 = 15
						target_state.station2_location = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 5
						target_state.backoff2 = (state.backoff2 - 1)
						if target_state.backoff2 < 0:
							raise OverflowError("Assigned value of " + str(target_state.backoff2) + " is less than the lower bound of 0 for variable \"backoff2\".")
						target_state.station2_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 5
						target_state.slot2 = (state.slot2 - 1)
						if target_state.slot2 < 0:
							raise OverflowError("Assigned value of " + str(target_state.slot2) + " is less than the lower bound of 0 for variable \"slot2\".")
						target_state.backoff2 = 15
						target_state.station2_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 8
						target_state.station2_location = 7
				elif transition == 3:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 6
						target_state.station2_location = 5
				elif transition == 4:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 11)
						target_state.station2_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 7
						target_state.station2_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.s2 = 6
						target_state.station2_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 5
						target_state.station2_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 6
						target_state.station2_location = 5
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 11)
						target_state.station2_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 9
						target_state.station2_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 11)
						target_state.station2_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 11
						target_state.station2_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 10
						target_state.station2_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 11)
						target_state.station2_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 2
						target_state.station2_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 12
						target_state.station2_location = 11
				elif transition == 2:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 10
						target_state.station2_location = 9
				elif transition == 3:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 11)
						target_state.station2_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 2
						target_state.station2_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 3
						target_state.station2_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 11)
						target_state.station2_location = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 12
						target_state.station2_location = 11

# Automaton: timer
class timerAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[0, 5]]
		self.branch_counts = [[1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		pass
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = 0
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[0]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[0][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = 0
		if location == 0:
			if transition == 0:
				return (state.t >= 80)
			elif transition == 1:
				return (state.t < 80)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = 0
		if location == 0:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass
				elif transition == 1:
					if branch == 0:
						target_state.t = min((state.t + 1), 80)

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_medium", "_aut_station1", "_aut_station2", "_aut_timer")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ", 1: "finish1", 2: "finish2", 3: "send1", 4: "send2", 5: "time" }
		self.sync_vectors = [[0, -1, -1, -1, 0], [-1, 0, -1, -1, 0], [-1, -1, 0, -1, 0], [-1, -1, -1, 0, 0], [1, 1, -1, -1, 1], [2, -1, 2, -1, 2], [3, 3, -1, -1, 3], [4, -1, 4, -1, 4], [-1, 5, 5, 5, 5]]
		self.properties = [
			Property("deadline", PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("c1", None, "int", 0, 2),
			VariableInfo("c2", None, "int", 0, 2),
			VariableInfo("x1", None, "int", 0, 11),
			VariableInfo("s1", None, "int", 1, 12),
			VariableInfo("slot1", None, "int", 0, 1),
			VariableInfo("backoff1", None, "int", 0, 15),
			VariableInfo("x2", None, "int", 0, 11),
			VariableInfo("s2", None, "int", 1, 12),
			VariableInfo("slot2", None, "int", 0, 1),
			VariableInfo("backoff2", None, "int", 0, 15),
			VariableInfo("t", None, "int", 0, 80),
			VariableInfo("station1_location", 1, "int", 0, 11),
			VariableInfo("station2_location", 2, "int", 0, 11)
		]
		self._aut_medium = mediumAutomaton(self)
		self._aut_station1 = station1Automaton(self)
		self._aut_station2 = station2Automaton(self)
		self._aut_timer = timerAutomaton(self)
		self.components = [self._aut_medium, self._aut_station1, self._aut_station2, self._aut_timer]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.c1 = 0
		state.c2 = 0
		state.x1 = 0
		state.s1 = 1
		state.slot1 = 0
		state.backoff1 = 0
		state.x2 = 0
		state.s2 = 1
		state.slot2 = 0
		state.backoff2 = 0
		state.t = 0
		self._aut_medium.set_initial_values(state)
		self._aut_station1.set_initial_values(state)
		self._aut_station2.set_initial_values(state)
		self._aut_timer.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_medium.set_initial_transient_values(transient)
		self._aut_station1.set_initial_transient_values(transient)
		self._aut_station2.set_initial_transient_values(transient)
		self._aut_timer.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return ((state.s1 == 12) and (state.s2 == 12))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return ((state.s1 == 12) and (state.s2 == 12))
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_medium.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_station1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_station2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_timer.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_medium = [[], [], [], [], [], []]
		transition_count = self._aut_medium.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_medium.get_guard_value(state, i):
				trans_medium[self._aut_medium.get_transition_label(state, i)].append(i)
		trans_station1 = [[], [], [], [], [], []]
		transition_count = self._aut_station1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_station1.get_guard_value(state, i):
				trans_station1[self._aut_station1.get_transition_label(state, i)].append(i)
		trans_station2 = [[], [], [], [], [], []]
		transition_count = self._aut_station2.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_station2.get_guard_value(state, i):
				trans_station2[self._aut_station2.get_transition_label(state, i)].append(i)
		trans_timer = [[], [], [], [], [], []]
		transition_count = self._aut_timer.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_timer.get_guard_value(state, i):
				trans_timer[self._aut_timer.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1]]
			# medium
			if synced is not None:
				if sv[0] != -1:
					if len(trans_medium[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_medium[sv[0]][0]
						for i in range(1, len(trans_medium[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_medium[sv[0]][i]
			# station1
			if synced is not None:
				if sv[1] != -1:
					if len(trans_station1[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_station1[sv[1]][0]
						for i in range(1, len(trans_station1[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_station1[sv[1]][i]
			# station2
			if synced is not None:
				if sv[2] != -1:
					if len(trans_station2[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_station2[sv[2]][0]
						for i in range(1, len(trans_station2[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_station2[sv[2]][i]
			# timer
			if synced is not None:
				if sv[3] != -1:
					if len(trans_timer[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_timer[sv[3]][0]
						for i in range(1, len(trans_timer[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_timer[sv[3]][i]
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
		combs = [[-1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_medium.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_medium.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_medium.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_station1.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_station1.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_station1.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_station2.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_station2.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_station2.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_timer.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_timer.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_timer.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
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
				self._aut_medium.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_station1.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_station2.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_timer.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
