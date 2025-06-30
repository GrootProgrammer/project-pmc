# rabin.3

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
	__slots__ = ("c", "b", "r", "p1", "b1", "r1", "draw1", "p2", "b2", "r2", "draw2", "p3", "b3", "r3", "draw3")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.c
		elif variable == 1:
			return self.b
		elif variable == 2:
			return self.r
		elif variable == 3:
			return self.p1
		elif variable == 4:
			return self.b1
		elif variable == 5:
			return self.r1
		elif variable == 6:
			return self.draw1
		elif variable == 7:
			return self.p2
		elif variable == 8:
			return self.b2
		elif variable == 9:
			return self.r2
		elif variable == 10:
			return self.draw2
		elif variable == 11:
			return self.p3
		elif variable == 12:
			return self.b3
		elif variable == 13:
			return self.r3
		elif variable == 14:
			return self.draw3
	
	def copy_to(self, other: State):
		other.c = self.c
		other.b = self.b
		other.r = self.r
		other.p1 = self.p1
		other.b1 = self.b1
		other.r1 = self.r1
		other.draw1 = self.draw1
		other.p2 = self.p2
		other.b2 = self.b2
		other.r2 = self.r2
		other.draw2 = self.draw2
		other.p3 = self.p3
		other.b3 = self.b3
		other.r3 = self.r3
		other.draw3 = self.draw3
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.c == other.c and self.b == other.b and self.r == other.r and self.p1 == other.p1 and self.b1 == other.b1 and self.r1 == other.r1 and self.draw1 == other.draw1 and self.p2 == other.p2 and self.b2 == other.b2 and self.r2 == other.r2 and self.draw2 == other.draw2 and self.p3 == other.p3 and self.b3 == other.b3 and self.r3 == other.r3 and self.draw3 == other.draw3
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.r)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.r1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.draw1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.r2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.draw2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.p3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.r3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.draw3)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "c = " + str(self.c)
		result += ", b = " + str(self.b)
		result += ", r = " + str(self.r)
		result += ", p1 = " + str(self.p1)
		result += ", b1 = " + str(self.b1)
		result += ", r1 = " + str(self.r1)
		result += ", draw1 = " + str(self.draw1)
		result += ", p2 = " + str(self.p2)
		result += ", b2 = " + str(self.b2)
		result += ", r2 = " + str(self.r2)
		result += ", draw2 = " + str(self.draw2)
		result += ", p3 = " + str(self.p3)
		result += ", b3 = " + str(self.b3)
		result += ", r3 = " + str(self.r3)
		result += ", draw3 = " + str(self.draw3)
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
		self.transition_counts = [5]
		self.transition_labels = [[0, 0, 0, 0, 0]]
		self.branch_counts = [[1, 1, 6, 2, 1]]
	
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
				return (((state.draw2 == 0) and (state.draw3 == 0)) and (state.p1 == 0))
			elif transition == 1:
				return ((((state.draw2 == 0) and (state.draw3 == 0)) and ((state.p1 == 1) and ((state.b < state.b1) or (state.r != state.r1)))) and (state.draw1 == 0))
			elif transition == 2:
				return (state.draw1 == 1)
			elif transition == 3:
				return ((((((state.draw2 == 0) and (state.draw3 == 0)) and (state.p1 == 1)) and (state.b == state.b1)) and (state.r == state.r1)) and (state.c == 0))
			elif transition == 4:
				return (((state.draw2 == 0) and (state.draw3 == 0)) and (state.p1 == 2))
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
				if branch == 0:
					return (5 / 10)
				elif branch == 1:
					return (25 / 100)
				elif branch == 2:
					return (125 / 1000)
				elif branch == 3:
					return (625 / 10000)
				elif branch >= 4:
					return (3125 / 100000)
			elif transition == 3:
				if True:
					return (5 / 10)
			elif transition == 4:
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
						target_state.p1 = 1
				elif transition == 1:
					if branch == 0:
						target_state.draw1 = 1
				elif transition == 2:
					if branch == 0:
						target_state.b = max(state.b, 1)
						target_state.b1 = 1
						target_state.r1 = state.r
						target_state.draw1 = 0
					elif branch == 1:
						target_state.b = max(state.b, 2)
						target_state.b1 = 2
						target_state.r1 = state.r
						target_state.draw1 = 0
					elif branch == 2:
						target_state.b = max(state.b, 3)
						target_state.b1 = 3
						target_state.r1 = state.r
						target_state.draw1 = 0
					elif branch == 3:
						target_state.b = max(state.b, 4)
						target_state.b1 = 4
						target_state.r1 = state.r
						target_state.draw1 = 0
					elif branch == 4:
						target_state.b = max(state.b, 5)
						target_state.b1 = 5
						target_state.r1 = state.r
						target_state.draw1 = 0
					elif branch == 5:
						target_state.b = max(state.b, 6)
						target_state.b1 = 6
						target_state.r1 = state.r
						target_state.draw1 = 0
				elif transition == 3:
					if branch == 0:
						target_state.c = 1
						target_state.b = 0
						target_state.r = 1
						target_state.p1 = 2
						target_state.b1 = 0
						target_state.r1 = 0
					elif branch == 1:
						target_state.c = 1
						target_state.b = 0
						target_state.r = 2
						target_state.p1 = 2
						target_state.b1 = 0
						target_state.r1 = 0
				elif transition == 4:
					if branch == 0:
						target_state.c = 0
						target_state.p1 = 0

