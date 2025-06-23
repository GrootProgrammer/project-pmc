# ij.10

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
	__slots__ = ("q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.q1
		elif variable == 1:
			return self.q2
		elif variable == 2:
			return self.q3
		elif variable == 3:
			return self.q4
		elif variable == 4:
			return self.q5
		elif variable == 5:
			return self.q6
		elif variable == 6:
			return self.q7
		elif variable == 7:
			return self.q8
		elif variable == 8:
			return self.q9
		elif variable == 9:
			return self.q10
	
	def copy_to(self, other: State):
		other.q1 = self.q1
		other.q2 = self.q2
		other.q3 = self.q3
		other.q4 = self.q4
		other.q5 = self.q5
		other.q6 = self.q6
		other.q7 = self.q7
		other.q8 = self.q8
		other.q9 = self.q9
		other.q10 = self.q10
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.q1 == other.q1 and self.q2 == other.q2 and self.q3 == other.q3 and self.q4 == other.q4 and self.q5 == other.q5 and self.q6 == other.q6 and self.q7 == other.q7 and self.q8 == other.q8 and self.q9 == other.q9 and self.q10 == other.q10
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q4)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q5)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q6)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q7)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q8)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q9)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.q10)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "q1 = " + str(self.q1)
		result += ", q2 = " + str(self.q2)
		result += ", q3 = " + str(self.q3)
		result += ", q4 = " + str(self.q4)
		result += ", q5 = " + str(self.q5)
		result += ", q6 = " + str(self.q6)
		result += ", q7 = " + str(self.q7)
		result += ", q8 = " + str(self.q8)
		result += ", q9 = " + str(self.q9)
		result += ", q10 = " + str(self.q10)
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

# Automaton: process1
class process1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q1 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q1 = 0
						target_state.q10 = 1
					elif branch == 1:
						target_state.q1 = 0
						target_state.q2 = 1

# Automaton: process2
class process2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q2 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q1 = 1
						target_state.q2 = 0
					elif branch == 1:
						target_state.q2 = 0
						target_state.q3 = 1

# Automaton: process3
class process3Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q3 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q2 = 1
						target_state.q3 = 0
					elif branch == 1:
						target_state.q3 = 0
						target_state.q4 = 1

# Automaton: process4
class process4Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q4 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q3 = 1
						target_state.q4 = 0
					elif branch == 1:
						target_state.q4 = 0
						target_state.q5 = 1

# Automaton: process5
class process5Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q5 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q4 = 1
						target_state.q5 = 0
					elif branch == 1:
						target_state.q5 = 0
						target_state.q6 = 1

# Automaton: process6
class process6Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q6 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q5 = 1
						target_state.q6 = 0
					elif branch == 1:
						target_state.q6 = 0
						target_state.q7 = 1

# Automaton: process7
class process7Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q7 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q6 = 1
						target_state.q7 = 0
					elif branch == 1:
						target_state.q7 = 0
						target_state.q8 = 1

# Automaton: process8
class process8Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q8 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q7 = 1
						target_state.q8 = 0
					elif branch == 1:
						target_state.q8 = 0
						target_state.q9 = 1

# Automaton: process9
class process9Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q9 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q8 = 1
						target_state.q9 = 0
					elif branch == 1:
						target_state.q9 = 0
						target_state.q10 = 1

