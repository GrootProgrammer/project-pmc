# pacman

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
	__slots__ = ("pMove", "steps", "xG0", "yG0", "dG0", "xG1", "yG1", "dG1", "xP", "yP", "dP", "arbiter_location")
	
	def udfs_global_deactive1_state(self):
		return (self.xG1 == 0)
	
	def udfs_global_deactive1_jump(self, transient):
		return (self.xG1 == 0)
	
	def udfs_global_deactive0_state(self):
		return (self.xG0 == 0)
	
	def udfs_global_deactive0_jump(self, transient):
		return (self.xG0 == 0)
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.pMove
		elif variable == 1:
			return self.steps
		elif variable == 2:
			return self.xG0
		elif variable == 3:
			return self.yG0
		elif variable == 4:
			return self.dG0
		elif variable == 5:
			return self.xG1
		elif variable == 6:
			return self.yG1
		elif variable == 7:
			return self.dG1
		elif variable == 8:
			return self.xP
		elif variable == 9:
			return self.yP
		elif variable == 10:
			return self.dP
		elif variable == 11:
			return self.arbiter_location
	
	def copy_to(self, other: State):
		other.pMove = self.pMove
		other.steps = self.steps
		other.xG0 = self.xG0
		other.yG0 = self.yG0
		other.dG0 = self.dG0
		other.xG1 = self.xG1
		other.yG1 = self.yG1
		other.dG1 = self.dG1
		other.xP = self.xP
		other.yP = self.yP
		other.dP = self.dP
		other.arbiter_location = self.arbiter_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.pMove == other.pMove and self.steps == other.steps and self.xG0 == other.xG0 and self.yG0 == other.yG0 and self.dG0 == other.dG0 and self.xG1 == other.xG1 and self.yG1 == other.yG1 and self.dG1 == other.dG1 and self.xP == other.xP and self.yP == other.yP and self.dP == other.dP and self.arbiter_location == other.arbiter_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.pMove)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.steps)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.xG0)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.yG0)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.dG0)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.xG1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.yG1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.dG1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.xP)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.yP)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.dP)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.arbiter_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "pMove = " + str(self.pMove)
		result += ", steps = " + str(self.steps)
		result += ", xG0 = " + str(self.xG0)
		result += ", yG0 = " + str(self.yG0)
		result += ", dG0 = " + str(self.dG0)
		result += ", xG1 = " + str(self.xG1)
		result += ", yG1 = " + str(self.yG1)
		result += ", dG1 = " + str(self.dG1)
		result += ", xP = " + str(self.xP)
		result += ", yP = " + str(self.yP)
		result += ", dP = " + str(self.dP)
		result += ", arbiter_location = " + str(self.arbiter_location)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("Crash")
	
	def copy_to(self, other: Transient):
		other.Crash = self.Crash
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.Crash == other.Crash
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Crash)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "Crash = " + str(self.Crash)
		result += ")"
		return result

