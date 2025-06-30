# beb-3-4

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
	__slots__ = ("cr", "line_seized", "gave_up", "Clock_location", "Host_location", "na", "ev", "wt", "Host_1_location", "na_1", "ev_1", "wt_1", "Host_2_location", "na_2", "ev_2", "wt_2")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.cr
		elif variable == 1:
			return self.line_seized
		elif variable == 2:
			return self.gave_up
		elif variable == 3:
			return self.Clock_location
		elif variable == 4:
			return self.Host_location
		elif variable == 5:
			return self.na
		elif variable == 6:
			return self.ev
		elif variable == 7:
			return self.wt
		elif variable == 8:
			return self.Host_1_location
		elif variable == 9:
			return self.na_1
		elif variable == 10:
			return self.ev_1
		elif variable == 11:
			return self.wt_1
		elif variable == 12:
			return self.Host_2_location
		elif variable == 13:
			return self.na_2
		elif variable == 14:
			return self.ev_2
		elif variable == 15:
			return self.wt_2
	
	def copy_to(self, other: State):
		other.cr = self.cr
		other.line_seized = self.line_seized
		other.gave_up = self.gave_up
		other.Clock_location = self.Clock_location
		other.Host_location = self.Host_location
		other.na = self.na
		other.ev = self.ev
		other.wt = self.wt
		other.Host_1_location = self.Host_1_location
		other.na_1 = self.na_1
		other.ev_1 = self.ev_1
		other.wt_1 = self.wt_1
		other.Host_2_location = self.Host_2_location
		other.na_2 = self.na_2
		other.ev_2 = self.ev_2
		other.wt_2 = self.wt_2
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.cr == other.cr and self.line_seized == other.line_seized and self.gave_up == other.gave_up and self.Clock_location == other.Clock_location and self.Host_location == other.Host_location and self.na == other.na and self.ev == other.ev and self.wt == other.wt and self.Host_1_location == other.Host_1_location and self.na_1 == other.na_1 and self.ev_1 == other.ev_1 and self.wt_1 == other.wt_1 and self.Host_2_location == other.Host_2_location and self.na_2 == other.na_2 and self.ev_2 == other.ev_2 and self.wt_2 == other.wt_2
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cr)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.line_seized)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.gave_up)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Clock_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Host_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.na)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ev)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.wt)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Host_1_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.na_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ev_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.wt_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Host_2_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.na_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ev_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.wt_2)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "cr = " + str(self.cr)
		result += ", line_seized = " + str(self.line_seized)
		result += ", gave_up = " + str(self.gave_up)
		result += ", Clock_location = " + str(self.Clock_location)
		result += ", Host_location = " + str(self.Host_location)
		result += ", na = " + str(self.na)
		result += ", ev = " + str(self.ev)
		result += ", wt = " + str(self.wt)
		result += ", Host_1_location = " + str(self.Host_1_location)
		result += ", na_1 = " + str(self.na_1)
		result += ", ev_1 = " + str(self.ev_1)
		result += ", wt_1 = " + str(self.wt_1)
		result += ", Host_2_location = " + str(self.Host_2_location)
		result += ", na_2 = " + str(self.na_2)
		result += ", ev_2 = " + str(self.ev_2)
		result += ", wt_2 = " + str(self.wt_2)
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