# Automaton: process2
class process2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [5]
		self.transition_labels = [[0, 0, 0, 0, 0]]
		self.branch_counts = [[1, 1, 6, 2, 1]]
	
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
				return (((state.draw1 == 0) and (state.draw3 == 0)) and (state.p2 == 0))
			elif transition == 1:
				return ((((state.draw1 == 0) and (state.draw3 == 0)) and ((state.p2 == 1) and ((state.b < state.b2) or (state.r != state.r2)))) and (state.draw2 == 0))
			elif transition == 2:
				return (state.draw2 == 1)
			elif transition == 3:
				return ((((((state.draw1 == 0) and (state.draw3 == 0)) and (state.p2 == 1)) and (state.b == state.b2)) and (state.r == state.r2)) and (state.c == 0))
			elif transition == 4:
				return (((state.draw1 == 0) and (state.draw3 == 0)) and (state.p2 == 2))
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
				if branch == 0:
					return (5 / 10)
				elif branch == 1:
					return (25 / 100)
				elif branch == 2:
					return (125 / 1000)
				elif branch == 3:
					return (625 / 10000)
				elif branch >= 4:
					return (3125 / 100000)
			elif transition == 3:
				if True:
					return (5 / 10)
			elif transition == 4:
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
						target_state.p2 = 1
				elif transition == 1:
					if branch == 0:
						target_state.draw2 = 1
				elif transition == 2:
					if branch == 0:
						target_state.b = max(state.b, 1)
						target_state.b2 = 1
						target_state.r2 = state.r
						target_state.draw2 = 0
					elif branch == 1:
						target_state.b = max(state.b, 2)
						target_state.b2 = 2
						target_state.r2 = state.r
						target_state.draw2 = 0
					elif branch == 2:
						target_state.b = max(state.b, 3)
						target_state.b2 = 3
						target_state.r2 = state.r
						target_state.draw2 = 0
					elif branch == 3:
						target_state.b = max(state.b, 4)
						target_state.b2 = 4
						target_state.r2 = state.r
						target_state.draw2 = 0
					elif branch == 4:
						target_state.b = max(state.b, 5)
						target_state.b2 = 5
						target_state.r2 = state.r
						target_state.draw2 = 0
					elif branch == 5:
						target_state.b = max(state.b, 6)
						target_state.b2 = 6
						target_state.r2 = state.r
						target_state.draw2 = 0
				elif transition == 3:
					if branch == 0:
						target_state.c = 1
						target_state.b = 0
						target_state.r = 1
						target_state.p2 = 2
						target_state.b2 = 0
						target_state.r2 = 0
					elif branch == 1:
						target_state.c = 1
						target_state.b = 0
						target_state.r = 2
						target_state.p2 = 2
						target_state.b2 = 0
						target_state.r2 = 0
				elif transition == 4:
					if branch == 0:
						target_state.c = 0
						target_state.p2 = 0