# Automaton: arbiter
class arbiterAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 6]
		self.transition_labels = [[2, 7], [3, 8], [0, 1, 4, 5, 6, 9]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1, 1, 1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.arbiter_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.arbiter_location
		if location == 0:
			if transient_variable == "Crash":
				return (((state.xP == state.xG0) and (state.yP == state.yG0)) or ((state.xP == state.xG1) and (state.yP == state.yG1)))
		elif location == 1:
			if transient_variable == "Crash":
				return (((state.xP == state.xG0) and (state.yP == state.yG0)) or ((state.xP == state.xG1) and (state.yP == state.yG1)))
		elif location == 2:
			if transient_variable == "Crash":
				return (((state.xP == state.xG0) and (state.yP == state.yG0)) or ((state.xP == state.xG1) and (state.yP == state.yG1)))
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.arbiter_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.arbiter_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.arbiter_location
		if location == 0:
			if transition == 0:
				return ((not state.udfs_global_deactive0_state()) and ((((state.xP - state.xG0) if (state.xG0 < state.xP) else (state.xG0 - state.xP)) + ((state.yP - state.yG0) if (state.yG0 < state.yP) else (state.yG0 - state.yP))) <= (2 * (5 - state.steps))))
			elif transition == 1:
				return (state.udfs_global_deactive0_state() or ((((state.xP - state.xG0) if (state.xG0 < state.xP) else (state.xG0 - state.xP)) + ((state.yP - state.yG0) if (state.yG0 < state.yP) else (state.yG0 - state.yP))) > (2 * (5 - state.steps))))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return ((not state.udfs_global_deactive1_state()) and ((((state.xP - state.xG1) if (state.xG1 < state.xP) else (state.xG1 - state.xP)) + ((state.yP - state.yG1) if (state.yG1 < state.yP) else (state.yG1 - state.yP))) <= (2 * (5 - state.steps))))
			elif transition == 1:
				return (state.udfs_global_deactive1_state() or ((((state.xP - state.xG1) if (state.xG1 < state.xP) else (state.xG1 - state.xP)) + ((state.yP - state.yG1) if (state.yG1 < state.yP) else (state.yG1 - state.yP))) > (2 * (5 - state.steps))))
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return ((state.steps == 5) or (state.udfs_global_deactive0_state() and state.udfs_global_deactive1_state()))
			elif transition >= 1:
				return (state.steps < 5)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.arbiter_location
		if location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.arbiter_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.arbiter_location
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
			location = state.arbiter_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.pMove = 1
						target_state.arbiter_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.pMove = 1
						target_state.arbiter_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.pMove = 2
						target_state.arbiter_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.pMove = 2
						target_state.arbiter_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.pMove = 2
						target_state.arbiter_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.pMove = 0
						target_state.steps = (state.steps + 1)
						if target_state.steps > 5:
							raise OverflowError("Assigned value of " + str(target_state.steps) + " is greater than the upper bound of 5 for variable \"steps\".")
						target_state.arbiter_location = 0
				elif transition == 2:
					if branch == 0:
						target_state.pMove = 0
						target_state.steps = (state.steps + 1)
						if target_state.steps > 5:
							raise OverflowError("Assigned value of " + str(target_state.steps) + " is greater than the upper bound of 5 for variable \"steps\".")
						target_state.arbiter_location = 0
				elif transition == 3:
					if branch == 0:
						target_state.pMove = 0
						target_state.steps = (state.steps + 1)
						if target_state.steps > 5:
							raise OverflowError("Assigned value of " + str(target_state.steps) + " is greater than the upper bound of 5 for variable \"steps\".")
						target_state.arbiter_location = 0
				elif transition == 4:
					if branch == 0:
						target_state.pMove = 0
						target_state.steps = (state.steps + 1)
						if target_state.steps > 5:
							raise OverflowError("Assigned value of " + str(target_state.steps) + " is greater than the upper bound of 5 for variable \"steps\".")
						target_state.arbiter_location = 0
				elif transition == 5:
					if branch == 0:
						target_state.pMove = 0
						target_state.steps = (state.steps + 1)
						if target_state.steps > 5:
							raise OverflowError("Assigned value of " + str(target_state.steps) + " is greater than the upper bound of 5 for variable \"steps\".")
						target_state.arbiter_location = 0

# Automaton: ghost0
class ghost0Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [67]
		self.transition_labels = [[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 5, 5, 6, 6, 7, 9, 9]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
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
				return ((state.xG0 > state.xG1) or ((state.xG0 == state.xG1) and (state.yG0 > state.yG1)))
			elif transition == 1:
				return ((state.xG0 <= state.xG1) and ((state.xG0 != state.xG1) or (state.yG0 <= state.yG1)))
			elif transition == 2:
				return ((((((((((((((((((((((((((((((state.dG0 == 0) and (state.xG0 >= 2)) and ((state.xG0 <= 2) and (state.yG0 == 1))) or (((state.dG0 == 0) and (state.xG0 >= 4)) and ((state.xG0 <= 5) and (state.yG0 == 1)))) or (((state.dG0 == 0) and (state.xG0 >= 7)) and ((state.xG0 <= 7) and (state.yG0 == 1)))) or (((state.dG0 == 0) and (state.xG0 >= 9)) and ((state.xG0 <= 9) and (state.yG0 == 1)))) or (((state.dG0 == 0) and (state.xG0 >= 2)) and ((state.xG0 <= 2) and (state.yG0 == 4)))) or (((state.dG0 == 0) and (state.xG0 >= 4)) and ((state.xG0 <= 4) and (state.yG0 == 4)))) or (((state.dG0 == 0) and (state.xG0 >= 7)) and ((state.xG0 <= 7) and (state.yG0 == 4)))) or (((state.dG0 == 0) and (state.xG0 >= 9)) and ((state.xG0 <= 9) and (state.yG0 == 4)))) or (((state.dG0 == 0) and (state.xG0 >= 2)) and ((state.xG0 <= 2) and (state.yG0 == 6)))) or (((state.dG0 == 0) and (state.xG0 >= 6)) and ((state.xG0 <= 9) and (state.yG0 == 6)))) or ((state.xG0 == 1) and (state.yG0 == 6))) or (((state.xG0 == 1) and (state.yG0 == 1)) and ((state.dG0 == 3) or (state.dG0 == 0)))) or (((state.xG0 == 1) and (state.yG0 == 4)) and ((state.dG0 == 1) or (state.dG0 == 0)))) or (((state.xG0 == 5) and (state.yG0 == 6)) and ((state.dG0 == 1) or (state.dG0 == 0)))) or ((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.yG0 < state.yP) and (state.xG0 == 3)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 5)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 5)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.yG0 > state.yP) and (state.xG0 == 6)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 < state.yP) and (state.xG0 == 8)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 8))))
			elif transition == 3:
				return ((((((((((((((((((((((((((((((((((((((state.dG0 == 2) and (state.xG0 >= 2)) and ((state.xG0 <= 2) and (state.yG0 == 1))) or (((state.dG0 == 2) and (state.xG0 >= 4)) and ((state.xG0 <= 5) and (state.yG0 == 1)))) or (((state.dG0 == 2) and (state.xG0 >= 7)) and ((state.xG0 <= 7) and (state.yG0 == 1)))) or (((state.dG0 == 2) and (state.xG0 >= 9)) and ((state.xG0 <= 9) and (state.yG0 == 1)))) or (((state.dG0 == 2) and (state.xG0 >= 2)) and ((state.xG0 <= 2) and (state.yG0 == 4)))) or (((state.dG0 == 2) and (state.xG0 >= 4)) and ((state.xG0 <= 4) and (state.yG0 == 4)))) or (((state.dG0 == 2) and (state.xG0 >= 7)) and ((state.xG0 <= 7) and (state.yG0 == 4)))) or (((state.dG0 == 2) and (state.xG0 >= 9)) and ((state.xG0 <= 9) and (state.yG0 == 4)))) or (((state.dG0 == 2) and (state.xG0 >= 2)) and ((state.xG0 <= 2) and (state.yG0 == 6)))) or (((state.dG0 == 2) and (state.xG0 >= 6)) and ((state.xG0 <= 9) and (state.yG0 == 6)))) or (((state.xG0 == 3) and (state.yG0 == 6)) and ((state.dG0 == 1) or (state.dG0 == 2)))) or (((state.xG0 == 10) and (state.yG0 == 1)) and ((state.dG0 == 3) or (state.dG0 == 2)))) or (((state.xG0 == 10) and (state.yG0 == 6)) and ((state.dG0 == 1) or (state.dG0 == 2)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.yG0 < state.yP) and (state.xG0 == 6)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.yG0 < state.yP) and (state.xG0 == 8)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 5)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 5)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 5)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.yG0 < state.yP) and (state.xG0 == 6)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.yG0 < state.yP) and (state.xG0 == 8)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 10)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 10))))
			elif transition == 4:
				return ((((((((((((((((((((state.dG0 == 1) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 1))) or (((state.dG0 == 1) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 3)))) or (((state.dG0 == 1) and (state.yG0 >= 5)) and ((state.yG0 <= 5) and (state.xG0 == 3)))) or (((state.dG0 == 1) and (state.yG0 >= 5)) and ((state.yG0 <= 5) and (state.xG0 == 5)))) or (((state.dG0 == 1) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 6)))) or (((state.dG0 == 1) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 8)))) or (((state.dG0 == 1) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 10)))) or (((state.dG0 == 1) and (state.yG0 >= 5)) and ((state.yG0 <= 5) and (state.xG0 == 10)))) or (((state.xG0 == 1) and (state.yG0 == 1)) and ((state.dG0 == 2) or (state.dG0 == 1)))) or (((state.xG0 == 10) and (state.yG0 == 1)) and ((state.dG0 == 0) or (state.dG0 == 1)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.yG0 < state.yP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.yG0 < state.yP) and (state.xG0 == 6)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 < state.yP) and (state.xG0 == 5)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 5))))
			elif transition == 5:
				return ((((((((((((((((((((((((((state.dG0 == 3) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 1))) or (((state.dG0 == 3) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 3)))) or (((state.dG0 == 3) and (state.yG0 >= 5)) and ((state.yG0 <= 5) and (state.xG0 == 3)))) or (((state.dG0 == 3) and (state.yG0 >= 5)) and ((state.yG0 <= 5) and (state.xG0 == 5)))) or (((state.dG0 == 3) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 6)))) or (((state.dG0 == 3) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 8)))) or (((state.dG0 == 3) and (state.yG0 >= 2)) and ((state.yG0 <= 3) and (state.xG0 == 10)))) or (((state.dG0 == 3) and (state.yG0 >= 5)) and ((state.yG0 <= 5) and (state.xG0 == 10)))) or (((state.xG0 == 1) and (state.yG0 == 4)) and ((state.dG0 == 2) or (state.dG0 == 3)))) or (((state.xG0 == 3) and (state.yG0 == 6)) and ((state.dG0 == 0) or (state.dG0 == 3)))) or (((state.xG0 == 5) and (state.yG0 == 6)) and ((state.dG0 == 2) or (state.dG0 == 3)))) or (((state.xG0 == 10) and (state.yG0 == 6)) and ((state.dG0 == 0) or (state.dG0 == 3)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.yG0 > state.yP) and (state.xG0 == 3)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.yG0 > state.yP) and (state.xG0 == 3)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 < state.yP) and (state.xG0 == 10)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 10)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.yG0 > state.yP) and (state.xG0 == 10)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 10))))
			elif transition == 6:
				return ((((((((((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 3))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 5)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 > state.yP) and (state.xG0 == 5)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 5))))
			elif transition == 7:
				return (((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 3))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 8))))
			elif transition == 8:
				return ((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.yG0 < state.yP) and (state.xG0 == 3)))
			elif transition == 9:
				return (((((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 3))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 5)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 8))))
			elif transition == 10:
				return ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))
			elif transition == 11:
				return ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))
			elif transition == 12:
				return ((((((((((state.yG0 == state.yP) and (state.yG0 == 1)) and ((state.xG0 == state.xP) and (state.xG0 == 3))) or (((state.yG0 == state.yP) and (state.yG0 == 1)) and ((state.xG0 == state.xP) and (state.xG0 == 6)))) or (((state.yG0 == state.yP) and (state.yG0 == 1)) and ((state.xG0 == state.xP) and (state.xG0 == 8)))) or (((state.yG0 == state.yP) and (state.yG0 == 4)) and ((state.xG0 == state.xP) and (state.xG0 == 3)))) or (((state.yG0 == state.yP) and (state.yG0 == 4)) and ((state.xG0 == state.xP) and (state.xG0 == 5)))) or (((state.yG0 == state.yP) and (state.yG0 == 4)) and ((state.xG0 == state.xP) and (state.xG0 == 6)))) or (((state.yG0 == state.yP) and (state.yG0 == 4)) and ((state.xG0 == state.xP) and (state.xG0 == 8)))) or (((state.yG0 == state.yP) and (state.yG0 == 4)) and ((state.xG0 == state.xP) and (state.xG0 == 10))))
			elif transition == 13:
				return ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))
			elif transition == 14:
				return ((((((((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.yG0 < state.yP) and (state.xG0 == 6))) or ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))) or ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 5)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.yG0 > state.yP) and (state.xG0 == 5)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.yG0 > state.yP) and (state.xG0 == 10)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 10))))
			elif transition == 15:
				return ((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))
			elif transition == 16:
				return ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))
			elif transition == 17:
				return ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))
			elif transition == 18:
				return (((((state.yG0 == state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 8))) or ((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.yG0 < state.yP) and (state.xG0 == 8))))
			elif transition == 19:
				return (((((((((((((state.xG0 == state.xP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.yG0 < state.yP) and (state.xG0 == 8))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.yG0 < state.yP) and (state.xG0 == 5)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.yG0 > state.yP) and (state.xG0 == 5)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 5)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.yG0 < state.yP) and (state.xG0 == 6)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.yG0 < state.yP) and (state.xG0 == 8)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.yG0 > state.yP) and (state.xG0 == 8)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 8))))
			elif transition == 20:
				return ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))
			elif transition == 21:
				return ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))
			elif transition == 22:
				return ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))
			elif transition == 23:
				return ((((state.yG0 < state.yP) and (state.yG0 == 1)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))
			elif transition == 24:
				return ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))
			elif transition == 25:
				return ((((((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 < state.yP) and (state.xG0 == 3))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 3))))
			elif transition == 26:
				return ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.yG0 < state.yP) and (state.xG0 == 3)))
			elif transition == 27:
				return ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.yG0 < state.yP) and (state.xG0 == 3)))
			elif transition == 28:
				return ((((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.yG0 < state.yP) and (state.xG0 == 3))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 3)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 3))))
			elif transition == 29:
				return (((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 3))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 3))))
			elif transition == 30:
				return (((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 > state.yP) and (state.xG0 == 3))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 8))))
			elif transition == 31:
				return (((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.yG0 > state.yP) and (state.xG0 == 3))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 3))))
			elif transition == 32:
				return (((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 3))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 5))))
			elif transition == 33:
				return ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))
			elif transition == 34:
				return (((((((((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 3))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 < state.yP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 > state.yP) and (state.xG0 == 6)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 8))))
			elif transition == 35:
				return ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 3)))
			elif transition == 36:
				return (((((((((((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 3))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.yG0 > state.yP) and (state.xG0 == 6)))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))) or ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.yG0 > state.yP) and (state.xG0 == 8)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))) or ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.yG0 < state.yP) and (state.xG0 == 10)))) or ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 10))))
			elif transition == 37:
				return (((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 < state.xP) and (state.xG0 == 5))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 < state.xP) and (state.xG0 == 6))))
			elif transition == 38:
				return ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.yG0 < state.yP) and (state.xG0 == 5)))
			elif transition == 39:
				return ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 5)))
			elif transition == 40:
				return ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 5)))
			elif transition == 41:
				return ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 5)))
			elif transition == 42:
				return ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 5)))
			elif transition == 43:
				return ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 5)))
			elif transition == 44:
				return ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))
			elif transition == 45:
				return ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))
			elif transition == 46:
				return ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 6)))
			elif transition == 47:
				return ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))
			elif transition == 48:
				return ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 < state.xP) and (state.xG0 == 6)))
			elif transition == 49:
				return ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 8)))
			elif transition == 50:
				return (((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 8))) or ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 2)) and ((state.xG0 > state.xP) and (state.xG0 == 8))))
			elif transition == 51:
				return ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 > state.yP) and (state.xG0 == 8)))
			elif transition == 52:
				return ((((state.yG0 > state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 < state.xP) and (state.xG0 == 8)))
			elif transition == 53:
				return ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.yG0 < state.yP) and (state.xG0 == 10)))
			elif transition == 54:
				return ((((state.yG0 == state.yP) and (state.yG0 == 4)) and (state.dG0 == 3)) and ((state.xG0 > state.xP) and (state.xG0 == 10)))
			elif transition == 55:
				return ((((state.xG0 == state.xP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.yG0 > state.yP) and (state.xG0 == 10)))
			elif transition == 56:
				return ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 0)) and ((state.xG0 > state.xP) and (state.xG0 == 10)))
			elif transition == 57:
				return ((((state.yG0 < state.yP) and (state.yG0 == 4)) and (state.dG0 == 1)) and ((state.xG0 > state.xP) and (state.xG0 == 10)))
			elif transition == 58:
				return ((state.xG0 <= state.xG1) and ((state.xG0 != state.xG1) or (state.yG0 <= state.yG1)))
			elif transition >= 59 and transition < 61:
				return ((state.xG0 > state.xG1) or ((state.xG0 == state.xG1) and (state.yG0 > state.yG1)))
			elif transition >= 61 and transition < 63:
				return ((state.xG0 <= state.xG1) and ((state.xG0 != state.xG1) or (state.yG0 <= state.yG1)))
			elif transition == 63:
				return ((state.xG0 > state.xG1) or ((state.xG0 == state.xG1) and (state.yG0 > state.yG1)))
			elif transition == 64:
				return True
			elif transition == 65:
				return ((state.xG0 > state.xG1) or ((state.xG0 == state.xG1) and (state.yG0 > state.yG1)))
			elif transition == 66:
				return ((state.xG0 <= state.xG1) and ((state.xG0 != state.xG1) or (state.yG0 <= state.yG1)))
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
				if True:
					return (5 / 10)
			elif transition == 7:
				if branch == 0:
					return (92 / 100)
				elif branch == 1:
					return (8 / 100)
			elif transition == 8:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 9:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 10:
				if branch == 0:
					return (78 / 100)
				elif branch == 1:
					return (22 / 100)
			elif transition == 11:
				if branch == 0:
					return (86 / 100)
				elif branch == 1:
					return (14 / 100)
			elif transition == 12:
				return 1
			elif transition == 13:
				if branch == 0:
					return (64 / 100)
				elif branch == 1:
					return (36 / 100)
			elif transition == 14:
				if True:
					return (5 / 10)
			elif transition == 15:
				if branch == 0:
					return (22 / 100)
				elif branch == 1:
					return (78 / 100)
			elif transition == 16:
				if branch == 0:
					return (46 / 100)
				elif branch == 1:
					return (54 / 100)
			elif transition == 17:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 18:
				if branch == 0:
					return (4 / 10)
				elif branch == 1:
					return (6 / 10)
			elif transition == 19:
				if True:
					return (5 / 10)
			elif transition == 20:
				if branch == 0:
					return (36 / 100)
				elif branch == 1:
					return (64 / 100)
			elif transition == 21:
				if branch == 0:
					return (75 / 100)
				elif branch == 1:
					return (25 / 100)
			elif transition == 22:
				if branch == 0:
					return (2 / 10)
				elif branch == 1:
					return (8 / 10)
			elif transition == 23:
				if branch == 0:
					return (67 / 100)
				elif branch == 1:
					return (33 / 100)
			elif transition == 24:
				if branch == 0:
					return (61 / 100)
				elif branch == 1:
					return (26 / 100)
				elif branch == 2:
					return (13 / 100)
			elif transition == 25:
				if branch == 0:
					return (34 / 100)
				elif branch >= 1:
					return (33 / 100)
			elif transition == 26:
				if branch == 0:
					return (16 / 100)
				elif branch == 1:
					return (67 / 100)
				elif branch == 2:
					return (17 / 100)
			elif transition == 27:
				if branch == 0:
					return (28 / 100)
				elif branch == 1:
					return (43 / 100)
				elif branch == 2:
					return (29 / 100)
			elif transition == 28:
				if branch == 0:
					return (34 / 100)
				elif branch >= 1:
					return (33 / 100)
			elif transition == 29:
				if branch == 0:
					return (34 / 100)
				elif branch >= 1:
					return (33 / 100)
			elif transition == 30:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 31:
				if branch == 0:
					return (34 / 100)
				elif branch >= 1:
					return (33 / 100)
			elif transition == 32:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 33:
				if branch == 0:
					return (5 / 10)
				elif branch >= 1:
					return (25 / 100)
			elif transition == 34:
				if True:
					return (5 / 10)
			elif transition == 35:
				if branch == 0:
					return (67 / 100)
				elif branch == 1:
					return (33 / 100)
			elif transition == 36:
				if True:
					return (5 / 10)
			elif transition == 37:
				if branch == 0:
					return (89 / 100)
				elif branch == 1:
					return (11 / 100)
			elif transition == 38:
				if branch == 0:
					return (83 / 100)
				elif branch == 1:
					return (17 / 100)
			elif transition == 39:
				if branch == 0:
					return (17 / 100)
				elif branch == 1:
					return (83 / 100)
			elif transition == 40:
				if branch == 0:
					return (17 / 100)
				elif branch == 1:
					return (83 / 100)
			elif transition == 41:
				if branch == 0:
					return (75 / 100)
				elif branch == 1:
					return (25 / 100)
			elif transition == 42:
				if branch == 0:
					return (95 / 100)
				elif branch == 1:
					return (5 / 100)
			elif transition == 43:
				if branch == 0:
					return (11 / 100)
				elif branch == 1:
					return (89 / 100)
			elif transition == 44:
				if branch == 0:
					return (57 / 100)
				elif branch == 1:
					return (43 / 100)
			elif transition == 45:
				if branch == 0:
					return (75 / 100)
				elif branch == 1:
					return (25 / 100)
			elif transition == 46:
				if branch == 0:
					return (67 / 100)
				elif branch == 1:
					return (33 / 100)
			elif transition == 47:
				if branch == 0:
					return (69 / 100)
				elif branch == 1:
					return (31 / 100)
			elif transition == 48:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 49:
				if branch == 0:
					return (44 / 100)
				elif branch == 1:
					return (56 / 100)
			elif transition == 50:
				if branch == 0:
					return (83 / 100)
				elif branch == 1:
					return (17 / 100)
			elif transition == 51:
				if branch == 0:
					return (43 / 100)
				elif branch == 1:
					return (57 / 100)
			elif transition == 52:
				if branch == 0:
					return (56 / 100)
				elif branch == 1:
					return (44 / 100)
			elif transition == 53:
				if branch == 0:
					return (45 / 100)
				elif branch == 1:
					return (55 / 100)
			elif transition == 54:
				if branch == 0:
					return (79 / 100)
				elif branch == 1:
					return (21 / 100)
			elif transition == 55:
				if branch == 0:
					return (2 / 10)
				elif branch == 1:
					return (8 / 10)
			elif transition == 56:
				if branch == 0:
					return (75 / 100)
				elif branch == 1:
					return (25 / 100)
			elif transition == 57:
				if branch == 0:
					return (44 / 100)
				elif branch == 1:
					return (56 / 100)
			elif transition == 58:
				return 1
			elif transition == 59:
				return 1
			elif transition == 60:
				return 1
			elif transition == 61:
				return 1
			elif transition == 62:
				return 1
			elif transition == 63:
				return 1
			elif transition == 64:
				return 1
			elif transition == 65:
				return 1
			elif transition == 66:
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
						target_state.xG0 = state.xG1
						target_state.yG0 = state.yG1
						target_state.dG0 = state.dG1
				elif transition == 1:
					if branch == 0:
						pass
				elif transition == 2:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
				elif transition == 3:
					if branch == 0:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 4:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
				elif transition == 5:
					if branch == 0:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 6:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
				elif transition == 7:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 8:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 9:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 10:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 11:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 12:
					if branch == 0:
						pass
				elif transition == 13:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 14:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 15:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 16:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
				elif transition == 17:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 18:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
				elif transition == 19:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 20:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
				elif transition == 21:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 22:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 23:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 24:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 2:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 25:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 2:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 26:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 2:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 27:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 2:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 28:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 2:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 29:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 2:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 30:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 31:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 2:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 32:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
				elif transition == 33:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 2:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 34:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 35:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
				elif transition == 36:
					if branch == 0:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 37:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 38:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 39:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 40:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 41:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 42:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
				elif transition == 43:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 44:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 45:
					if branch == 0:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 46:
					if branch == 0:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 47:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 48:
					if branch == 0:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 49:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 50:
					if branch == 0:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 51:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 52:
					if branch == 0:
						target_state.xG0 = (state.xG0 + 1)
						if target_state.xG0 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is greater than the upper bound of 11 for variable \"xG0\".")
						target_state.dG0 = 0
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 53:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 54:
					if branch == 0:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 55:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 56:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.yG0 = (state.yG0 - 1)
						if target_state.yG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is less than the lower bound of 0 for variable \"yG0\".")
						target_state.dG0 = 3
				elif transition == 57:
					if branch == 0:
						target_state.yG0 = (state.yG0 + 1)
						if target_state.yG0 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG0) + " is greater than the upper bound of 7 for variable \"yG0\".")
						target_state.dG0 = 1
					elif branch == 1:
						target_state.xG0 = (state.xG0 - 1)
						if target_state.xG0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG0) + " is less than the lower bound of 0 for variable \"xG0\".")
						target_state.dG0 = 2
				elif transition == 58:
					if branch == 0:
						pass
				elif transition == 59:
					if branch == 0:
						target_state.xG0 = state.xG1
						target_state.yG0 = state.yG1
						target_state.dG0 = state.dG1
				elif transition == 60:
					if branch == 0:
						target_state.xG0 = state.xG1
						target_state.yG0 = state.yG1
						target_state.dG0 = state.dG1
				elif transition == 61:
					if branch == 0:
						pass
				elif transition == 62:
					if branch == 0:
						pass
				elif transition == 63:
					if branch == 0:
						target_state.xG0 = state.xG1
						target_state.yG0 = state.yG1
						target_state.dG0 = state.dG1
				elif transition == 64:
					if branch == 0:
						target_state.xG0 = 0
						target_state.yG0 = 0
				elif transition == 65:
					if branch == 0:
						target_state.xG0 = state.xG1
						target_state.yG0 = state.yG1
						target_state.dG0 = state.dG1
				elif transition == 66:
					if branch == 0:
						pass

