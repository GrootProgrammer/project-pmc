# breakdown-queues

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
	__slots__ = ("buf", "reset", "BufferedServer_location", "on", "TypeOneSources_location", "on_1", "TypeTwoSources_location", "on_2", "Repair_location", "down")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.buf
		elif variable == 1:
			return self.reset
		elif variable == 2:
			return self.BufferedServer_location
		elif variable == 3:
			return self.on
		elif variable == 4:
			return self.TypeOneSources_location
		elif variable == 5:
			return self.on_1
		elif variable == 6:
			return self.TypeTwoSources_location
		elif variable == 7:
			return self.on_2
		elif variable == 8:
			return self.Repair_location
		elif variable == 9:
			return self.down
	
	def copy_to(self, other: State):
		other.buf = self.buf
		other.reset = self.reset
		other.BufferedServer_location = self.BufferedServer_location
		other.on = self.on
		other.TypeOneSources_location = self.TypeOneSources_location
		other.on_1 = self.on_1
		other.TypeTwoSources_location = self.TypeTwoSources_location
		other.on_2 = self.on_2
		other.Repair_location = self.Repair_location
		other.down = self.down
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.buf == other.buf and self.reset == other.reset and self.BufferedServer_location == other.BufferedServer_location and self.on == other.on and self.TypeOneSources_location == other.TypeOneSources_location and self.on_1 == other.on_1 and self.TypeTwoSources_location == other.TypeTwoSources_location and self.on_2 == other.on_2 and self.Repair_location == other.Repair_location and self.down == other.down
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.buf)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.reset)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.BufferedServer_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.on)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.TypeOneSources_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.on_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.TypeTwoSources_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.on_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Repair_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.down)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "buf = " + str(self.buf)
		result += ", reset = " + str(self.reset)
		result += ", BufferedServer_location = " + str(self.BufferedServer_location)
		result += ", on = " + str(self.on)
		result += ", TypeOneSources_location = " + str(self.TypeOneSources_location)
		result += ", on_1 = " + str(self.on_1)
		result += ", TypeTwoSources_location = " + str(self.TypeTwoSources_location)
		result += ", on_2 = " + str(self.on_2)
		result += ", Repair_location = " + str(self.Repair_location)
		result += ", down = " + str(self.down)
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

