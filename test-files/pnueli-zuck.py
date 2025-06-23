# pnueli-zuck.3

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
	__slots__ = ("p0", "p1", "p2", "process0_location", "process1_location", "process2_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.p0
		elif variable == 1:
			return self.p1
		elif variable == 2:
			return self.p2
		elif variable == 3:
			return self.process0_location
		elif variable == 4:
			return self.process1_location
		elif variable == 5:
			return self.process2_location
	
	def copy_to(self, other: State):
		other.p0 = self.p0
		other.p1 = self.p1
		other.p2 = self.p2
		other.process0_location = self.process0_location
		other.process1_location = self.process1_location
		other.process2_location = self.process2_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.p0 == other.p0 and self.p1 == other.p1 and self.p2 == other.p2 and self.process0_location == other.process0_location and self.process1_location == other.process1_location and self.process2_location == other.process2_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p0)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.process0_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.process1_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.process2_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "p0 = " + str(self.p0)
		result += ", p1 = " + str(self.p1)
		result += ", p2 = " + str(self.p2)
		result += ", process0_location = " + str(self.process0_location)
		result += ", process1_location = " + str(self.process1_location)
		result += ", process2_location = " + str(self.process2_location)
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

# Automaton: process0
class process0Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1]
		self.transition_labels = [[0, 0], [0], [0, 0], [0, 0], [0, 0], [0], [0, 0], [0, 0], [0], [0], [0], [0, 0], [0], [0], [0, 0], [0]]
		self.branch_counts = [[1, 1], [1], [1, 1], [1, 1], [1, 1], [1], [1, 1], [1, 1], [1], [2], [1], [1, 1], [1], [1], [1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.process0_location = 1
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.process0_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.process0_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.process0_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.process0_location
		if location == 1 or location == 5 or location == 8 or location == 9 or location == 10 or location == 12 or location == 13 or location == 15:
			return True
		elif location == 0:
			return True
		elif location == 2:
			if transition == 0:
				return ((((state.p1 < 4) or (state.p1 > 13)) and ((state.p2 < 4) or (state.p2 > 13))) or (((state.p1 >= 14) and (state.p1 <= 15)) or ((state.p2 >= 14) and (state.p2 <= 15))))
			elif transition == 1:
				return (not ((((state.p1 < 4) or (state.p1 > 13)) and ((state.p2 < 4) or (state.p2 > 13))) or (((state.p1 >= 14) and (state.p1 <= 15)) or ((state.p2 >= 14) and (state.p2 <= 15)))))
			else:
				raise IndexError
		elif location == 3:
			return True
		elif location == 4:
			if transition == 0:
				return (((((state.p1 >= 4) and (state.p1 <= 5)) or ((state.p1 >= 10) and (state.p1 <= 15))) or ((state.p2 >= 4) and (state.p2 <= 5))) or ((state.p2 >= 10) and (state.p2 <= 15)))
			elif transition == 1:
				return (not (((((state.p1 >= 4) and (state.p1 <= 5)) or ((state.p1 >= 10) and (state.p1 <= 15))) or ((state.p2 >= 4) and (state.p2 <= 5))) or ((state.p2 >= 10) and (state.p2 <= 15))))
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return (((((state.p1 >= 4) and (state.p1 <= 5)) or ((state.p1 >= 10) and (state.p1 <= 15))) or ((state.p2 >= 4) and (state.p2 <= 5))) or ((state.p2 >= 10) and (state.p2 <= 15)))
			elif transition == 1:
				return (not (((((state.p1 >= 4) and (state.p1 <= 5)) or ((state.p1 >= 10) and (state.p1 <= 15))) or ((state.p2 >= 4) and (state.p2 <= 5))) or ((state.p2 >= 10) and (state.p2 <= 15))))
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (((((state.p1 >= 0) and (state.p1 <= 3)) or ((state.p1 >= 7) and (state.p1 <= 8))) or ((state.p2 >= 0) and (state.p2 <= 3))) or ((state.p2 >= 7) and (state.p2 <= 8)))
			elif transition == 1:
				return (not (((((state.p1 >= 0) and (state.p1 <= 3)) or ((state.p1 >= 7) and (state.p1 <= 8))) or ((state.p2 >= 0) and (state.p2 <= 3))) or ((state.p2 >= 7) and (state.p2 <= 8))))
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return (((state.p1 < 4) or (state.p1 > 13)) and ((state.p2 < 4) or (state.p2 > 13)))
			elif transition == 1:
				return (not (((state.p1 < 4) or (state.p1 > 13)) and ((state.p2 < 4) or (state.p2 > 13))))
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return (((state.p1 < 2) or (state.p1 > 3)) and ((state.p2 < 2) or (state.p2 > 3)))
			elif transition == 1:
				return (not (((state.p1 < 2) or (state.p1 > 3)) and ((state.p2 < 2) or (state.p2 > 3))))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.process0_location
		if location == 1 or location == 5 or location == 8 or location == 9 or location == 10 or location == 12 or location == 13 or location == 15:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 11:
			return None
		elif location == 14:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.process0_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.process0_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
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
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
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
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				if True:
					return (5 / 10)
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
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.process0_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 0
						target_state.process0_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.p0 = 1
						target_state.process0_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 2
						target_state.process0_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 3
						target_state.process0_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.p0 = 2
						target_state.process0_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 4
						target_state.process0_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.p0 = 7
						target_state.process0_location = 7
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 5
						target_state.process0_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.p0 = 10
						target_state.process0_location = 10
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 6
						target_state.process0_location = 6
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 6
						target_state.process0_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.p0 = 9
						target_state.process0_location = 9
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 8
						target_state.process0_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p0 = 7
						target_state.process0_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 9
						target_state.process0_location = 9
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 4
						target_state.process0_location = 4
					elif branch == 1:
						target_state.p0 = 7
						target_state.process0_location = 7
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 11
						target_state.process0_location = 11
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 13
						target_state.process0_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.p0 = 12
						target_state.process0_location = 12
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 0
						target_state.process0_location = 0
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 14
						target_state.process0_location = 14
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 15
						target_state.process0_location = 15
				elif transition == 1:
					if branch == 0:
						target_state.p0 = 14
						target_state.process0_location = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.p0 = 0
						target_state.process0_location = 0

# Automaton: process1
class process1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1]
		self.transition_labels = [[0, 0], [0], [0, 0], [0, 0], [0, 0], [0], [0, 0], [0, 0], [0], [0], [0], [0, 0], [0], [0], [0, 0], [0]]
		self.branch_counts = [[1, 1], [1], [1, 1], [1, 1], [1, 1], [1], [1, 1], [1, 1], [1], [2], [1], [1, 1], [1], [1], [1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.process1_location = 1
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.process1_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.process1_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.process1_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.process1_location
		if location == 1 or location == 5 or location == 8 or location == 9 or location == 10 or location == 12 or location == 13 or location == 15:
			return True
		elif location == 0:
			return True
		elif location == 2:
			if transition == 0:
				return ((((state.p0 < 4) or (state.p0 > 13)) and ((state.p2 < 4) or (state.p2 > 13))) or (((state.p0 >= 14) and (state.p0 <= 15)) or ((state.p2 >= 14) and (state.p2 <= 15))))
			elif transition == 1:
				return (not ((((state.p0 < 4) or (state.p0 > 13)) and ((state.p2 < 4) or (state.p2 > 13))) or (((state.p0 >= 14) and (state.p0 <= 15)) or ((state.p2 >= 14) and (state.p2 <= 15)))))
			else:
				raise IndexError
		elif location == 3:
			return True
		elif location == 4:
			if transition == 0:
				return (((((state.p0 >= 4) and (state.p0 <= 5)) or ((state.p0 >= 10) and (state.p0 <= 15))) or ((state.p2 >= 4) and (state.p2 <= 5))) or ((state.p2 >= 10) and (state.p2 <= 15)))
			elif transition == 1:
				return (not (((((state.p0 >= 4) and (state.p0 <= 5)) or ((state.p0 >= 10) and (state.p0 <= 15))) or ((state.p2 >= 4) and (state.p2 <= 5))) or ((state.p2 >= 10) and (state.p2 <= 15))))
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return (((((state.p0 >= 4) and (state.p0 <= 5)) or ((state.p0 >= 10) and (state.p0 <= 15))) or ((state.p2 >= 4) and (state.p2 <= 5))) or ((state.p2 >= 10) and (state.p2 <= 15)))
			elif transition == 1:
				return (not (((((state.p0 >= 4) and (state.p0 <= 5)) or ((state.p0 >= 10) and (state.p0 <= 15))) or ((state.p2 >= 4) and (state.p2 <= 5))) or ((state.p2 >= 10) and (state.p2 <= 15))))
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (((((state.p0 >= 0) and (state.p0 <= 3)) or ((state.p0 >= 7) and (state.p0 <= 8))) or ((state.p2 >= 0) and (state.p2 <= 3))) or ((state.p2 >= 7) and (state.p2 <= 8)))
			elif transition == 1:
				return (not (((((state.p0 >= 0) and (state.p0 <= 3)) or ((state.p0 >= 7) and (state.p0 <= 8))) or ((state.p2 >= 0) and (state.p2 <= 3))) or ((state.p2 >= 7) and (state.p2 <= 8))))
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return (((state.p0 < 4) or (state.p0 > 13)) and ((state.p2 < 4) or (state.p2 > 13)))
			elif transition == 1:
				return (not (((state.p0 < 4) or (state.p0 > 13)) and ((state.p2 < 4) or (state.p2 > 13))))
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return (((state.p0 < 2) or (state.p0 > 3)) and ((state.p2 < 2) or (state.p2 > 3)))
			elif transition == 1:
				return (not (((state.p0 < 2) or (state.p0 > 3)) and ((state.p2 < 2) or (state.p2 > 3))))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.process1_location
		if location == 1 or location == 5 or location == 8 or location == 9 or location == 10 or location == 12 or location == 13 or location == 15:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 11:
			return None
		elif location == 14:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.process1_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.process1_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
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
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
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
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				if True:
					return (5 / 10)
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
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.process1_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 0
						target_state.process1_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 1
						target_state.process1_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 2
						target_state.process1_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 3
						target_state.process1_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 2
						target_state.process1_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 4
						target_state.process1_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 7
						target_state.process1_location = 7
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 5
						target_state.process1_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 10
						target_state.process1_location = 10
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 6
						target_state.process1_location = 6
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 6
						target_state.process1_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 9
						target_state.process1_location = 9
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 8
						target_state.process1_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 7
						target_state.process1_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 9
						target_state.process1_location = 9
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 4
						target_state.process1_location = 4
					elif branch == 1:
						target_state.p1 = 7
						target_state.process1_location = 7
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 11
						target_state.process1_location = 11
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 13
						target_state.process1_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 12
						target_state.process1_location = 12
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 0
						target_state.process1_location = 0
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 14
						target_state.process1_location = 14
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 15
						target_state.process1_location = 15
				elif transition == 1:
					if branch == 0:
						target_state.p1 = 14
						target_state.process1_location = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.p1 = 0
						target_state.process1_location = 0

# Automaton: process2
class process2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1]
		self.transition_labels = [[0, 0], [0], [0, 0], [0, 0], [0, 0], [0], [0, 0], [0, 0], [0], [0], [0], [0, 0], [0], [0], [0, 0], [0]]
		self.branch_counts = [[1, 1], [1], [1, 1], [1, 1], [1, 1], [1], [1, 1], [1, 1], [1], [2], [1], [1, 1], [1], [1], [1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.process2_location = 1
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.process2_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.process2_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.process2_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.process2_location
		if location == 1 or location == 5 or location == 8 or location == 9 or location == 10 or location == 12 or location == 13 or location == 15:
			return True
		elif location == 0:
			return True
		elif location == 2:
			if transition == 0:
				return ((((state.p1 < 4) or (state.p1 > 13)) and ((state.p0 < 4) or (state.p0 > 13))) or (((state.p1 >= 14) and (state.p1 <= 15)) or ((state.p0 >= 14) and (state.p0 <= 15))))
			elif transition == 1:
				return (not ((((state.p1 < 4) or (state.p1 > 13)) and ((state.p0 < 4) or (state.p0 > 13))) or (((state.p1 >= 14) and (state.p1 <= 15)) or ((state.p0 >= 14) and (state.p0 <= 15)))))
			else:
				raise IndexError
		elif location == 3:
			return True
		elif location == 4:
			if transition == 0:
				return (((((state.p1 >= 4) and (state.p1 <= 5)) or ((state.p1 >= 10) and (state.p1 <= 15))) or ((state.p0 >= 4) and (state.p0 <= 5))) or ((state.p0 >= 10) and (state.p0 <= 15)))
			elif transition == 1:
				return (not (((((state.p1 >= 4) and (state.p1 <= 5)) or ((state.p1 >= 10) and (state.p1 <= 15))) or ((state.p0 >= 4) and (state.p0 <= 5))) or ((state.p0 >= 10) and (state.p0 <= 15))))
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return (((((state.p1 >= 4) and (state.p1 <= 5)) or ((state.p1 >= 10) and (state.p1 <= 15))) or ((state.p0 >= 4) and (state.p0 <= 5))) or ((state.p0 >= 10) and (state.p0 <= 15)))
			elif transition == 1:
				return (not (((((state.p1 >= 4) and (state.p1 <= 5)) or ((state.p1 >= 10) and (state.p1 <= 15))) or ((state.p0 >= 4) and (state.p0 <= 5))) or ((state.p0 >= 10) and (state.p0 <= 15))))
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (((((state.p1 >= 0) and (state.p1 <= 3)) or ((state.p1 >= 7) and (state.p1 <= 8))) or ((state.p0 >= 0) and (state.p0 <= 3))) or ((state.p0 >= 7) and (state.p0 <= 8)))
			elif transition == 1:
				return (not (((((state.p1 >= 0) and (state.p1 <= 3)) or ((state.p1 >= 7) and (state.p1 <= 8))) or ((state.p0 >= 0) and (state.p0 <= 3))) or ((state.p0 >= 7) and (state.p0 <= 8))))
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return (((state.p1 < 4) or (state.p1 > 13)) and ((state.p0 < 4) or (state.p0 > 13)))
			elif transition == 1:
				return (not (((state.p1 < 4) or (state.p1 > 13)) and ((state.p0 < 4) or (state.p0 > 13))))
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return (((state.p1 < 2) or (state.p1 > 3)) and ((state.p0 < 2) or (state.p0 > 3)))
			elif transition == 1:
				return (not (((state.p1 < 2) or (state.p1 > 3)) and ((state.p0 < 2) or (state.p0 > 3))))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.process2_location
		if location == 1 or location == 5 or location == 8 or location == 9 or location == 10 or location == 12 or location == 13 or location == 15:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 11:
			return None
		elif location == 14:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.process2_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.process2_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
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
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
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
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				if True:
					return (5 / 10)
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
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.process2_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 0
						target_state.process2_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 1
						target_state.process2_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 2
						target_state.process2_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 3
						target_state.process2_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 2
						target_state.process2_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 4
						target_state.process2_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 7
						target_state.process2_location = 7
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 5
						target_state.process2_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 10
						target_state.process2_location = 10
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 6
						target_state.process2_location = 6
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 6
						target_state.process2_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 9
						target_state.process2_location = 9
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 8
						target_state.process2_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 7
						target_state.process2_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 9
						target_state.process2_location = 9
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 4
						target_state.process2_location = 4
					elif branch == 1:
						target_state.p2 = 7
						target_state.process2_location = 7
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 11
						target_state.process2_location = 11
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 13
						target_state.process2_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 12
						target_state.process2_location = 12
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 0
						target_state.process2_location = 0
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 14
						target_state.process2_location = 14
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 15
						target_state.process2_location = 15
				elif transition == 1:
					if branch == 0:
						target_state.p2 = 14
						target_state.process2_location = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.p2 = 0
						target_state.process2_location = 0

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_process0", "_aut_process1", "_aut_process2")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ" }
		self.sync_vectors = [[0, -1, -1, 0], [-1, 0, -1, 0], [-1, -1, 0, 0]]
		self.properties = [
			Property("live", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("p0", None, "int", 0, 15),
			VariableInfo("p1", None, "int", 0, 15),
			VariableInfo("p2", None, "int", 0, 15),
			VariableInfo("process0_location", 0, "int", 0, 15),
			VariableInfo("process1_location", 1, "int", 0, 15),
			VariableInfo("process2_location", 2, "int", 0, 15)
		]
		self._aut_process0 = process0Automaton(self)
		self._aut_process1 = process1Automaton(self)
		self._aut_process2 = process2Automaton(self)
		self.components = [self._aut_process0, self._aut_process1, self._aut_process2]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.p0 = 1
		state.p1 = 1
		state.p2 = 1
		self._aut_process0.set_initial_values(state)
		self._aut_process1.set_initial_values(state)
		self._aut_process2.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_process0.set_initial_transient_values(transient)
		self._aut_process1.set_initial_transient_values(transient)
		self._aut_process2.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return (state.p1 == 10)
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return (state.p1 == 10)
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_process0.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_process0 = [[]]
		transition_count = self._aut_process0.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process0.get_guard_value(state, i):
				trans_process0[self._aut_process0.get_transition_label(state, i)].append(i)
		trans_process1 = [[]]
		transition_count = self._aut_process1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process1.get_guard_value(state, i):
				trans_process1[self._aut_process1.get_transition_label(state, i)].append(i)
		trans_process2 = [[]]
		transition_count = self._aut_process2.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process2.get_guard_value(state, i):
				trans_process2[self._aut_process2.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1]]
			# process0
			if synced is not None:
				if sv[0] != -1:
					if len(trans_process0[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_process0[sv[0]][0]
						for i in range(1, len(trans_process0[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_process0[sv[0]][i]
			# process1
			if synced is not None:
				if sv[1] != -1:
					if len(trans_process1[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_process1[sv[1]][0]
						for i in range(1, len(trans_process1[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_process1[sv[1]][i]
			# process2
			if synced is not None:
				if sv[2] != -1:
					if len(trans_process2[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_process2[sv[2]][0]
						for i in range(1, len(trans_process2[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_process2[sv[2]][i]
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
			branch_count = self._aut_process0.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_process0.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process0.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_process1.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_process1.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process1.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_process2.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_process2.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process2.get_probability_value(state, transition.transitions[2], 0)
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
				self._aut_process0.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_process1.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_process2.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
