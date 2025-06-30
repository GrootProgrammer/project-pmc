# philosophers-mdp.3

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
	__slots__ = ("p1", "p2", "p3", "phil1_location", "phil2_location", "phil3_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.p1
		elif variable == 1:
			return self.p2
		elif variable == 2:
			return self.p3
		elif variable == 3:
			return self.phil1_location
		elif variable == 4:
			return self.phil2_location
		elif variable == 5:
			return self.phil3_location
	
	def copy_to(self, other: State):
		other.p1 = self.p1
		other.p2 = self.p2
		other.p3 = self.p3
		other.phil1_location = self.phil1_location
		other.phil2_location = self.phil2_location
		other.phil3_location = self.phil3_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.p1 == other.p1 and self.p2 == other.p2 and self.p3 == other.p3 and self.phil1_location == other.phil1_location and self.phil2_location == other.phil2_location and self.phil3_location == other.phil3_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.phil1_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.phil2_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.phil3_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "p1 = " + str(self.p1)
		result += ", p2 = " + str(self.p2)
		result += ", p3 = " + str(self.p3)
		result += ", phil1_location = " + str(self.phil1_location)
		result += ", phil2_location = " + str(self.phil2_location)
		result += ", phil3_location = " + str(self.phil3_location)
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

# Automaton: phil1
class phil1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1]
		self.transition_labels = [[0, 0], [0], [0, 0], [0, 0], [0, 0], [0, 0], [0], [0], [0], [0, 0], [0], [0]]
		self.branch_counts = [[1, 1], [2], [1, 1], [1, 1], [1, 1], [1, 1], [1], [1], [1], [1, 1], [1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.phil1_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.phil1_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.phil1_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.phil1_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.phil1_location
		if location == 1 or location == 6 or location == 7 or location == 8 or location == 10 or location == 11:
			return True
		elif location == 0:
			return True
		elif location == 2:
			if transition == 0:
				return ((((state.p2 >= 0) and (state.p2 <= 4)) or (state.p2 == 6)) or (state.p2 == 10))
			elif transition == 1:
				return (not ((((state.p2 >= 0) and (state.p2 <= 4)) or (state.p2 == 6)) or (state.p2 == 10)))
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (((((state.p3 >= 0) and (state.p3 <= 3)) or (state.p3 == 5)) or (state.p3 == 7)) or (state.p3 == 11))
			elif transition == 1:
				return (not (((((state.p3 >= 0) and (state.p3 <= 3)) or (state.p3 == 5)) or (state.p3 == 7)) or (state.p3 == 11)))
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (((((state.p3 >= 0) and (state.p3 <= 3)) or (state.p3 == 5)) or (state.p3 == 7)) or (state.p3 == 11))
			elif transition == 1:
				return (not (((((state.p3 >= 0) and (state.p3 <= 3)) or (state.p3 == 5)) or (state.p3 == 7)) or (state.p3 == 11)))
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return ((((state.p2 >= 0) and (state.p2 <= 4)) or (state.p2 == 6)) or (state.p2 == 10))
			elif transition == 1:
				return (not ((((state.p2 >= 0) and (state.p2 <= 4)) or (state.p2 == 6)) or (state.p2 == 10)))
			else:
				raise IndexError
		elif location == 9:
			return True
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.phil1_location
		if location == 1 or location == 6 or location == 7 or location == 8 or location == 10 or location == 11:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 9:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.phil1_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.phil1_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				if True:
					return (5 / 10)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
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
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
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
			location = state.phil1_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 0
						target_state.phil1_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 1
						target_state.phil1_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 2
						target_state.phil1_location = 2
					elif branch == 1:
						target_state.p1 = 3
						target_state.phil1_location = 3
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 4
						target_state.phil1_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 2
						target_state.phil1_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 5
						target_state.phil1_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 3
						target_state.phil1_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 8
						target_state.phil1_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 6
						target_state.phil1_location = 6
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 8
						target_state.phil1_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 7
						target_state.phil1_location = 7
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 1
						target_state.phil1_location = 1
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 1
						target_state.phil1_location = 1
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 9
						target_state.phil1_location = 9
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 10
						target_state.phil1_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 11
						target_state.phil1_location = 11
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 0
						target_state.phil1_location = 0
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 0
						target_state.phil1_location = 0

# Automaton: phil2
class phil2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1]
		self.transition_labels = [[0, 0], [0], [0, 0], [0, 0], [0, 0], [0, 0], [0], [0], [0], [0, 0], [0], [0]]
		self.branch_counts = [[1, 1], [2], [1, 1], [1, 1], [1, 1], [1, 1], [1], [1], [1], [1, 1], [1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.phil2_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.phil2_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.phil2_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.phil2_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.phil2_location
		if location == 1 or location == 6 or location == 7 or location == 8 or location == 10 or location == 11:
			return True
		elif location == 0:
			return True
		elif location == 2:
			if transition == 0:
				return ((((state.p3 >= 0) and (state.p3 <= 4)) or (state.p3 == 6)) or (state.p3 == 10))
			elif transition == 1:
				return (not ((((state.p3 >= 0) and (state.p3 <= 4)) or (state.p3 == 6)) or (state.p3 == 10)))
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (((((state.p1 >= 0) and (state.p1 <= 3)) or (state.p1 == 5)) or (state.p1 == 7)) or (state.p1 == 11))
			elif transition == 1:
				return (not (((((state.p1 >= 0) and (state.p1 <= 3)) or (state.p1 == 5)) or (state.p1 == 7)) or (state.p1 == 11)))
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (((((state.p1 >= 0) and (state.p1 <= 3)) or (state.p1 == 5)) or (state.p1 == 7)) or (state.p1 == 11))
			elif transition == 1:
				return (not (((((state.p1 >= 0) and (state.p1 <= 3)) or (state.p1 == 5)) or (state.p1 == 7)) or (state.p1 == 11)))
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return ((((state.p3 >= 0) and (state.p3 <= 4)) or (state.p3 == 6)) or (state.p3 == 10))
			elif transition == 1:
				return (not ((((state.p3 >= 0) and (state.p3 <= 4)) or (state.p3 == 6)) or (state.p3 == 10)))
			else:
				raise IndexError
		elif location == 9:
			return True
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.phil2_location
		if location == 1 or location == 6 or location == 7 or location == 8 or location == 10 or location == 11:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 9:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.phil2_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.phil2_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				if True:
					return (5 / 10)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
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
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
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
			location = state.phil2_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 0
						target_state.phil2_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 1
						target_state.phil2_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 2
						target_state.phil2_location = 2
					elif branch == 1:
						target_state.p2 = 3
						target_state.phil2_location = 3
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 4
						target_state.phil2_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 2
						target_state.phil2_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 5
						target_state.phil2_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 3
						target_state.phil2_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 8
						target_state.phil2_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 6
						target_state.phil2_location = 6
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 8
						target_state.phil2_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 7
						target_state.phil2_location = 7
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 1
						target_state.phil2_location = 1
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 1
						target_state.phil2_location = 1
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 9
						target_state.phil2_location = 9
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 10
						target_state.phil2_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 11
						target_state.phil2_location = 11
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 0
						target_state.phil2_location = 0
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 0
						target_state.phil2_location = 0

# Automaton: phil3
class phil3Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1]
		self.transition_labels = [[0, 0], [0], [0, 0], [0, 0], [0, 0], [0, 0], [0], [0], [0], [0, 0], [0], [0]]
		self.branch_counts = [[1, 1], [2], [1, 1], [1, 1], [1, 1], [1, 1], [1], [1], [1], [1, 1], [1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.phil3_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.phil3_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.phil3_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.phil3_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.phil3_location
		if location == 1 or location == 6 or location == 7 or location == 8 or location == 10 or location == 11:
			return True
		elif location == 0:
			return True
		elif location == 2:
			if transition == 0:
				return ((((state.p1 >= 0) and (state.p1 <= 4)) or (state.p1 == 6)) or (state.p1 == 10))
			elif transition == 1:
				return (not ((((state.p1 >= 0) and (state.p1 <= 4)) or (state.p1 == 6)) or (state.p1 == 10)))
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (((((state.p2 >= 0) and (state.p2 <= 3)) or (state.p2 == 5)) or (state.p2 == 7)) or (state.p2 == 11))
			elif transition == 1:
				return (not (((((state.p2 >= 0) and (state.p2 <= 3)) or (state.p2 == 5)) or (state.p2 == 7)) or (state.p2 == 11)))
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (((((state.p2 >= 0) and (state.p2 <= 3)) or (state.p2 == 5)) or (state.p2 == 7)) or (state.p2 == 11))
			elif transition == 1:
				return (not (((((state.p2 >= 0) and (state.p2 <= 3)) or (state.p2 == 5)) or (state.p2 == 7)) or (state.p2 == 11)))
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return ((((state.p1 >= 0) and (state.p1 <= 4)) or (state.p1 == 6)) or (state.p1 == 10))
			elif transition == 1:
				return (not ((((state.p1 >= 0) and (state.p1 <= 4)) or (state.p1 == 6)) or (state.p1 == 10)))
			else:
				raise IndexError
		elif location == 9:
			return True
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.phil3_location
		if location == 1 or location == 6 or location == 7 or location == 8 or location == 10 or location == 11:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 9:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.phil3_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.phil3_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				if True:
					return (5 / 10)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
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
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
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
			location = state.phil3_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 0
						target_state.phil3_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.p3 = 1
						target_state.phil3_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 2
						target_state.phil3_location = 2
					elif branch == 1:
						target_state.p3 = 3
						target_state.phil3_location = 3
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 4
						target_state.phil3_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.p3 = 2
						target_state.phil3_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 5
						target_state.phil3_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.p3 = 3
						target_state.phil3_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 8
						target_state.phil3_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p3 = 6
						target_state.phil3_location = 6
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 8
						target_state.phil3_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p3 = 7
						target_state.phil3_location = 7
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 1
						target_state.phil3_location = 1
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 1
						target_state.phil3_location = 1
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 9
						target_state.phil3_location = 9
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 10
						target_state.phil3_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.p3 = 11
						target_state.phil3_location = 11
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 0
						target_state.phil3_location = 0
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.p3 = 0
						target_state.phil3_location = 0

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_phil1", "_aut_phil2", "_aut_phil3")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ" }
		self.sync_vectors = [[0, -1, -1, 0], [-1, 0, -1, 0], [-1, -1, 0, 0]]
		self.properties = [
			Property("eat", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("p1", None, "int", 0, 11),
			VariableInfo("p2", None, "int", 0, 11),
			VariableInfo("p3", None, "int", 0, 11),
			VariableInfo("phil1_location", 0, "int", 0, 11),
			VariableInfo("phil2_location", 1, "int", 0, 11),
			VariableInfo("phil3_location", 2, "int", 0, 11)
		]
		self._aut_phil1 = phil1Automaton(self)
		self._aut_phil2 = phil2Automaton(self)
		self._aut_phil3 = phil3Automaton(self)
		self.components = [self._aut_phil1, self._aut_phil2, self._aut_phil3]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.p1 = 0
		state.p2 = 0
		state.p3 = 0
		self._aut_phil1.set_initial_values(state)
		self._aut_phil2.set_initial_values(state)
		self._aut_phil3.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_phil1.set_initial_transient_values(transient)
		self._aut_phil2.set_initial_transient_values(transient)
		self._aut_phil3.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return ((((state.p1 >= 8) and (state.p1 <= 9)) or ((state.p2 >= 8) and (state.p2 <= 9))) or ((state.p3 >= 8) and (state.p3 <= 9)))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return ((((state.p1 >= 8) and (state.p1 <= 9)) or ((state.p2 >= 8) and (state.p2 <= 9))) or ((state.p3 >= 8) and (state.p3 <= 9)))
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_phil1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_phil2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_phil3.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_phil1 = [[]]
		transition_count = self._aut_phil1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_phil1.get_guard_value(state, i):
				trans_phil1[self._aut_phil1.get_transition_label(state, i)].append(i)
		trans_phil2 = [[]]
		transition_count = self._aut_phil2.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_phil2.get_guard_value(state, i):
				trans_phil2[self._aut_phil2.get_transition_label(state, i)].append(i)
		trans_phil3 = [[]]
		transition_count = self._aut_phil3.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_phil3.get_guard_value(state, i):
				trans_phil3[self._aut_phil3.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1]]
			# phil1
			if synced is not None:
				if sv[0] != -1:
					if len(trans_phil1[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_phil1[sv[0]][0]
						for i in range(1, len(trans_phil1[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_phil1[sv[0]][i]
			# phil2
			if synced is not None:
				if sv[1] != -1:
					if len(trans_phil2[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_phil2[sv[1]][0]
						for i in range(1, len(trans_phil2[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_phil2[sv[1]][i]
			# phil3
			if synced is not None:
				if sv[2] != -1:
					if len(trans_phil3[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_phil3[sv[2]][0]
						for i in range(1, len(trans_phil3[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_phil3[sv[2]][i]
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
		combs = [[-1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_phil1.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_phil1.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_phil1.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_phil2.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_phil2.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_phil2.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_phil3.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_phil3.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_phil3.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
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
				self._aut_phil1.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_phil2.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_phil3.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