# Automaton: BufferedServer
class BufferedServerAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [4, 4, 1]
		self.transition_labels = [[0, 1, 0, 2], [0, 1, 0, 2], [3]]
		self.branch_counts = [[1, 1, 1, 1], [1, 1, 1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.BufferedServer_location = 0
		state.on = False
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.BufferedServer_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.BufferedServer_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.BufferedServer_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.BufferedServer_location
		if location == 2:
			return True
		elif location == 0:
			if transition == 0:
				return state.on
			elif transition == 1:
				return (not state.on)
			elif transition == 2:
				return state.on
			elif transition == 3:
				return True
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return state.on
			elif transition == 1:
				return (not state.on)
			elif transition == 2:
				return state.on
			elif transition == 3:
				return True
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.BufferedServer_location
		if location == 2:
			return None
		elif location == 0:
			if transition == 0:
				return 3
			elif transition == 1:
				return None
			elif transition == 2:
				return 100
			elif transition == 3:
				return None
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return 3
			elif transition == 1:
				return None
			elif transition == 2:
				return 100
			elif transition == 3:
				return None
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.BufferedServer_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.BufferedServer_location
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
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.BufferedServer_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.on = False
				elif transition == 1:
					if branch == 0:
						target_state.on = True
				elif transition == 2:
					if branch == 0:
						target_state.buf = max(0, (state.buf - 1))
						target_state.reset = (state.reset or (state.buf == 1))
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.on = False
				elif transition == 1:
					if branch == 0:
						target_state.on = True
				elif transition == 2:
					if branch == 0:
						target_state.buf = max(0, (state.buf - 1))
						target_state.reset = (state.reset or (state.buf == 1))
		elif assignment_index == 1:
			location = state.BufferedServer_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.BufferedServer_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.BufferedServer_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.BufferedServer_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.buf = min(8, (state.buf + 1))
						target_state.BufferedServer_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.BufferedServer_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.BufferedServer_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.BufferedServer_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.buf = min(8, (state.buf + 1))
						target_state.BufferedServer_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.BufferedServer_location = 1

# Automaton: TypeOneSources
class TypeOneSourcesAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 1, 3, 1]
		self.transition_labels = [[0, 4, 0], [5], [0, 4, 0], [3]]
		self.branch_counts = [[1, 1, 1], [1], [1, 1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.TypeOneSources_location = 0
		state.on_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.TypeOneSources_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.TypeOneSources_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.TypeOneSources_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.TypeOneSources_location
		if location == 1 or location == 3:
			return True
		elif location == 0:
			if transition == 0:
				return (state.on_1 > 0)
			elif transition == 1:
				return (state.on_1 < 5)
			elif transition == 2:
				return (state.on_1 > 0)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.on_1 > 0)
			elif transition == 1:
				return (state.on_1 < 5)
			elif transition == 2:
				return (state.on_1 > 0)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.TypeOneSources_location
		if location == 1 or location == 3:
			return None
		elif location == 0:
			if transition == 0:
				return (2 * state.on_1)
			elif transition == 1:
				return None
			elif transition == 2:
				return (3 * state.on_1)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (2 * state.on_1)
			elif transition == 1:
				return None
			elif transition == 2:
				return (3 * state.on_1)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.TypeOneSources_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.TypeOneSources_location
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
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.TypeOneSources_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.on_1 = (state.on_1 - 1)
						if target_state.on_1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.on_1) + " is less than the lower bound of 0 for variable \"on_1\".")
				elif transition == 1:
					if branch == 0:
						target_state.on_1 = (state.on_1 + 1)
						if target_state.on_1 > 5:
							raise OverflowError("Assigned value of " + str(target_state.on_1) + " is greater than the upper bound of 5 for variable \"on_1\".")
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.on_1 = (state.on_1 - 1)
						if target_state.on_1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.on_1) + " is less than the lower bound of 0 for variable \"on_1\".")
				elif transition == 1:
					if branch == 0:
						target_state.on_1 = (state.on_1 + 1)
						if target_state.on_1 > 5:
							raise OverflowError("Assigned value of " + str(target_state.on_1) + " is greater than the upper bound of 5 for variable \"on_1\".")
		elif assignment_index == 1:
			location = state.TypeOneSources_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.TypeOneSources_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.TypeOneSources_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.TypeOneSources_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.TypeOneSources_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.TypeOneSources_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.TypeOneSources_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.TypeOneSources_location = 1
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.TypeOneSources_location = 2