# Automaton: process10
class process10Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[0]]
		self.branch_counts = [[2]]
	
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
			return (state.q10 == 1)
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
				if True:
					return (5 / 10)
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
						target_state.q9 = 1
						target_state.q10 = 0
					elif branch == 1:
						target_state.q1 = 1
						target_state.q10 = 0

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_process1", "_aut_process2", "_aut_process3", "_aut_process4", "_aut_process5", "_aut_process6", "_aut_process7", "_aut_process8", "_aut_process9", "_aut_process10")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ" }
		self.sync_vectors = [[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], [-1, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0], [-1, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0], [-1, -1, -1, 0, -1, -1, -1, -1, -1, -1, 0], [-1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], [-1, -1, -1, -1, -1, 0, -1, -1, -1, -1, 0], [-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0], [-1, -1, -1, -1, -1, -1, -1, 0, -1, -1, 0], [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0]]
		self.properties = [
			Property("stable", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("q1", None, "int", 0, 1),
			VariableInfo("q2", None, "int", 0, 1),
			VariableInfo("q3", None, "int", 0, 1),
			VariableInfo("q4", None, "int", 0, 1),
			VariableInfo("q5", None, "int", 0, 1),
			VariableInfo("q6", None, "int", 0, 1),
			VariableInfo("q7", None, "int", 0, 1),
			VariableInfo("q8", None, "int", 0, 1),
			VariableInfo("q9", None, "int", 0, 1),
			VariableInfo("q10", None, "int", 0, 1)
		]
		self._aut_process1 = process1Automaton(self)
		self._aut_process2 = process2Automaton(self)
		self._aut_process3 = process3Automaton(self)
		self._aut_process4 = process4Automaton(self)
		self._aut_process5 = process5Automaton(self)
		self._aut_process6 = process6Automaton(self)
		self._aut_process7 = process7Automaton(self)
		self._aut_process8 = process8Automaton(self)
		self._aut_process9 = process9Automaton(self)
		self._aut_process10 = process10Automaton(self)
		self.components = [self._aut_process1, self._aut_process2, self._aut_process3, self._aut_process4, self._aut_process5, self._aut_process6, self._aut_process7, self._aut_process8, self._aut_process9, self._aut_process10]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.q1 = 1
		state.q2 = 1
		state.q3 = 1
		state.q4 = 1
		state.q5 = 1
		state.q6 = 1
		state.q7 = 1
		state.q8 = 1
		state.q9 = 1
		state.q10 = 1
		self._aut_process1.set_initial_values(state)
		self._aut_process2.set_initial_values(state)
		self._aut_process3.set_initial_values(state)
		self._aut_process4.set_initial_values(state)
		self._aut_process5.set_initial_values(state)
		self._aut_process6.set_initial_values(state)
		self._aut_process7.set_initial_values(state)
		self._aut_process8.set_initial_values(state)
		self._aut_process9.set_initial_values(state)
		self._aut_process10.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_process1.set_initial_transient_values(transient)
		self._aut_process2.set_initial_transient_values(transient)
		self._aut_process3.set_initial_transient_values(transient)
		self._aut_process4.set_initial_transient_values(transient)
		self._aut_process5.set_initial_transient_values(transient)
		self._aut_process6.set_initial_transient_values(transient)
		self._aut_process7.set_initial_transient_values(transient)
		self._aut_process8.set_initial_transient_values(transient)
		self._aut_process9.set_initial_transient_values(transient)
		self._aut_process10.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return ((((((((((state.q1 + state.q2) + state.q3) + state.q4) + state.q5) + state.q6) + state.q7) + state.q8) + state.q9) + state.q10) == 1)
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return ((((((((((state.q1 + state.q2) + state.q3) + state.q4) + state.q5) + state.q6) + state.q7) + state.q8) + state.q9) + state.q10) == 1)
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_process1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process3.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process4.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process5.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process6.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process7.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process8.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process9.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_process10.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
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
		trans_process3 = [[]]
		transition_count = self._aut_process3.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process3.get_guard_value(state, i):
				trans_process3[self._aut_process3.get_transition_label(state, i)].append(i)
		trans_process4 = [[]]
		transition_count = self._aut_process4.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process4.get_guard_value(state, i):
				trans_process4[self._aut_process4.get_transition_label(state, i)].append(i)
		trans_process5 = [[]]
		transition_count = self._aut_process5.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process5.get_guard_value(state, i):
				trans_process5[self._aut_process5.get_transition_label(state, i)].append(i)
		trans_process6 = [[]]
		transition_count = self._aut_process6.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process6.get_guard_value(state, i):
				trans_process6[self._aut_process6.get_transition_label(state, i)].append(i)
		trans_process7 = [[]]
		transition_count = self._aut_process7.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process7.get_guard_value(state, i):
				trans_process7[self._aut_process7.get_transition_label(state, i)].append(i)
		trans_process8 = [[]]
		transition_count = self._aut_process8.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process8.get_guard_value(state, i):
				trans_process8[self._aut_process8.get_transition_label(state, i)].append(i)
		trans_process9 = [[]]
		transition_count = self._aut_process9.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process9.get_guard_value(state, i):
				trans_process9[self._aut_process9.get_transition_label(state, i)].append(i)
		trans_process10 = [[]]
		transition_count = self._aut_process10.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_process10.get_guard_value(state, i):
				trans_process10[self._aut_process10.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
			# process1
			if synced is not None:
				if sv[0] != -1:
					if len(trans_process1[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_process1[sv[0]][0]
						for i in range(1, len(trans_process1[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_process1[sv[0]][i]
			# process2
			if synced is not None:
				if sv[1] != -1:
					if len(trans_process2[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_process2[sv[1]][0]
						for i in range(1, len(trans_process2[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_process2[sv[1]][i]
			# process3
			if synced is not None:
				if sv[2] != -1:
					if len(trans_process3[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_process3[sv[2]][0]
						for i in range(1, len(trans_process3[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_process3[sv[2]][i]
			# process4
			if synced is not None:
				if sv[3] != -1:
					if len(trans_process4[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_process4[sv[3]][0]
						for i in range(1, len(trans_process4[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_process4[sv[3]][i]
			# process5
			if synced is not None:
				if sv[4] != -1:
					if len(trans_process5[sv[4]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][4] = trans_process5[sv[4]][0]
						for i in range(1, len(trans_process5[sv[4]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][4] = trans_process5[sv[4]][i]
			# process6
			if synced is not None:
				if sv[5] != -1:
					if len(trans_process6[sv[5]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][5] = trans_process6[sv[5]][0]
						for i in range(1, len(trans_process6[sv[5]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][5] = trans_process6[sv[5]][i]
			# process7
			if synced is not None:
				if sv[6] != -1:
					if len(trans_process7[sv[6]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][6] = trans_process7[sv[6]][0]
						for i in range(1, len(trans_process7[sv[6]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][6] = trans_process7[sv[6]][i]
			# process8
			if synced is not None:
				if sv[7] != -1:
					if len(trans_process8[sv[7]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][7] = trans_process8[sv[7]][0]
						for i in range(1, len(trans_process8[sv[7]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][7] = trans_process8[sv[7]][i]
			# process9
			if synced is not None:
				if sv[8] != -1:
					if len(trans_process9[sv[8]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][8] = trans_process9[sv[8]][0]
						for i in range(1, len(trans_process9[sv[8]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][8] = trans_process9[sv[8]][i]
			# process10
			if synced is not None:
				if sv[9] != -1:
					if len(trans_process10[sv[9]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][9] = trans_process10[sv[9]][0]
						for i in range(1, len(trans_process10[sv[9]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][9] = trans_process10[sv[9]][i]
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
		combs = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_process1.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_process1.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process1.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_process2.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_process2.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process2.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_process3.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_process3.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process3.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_process4.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_process4.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process4.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		if transition.transitions[4] != -1:
			existing = len(combs)
			branch_count = self._aut_process5.get_branch_count(state, transition.transitions[4])
			for i in range(1, branch_count):
				probability = self._aut_process5.get_probability_value(state, transition.transitions[4], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][4] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process5.get_probability_value(state, transition.transitions[4], 0)
			for i in range(existing):
				combs[i][4] = 0
				probs[i] *= probability
		if transition.transitions[5] != -1:
			existing = len(combs)
			branch_count = self._aut_process6.get_branch_count(state, transition.transitions[5])
			for i in range(1, branch_count):
				probability = self._aut_process6.get_probability_value(state, transition.transitions[5], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][5] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process6.get_probability_value(state, transition.transitions[5], 0)
			for i in range(existing):
				combs[i][5] = 0
				probs[i] *= probability
		if transition.transitions[6] != -1:
			existing = len(combs)
			branch_count = self._aut_process7.get_branch_count(state, transition.transitions[6])
			for i in range(1, branch_count):
				probability = self._aut_process7.get_probability_value(state, transition.transitions[6], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][6] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process7.get_probability_value(state, transition.transitions[6], 0)
			for i in range(existing):
				combs[i][6] = 0
				probs[i] *= probability
		if transition.transitions[7] != -1:
			existing = len(combs)
			branch_count = self._aut_process8.get_branch_count(state, transition.transitions[7])
			for i in range(1, branch_count):
				probability = self._aut_process8.get_probability_value(state, transition.transitions[7], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][7] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process8.get_probability_value(state, transition.transitions[7], 0)
			for i in range(existing):
				combs[i][7] = 0
				probs[i] *= probability
		if transition.transitions[8] != -1:
			existing = len(combs)
			branch_count = self._aut_process9.get_branch_count(state, transition.transitions[8])
			for i in range(1, branch_count):
				probability = self._aut_process9.get_probability_value(state, transition.transitions[8], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][8] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process9.get_probability_value(state, transition.transitions[8], 0)
			for i in range(existing):
				combs[i][8] = 0
				probs[i] *= probability
		if transition.transitions[9] != -1:
			existing = len(combs)
			branch_count = self._aut_process10.get_branch_count(state, transition.transitions[9])
			for i in range(1, branch_count):
				probability = self._aut_process10.get_probability_value(state, transition.transitions[9], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][9] = i
					probs.append(probs[j] * probability)
			probability = self._aut_process10.get_probability_value(state, transition.transitions[9], 0)
			for i in range(existing):
				combs[i][9] = 0
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
				self._aut_process1.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_process2.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_process3.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_process4.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			if transition.transitions[4] != -1:
				self._aut_process5.jump(state, transient, transition.transitions[4], branch.branches[4], i, target_state, target_transient)
			if transition.transitions[5] != -1:
				self._aut_process6.jump(state, transient, transition.transitions[5], branch.branches[5], i, target_state, target_transient)
			if transition.transitions[6] != -1:
				self._aut_process7.jump(state, transient, transition.transitions[6], branch.branches[6], i, target_state, target_transient)
			if transition.transitions[7] != -1:
				self._aut_process8.jump(state, transient, transition.transitions[7], branch.branches[7], i, target_state, target_transient)
			if transition.transitions[8] != -1:
				self._aut_process9.jump(state, transient, transition.transitions[8], branch.branches[8], i, target_state, target_transient)
			if transition.transitions[9] != -1:
				self._aut_process10.jump(state, transient, transition.transitions[9], branch.branches[9], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