# Automaton: Clock
class ClockAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1, 1, 1, 1]
		self.transition_labels = [[1], [2], [0], [3]]
		self.branch_counts = [[1], [1], [1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Clock_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Clock_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Clock_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Clock_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Clock_location
		if location == 0 or location == 1 or location == 2 or location == 3:
			return True
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Clock_location
		if location == 0 or location == 1 or location == 2 or location == 3:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Clock_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Clock_location
		if location == 0:
			if transition == 0:
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
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Clock_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Clock_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Clock_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.cr = 0
						target_state.Clock_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Clock_location = 0

# Automaton: Host
class HostAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 6, 1, 1, 2, 0]
		self.transition_labels = [[1, 0], [1], [0, 0, 0, 0, 0, 0], [2], [3], [1, 0], []]
		self.branch_counts = [[1, 1], [1], [1, 1, 1, 2, 3, 4], [1], [1], [1, 1], []]
	
	def set_initial_values(self, state: State) -> None:
		state.Host_location = 0
		state.na = 0
		state.ev = 2
		state.wt = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Host_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Host_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Host_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Host_location
		if location == 1 or location == 3 or location == 4:
			return True
		elif location == 0:
			if transition == 0:
				return (state.wt > 0)
			elif transition == 1:
				return (state.wt <= 0)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.cr == 1)
			elif transition == 1:
				return ((state.na >= 3) and (state.cr != 1))
			elif transition == 2:
				return (((state.na < 3) and (state.cr != 1)) and (max(0, (state.ev - 1)) == 0))
			elif transition == 3:
				return (((state.na < 3) and (state.cr != 1)) and (max(0, (state.ev - 1)) == 1))
			elif transition == 4:
				return (((state.na < 3) and (state.cr != 1)) and (max(0, (state.ev - 1)) == 2))
			elif transition == 5:
				return (((state.na < 3) and (state.cr != 1)) and (max(0, (state.ev - 1)) == 3))
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return (state.wt > 0)
			elif transition == 1:
				return (state.wt <= 0)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Host_location
		if location == 1 or location == 3 or location == 4:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 5:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Host_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Host_location
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
			elif transition == 2:
				return 1
			elif transition == 3:
				if True:
					return (1 / 2)
			elif transition == 4:
				if True:
					return (1 / 3)
			elif transition == 5:
				if True:
					return (1 / 4)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
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
			raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Host_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.wt = (state.wt - 1)
						if target_state.wt < 0:
							raise OverflowError("Assigned value of " + str(target_state.wt) + " is less than the lower bound of 0 for variable \"wt\".")
						target_state.Host_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.cr = min(2, (state.cr + 1))
						target_state.wt = 0
						target_state.Host_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Host_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.line_seized = True
						target_state.na = 0
						target_state.ev = 0
						target_state.Host_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.gave_up = True
						target_state.na = 0
						target_state.ev = 0
						target_state.Host_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 0
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 0
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
					elif branch == 1:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 1
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
				elif transition == 4:
					if branch == 0:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 0
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
					elif branch == 1:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 1
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
					elif branch == 2:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 2
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
				elif transition == 5:
					if branch == 0:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 0
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
					elif branch == 1:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 1
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
					elif branch == 2:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 2
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
					elif branch == 3:
						target_state.na = (state.na + 1)
						if target_state.na > 3:
							raise OverflowError("Assigned value of " + str(target_state.na) + " is greater than the upper bound of 3 for variable \"na\".")
						target_state.wt = 3
						target_state.ev = min((2 * state.ev), 4)
						target_state.Host_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Host_location = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Host_location = 5
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.wt = (state.wt - 1)
						if target_state.wt < 0:
							raise OverflowError("Assigned value of " + str(target_state.wt) + " is less than the lower bound of 0 for variable \"wt\".")
						target_state.Host_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.cr = min(2, (state.cr + 1))
						target_state.wt = 0
						target_state.Host_location = 1

# Automaton: Host_1
class Host_1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 6, 1, 1, 2, 0]
		self.transition_labels = [[1, 0], [1], [0, 0, 0, 0, 0, 0], [2], [3], [1, 0], []]
		self.branch_counts = [[1, 1], [1], [1, 1, 1, 2, 3, 4], [1], [1], [1, 1], []]
	
	def set_initial_values(self, state: State) -> None:
		state.Host_1_location = 0
		state.na_1 = 0
		state.ev_1 = 2
		state.wt_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Host_1_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Host_1_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Host_1_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Host_1_location
		if location == 1 or location == 3 or location == 4:
			return True
		elif location == 0:
			if transition == 0:
				return (state.wt_1 > 0)
			elif transition == 1:
				return (state.wt_1 <= 0)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.cr == 1)
			elif transition == 1:
				return ((state.na_1 >= 3) and (state.cr != 1))
			elif transition == 2:
				return (((state.na_1 < 3) and (state.cr != 1)) and (max(0, (state.ev_1 - 1)) == 0))
			elif transition == 3:
				return (((state.na_1 < 3) and (state.cr != 1)) and (max(0, (state.ev_1 - 1)) == 1))
			elif transition == 4:
				return (((state.na_1 < 3) and (state.cr != 1)) and (max(0, (state.ev_1 - 1)) == 2))
			elif transition == 5:
				return (((state.na_1 < 3) and (state.cr != 1)) and (max(0, (state.ev_1 - 1)) == 3))
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return (state.wt_1 > 0)
			elif transition == 1:
				return (state.wt_1 <= 0)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Host_1_location
		if location == 1 or location == 3 or location == 4:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 5:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Host_1_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Host_1_location
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
			elif transition == 2:
				return 1
			elif transition == 3:
				if True:
					return (1 / 2)
			elif transition == 4:
				if True:
					return (1 / 3)
			elif transition == 5:
				if True:
					return (1 / 4)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
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
			raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Host_1_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.wt_1 = (state.wt_1 - 1)
						if target_state.wt_1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.wt_1) + " is less than the lower bound of 0 for variable \"wt_1\".")
						target_state.Host_1_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.cr = min(2, (state.cr + 1))
						target_state.wt_1 = 0
						target_state.Host_1_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Host_1_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.line_seized = True
						target_state.na_1 = 0
						target_state.ev_1 = 0
						target_state.Host_1_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.gave_up = True
						target_state.na_1 = 0
						target_state.ev_1 = 0
						target_state.Host_1_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 0
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 0
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
					elif branch == 1:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 1
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
				elif transition == 4:
					if branch == 0:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 0
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
					elif branch == 1:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 1
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
					elif branch == 2:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 2
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
				elif transition == 5:
					if branch == 0:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 0
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
					elif branch == 1:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 1
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
					elif branch == 2:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 2
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
					elif branch == 3:
						target_state.na_1 = (state.na_1 + 1)
						if target_state.na_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_1) + " is greater than the upper bound of 3 for variable \"na_1\".")
						target_state.wt_1 = 3
						target_state.ev_1 = min((2 * state.ev_1), 4)
						target_state.Host_1_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Host_1_location = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Host_1_location = 5
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.wt_1 = (state.wt_1 - 1)
						if target_state.wt_1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.wt_1) + " is less than the lower bound of 0 for variable \"wt_1\".")
						target_state.Host_1_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.cr = min(2, (state.cr + 1))
						target_state.wt_1 = 0
						target_state.Host_1_location = 1

