# firewire.false

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
	__slots__ = ("w12", "y1", "y2", "x1", "s1", "w21", "z1", "z2", "x2", "s2", "node1_location", "wire21_location", "node2_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.w12
		elif variable == 1:
			return self.y1
		elif variable == 2:
			return self.y2
		elif variable == 3:
			return self.x1
		elif variable == 4:
			return self.s1
		elif variable == 5:
			return self.w21
		elif variable == 6:
			return self.z1
		elif variable == 7:
			return self.z2
		elif variable == 8:
			return self.x2
		elif variable == 9:
			return self.s2
		elif variable == 10:
			return self.node1_location
		elif variable == 11:
			return self.wire21_location
		elif variable == 12:
			return self.node2_location
	
	def copy_to(self, other: State):
		other.w12 = self.w12
		other.y1 = self.y1
		other.y2 = self.y2
		other.x1 = self.x1
		other.s1 = self.s1
		other.w21 = self.w21
		other.z1 = self.z1
		other.z2 = self.z2
		other.x2 = self.x2
		other.s2 = self.s2
		other.node1_location = self.node1_location
		other.wire21_location = self.wire21_location
		other.node2_location = self.node2_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.w12 == other.w12 and self.y1 == other.y1 and self.y2 == other.y2 and self.x1 == other.x1 and self.s1 == other.s1 and self.w21 == other.w21 and self.z1 == other.z1 and self.z2 == other.z2 and self.x2 == other.x2 and self.s2 == other.s2 and self.node1_location == other.node1_location and self.wire21_location == other.wire21_location and self.node2_location == other.node2_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.w12)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.y1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.y2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.s1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.w21)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.z1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.z2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.s2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.node1_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.wire21_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.node2_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "w12 = " + str(self.w12)
		result += ", y1 = " + str(self.y1)
		result += ", y2 = " + str(self.y2)
		result += ", x1 = " + str(self.x1)
		result += ", s1 = " + str(self.s1)
		result += ", w21 = " + str(self.w21)
		result += ", z1 = " + str(self.z1)
		result += ", z2 = " + str(self.z2)
		result += ", x2 = " + str(self.x2)
		result += ", s2 = " + str(self.s2)
		result += ", node1_location = " + str(self.node1_location)
		result += ", wire21_location = " + str(self.wire21_location)
		result += ", node2_location = " + str(self.node2_location)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("done", "time", "time_sending")
	
	def copy_to(self, other: Transient):
		other.done = self.done
		other.time = self.time
		other.time_sending = self.time_sending
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.done == other.done and self.time == other.time and self.time_sending == other.time_sending
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.done)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.time_sending)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "done = " + str(self.done)
		result += ", time = " + str(self.time)
		result += ", time_sending = " + str(self.time_sending)
		result += ")"
		return result