# Automaton: TypeTwoSources
class TypeTwoSourcesAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 1, 3, 1]
		self.transition_labels = [[0, 6, 0], [5], [0, 6, 0], [3]]
		self.branch_counts = [[1, 1, 1], [1], [1, 1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.TypeTwoSources_location = 0
		state.on_2 = 1
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.TypeTwoSources_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.TypeTwoSources_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.TypeTwoSources_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.TypeTwoSources_location
		if location == 1 or location == 3:
			return True
		elif location == 0:
			if transition == 0:
				return (state.on_2 > 0)
			elif transition == 1:
				return (state.on_2 < 5)
			elif transition == 2:
				return (state.on_2 > 0)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.on_2 > 0)
			elif transition == 1:
				return (state.on_2 < 5)
			elif transition == 2:
				return (state.on_2 > 0)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.TypeTwoSources_location
		if location == 1 or location == 3:
			return None
		elif location == 0:
			if transition == 0:
				return (4 * state.on_2)
			elif transition == 1:
				return None
			elif transition == 2:
				return (6 * state.on_2)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (4 * state.on_2)
			elif transition == 1:
				return None
			elif transition == 2:
				return (6 * state.on_2)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.TypeTwoSources_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.TypeTwoSources_location
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
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.TypeTwoSources_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.on_2 = (state.on_2 - 1)
						if target_state.on_2 < 0:
							raise OverflowError("Assigned value of " + str(target_state.on_2) + " is less than the lower bound of 0 for variable \"on_2\".")
				elif transition == 1:
					if branch == 0:
						target_state.on_2 = (state.on_2 + 1)
						if target_state.on_2 > 5:
							raise OverflowError("Assigned value of " + str(target_state.on_2) + " is greater than the upper bound of 5 for variable \"on_2\".")
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.on_2 = (state.on_2 - 1)
						if target_state.on_2 < 0:
							raise OverflowError("Assigned value of " + str(target_state.on_2) + " is less than the lower bound of 0 for variable \"on_2\".")
				elif transition == 1:
					if branch == 0:
						target_state.on_2 = (state.on_2 + 1)
						if target_state.on_2 > 5:
							raise OverflowError("Assigned value of " + str(target_state.on_2) + " is greater than the upper bound of 5 for variable \"on_2\".")
		elif assignment_index == 1:
			location = state.TypeTwoSources_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.TypeTwoSources_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.TypeTwoSources_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.TypeTwoSources_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.TypeTwoSources_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.TypeTwoSources_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.TypeTwoSources_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.TypeTwoSources_location = 1
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.TypeTwoSources_location = 2

# Automaton: Repair
class RepairAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 1, 3, 2, 4, 2]
		self.transition_labels = [[0, 7], [0], [0], [8, 9, 10], [0, 7], [7, 8, 9, 10], [0, 7]]
		self.branch_counts = [[1, 1], [1], [1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Repair_location = 0
		state.down = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Repair_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Repair_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Repair_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Repair_location
		if location == 1:
			return (state.down > 0)
		elif location == 2:
			return True
		elif location == 0:
			if transition == 0:
				return (state.down > 0)
			elif transition == 1:
				return True
			else:
				raise IndexError
		elif location == 3:
			return True
		elif location == 4:
			return True
		elif location == 5:
			return True
		elif location == 6:
			if transition == 0:
				return (state.down > 0)
			elif transition == 1:
				return True
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Repair_location
		if location == 1:
			return None
		elif location == 2:
			return 2
		elif location == 0:
			return None
		elif location == 3:
			return None
		elif location == 4:
			if transition == 0:
				return 2
			elif transition == 1:
				return None
			else:
				raise IndexError
		elif location == 5:
			return None
		elif location == 6:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Repair_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Repair_location
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
			else:
				raise IndexError
		elif location == 6:
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
			location = state.Repair_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.down = (state.down - 1)
						if target_state.down < 0:
							raise OverflowError("Assigned value of " + str(target_state.down) + " is less than the lower bound of 0 for variable \"down\".")
				elif transition == 1:
					if branch == 0:
						target_state.down = max((state.down + 1), 11)
						if target_state.down > 11:
							raise OverflowError("Assigned value of " + str(target_state.down) + " is greater than the upper bound of 11 for variable \"down\".")
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.down = (state.down - 1)
						if target_state.down < 0:
							raise OverflowError("Assigned value of " + str(target_state.down) + " is less than the lower bound of 0 for variable \"down\".")
			elif location == 4:
				if transition == 1:
					if branch == 0:
						target_state.down = max((state.down + 1), 11)
						if target_state.down > 11:
							raise OverflowError("Assigned value of " + str(target_state.down) + " is greater than the upper bound of 11 for variable \"down\".")
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.down = max((state.down + 1), 11)
						if target_state.down > 11:
							raise OverflowError("Assigned value of " + str(target_state.down) + " is greater than the upper bound of 11 for variable \"down\".")
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.down = (state.down - 1)
						if target_state.down < 0:
							raise OverflowError("Assigned value of " + str(target_state.down) + " is less than the lower bound of 0 for variable \"down\".")
				elif transition == 1:
					if branch == 0:
						target_state.down = max((state.down + 1), 11)
						if target_state.down > 11:
							raise OverflowError("Assigned value of " + str(target_state.down) + " is greater than the upper bound of 11 for variable \"down\".")
		elif assignment_index == 1:
			location = state.Repair_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Repair_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Repair_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Repair_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Repair_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Repair_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Repair_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Repair_location = 1
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Repair_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.Repair_location = 2
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Repair_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Repair_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.Repair_location = 6
				elif transition == 3:
					if branch == 0:
						target_state.Repair_location = 6
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.Repair_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Repair_location = 1

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_BufferedServer", "_aut_TypeOneSources", "_aut_TypeTwoSources", "_aut_Repair")
	
	def __init__(self):
		self.network = self
		self.model_type = "ma"
		self.transition_labels = { 0: "τ", 1: "rs?", 2: "produce?", 3: "fail!", 4: "r1?", 5: "produce!", 6: "r2?", 7: "fail?", 8: "r1!", 9: "r2!", 10: "rs!", 11: "produce", 12: "fail", 13: "rs", 14: "r1", 15: "r2" }
		self.sync_vectors = [[0, -1, -1, -1, 0], [-1, 0, -1, -1, 0], [-1, -1, 0, -1, 0], [-1, -1, -1, 0, 0], [2, 5, -1, -1, 11], [2, -1, 5, -1, 11], [3, -1, -1, 7, 12], [-1, 3, -1, 7, 12], [-1, -1, 3, 7, 12], [1, -1, -1, 10, 13], [-1, 4, -1, 8, 14], [-1, -1, 6, 9, 15]]
		self.properties = [
			Property("Min", PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])])),
			Property("Max", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("buf", None, "int", 0, 8),
			VariableInfo("reset", None, "bool"),
			VariableInfo("BufferedServer_location", 0, "int", 0, 2),
			VariableInfo("on", 0, "bool"),
			VariableInfo("TypeOneSources_location", 1, "int", 0, 3),
			VariableInfo("on", 1, "int", 0, 5),
			VariableInfo("TypeTwoSources_location", 2, "int", 0, 3),
			VariableInfo("on", 2, "int", 0, 5),
			VariableInfo("Repair_location", 3, "int", 0, 6),
			VariableInfo("down", 3, "int", 0, 11)
		]
		self._aut_BufferedServer = BufferedServerAutomaton(self)
		self._aut_TypeOneSources = TypeOneSourcesAutomaton(self)
		self._aut_TypeTwoSources = TypeTwoSourcesAutomaton(self)
		self._aut_Repair = RepairAutomaton(self)
		self.components = [self._aut_BufferedServer, self._aut_TypeOneSources, self._aut_TypeTwoSources, self._aut_Repair]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.buf = 1
		state.reset = False
		self._aut_BufferedServer.set_initial_values(state)
		self._aut_TypeOneSources.set_initial_values(state)
		self._aut_TypeTwoSources.set_initial_values(state)
		self._aut_Repair.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_BufferedServer.set_initial_transient_values(transient)
		self._aut_TypeOneSources.set_initial_transient_values(transient)
		self._aut_TypeTwoSources.set_initial_transient_values(transient)
		self._aut_Repair.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return ((state.buf == 8) and (not state.reset))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return ((state.buf == 8) and (not state.reset))
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_BufferedServer.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_TypeOneSources.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_TypeTwoSources.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Repair.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_BufferedServer = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_BufferedServer.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_BufferedServer.get_guard_value(state, i):
				trans_BufferedServer[self._aut_BufferedServer.get_transition_label(state, i)].append(i)
		trans_TypeOneSources = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_TypeOneSources.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_TypeOneSources.get_guard_value(state, i):
				trans_TypeOneSources[self._aut_TypeOneSources.get_transition_label(state, i)].append(i)
		trans_TypeTwoSources = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_TypeTwoSources.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_TypeTwoSources.get_guard_value(state, i):
				trans_TypeTwoSources[self._aut_TypeTwoSources.get_transition_label(state, i)].append(i)
		trans_Repair = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Repair.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Repair.get_guard_value(state, i):
				trans_Repair[self._aut_Repair.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1]]
			# BufferedServer
			if synced is not None:
				if sv[0] != -1:
					if len(trans_BufferedServer[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_BufferedServer[sv[0]][0]
						for i in range(1, len(trans_BufferedServer[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_BufferedServer[sv[0]][i]
			# TypeOneSources
			if synced is not None:
				if sv[1] != -1:
					if len(trans_TypeOneSources[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_TypeOneSources[sv[1]][0]
						for i in range(1, len(trans_TypeOneSources[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_TypeOneSources[sv[1]][i]
			# TypeTwoSources
			if synced is not None:
				if sv[2] != -1:
					if len(trans_TypeTwoSources[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_TypeTwoSources[sv[2]][0]
						for i in range(1, len(trans_TypeTwoSources[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_TypeTwoSources[sv[2]][i]
			# Repair
			if synced is not None:
				if sv[3] != -1:
					if len(trans_Repair[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_Repair[sv[3]][0]
						for i in range(1, len(trans_Repair[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_Repair[sv[3]][i]
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
			branch_count = self._aut_BufferedServer.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_BufferedServer.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_BufferedServer.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_TypeOneSources.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_TypeOneSources.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_TypeOneSources.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_TypeTwoSources.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_TypeTwoSources.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_TypeTwoSources.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_Repair.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_Repair.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Repair.get_probability_value(state, transition.transitions[3], 0)
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
		for i in range(0, 2):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self._aut_BufferedServer.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_TypeOneSources.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_TypeTwoSources.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_Repair.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