# Automaton: ghost1
class ghost1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [67]
		self.transition_labels = [[1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 8, 9, 9]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
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
				return ((state.xG0 > state.xG1) or ((state.xG0 == state.xG1) and (state.yG0 > state.yG1)))
			elif transition == 1:
				return ((state.xG0 <= state.xG1) and ((state.xG0 != state.xG1) or (state.yG0 <= state.yG1)))
			elif transition == 2:
				return ((((((((((((((((((((((((((((((state.dG1 == 0) and (state.xG1 >= 2)) and ((state.xG1 <= 2) and (state.yG1 == 1))) or (((state.dG1 == 0) and (state.xG1 >= 4)) and ((state.xG1 <= 5) and (state.yG1 == 1)))) or (((state.dG1 == 0) and (state.xG1 >= 7)) and ((state.xG1 <= 7) and (state.yG1 == 1)))) or (((state.dG1 == 0) and (state.xG1 >= 9)) and ((state.xG1 <= 9) and (state.yG1 == 1)))) or (((state.dG1 == 0) and (state.xG1 >= 2)) and ((state.xG1 <= 2) and (state.yG1 == 4)))) or (((state.dG1 == 0) and (state.xG1 >= 4)) and ((state.xG1 <= 4) and (state.yG1 == 4)))) or (((state.dG1 == 0) and (state.xG1 >= 7)) and ((state.xG1 <= 7) and (state.yG1 == 4)))) or (((state.dG1 == 0) and (state.xG1 >= 9)) and ((state.xG1 <= 9) and (state.yG1 == 4)))) or (((state.dG1 == 0) and (state.xG1 >= 2)) and ((state.xG1 <= 2) and (state.yG1 == 6)))) or (((state.dG1 == 0) and (state.xG1 >= 6)) and ((state.xG1 <= 9) and (state.yG1 == 6)))) or ((state.xG1 == 1) and (state.yG1 == 6))) or (((state.xG1 == 1) and (state.yG1 == 1)) and ((state.dG1 == 3) or (state.dG1 == 0)))) or (((state.xG1 == 1) and (state.yG1 == 4)) and ((state.dG1 == 1) or (state.dG1 == 0)))) or (((state.xG1 == 5) and (state.yG1 == 6)) and ((state.dG1 == 1) or (state.dG1 == 0)))) or ((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.yG1 < state.yP) and (state.xG1 == 3)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 5)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 5)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.yG1 > state.yP) and (state.xG1 == 6)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 < state.yP) and (state.xG1 == 8)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 8))))
			elif transition == 3:
				return ((((((((((((((((((((((((((((((((((((((state.dG1 == 2) and (state.xG1 >= 2)) and ((state.xG1 <= 2) and (state.yG1 == 1))) or (((state.dG1 == 2) and (state.xG1 >= 4)) and ((state.xG1 <= 5) and (state.yG1 == 1)))) or (((state.dG1 == 2) and (state.xG1 >= 7)) and ((state.xG1 <= 7) and (state.yG1 == 1)))) or (((state.dG1 == 2) and (state.xG1 >= 9)) and ((state.xG1 <= 9) and (state.yG1 == 1)))) or (((state.dG1 == 2) and (state.xG1 >= 2)) and ((state.xG1 <= 2) and (state.yG1 == 4)))) or (((state.dG1 == 2) and (state.xG1 >= 4)) and ((state.xG1 <= 4) and (state.yG1 == 4)))) or (((state.dG1 == 2) and (state.xG1 >= 7)) and ((state.xG1 <= 7) and (state.yG1 == 4)))) or (((state.dG1 == 2) and (state.xG1 >= 9)) and ((state.xG1 <= 9) and (state.yG1 == 4)))) or (((state.dG1 == 2) and (state.xG1 >= 2)) and ((state.xG1 <= 2) and (state.yG1 == 6)))) or (((state.dG1 == 2) and (state.xG1 >= 6)) and ((state.xG1 <= 9) and (state.yG1 == 6)))) or (((state.xG1 == 3) and (state.yG1 == 6)) and ((state.dG1 == 1) or (state.dG1 == 2)))) or (((state.xG1 == 10) and (state.yG1 == 1)) and ((state.dG1 == 3) or (state.dG1 == 2)))) or (((state.xG1 == 10) and (state.yG1 == 6)) and ((state.dG1 == 1) or (state.dG1 == 2)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.yG1 < state.yP) and (state.xG1 == 6)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.yG1 < state.yP) and (state.xG1 == 8)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 5)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 5)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 5)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.yG1 < state.yP) and (state.xG1 == 6)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.yG1 < state.yP) and (state.xG1 == 8)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 10)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 10))))
			elif transition == 4:
				return ((((((((((((((((((((state.dG1 == 1) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 1))) or (((state.dG1 == 1) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 3)))) or (((state.dG1 == 1) and (state.yG1 >= 5)) and ((state.yG1 <= 5) and (state.xG1 == 3)))) or (((state.dG1 == 1) and (state.yG1 >= 5)) and ((state.yG1 <= 5) and (state.xG1 == 5)))) or (((state.dG1 == 1) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 6)))) or (((state.dG1 == 1) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 8)))) or (((state.dG1 == 1) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 10)))) or (((state.dG1 == 1) and (state.yG1 >= 5)) and ((state.yG1 <= 5) and (state.xG1 == 10)))) or (((state.xG1 == 1) and (state.yG1 == 1)) and ((state.dG1 == 2) or (state.dG1 == 1)))) or (((state.xG1 == 10) and (state.yG1 == 1)) and ((state.dG1 == 0) or (state.dG1 == 1)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.yG1 < state.yP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.yG1 < state.yP) and (state.xG1 == 6)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 < state.yP) and (state.xG1 == 5)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 5))))
			elif transition == 5:
				return ((((((((((((((((((((((((((state.dG1 == 3) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 1))) or (((state.dG1 == 3) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 3)))) or (((state.dG1 == 3) and (state.yG1 >= 5)) and ((state.yG1 <= 5) and (state.xG1 == 3)))) or (((state.dG1 == 3) and (state.yG1 >= 5)) and ((state.yG1 <= 5) and (state.xG1 == 5)))) or (((state.dG1 == 3) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 6)))) or (((state.dG1 == 3) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 8)))) or (((state.dG1 == 3) and (state.yG1 >= 2)) and ((state.yG1 <= 3) and (state.xG1 == 10)))) or (((state.dG1 == 3) and (state.yG1 >= 5)) and ((state.yG1 <= 5) and (state.xG1 == 10)))) or (((state.xG1 == 1) and (state.yG1 == 4)) and ((state.dG1 == 2) or (state.dG1 == 3)))) or (((state.xG1 == 3) and (state.yG1 == 6)) and ((state.dG1 == 0) or (state.dG1 == 3)))) or (((state.xG1 == 5) and (state.yG1 == 6)) and ((state.dG1 == 2) or (state.dG1 == 3)))) or (((state.xG1 == 10) and (state.yG1 == 6)) and ((state.dG1 == 0) or (state.dG1 == 3)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.yG1 > state.yP) and (state.xG1 == 3)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.yG1 > state.yP) and (state.xG1 == 3)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 < state.yP) and (state.xG1 == 10)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 10)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.yG1 > state.yP) and (state.xG1 == 10)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 10))))
			elif transition == 6:
				return ((((((((((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 3))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 5)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 > state.yP) and (state.xG1 == 5)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 5))))
			elif transition == 7:
				return (((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 3))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 8))))
			elif transition == 8:
				return ((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.yG1 < state.yP) and (state.xG1 == 3)))
			elif transition == 9:
				return (((((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 3))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 5)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 8))))
			elif transition == 10:
				return ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))
			elif transition == 11:
				return ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))
			elif transition == 12:
				return ((((((((((state.yG1 == state.yP) and (state.yG1 == 1)) and ((state.xG1 == state.xP) and (state.xG1 == 3))) or (((state.yG1 == state.yP) and (state.yG1 == 1)) and ((state.xG1 == state.xP) and (state.xG1 == 6)))) or (((state.yG1 == state.yP) and (state.yG1 == 1)) and ((state.xG1 == state.xP) and (state.xG1 == 8)))) or (((state.yG1 == state.yP) and (state.yG1 == 4)) and ((state.xG1 == state.xP) and (state.xG1 == 3)))) or (((state.yG1 == state.yP) and (state.yG1 == 4)) and ((state.xG1 == state.xP) and (state.xG1 == 5)))) or (((state.yG1 == state.yP) and (state.yG1 == 4)) and ((state.xG1 == state.xP) and (state.xG1 == 6)))) or (((state.yG1 == state.yP) and (state.yG1 == 4)) and ((state.xG1 == state.xP) and (state.xG1 == 8)))) or (((state.yG1 == state.yP) and (state.yG1 == 4)) and ((state.xG1 == state.xP) and (state.xG1 == 10))))
			elif transition == 13:
				return ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))
			elif transition == 14:
				return ((((((((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.yG1 < state.yP) and (state.xG1 == 6))) or ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))) or ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 5)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.yG1 > state.yP) and (state.xG1 == 5)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.yG1 > state.yP) and (state.xG1 == 10)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 10))))
			elif transition == 15:
				return ((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))
			elif transition == 16:
				return ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))
			elif transition == 17:
				return ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))
			elif transition == 18:
				return (((((state.yG1 == state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 8))) or ((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.yG1 < state.yP) and (state.xG1 == 8))))
			elif transition == 19:
				return (((((((((((((state.xG1 == state.xP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.yG1 < state.yP) and (state.xG1 == 8))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.yG1 < state.yP) and (state.xG1 == 5)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.yG1 > state.yP) and (state.xG1 == 5)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 5)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.yG1 < state.yP) and (state.xG1 == 6)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.yG1 < state.yP) and (state.xG1 == 8)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.yG1 > state.yP) and (state.xG1 == 8)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 8))))
			elif transition == 20:
				return ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))
			elif transition == 21:
				return ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))
			elif transition == 22:
				return ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))
			elif transition == 23:
				return ((((state.yG1 < state.yP) and (state.yG1 == 1)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))
			elif transition == 24:
				return ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))
			elif transition == 25:
				return ((((((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 < state.yP) and (state.xG1 == 3))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 3))))
			elif transition == 26:
				return ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.yG1 < state.yP) and (state.xG1 == 3)))
			elif transition == 27:
				return ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.yG1 < state.yP) and (state.xG1 == 3)))
			elif transition == 28:
				return ((((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.yG1 < state.yP) and (state.xG1 == 3))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 3)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 3))))
			elif transition == 29:
				return (((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 3))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 3))))
			elif transition == 30:
				return (((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 > state.yP) and (state.xG1 == 3))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 8))))
			elif transition == 31:
				return (((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.yG1 > state.yP) and (state.xG1 == 3))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 3))))
			elif transition == 32:
				return (((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 3))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 5))))
			elif transition == 33:
				return ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))
			elif transition == 34:
				return (((((((((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 3))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 < state.yP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 > state.yP) and (state.xG1 == 6)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 8))))
			elif transition == 35:
				return ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 3)))
			elif transition == 36:
				return (((((((((((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 3))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.yG1 > state.yP) and (state.xG1 == 6)))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))) or ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.yG1 > state.yP) and (state.xG1 == 8)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))) or ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.yG1 < state.yP) and (state.xG1 == 10)))) or ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 10))))
			elif transition == 37:
				return (((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 < state.xP) and (state.xG1 == 5))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 < state.xP) and (state.xG1 == 6))))
			elif transition == 38:
				return ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.yG1 < state.yP) and (state.xG1 == 5)))
			elif transition == 39:
				return ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 5)))
			elif transition == 40:
				return ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 5)))
			elif transition == 41:
				return ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 5)))
			elif transition == 42:
				return ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 5)))
			elif transition == 43:
				return ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 5)))
			elif transition == 44:
				return ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))
			elif transition == 45:
				return ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))
			elif transition == 46:
				return ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 6)))
			elif transition == 47:
				return ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))
			elif transition == 48:
				return ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 < state.xP) and (state.xG1 == 6)))
			elif transition == 49:
				return ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 8)))
			elif transition == 50:
				return (((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 8))) or ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 2)) and ((state.xG1 > state.xP) and (state.xG1 == 8))))
			elif transition == 51:
				return ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 > state.yP) and (state.xG1 == 8)))
			elif transition == 52:
				return ((((state.yG1 > state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 < state.xP) and (state.xG1 == 8)))
			elif transition == 53:
				return ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.yG1 < state.yP) and (state.xG1 == 10)))
			elif transition == 54:
				return ((((state.yG1 == state.yP) and (state.yG1 == 4)) and (state.dG1 == 3)) and ((state.xG1 > state.xP) and (state.xG1 == 10)))
			elif transition == 55:
				return ((((state.xG1 == state.xP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.yG1 > state.yP) and (state.xG1 == 10)))
			elif transition == 56:
				return ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 0)) and ((state.xG1 > state.xP) and (state.xG1 == 10)))
			elif transition == 57:
				return ((((state.yG1 < state.yP) and (state.yG1 == 4)) and (state.dG1 == 1)) and ((state.xG1 > state.xP) and (state.xG1 == 10)))
			elif transition == 58:
				return ((state.xG0 <= state.xG1) and ((state.xG0 != state.xG1) or (state.yG0 <= state.yG1)))
			elif transition >= 59 and transition < 61:
				return ((state.xG0 > state.xG1) or ((state.xG0 == state.xG1) and (state.yG0 > state.yG1)))
			elif transition >= 61 and transition < 63:
				return ((state.xG0 <= state.xG1) and ((state.xG0 != state.xG1) or (state.yG0 <= state.yG1)))
			elif transition == 63:
				return ((state.xG0 > state.xG1) or ((state.xG0 == state.xG1) and (state.yG0 > state.yG1)))
			elif transition == 64:
				return True
			elif transition == 65:
				return ((state.xG0 > state.xG1) or ((state.xG0 == state.xG1) and (state.yG0 > state.yG1)))
			elif transition == 66:
				return ((state.xG0 <= state.xG1) and ((state.xG0 != state.xG1) or (state.yG0 <= state.yG1)))
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
				if True:
					return (5 / 10)
			elif transition == 7:
				if branch == 0:
					return (92 / 100)
				elif branch == 1:
					return (8 / 100)
			elif transition == 8:
				if branch == 0:
					return (8 / 10)
				elif branch == 1:
					return (2 / 10)
			elif transition == 9:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 10:
				if branch == 0:
					return (78 / 100)
				elif branch == 1:
					return (22 / 100)
			elif transition == 11:
				if branch == 0:
					return (86 / 100)
				elif branch == 1:
					return (14 / 100)
			elif transition == 12:
				return 1
			elif transition == 13:
				if branch == 0:
					return (64 / 100)
				elif branch == 1:
					return (36 / 100)
			elif transition == 14:
				if True:
					return (5 / 10)
			elif transition == 15:
				if branch == 0:
					return (22 / 100)
				elif branch == 1:
					return (78 / 100)
			elif transition == 16:
				if branch == 0:
					return (46 / 100)
				elif branch == 1:
					return (54 / 100)
			elif transition == 17:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 18:
				if branch == 0:
					return (4 / 10)
				elif branch == 1:
					return (6 / 10)
			elif transition == 19:
				if True:
					return (5 / 10)
			elif transition == 20:
				if branch == 0:
					return (36 / 100)
				elif branch == 1:
					return (64 / 100)
			elif transition == 21:
				if branch == 0:
					return (75 / 100)
				elif branch == 1:
					return (25 / 100)
			elif transition == 22:
				if branch == 0:
					return (2 / 10)
				elif branch == 1:
					return (8 / 10)
			elif transition == 23:
				if branch == 0:
					return (67 / 100)
				elif branch == 1:
					return (33 / 100)
			elif transition == 24:
				if branch == 0:
					return (61 / 100)
				elif branch == 1:
					return (26 / 100)
				elif branch == 2:
					return (13 / 100)
			elif transition == 25:
				if branch == 0:
					return (34 / 100)
				elif branch >= 1:
					return (33 / 100)
			elif transition == 26:
				if branch == 0:
					return (16 / 100)
				elif branch == 1:
					return (67 / 100)
				elif branch == 2:
					return (17 / 100)
			elif transition == 27:
				if branch == 0:
					return (28 / 100)
				elif branch == 1:
					return (43 / 100)
				elif branch == 2:
					return (29 / 100)
			elif transition == 28:
				if branch == 0:
					return (34 / 100)
				elif branch >= 1:
					return (33 / 100)
			elif transition == 29:
				if branch == 0:
					return (34 / 100)
				elif branch >= 1:
					return (33 / 100)
			elif transition == 30:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 31:
				if branch == 0:
					return (34 / 100)
				elif branch >= 1:
					return (33 / 100)
			elif transition == 32:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 33:
				if branch == 0:
					return (5 / 10)
				elif branch >= 1:
					return (25 / 100)
			elif transition == 34:
				if True:
					return (5 / 10)
			elif transition == 35:
				if branch == 0:
					return (67 / 100)
				elif branch == 1:
					return (33 / 100)
			elif transition == 36:
				if True:
					return (5 / 10)
			elif transition == 37:
				if branch == 0:
					return (89 / 100)
				elif branch == 1:
					return (11 / 100)
			elif transition == 38:
				if branch == 0:
					return (83 / 100)
				elif branch == 1:
					return (17 / 100)
			elif transition == 39:
				if branch == 0:
					return (17 / 100)
				elif branch == 1:
					return (83 / 100)
			elif transition == 40:
				if branch == 0:
					return (17 / 100)
				elif branch == 1:
					return (83 / 100)
			elif transition == 41:
				if branch == 0:
					return (75 / 100)
				elif branch == 1:
					return (25 / 100)
			elif transition == 42:
				if branch == 0:
					return (95 / 100)
				elif branch == 1:
					return (5 / 100)
			elif transition == 43:
				if branch == 0:
					return (11 / 100)
				elif branch == 1:
					return (89 / 100)
			elif transition == 44:
				if branch == 0:
					return (57 / 100)
				elif branch == 1:
					return (43 / 100)
			elif transition == 45:
				if branch == 0:
					return (75 / 100)
				elif branch == 1:
					return (25 / 100)
			elif transition == 46:
				if branch == 0:
					return (67 / 100)
				elif branch == 1:
					return (33 / 100)
			elif transition == 47:
				if branch == 0:
					return (69 / 100)
				elif branch == 1:
					return (31 / 100)
			elif transition == 48:
				if branch == 0:
					return (33 / 100)
				elif branch == 1:
					return (67 / 100)
			elif transition == 49:
				if branch == 0:
					return (44 / 100)
				elif branch == 1:
					return (56 / 100)
			elif transition == 50:
				if branch == 0:
					return (83 / 100)
				elif branch == 1:
					return (17 / 100)
			elif transition == 51:
				if branch == 0:
					return (43 / 100)
				elif branch == 1:
					return (57 / 100)
			elif transition == 52:
				if branch == 0:
					return (56 / 100)
				elif branch == 1:
					return (44 / 100)
			elif transition == 53:
				if branch == 0:
					return (45 / 100)
				elif branch == 1:
					return (55 / 100)
			elif transition == 54:
				if branch == 0:
					return (79 / 100)
				elif branch == 1:
					return (21 / 100)
			elif transition == 55:
				if branch == 0:
					return (2 / 10)
				elif branch == 1:
					return (8 / 10)
			elif transition == 56:
				if branch == 0:
					return (75 / 100)
				elif branch == 1:
					return (25 / 100)
			elif transition == 57:
				if branch == 0:
					return (44 / 100)
				elif branch == 1:
					return (56 / 100)
			elif transition == 58:
				return 1
			elif transition == 59:
				return 1
			elif transition == 60:
				return 1
			elif transition == 61:
				return 1
			elif transition == 62:
				return 1
			elif transition == 63:
				return 1
			elif transition == 64:
				return 1
			elif transition == 65:
				return 1
			elif transition == 66:
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
						target_state.xG1 = state.xG0
						target_state.yG1 = state.yG0
						target_state.dG1 = state.dG0
				elif transition == 1:
					if branch == 0:
						pass
				elif transition == 2:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
				elif transition == 3:
					if branch == 0:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 4:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
				elif transition == 5:
					if branch == 0:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 6:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
				elif transition == 7:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 8:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 9:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 10:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 11:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 12:
					if branch == 0:
						pass
				elif transition == 13:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 14:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 15:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 16:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
				elif transition == 17:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 18:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
				elif transition == 19:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 20:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
				elif transition == 21:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 22:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 23:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 24:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 2:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 25:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 2:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 26:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 2:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 27:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 2:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 28:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 2:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 29:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 2:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 30:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 31:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 2:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 32:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
				elif transition == 33:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 2:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 34:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 35:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
				elif transition == 36:
					if branch == 0:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 37:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 38:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 39:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 40:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 41:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 42:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
				elif transition == 43:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 44:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 45:
					if branch == 0:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 46:
					if branch == 0:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 47:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 48:
					if branch == 0:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 49:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 50:
					if branch == 0:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 51:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 52:
					if branch == 0:
						target_state.xG1 = (state.xG1 + 1)
						if target_state.xG1 > 11:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is greater than the upper bound of 11 for variable \"xG1\".")
						target_state.dG1 = 0
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 53:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 54:
					if branch == 0:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 55:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 56:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.yG1 = (state.yG1 - 1)
						if target_state.yG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is less than the lower bound of 0 for variable \"yG1\".")
						target_state.dG1 = 3
				elif transition == 57:
					if branch == 0:
						target_state.yG1 = (state.yG1 + 1)
						if target_state.yG1 > 7:
							raise OverflowError("Assigned value of " + str(target_state.yG1) + " is greater than the upper bound of 7 for variable \"yG1\".")
						target_state.dG1 = 1
					elif branch == 1:
						target_state.xG1 = (state.xG1 - 1)
						if target_state.xG1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.xG1) + " is less than the lower bound of 0 for variable \"xG1\".")
						target_state.dG1 = 2
				elif transition == 58:
					if branch == 0:
						pass
				elif transition == 59:
					if branch == 0:
						target_state.xG1 = state.xG0
						target_state.yG1 = state.yG0
						target_state.dG1 = state.dG0
				elif transition == 60:
					if branch == 0:
						target_state.xG1 = state.xG0
						target_state.yG1 = state.yG0
						target_state.dG1 = state.dG0
				elif transition == 61:
					if branch == 0:
						pass
				elif transition == 62:
					if branch == 0:
						pass
				elif transition == 63:
					if branch == 0:
						target_state.xG1 = state.xG0
						target_state.yG1 = state.yG0
						target_state.dG1 = state.dG0
				elif transition == 64:
					if branch == 0:
						target_state.xG1 = 0
						target_state.yG1 = 0
				elif transition == 65:
					if branch == 0:
						target_state.xG1 = state.xG0
						target_state.yG1 = state.yG0
						target_state.dG1 = state.dG0
				elif transition == 66:
					if branch == 0:
						pass