# Automaton: wire12
class wire12Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [29]
		self.transition_labels = [[1, 1, 1, 3, 3, 3, 5, 5, 5, 7, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11, 13, 13]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		pass
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = 0
		if location == 0:
			if transient_variable == "done":
				return (((state.s1 == 8) and (state.s2 == 7)) or ((state.s1 == 7) and (state.s2 == 8)))
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[0]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[0][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = 0
		if location == 0:
			if transition == 0:
				return (state.w12 == 3)
			elif transition == 1:
				return (state.w12 == 4)
			elif transition == 2:
				return (state.w12 == 7)
			elif transition == 3:
				return (state.w12 == 6)
			elif transition == 4:
				return (state.w12 == 5)
			elif transition == 5:
				return (state.w12 == 9)
			elif transition == 6:
				return (state.w12 == 1)
			elif transition == 7:
				return (state.w12 == 8)
			elif transition == 8:
				return (state.w12 == 2)
			elif transition == 9:
				return (state.w12 == 3)
			elif transition == 10:
				return (state.w12 == 0)
			elif transition == 11:
				return (state.w12 == 2)
			elif transition == 12:
				return (state.w12 == 5)
			elif transition == 13:
				return (state.w12 == 9)
			elif transition >= 14 and transition < 16:
				return (state.w12 == 1)
			elif transition == 16:
				return (state.w12 == 0)
			elif transition == 17:
				return (state.w12 == 4)
			elif transition == 18:
				return (state.w12 == 5)
			elif transition == 19:
				return (state.w12 == 8)
			elif transition >= 20 and transition < 22:
				return (state.w12 == 3)
			elif transition == 22:
				return (state.w12 == 5)
			elif transition == 23:
				return (state.w12 == 0)
			elif transition == 24:
				return (state.w12 == 1)
			elif transition == 25:
				return (state.w12 == 7)
			elif transition == 26:
				return (state.w12 == 6)
			elif transition == 27:
				return ((((((((((state.w12 == 1) and (state.y2 < 3)) or ((state.w12 == 5) and (state.y2 < 3))) or ((state.w12 == 6) and (state.y1 < 3))) or ((state.w12 == 7) and (state.y1 < 3))) or ((state.w12 == 4) and (state.y1 < 3))) or ((state.w12 == 8) and (state.y1 < 3))) or ((state.w12 == 2) and (state.y1 < 3))) or ((state.w12 == 3) and (state.y2 < 3))) or ((state.w12 == 9) and (state.y1 < 3)))
			elif transition == 28:
				return (state.w12 == 0)
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
						target_state.w12 = 0
						target_state.y1 = 0
						target_state.y2 = 0
				elif transition == 1:
					if branch == 0:
						target_state.w12 = 5
				elif transition == 2:
					if branch == 0:
						target_state.w12 = 1
				elif transition == 3:
					if branch == 0:
						target_state.w12 = 1
				elif transition == 4:
					if branch == 0:
						target_state.w12 = 0
						target_state.y1 = 0
						target_state.y2 = 0
				elif transition == 5:
					if branch == 0:
						target_state.w12 = 3
				elif transition == 6:
					if branch == 0:
						target_state.w12 = 0
						target_state.y1 = 0
						target_state.y2 = 0
				elif transition == 7:
					if branch == 0:
						target_state.w12 = 5
				elif transition == 8:
					if branch == 0:
						target_state.w12 = 3
				elif transition == 9:
					if branch == 0:
						target_state.w12 = 3
				elif transition == 10:
					if branch == 0:
						target_state.w12 = 3
						target_state.y1 = 0
						target_state.y2 = 0
				elif transition == 11:
					if branch == 0:
						target_state.w12 = 2
				elif transition == 12:
					if branch == 0:
						target_state.w12 = 9
						target_state.y2 = 0
				elif transition == 13:
					if branch == 0:
						target_state.w12 = 9
				elif transition == 14:
					if branch == 0:
						target_state.w12 = 2
						target_state.y2 = 0
				elif transition == 15:
					if branch == 0:
						target_state.w12 = 8
						target_state.y2 = 0
				elif transition == 16:
					if branch == 0:
						target_state.w12 = 5
						target_state.y1 = 0
						target_state.y2 = 0
				elif transition == 17:
					if branch == 0:
						target_state.w12 = 4
				elif transition == 18:
					if branch == 0:
						target_state.w12 = 5
				elif transition == 19:
					if branch == 0:
						target_state.w12 = 8
				elif transition == 20:
					if branch == 0:
						target_state.w12 = 4
						target_state.y2 = 0
				elif transition == 21:
					if branch == 0:
						target_state.w12 = 7
						target_state.y2 = 0
				elif transition == 22:
					if branch == 0:
						target_state.w12 = 6
						target_state.y2 = 0
				elif transition == 23:
					if branch == 0:
						target_state.w12 = 1
						target_state.y1 = 0
						target_state.y2 = 0
				elif transition == 24:
					if branch == 0:
						target_state.w12 = 1
				elif transition == 25:
					if branch == 0:
						target_state.w12 = 7
				elif transition == 26:
					if branch == 0:
						target_state.w12 = 6
				elif transition == 27:
					if branch == 0:
						target_state.y1 = min((state.y1 + 1), 4)
						target_state.y2 = min((state.y2 + 1), 4)
						target_transient.time = 1
						target_transient.time_sending = (1 if ((state.w12 > 0) or (state.w21 > 0)) else 0)
				elif transition == 28:
					if branch == 0:
						target_transient.time = 1
						target_transient.time_sending = (1 if ((state.w12 > 0) or (state.w21 > 0)) else 0)

# Automaton: node1
class node1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 3, 3, 3, 3, 3, 2, 2]
		self.transition_labels = [[4, 9], [6, 9], [4, 7, 13], [4, 7, 13], [6, 11, 13], [6, 11, 13], [2, 6, 13], [0, 13], [0, 13]]
		self.branch_counts = [[1, 2], [1, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.node1_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.node1_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.node1_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.node1_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.node1_location
		if location == 0:
			return True
		elif location == 1:
			return True
		elif location == 2:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.x1 >= 76)
			elif transition == 2:
				return (state.x1 < 85)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.x1 >= 159)
			elif transition == 2:
				return (state.x1 < 167)
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.x1 >= 76)
			elif transition == 2:
				return (state.x1 < 85)
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.x1 >= 159)
			elif transition == 2:
				return (state.x1 < 167)
			else:
				raise IndexError
		elif location == 6:
			return True
		elif location == 7:
			if transition == 0:
				return (state.s2 == 8)
			elif transition == 1:
				return True
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return (state.s2 == 7)
			elif transition == 1:
				return True
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.node1_location
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
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 8:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.node1_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.node1_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				if True:
					return (5 / 10)
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				if True:
					return (5 / 10)
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
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.node1_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 1
						target_state.node1_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 2
						target_state.node1_location = 2
					elif branch == 1:
						target_state.x1 = 0
						target_state.s1 = 3
						target_state.node1_location = 3
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 0
						target_state.node1_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 4
						target_state.node1_location = 4
					elif branch == 1:
						target_state.x1 = 0
						target_state.s1 = 5
						target_state.node1_location = 5
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 4
						target_state.node1_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 7
						target_state.node1_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 168)
						target_state.node1_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 5
						target_state.node1_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 7
						target_state.node1_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 168)
						target_state.node1_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 2
						target_state.node1_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 6
						target_state.node1_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 168)
						target_state.node1_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 3
						target_state.node1_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.x1 = 0
						target_state.s1 = 6
						target_state.node1_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 168)
						target_state.node1_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.s1 = 8
						target_state.node1_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.s1 = 0
						target_state.node1_location = 0
				elif transition == 2:
					if branch == 0:
						target_state.node1_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.node1_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.node1_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.node1_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.node1_location = 8