# Automaton: Host_2
class Host_2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 6, 1, 1, 2, 0]
		self.transition_labels = [[1, 0], [1], [0, 0, 0, 0, 0, 0], [2], [3], [1, 0], []]
		self.branch_counts = [[1, 1], [1], [1, 1, 1, 2, 3, 4], [1], [1], [1, 1], []]
	
	def set_initial_values(self, state: State) -> None:
		state.Host_2_location = 0
		state.na_2 = 0
		state.ev_2 = 2
		state.wt_2 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Host_2_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Host_2_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Host_2_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Host_2_location
		if location == 1 or location == 3 or location == 4:
			return True
		elif location == 0:
			if transition == 0:
				return (state.wt_2 > 0)
			elif transition == 1:
				return (state.wt_2 <= 0)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.cr == 1)
			elif transition == 1:
				return ((state.na_2 >= 3) and (state.cr != 1))
			elif transition == 2:
				return (((state.na_2 < 3) and (state.cr != 1)) and (max(0, (state.ev_2 - 1)) == 0))
			elif transition == 3:
				return (((state.na_2 < 3) and (state.cr != 1)) and (max(0, (state.ev_2 - 1)) == 1))
			elif transition == 4:
				return (((state.na_2 < 3) and (state.cr != 1)) and (max(0, (state.ev_2 - 1)) == 2))
			elif transition == 5:
				return (((state.na_2 < 3) and (state.cr != 1)) and (max(0, (state.ev_2 - 1)) == 3))
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return (state.wt_2 > 0)
			elif transition == 1:
				return (state.wt_2 <= 0)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Host_2_location
		if location == 1 or location == 3 or location == 4:
			return None
		elif location == 0:
			return None
		elif location == 2:
			return None
		elif location == 5:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Host_2_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Host_2_location
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
			elif transition == 2:
				return 1
			elif transition == 3:
				if True:
					return (1 / 2)
			elif transition == 4:
				if True:
					return (1 / 3)
			elif transition == 5:
				if True:
					return (1 / 4)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
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
			raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Host_2_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.wt_2 = (state.wt_2 - 1)
						if target_state.wt_2 < 0:
							raise OverflowError("Assigned value of " + str(target_state.wt_2) + " is less than the lower bound of 0 for variable \"wt_2\".")
						target_state.Host_2_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.cr = min(2, (state.cr + 1))
						target_state.wt_2 = 0
						target_state.Host_2_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Host_2_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.line_seized = True
						target_state.na_2 = 0
						target_state.ev_2 = 0
						target_state.Host_2_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.gave_up = True
						target_state.na_2 = 0
						target_state.ev_2 = 0
						target_state.Host_2_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 0
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 0
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
					elif branch == 1:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 1
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
				elif transition == 4:
					if branch == 0:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 0
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
					elif branch == 1:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 1
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
					elif branch == 2:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 2
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
				elif transition == 5:
					if branch == 0:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 0
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
					elif branch == 1:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 1
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
					elif branch == 2:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 2
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
					elif branch == 3:
						target_state.na_2 = (state.na_2 + 1)
						if target_state.na_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.na_2) + " is greater than the upper bound of 3 for variable \"na_2\".")
						target_state.wt_2 = 3
						target_state.ev_2 = min((2 * state.ev_2), 4)
						target_state.Host_2_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Host_2_location = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Host_2_location = 5
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.wt_2 = (state.wt_2 - 1)
						if target_state.wt_2 < 0:
							raise OverflowError("Assigned value of " + str(target_state.wt_2) + " is less than the lower bound of 0 for variable \"wt_2\".")
						target_state.Host_2_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.cr = min(2, (state.cr + 1))
						target_state.wt_2 = 0
						target_state.Host_2_location = 1

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Clock", "_aut_Host", "_aut_Host_1", "_aut_Host_2")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ", 1: "tick", 2: "tack", 3: "tock" }
		self.sync_vectors = [[0, -1, -1, -1, 0], [-1, 0, -1, -1, 0], [-1, -1, 0, -1, 0], [-1, -1, -1, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
		self.properties = [
			Property("LineSeized", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])])),
			Property("GaveUp", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [1])])]))
		]
		self.variables = [
			VariableInfo("cr", None, "int", 0, 2),
			VariableInfo("line_seized", None, "bool"),
			VariableInfo("gave_up", None, "bool"),
			VariableInfo("Clock_location", 0, "int", 0, 3),
			VariableInfo("Host_location", 1, "int", 0, 6),
			VariableInfo("na", 1, "int", 0, 3),
			VariableInfo("ev", 1, "int", 0, 4),
			VariableInfo("wt", 1, "int", 0, 4),
			VariableInfo("Host_1_location", 2, "int", 0, 6),
			VariableInfo("na", 2, "int", 0, 3),
			VariableInfo("ev", 2, "int", 0, 4),
			VariableInfo("wt", 2, "int", 0, 4),
			VariableInfo("Host_2_location", 3, "int", 0, 6),
			VariableInfo("na", 3, "int", 0, 3),
			VariableInfo("ev", 3, "int", 0, 4),
			VariableInfo("wt", 3, "int", 0, 4)
		]
		self._aut_Clock = ClockAutomaton(self)
		self._aut_Host = HostAutomaton(self)
		self._aut_Host_1 = Host_1Automaton(self)
		self._aut_Host_2 = Host_2Automaton(self)
		self.components = [self._aut_Clock, self._aut_Host, self._aut_Host_1, self._aut_Host_2]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.cr = 0
		state.line_seized = False
		state.gave_up = False
		self._aut_Clock.set_initial_values(state)
		self._aut_Host.set_initial_values(state)
		self._aut_Host_1.set_initial_values(state)
		self._aut_Host_2.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_Clock.set_initial_transient_values(transient)
		self._aut_Host.set_initial_transient_values(transient)
		self._aut_Host_1.set_initial_transient_values(transient)
		self._aut_Host_2.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return state.line_seized
		elif expression == 1:
			return state.gave_up
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return state.line_seized
		elif expression == 1:
			return state.gave_up
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Clock.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Host.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Host_1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Host_2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_Clock = [[], [], [], []]
		transition_count = self._aut_Clock.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Clock.get_guard_value(state, i):
				trans_Clock[self._aut_Clock.get_transition_label(state, i)].append(i)
		trans_Host = [[], [], [], []]
		transition_count = self._aut_Host.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Host.get_guard_value(state, i):
				trans_Host[self._aut_Host.get_transition_label(state, i)].append(i)
		trans_Host_1 = [[], [], [], []]
		transition_count = self._aut_Host_1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Host_1.get_guard_value(state, i):
				trans_Host_1[self._aut_Host_1.get_transition_label(state, i)].append(i)
		trans_Host_2 = [[], [], [], []]
		transition_count = self._aut_Host_2.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Host_2.get_guard_value(state, i):
				trans_Host_2[self._aut_Host_2.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1]]
			# Clock
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Clock[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Clock[sv[0]][0]
						for i in range(1, len(trans_Clock[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Clock[sv[0]][i]
			# Host
			if synced is not None:
				if sv[1] != -1:
					if len(trans_Host[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_Host[sv[1]][0]
						for i in range(1, len(trans_Host[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_Host[sv[1]][i]
			# Host_1
			if synced is not None:
				if sv[2] != -1:
					if len(trans_Host_1[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_Host_1[sv[2]][0]
						for i in range(1, len(trans_Host_1[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_Host_1[sv[2]][i]
			# Host_2
			if synced is not None:
				if sv[3] != -1:
					if len(trans_Host_2[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_Host_2[sv[3]][0]
						for i in range(1, len(trans_Host_2[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_Host_2[sv[3]][i]
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
			branch_count = self._aut_Clock.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Clock.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Clock.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_Host.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_Host.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Host.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_Host_1.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_Host_1.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Host_1.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_Host_2.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_Host_2.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Host_2.get_probability_value(state, transition.transitions[3], 0)
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
				self._aut_Clock.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_Host.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_Host_1.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_Host_2.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