# Automaton: pacman
class pacmanAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [11]
		self.transition_labels = [[1, 1, 4, 5, 5, 5, 5, 6, 6, 9, 9]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
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
				return ((((((state.xP == 3) and (state.yP == 1)) and (state.pMove == 2)) or (((state.xP == 6) and (state.yP == 1)) and (state.pMove == 2))) or (((state.xP == 8) and (state.yP == 1)) and (state.pMove == 2))) or (((state.xP == 5) and (state.yP == 4)) and (state.pMove == 2)))
			elif transition == 1:
				return (((((state.xP == 3) and (state.yP == 4)) or ((state.xP == 6) and (state.yP == 4))) or ((state.xP == 8) and (state.yP == 4))) or ((state.xP == 10) and (state.yP == 4)))
			elif transition == 2:
				return (((((((((state.xP == 5) and (state.yP == 4)) or ((state.xP == 8) and (state.yP == 1))) or ((state.xP == 6) and (state.yP == 4))) or ((state.xP == 6) and (state.yP == 1))) or ((state.xP == 8) and (state.yP == 4))) or ((state.xP == 3) and (state.yP == 4))) or ((state.xP == 10) and (state.yP == 4))) or ((state.xP == 3) and (state.yP == 1)))
			elif transition == 3:
				return ((((((((((((((((state.dP == 0) and (state.xP >= 2)) and ((state.xP <= 2) and (state.yP == 6))) or (((state.dP == 0) and (state.xP >= 6)) and ((state.xP <= 9) and (state.yP == 6)))) or (((state.xP == 5) and (state.yP == 6)) and ((state.dP == 1) or (state.dP == 0)))) or (((state.dP == 0) and (state.xP >= 2)) and ((state.xP <= 2) and (state.yP == 1)))) or (((state.dP == 0) and (state.xP >= 4)) and ((state.xP <= 5) and (state.yP == 1)))) or (((state.dP == 0) and (state.xP >= 7)) and ((state.xP <= 7) and (state.yP == 1)))) or (((state.dP == 0) and (state.xP >= 9)) and ((state.xP <= 9) and (state.yP == 1)))) or (((state.dP == 0) and (state.xP >= 2)) and ((state.xP <= 2) and (state.yP == 4)))) or ((state.xP == 1) and (state.yP == 6))) or (((state.dP == 0) and (state.xP >= 4)) and ((state.xP <= 4) and (state.yP == 4)))) or (((state.xP == 1) and (state.yP == 1)) and ((state.dP == 3) or (state.dP == 0)))) or (((state.dP == 0) and (state.xP >= 7)) and ((state.xP <= 7) and (state.yP == 4)))) or (((state.xP == 1) and (state.yP == 4)) and ((state.dP == 1) or (state.dP == 0)))) or (((state.dP == 0) and (state.xP >= 9)) and ((state.xP <= 9) and (state.yP == 4))))
			elif transition == 4:
				return (((((((((((((((state.dP == 2) and (state.xP >= 2)) and ((state.xP <= 2) and (state.yP == 6))) or (((state.dP == 2) and (state.xP >= 6)) and ((state.xP <= 9) and (state.yP == 6)))) or (((state.dP == 2) and (state.xP >= 2)) and ((state.xP <= 2) and (state.yP == 1)))) or (((state.dP == 2) and (state.xP >= 4)) and ((state.xP <= 5) and (state.yP == 1)))) or (((state.dP == 2) and (state.xP >= 7)) and ((state.xP <= 7) and (state.yP == 1)))) or (((state.dP == 2) and (state.xP >= 9)) and ((state.xP <= 9) and (state.yP == 1)))) or (((state.dP == 2) and (state.xP >= 2)) and ((state.xP <= 2) and (state.yP == 4)))) or (((state.dP == 2) and (state.xP >= 4)) and ((state.xP <= 4) and (state.yP == 4)))) or (((state.dP == 2) and (state.xP >= 7)) and ((state.xP <= 7) and (state.yP == 4)))) or (((state.dP == 2) and (state.xP >= 9)) and ((state.xP <= 9) and (state.yP == 4)))) or (((state.xP == 3) and (state.yP == 6)) and ((state.dP == 1) or (state.dP == 2)))) or (((state.xP == 10) and (state.yP == 1)) and ((state.dP == 3) or (state.dP == 2)))) or (((state.xP == 10) and (state.yP == 6)) and ((state.dP == 1) or (state.dP == 2))))
			elif transition == 5:
				return ((((((((((((state.dP == 1) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 1))) or (((state.dP == 1) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 3)))) or (((state.dP == 1) and (state.yP >= 5)) and ((state.yP <= 5) and (state.xP == 3)))) or (((state.xP == 1) and (state.yP == 1)) and ((state.dP == 2) or (state.dP == 1)))) or (((state.xP == 10) and (state.yP == 1)) and ((state.dP == 0) or (state.dP == 1)))) or (((state.dP == 1) and (state.yP >= 5)) and ((state.yP <= 5) and (state.xP == 5)))) or (((state.dP == 1) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 6)))) or (((state.dP == 1) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 8)))) or (((state.dP == 1) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 10)))) or (((state.dP == 1) and (state.yP >= 5)) and ((state.yP <= 5) and (state.xP == 10))))
			elif transition == 6:
				return ((((((((((((((state.dP == 3) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 1))) or (((state.dP == 3) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 3)))) or (((state.dP == 3) and (state.yP >= 5)) and ((state.yP <= 5) and (state.xP == 3)))) or (((state.dP == 3) and (state.yP >= 5)) and ((state.yP <= 5) and (state.xP == 5)))) or (((state.dP == 3) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 6)))) or (((state.dP == 3) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 8)))) or (((state.dP == 3) and (state.yP >= 2)) and ((state.yP <= 3) and (state.xP == 10)))) or (((state.dP == 3) and (state.yP >= 5)) and ((state.yP <= 5) and (state.xP == 10)))) or (((state.xP == 1) and (state.yP == 4)) and ((state.dP == 2) or (state.dP == 3)))) or (((state.xP == 3) and (state.yP == 6)) and ((state.dP == 0) or (state.dP == 3)))) or (((state.xP == 5) and (state.yP == 6)) and ((state.dP == 2) or (state.dP == 3)))) or (((state.xP == 10) and (state.yP == 6)) and ((state.dP == 0) or (state.dP == 3))))
			elif transition == 7:
				return ((((((((state.xP == 8) and (state.yP == 1)) or ((state.xP == 3) and (state.yP == 1))) or ((state.xP == 8) and (state.yP == 4))) or ((state.xP == 5) and (state.yP == 4))) or ((state.xP == 6) and (state.yP == 1))) or ((state.xP == 3) and (state.yP == 4))) or ((state.xP == 6) and (state.yP == 4)))
			elif transition == 8:
				return (((state.xP == 10) and (state.yP == 4)) and (state.pMove == 2))
			elif transition == 9:
				return (((((((state.xP == 3) and (state.yP == 1)) or ((state.xP == 5) and (state.yP == 4))) or ((state.xP == 3) and (state.yP == 4))) or ((state.xP == 6) and (state.yP == 1))) or ((state.xP == 10) and (state.yP == 4))) or ((state.xP == 8) and (state.yP == 1)))
			elif transition == 10:
				return ((((state.xP == 8) and (state.yP == 4)) and (state.pMove == 2)) or (((state.xP == 6) and (state.yP == 4)) and (state.pMove == 2)))
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
						target_state.yP = (state.yP - 1)
						if target_state.yP < 1:
							raise OverflowError("Assigned value of " + str(target_state.yP) + " is less than the lower bound of 1 for variable \"yP\".")
						target_state.dP = 3
				elif transition == 2:
					if branch == 0:
						target_state.xP = (state.xP - 1)
						if target_state.xP < 1:
							raise OverflowError("Assigned value of " + str(target_state.xP) + " is less than the lower bound of 1 for variable \"xP\".")
						target_state.dP = 2
				elif transition == 3:
					if branch == 0:
						target_state.xP = (state.xP + 1)
						if target_state.xP > 11:
							raise OverflowError("Assigned value of " + str(target_state.xP) + " is greater than the upper bound of 11 for variable \"xP\".")
						target_state.dP = 0
				elif transition == 4:
					if branch == 0:
						target_state.xP = (state.xP - 1)
						if target_state.xP < 1:
							raise OverflowError("Assigned value of " + str(target_state.xP) + " is less than the lower bound of 1 for variable \"xP\".")
						target_state.dP = 2
				elif transition == 5:
					if branch == 0:
						target_state.yP = (state.yP + 1)
						if target_state.yP > 7:
							raise OverflowError("Assigned value of " + str(target_state.yP) + " is greater than the upper bound of 7 for variable \"yP\".")
						target_state.dP = 1
				elif transition == 6:
					if branch == 0:
						target_state.yP = (state.yP - 1)
						if target_state.yP < 1:
							raise OverflowError("Assigned value of " + str(target_state.yP) + " is less than the lower bound of 1 for variable \"yP\".")
						target_state.dP = 3
				elif transition == 7:
					if branch == 0:
						target_state.xP = (state.xP + 1)
						if target_state.xP > 11:
							raise OverflowError("Assigned value of " + str(target_state.xP) + " is greater than the upper bound of 11 for variable \"xP\".")
						target_state.dP = 0
				elif transition == 8:
					if branch == 0:
						pass
				elif transition == 9:
					if branch == 0:
						target_state.yP = (state.yP + 1)
						if target_state.yP > 7:
							raise OverflowError("Assigned value of " + str(target_state.yP) + " is greater than the upper bound of 7 for variable \"yP\".")
						target_state.dP = 1
				elif transition == 10:
					if branch == 0:
						pass

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_arbiter", "_aut_ghost0", "_aut_ghost1", "_aut_pacman")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ", 1: "down", 2: "g0", 3: "g1", 4: "left", 5: "p", 6: "right", 7: "stop0", 8: "stop1", 9: "up" }
		self.sync_vectors = [[0, -1, -1, -1, 0], [-1, 0, -1, -1, 0], [-1, -1, 0, -1, 0], [-1, -1, -1, 0, 0], [1, 1, 1, 1, 1], [2, 2, -1, -1, 2], [3, -1, 3, -1, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6], [7, 7, -1, -1, 7], [8, -1, 8, -1, 8], [9, 9, 9, 9, 9]]
		self.properties = [
			Property("crash", PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("pMove", None, "int", 0, 2),
			VariableInfo("steps", None, "int", 0, 5),
			VariableInfo("xG0", None, "int", 0, 11),
			VariableInfo("yG0", None, "int", 0, 7),
			VariableInfo("dG0", None, "int", 0, 3),
			VariableInfo("xG1", None, "int", 0, 11),
			VariableInfo("yG1", None, "int", 0, 7),
			VariableInfo("dG1", None, "int", 0, 3),
			VariableInfo("xP", None, "int", 1, 11),
			VariableInfo("yP", None, "int", 1, 7),
			VariableInfo("dP", None, "int", 0, 3),
			VariableInfo("arbiter_location", 0, "int", 0, 2)
		]
		self._aut_arbiter = arbiterAutomaton(self)
		self._aut_ghost0 = ghost0Automaton(self)
		self._aut_ghost1 = ghost1Automaton(self)
		self._aut_pacman = pacmanAutomaton(self)
		self.components = [self._aut_arbiter, self._aut_ghost0, self._aut_ghost1, self._aut_pacman]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.pMove = 0
		state.steps = 0
		state.xG0 = 3
		state.yG0 = 4
		state.dG0 = 0
		state.xG1 = 3
		state.yG1 = 4
		state.dG1 = 0
		state.xP = 1
		state.yP = 1
		state.dP = 0
		self._aut_arbiter.set_initial_values(state)
		self._aut_ghost0.set_initial_values(state)
		self._aut_ghost1.set_initial_values(state)
		self._aut_pacman.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.Crash = False
		self._aut_arbiter.set_initial_transient_values(transient)
		self._aut_ghost0.set_initial_transient_values(transient)
		self._aut_ghost1.set_initial_transient_values(transient)
		self._aut_pacman.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return self.network._get_transient_value(state, "Crash")
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return transient.Crash
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_arbiter.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_ghost0.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_ghost1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_pacman.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_arbiter = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_arbiter.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_arbiter.get_guard_value(state, i):
				trans_arbiter[self._aut_arbiter.get_transition_label(state, i)].append(i)
		trans_ghost0 = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_ghost0.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_ghost0.get_guard_value(state, i):
				trans_ghost0[self._aut_ghost0.get_transition_label(state, i)].append(i)
		trans_ghost1 = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_ghost1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_ghost1.get_guard_value(state, i):
				trans_ghost1[self._aut_ghost1.get_transition_label(state, i)].append(i)
		trans_pacman = [[], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_pacman.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_pacman.get_guard_value(state, i):
				trans_pacman[self._aut_pacman.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1]]
			# arbiter
			if synced is not None:
				if sv[0] != -1:
					if len(trans_arbiter[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_arbiter[sv[0]][0]
						for i in range(1, len(trans_arbiter[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_arbiter[sv[0]][i]
			# ghost0
			if synced is not None:
				if sv[1] != -1:
					if len(trans_ghost0[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_ghost0[sv[1]][0]
						for i in range(1, len(trans_ghost0[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_ghost0[sv[1]][i]
			# ghost1
			if synced is not None:
				if sv[2] != -1:
					if len(trans_ghost1[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_ghost1[sv[2]][0]
						for i in range(1, len(trans_ghost1[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_ghost1[sv[2]][i]
			# pacman
			if synced is not None:
				if sv[3] != -1:
					if len(trans_pacman[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_pacman[sv[3]][0]
						for i in range(1, len(trans_pacman[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_pacman[sv[3]][i]
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
			branch_count = self._aut_arbiter.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_arbiter.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_arbiter.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_ghost0.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_ghost0.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_ghost0.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_ghost1.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_ghost1.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_ghost1.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_pacman.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_pacman.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_pacman.get_probability_value(state, transition.transitions[3], 0)
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
				self._aut_arbiter.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_ghost0.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_ghost1.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_pacman.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