# Automaton: process3
class process3Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [5]
		self.transition_labels = [[0, 0, 0, 0, 0]]
		self.branch_counts = [[1, 1, 6, 2, 1]]
	
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
				return (((state.draw2 == 0) and (state.draw1 == 0)) and (state.p3 == 0))
			elif transition == 1:
				return ((((state.draw2 == 0) and (state.draw1 == 0)) and ((state.p3 == 1) and ((state.b < state.b3) or (state.r != state.r3)))) and (state.draw3 == 0))
			elif transition == 2:
				return (state.draw3 == 1)
			elif transition == 3:
				return ((((((state.draw2 == 0) and (state.draw1 == 0)) and (state.p3 == 1)) and (state.b == state.b3)) and (state.r == state.r3)) and (state.c == 0))
			elif transition == 4:
				return (((state.draw2 == 0) and (state.draw1 == 0)) and (state.p3 == 2))
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
				if branch == 0:
					return (5 / 10)
				elif branch == 1:
					return (25 / 100)
				elif branch == 2:
					return (125 / 1000)
				elif branch == 3:
					return (625 / 10000)
				elif branch >= 4:
					return (3125 / 100000)
			elif transition == 3:
				if True:
					return (5 / 10)
			elif transition == 4:
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
						target_state.p3 = 1
				elif transition == 1:
					if branch == 0:
						target_state.draw3 = 1
				elif transition == 2:
					if branch == 0:
						target_state.b = max(state.b, 1)
						target_state.b3 = 1
						target_state.r3 = state.r
						target_state.draw3 = 0
					elif branch == 1:
						target_state.b = max(state.b, 2)
						target_state.b3 = 2
						target_state.r3 = state.r
						target_state.draw3 = 0
					elif branch == 2:
						target_state.b = max(state.b, 3)
						target_state.b3 = 3
						target_state.r3 = state.r
						target_state.draw3 = 0
					elif branch == 3:
						target_state.b = max(state.b, 4)
						target_state.b3 = 4
						target_state.r3 = state.r
						target_state.draw3 = 0
					elif branch == 4:
						target_state.b = max(state.b, 5)
						target_state.b3 = 5
						target_state.r3 = state.r
						target_state.draw3 = 0
					elif branch == 5:
						target_state.b = max(state.b, 6)
						target_state.b3 = 6
						target_state.r3 = state.r
						target_state.draw3 = 0
				elif transition == 3:
					if branch == 0:
						target_state.c = 1
						target_state.b = 0
						target_state.r = 1
						target_state.p3 = 2
						target_state.b3 = 0
						target_state.r3 = 0
					elif branch == 1:
						target_state.c = 1
						target_state.b = 0
						target_state.r = 2
						target_state.p3 = 2
						target_state.b3 = 0
						target_state.r3 = 0
				elif transition == 4:
					if branch == 0:
						target_state.c = 0
						target_state.p3 = 0

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_process1", "_aut_process2", "_aut_process3")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ" }
		self.sync_vectors = [[0, -1, -1, 0], [-1, 0, -1, 0], [-1, -1, 0, 0]]
		self.properties = [
			Property("live", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("c", None, "int", 0, 1),
			VariableInfo("b", None, "int", 0, 6),
			VariableInfo("r", None, "int", 1, 2),
			VariableInfo("p1", None, "int", 0, 2),
			VariableInfo("b1", None, "int", 0, 6),
			VariableInfo("r1", None, "int", 0, 2),
			VariableInfo("draw1", None, "int", 0, 1),
			VariableInfo("p2", None, "int", 0, 2),
			VariableInfo("b2", None, "int", 0, 6),
			VariableInfo("r2", None, "int", 0, 2),
			VariableInfo("draw2", None, "int", 0, 1),
			VariableInfo("p3", None, "int", 0, 2),
			VariableInfo("b3", None, "int", 0, 6),
			VariableInfo("r3", None, "int", 0, 2),
			VariableInfo("draw3", None, "int", 0, 1)
		]
		self._aut_process1 = process1Automaton(self)
		self._aut_process2 = process2Automaton(self)
		self._aut_process3 = process3Automaton(self)
		self.components = [self._aut_process1, self._aut_process2, self._aut_process3]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.c = 0
		state.b = 0
		state.r = 1
		state.p1 = 0
		state.b1 = 0
		state.r1 = 0
		state.draw1 = 0
		state.p2 = 0
		state.b2 = 0
		state.r2 = 0
		state.draw2 = 0
		state.p3 = 0
		state.b3 = 0
		state.r3 = 0
		state.draw3 = 0
		self._aut_process1.set_initial_values(state)
		self._aut_process2.set_initial_values(state)
		self._aut_process3.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_process1.set_initial_transient_values(transient)
		self._aut_process2.set_initial_transient_values(transient)
		self._aut_process3.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return (((state.p1 == 2) or (state.p2 == 2)) or (state.p3 == 2))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return (((state.p1 == 2) or (state.p2 == 2)) or (state.p3 == 2))
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
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1]]
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
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