# Automaton: wire21
class wire21Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [4, 5, 3, 5, 3, 5, 3, 3, 3, 3]
		self.transition_labels = [[8, 10, 12, 13], [6, 8, 10, 12, 13], [6, 8, 13], [2, 8, 10, 12, 13], [2, 10, 13], [4, 8, 10, 12, 13], [4, 12, 13], [2, 12, 13], [6, 10, 13], [4, 8, 13]]
		self.branch_counts = [[1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.wire21_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.wire21_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.wire21_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.wire21_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.wire21_location
		if location == 0:
			return True
		elif location == 1:
			if transition >= 0 and transition < 4:
				return True
			elif transition == 4:
				return (state.z2 < 3)
			else:
				raise IndexError
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
			elif transition == 2:
				return (state.z1 < 3)
			else:
				raise IndexError
		elif location == 3:
			if transition >= 0 and transition < 4:
				return True
			elif transition == 4:
				return (state.z2 < 3)
			else:
				raise IndexError
		elif location == 4:
			if transition >= 0 and transition < 2:
				return True
			elif transition == 2:
				return (state.z1 < 3)
			else:
				raise IndexError
		elif location == 5:
			if transition >= 0 and transition < 4:
				return True
			elif transition == 4:
				return (state.z2 < 3)
			else:
				raise IndexError
		elif location == 6:
			if transition >= 0 and transition < 2:
				return True
			elif transition == 2:
				return (state.z1 < 3)
			else:
				raise IndexError
		elif location == 7:
			if transition >= 0 and transition < 2:
				return True
			elif transition == 2:
				return (state.z1 < 3)
			else:
				raise IndexError
		elif location == 8:
			if transition >= 0 and transition < 2:
				return True
			elif transition == 2:
				return (state.z1 < 3)
			else:
				raise IndexError
		elif location == 9:
			if transition >= 0 and transition < 2:
				return True
			elif transition == 2:
				return (state.z1 < 3)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.wire21_location
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
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.wire21_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.wire21_location
		if location == 0:
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
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 5:
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
			elif transition == 2:
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
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.wire21_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 3
						target_state.z1 = 0
						target_state.z2 = 0
						target_state.wire21_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 5
						target_state.z1 = 0
						target_state.z2 = 0
						target_state.wire21_location = 5
				elif transition == 2:
					if branch == 0:
						target_state.w21 = 1
						target_state.z1 = 0
						target_state.z2 = 0
						target_state.wire21_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.wire21_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 0
						target_state.z1 = 0
						target_state.z2 = 0
						target_state.wire21_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 2
						target_state.z2 = 0
						target_state.wire21_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.w21 = 8
						target_state.z2 = 0
						target_state.wire21_location = 8
				elif transition == 3:
					if branch == 0:
						target_state.w21 = 1
						target_state.wire21_location = 1
				elif transition == 4:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 3
						target_state.wire21_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 2
						target_state.wire21_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 0
						target_state.z1 = 0
						target_state.z2 = 0
						target_state.wire21_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 3
						target_state.wire21_location = 3
				elif transition == 2:
					if branch == 0:
						target_state.w21 = 4
						target_state.z2 = 0
						target_state.wire21_location = 4
				elif transition == 3:
					if branch == 0:
						target_state.w21 = 7
						target_state.z2 = 0
						target_state.wire21_location = 7
				elif transition == 4:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 5
						target_state.wire21_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 4
						target_state.wire21_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 0
						target_state.z1 = 0
						target_state.z2 = 0
						target_state.wire21_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 9
						target_state.z2 = 0
						target_state.wire21_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.w21 = 5
						target_state.wire21_location = 5
				elif transition == 3:
					if branch == 0:
						target_state.w21 = 6
						target_state.z2 = 0
						target_state.wire21_location = 6
				elif transition == 4:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 1
						target_state.wire21_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 6
						target_state.wire21_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 1
						target_state.wire21_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 7
						target_state.wire21_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 5
						target_state.wire21_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 8
						target_state.wire21_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.w21 = 3
						target_state.wire21_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.w21 = 9
						target_state.wire21_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.z1 = min((state.z1 + 1), 4)
						target_state.z2 = min((state.z2 + 1), 4)
						target_state.wire21_location = 9

# Automaton: node2
class node2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 3, 3, 3, 3, 3, 2, 2]
		self.transition_labels = [[3, 10], [5, 10], [3, 8, 13], [3, 8, 13], [5, 12, 13], [5, 12, 13], [1, 5, 13], [0, 13], [0, 13]]
		self.branch_counts = [[1, 2], [1, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.node2_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.node2_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.node2_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.node2_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.node2_location
		if location == 0:
			return True
		elif location == 1:
			return True
		elif location == 2:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.x2 >= 76)
			elif transition == 2:
				return (state.x2 < 85)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.x2 >= 159)
			elif transition == 2:
				return (state.x2 < 167)
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.x2 >= 76)
			elif transition == 2:
				return (state.x2 < 85)
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.x2 >= 159)
			elif transition == 2:
				return (state.x2 < 167)
			else:
				raise IndexError
		elif location == 6:
			return True
		elif location == 7:
			if transition == 0:
				return (state.s1 == 8)
			elif transition == 1:
				return True
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return (state.s1 == 7)
			elif transition == 1:
				return True
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.node2_location
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
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 8:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.node2_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.node2_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				if True:
					return (5 / 10)
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				if True:
					return (5 / 10)
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
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.node2_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 1
						target_state.node2_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 2
						target_state.node2_location = 2
					elif branch == 1:
						target_state.x2 = 0
						target_state.s2 = 3
						target_state.node2_location = 3
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 0
						target_state.node2_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 4
						target_state.node2_location = 4
					elif branch == 1:
						target_state.x2 = 0
						target_state.s2 = 5
						target_state.node2_location = 5
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 4
						target_state.node2_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 7
						target_state.node2_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 168)
						target_state.node2_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 5
						target_state.node2_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 7
						target_state.node2_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 168)
						target_state.node2_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 2
						target_state.node2_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 6
						target_state.node2_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 168)
						target_state.node2_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 3
						target_state.node2_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.x2 = 0
						target_state.s2 = 6
						target_state.node2_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 168)
						target_state.node2_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.s2 = 8
						target_state.node2_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.s2 = 0
						target_state.node2_location = 0
				elif transition == 2:
					if branch == 0:
						target_state.node2_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.node2_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.node2_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.node2_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.node2_location = 8

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_wire12", "_aut_node1", "_aut_wire21", "_aut_node2")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ", 1: "rec_ack12", 2: "rec_ack21", 3: "rec_idle12", 4: "rec_idle21", 5: "rec_req12", 6: "rec_req21", 7: "snd_ack12", 8: "snd_ack21", 9: "snd_idle12", 10: "snd_idle21", 11: "snd_req12", 12: "snd_req21", 13: "time" }
		self.sync_vectors = [[0, -1, -1, -1, 0], [-1, 0, -1, -1, 0], [-1, -1, 0, -1, 0], [-1, -1, -1, 0, 0], [1, -1, -1, 1, 1], [-1, 2, 2, -1, 2], [3, -1, -1, 3, 3], [-1, 4, 4, -1, 4], [5, -1, -1, 5, 5], [-1, 6, 6, -1, 6], [7, 7, -1, -1, 7], [-1, -1, 8, 8, 8], [9, 9, -1, -1, 9], [-1, -1, 10, 10, 10], [11, 11, -1, -1, 11], [-1, -1, 12, 12, 12], [13, 13, 13, 13, 13]]
		self.properties = [
			Property("elected", PropertyExpression(">=", [PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]), 1.0])),
			Property("time_max", PropertyExpression("e_max_s", [1, PropertyExpression("ap", [0])])),
			Property("time_min", PropertyExpression("e_min_s", [1, PropertyExpression("ap", [0])])),
			Property("time_sending", PropertyExpression("e_max_s", [2, PropertyExpression("ap", [0])])),
		]
		self.variables = [
			VariableInfo("w12", None, "int", 0, 9),
			VariableInfo("y1", None, "int", 0, 4),
			VariableInfo("y2", None, "int", 0, 4),
			VariableInfo("x1", None, "int", 0, 168),
			VariableInfo("s1", None, "int", 0, 8),
			VariableInfo("w21", None, "int", 0, 9),
			VariableInfo("z1", None, "int", 0, 4),
			VariableInfo("z2", None, "int", 0, 4),
			VariableInfo("x2", None, "int", 0, 168),
			VariableInfo("s2", None, "int", 0, 8),
			VariableInfo("node1_location", 1, "int", 0, 8),
			VariableInfo("wire21_location", 2, "int", 0, 9),
			VariableInfo("node2_location", 3, "int", 0, 8)
		]
		self._aut_wire12 = wire12Automaton(self)
		self._aut_node1 = node1Automaton(self)
		self._aut_wire21 = wire21Automaton(self)
		self._aut_node2 = node2Automaton(self)
		self.components = [self._aut_wire12, self._aut_node1, self._aut_wire21, self._aut_node2]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.w12 = 0
		state.y1 = 0
		state.y2 = 0
		state.x1 = 0
		state.s1 = 0
		state.w21 = 0
		state.z1 = 0
		state.z2 = 0
		state.x2 = 0
		state.s2 = 0
		self._aut_wire12.set_initial_values(state)
		self._aut_node1.set_initial_values(state)
		self._aut_wire21.set_initial_values(state)
		self._aut_node2.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.done = False
		transient.time = 0
		transient.time_sending = 0
		self._aut_wire12.set_initial_transient_values(transient)
		self._aut_node1.set_initial_transient_values(transient)
		self._aut_wire21.set_initial_transient_values(transient)
		self._aut_node2.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return self.network._get_transient_value(state, "done")
		elif expression == 1:
			return self.network._get_transient_value(state, "time")
		elif expression == 2:
			return self.network._get_transient_value(state, "time_sending")
		elif expression == 3:
			return (((state.s1 == 8) and (state.s2 == 7)) or ((state.s1 == 7) and (state.s2 == 8)))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return transient.done
		elif expression == 1:
			return transient.time
		elif expression == 2:
			return transient.time_sending
		elif expression == 3:
			return (((state.s1 == 8) and (state.s2 == 7)) or ((state.s1 == 7) and (state.s2 == 8)))
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_wire12.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_node1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_wire21.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_node2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_wire12 = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_wire12.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_wire12.get_guard_value(state, i):
				trans_wire12[self._aut_wire12.get_transition_label(state, i)].append(i)
		trans_node1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_node1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_node1.get_guard_value(state, i):
				trans_node1[self._aut_node1.get_transition_label(state, i)].append(i)
		trans_wire21 = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_wire21.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_wire21.get_guard_value(state, i):
				trans_wire21[self._aut_wire21.get_transition_label(state, i)].append(i)
		trans_node2 = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_node2.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_node2.get_guard_value(state, i):
				trans_node2[self._aut_node2.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1]]
			# wire12
			if synced is not None:
				if sv[0] != -1:
					if len(trans_wire12[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_wire12[sv[0]][0]
						for i in range(1, len(trans_wire12[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_wire12[sv[0]][i]
			# node1
			if synced is not None:
				if sv[1] != -1:
					if len(trans_node1[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_node1[sv[1]][0]
						for i in range(1, len(trans_node1[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_node1[sv[1]][i]
			# wire21
			if synced is not None:
				if sv[2] != -1:
					if len(trans_wire21[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_wire21[sv[2]][0]
						for i in range(1, len(trans_wire21[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_wire21[sv[2]][i]
			# node2
			if synced is not None:
				if sv[3] != -1:
					if len(trans_node2[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_node2[sv[3]][0]
						for i in range(1, len(trans_node2[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_node2[sv[3]][i]
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
			branch_count = self._aut_wire12.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_wire12.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_wire12.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_node1.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_node1.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_node1.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_wire21.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_wire21.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_wire21.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_node2.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_node2.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_node2.get_probability_value(state, transition.transitions[3], 0)
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
				self._aut_wire12.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_node1.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_wire21.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_node2.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
