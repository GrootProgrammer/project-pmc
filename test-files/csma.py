# csma.2-2

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
	__slots__ = ("b", "y1", "y2", "s1", "x1", "bc1", "cd1", "s2", "x2", "bc2", "cd2")
	
	def udfs_global_min_backoff_after_success_state(self, min_backoff_after_success__param__s1, min_backoff_after_success__param__cd1, min_backoff_after_success__param__s2, min_backoff_after_success__param__cd2):
		return min((min_backoff_after_success__param__cd1 if (min_backoff_after_success__param__s1 == 4) else 3), (min_backoff_after_success__param__cd2 if (min_backoff_after_success__param__s2 == 4) else 3))
	
	def udfs_global_min_backoff_after_success_jump(self, transient, min_backoff_after_success__param__s1, min_backoff_after_success__param__cd1, min_backoff_after_success__param__s2, min_backoff_after_success__param__cd2):
		return min((min_backoff_after_success__param__cd1 if (min_backoff_after_success__param__s1 == 4) else 3), (min_backoff_after_success__param__cd2 if (min_backoff_after_success__param__s2 == 4) else 3))
	
	def udfs_global_min_collisions_state(self, min_collisions__param__cd1, min_collisions__param__cd2):
		return min(min_collisions__param__cd1, min_collisions__param__cd2)
	
	def udfs_global_min_collisions_jump(self, transient, min_collisions__param__cd1, min_collisions__param__cd2):
		return min(min_collisions__param__cd1, min_collisions__param__cd2)
	
	def udfs_global_max_collisions_state(self, max_collisions__param__cd1, max_collisions__param__cd2):
		return max(max_collisions__param__cd1, max_collisions__param__cd2)
	
	def udfs_global_max_collisions_jump(self, transient, max_collisions__param__cd1, max_collisions__param__cd2):
		return max(max_collisions__param__cd1, max_collisions__param__cd2)
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.b
		elif variable == 1:
			return self.y1
		elif variable == 2:
			return self.y2
		elif variable == 3:
			return self.s1
		elif variable == 4:
			return self.x1
		elif variable == 5:
			return self.bc1
		elif variable == 6:
			return self.cd1
		elif variable == 7:
			return self.s2
		elif variable == 8:
			return self.x2
		elif variable == 9:
			return self.bc2
		elif variable == 10:
			return self.cd2
	
	def copy_to(self, other: State):
		other.b = self.b
		other.y1 = self.y1
		other.y2 = self.y2
		other.s1 = self.s1
		other.x1 = self.x1
		other.bc1 = self.bc1
		other.cd1 = self.cd1
		other.s2 = self.s2
		other.x2 = self.x2
		other.bc2 = self.bc2
		other.cd2 = self.cd2
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.b == other.b and self.y1 == other.y1 and self.y2 == other.y2 and self.s1 == other.s1 and self.x1 == other.x1 and self.bc1 == other.bc1 and self.cd1 == other.cd1 and self.s2 == other.s2 and self.x2 == other.x2 and self.bc2 == other.bc2 and self.cd2 == other.cd2
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.y1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.y2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.s1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.bc1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cd1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.s2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.bc2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cd2)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "b = " + str(self.b)
		result += ", y1 = " + str(self.y1)
		result += ", y2 = " + str(self.y2)
		result += ", s1 = " + str(self.s1)
		result += ", x1 = " + str(self.x1)
		result += ", bc1 = " + str(self.bc1)
		result += ", cd1 = " + str(self.cd1)
		result += ", s2 = " + str(self.s2)
		result += ", x2 = " + str(self.x2)
		result += ", bc2 = " + str(self.bc2)
		result += ", cd2 = " + str(self.cd2)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("all_delivered", "one_delivered", "collision_max_backoff", "time")
	
	def copy_to(self, other: Transient):
		other.all_delivered = self.all_delivered
		other.one_delivered = self.one_delivered
		other.collision_max_backoff = self.collision_max_backoff
		other.time = self.time
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.all_delivered == other.all_delivered and self.one_delivered == other.one_delivered and self.collision_max_backoff == other.collision_max_backoff and self.time == other.time
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.all_delivered)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.one_delivered)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.collision_max_backoff)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.time)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "all_delivered = " + str(self.all_delivered)
		result += ", one_delivered = " + str(self.one_delivered)
		result += ", collision_max_backoff = " + str(self.collision_max_backoff)
		result += ", time = " + str(self.time)
		result += ")"
		return result

# Automaton: bus
class busAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [12]
		self.transition_labels = [[1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		pass
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = 0
		if location == 0:
			if transient_variable == "all_delivered":
				return ((state.s1 == 4) and (state.s2 == 4))
			elif transient_variable == "one_delivered":
				return ((state.s1 == 4) or (state.s2 == 4))
			elif transient_variable == "collision_max_backoff":
				return ((((state.cd1 == 2) and (state.s1 == 1)) and (state.b == 2)) or (((state.cd2 == 2) and (state.s2 == 1)) and (state.b == 2)))
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[0]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[0][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = 0
		if location == 0:
			if transition >= 0 and transition < 2:
				return (((state.b == 1) or (state.b == 2)) and (state.y1 >= 1))
			elif transition == 2:
				return ((state.b == 2) and (state.y2 <= 1))
			elif transition >= 3 and transition < 5:
				return (state.b == 1)
			elif transition == 5:
				return (((state.b == 1) or (state.b == 2)) and (state.y1 < 1))
			elif transition >= 6 and transition < 8:
				return (state.b == 0)
			elif transition == 8:
				return (((state.b == 1) or (state.b == 2)) and (state.y1 < 1))
			elif transition == 9:
				return (state.b == 0)
			elif transition == 10:
				return (state.b == 1)
			elif transition == 11:
				return ((state.b == 2) and (state.y2 < 1))
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
						pass
				elif transition == 2:
					if branch == 0:
						target_state.b = 0
						target_state.y1 = 0
						target_state.y2 = 0
				elif transition == 3:
					if branch == 0:
						target_state.b = 0
						target_state.y1 = 0
				elif transition == 4:
					if branch == 0:
						target_state.b = 0
						target_state.y1 = 0
				elif transition == 5:
					if branch == 0:
						target_state.b = 2
				elif transition == 6:
					if branch == 0:
						target_state.b = 1
				elif transition == 7:
					if branch == 0:
						target_state.b = 1
				elif transition == 8:
					if branch == 0:
						target_state.b = 2
				elif transition == 9:
					if branch == 0:
						target_state.y1 = 0
						target_transient.time = 1
				elif transition == 10:
					if branch == 0:
						target_state.y1 = min((state.y1 + 1), 2)
						target_transient.time = 1
				elif transition == 11:
					if branch == 0:
						target_state.y1 = min((state.y1 + 1), 2)
						target_state.y2 = min((state.y2 + 1), 2)
						target_transient.time = 1

# Automaton: station1
class station1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [11]
		self.transition_labels = [[0, 0, 1, 3, 3, 4, 6, 8, 8, 8, 8]]
		self.branch_counts = [[2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
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
				return ((state.s1 == 2) and (state.cd1 == 1))
			elif transition == 1:
				return ((state.s1 == 2) and (state.cd1 == 2))
			elif transition == 2:
				return ((state.s1 == 0) or (((state.s1 == 3) and (state.x1 == 2)) and (state.bc1 == 0)))
			elif transition == 3:
				return (state.s1 != 1)
			elif transition == 4:
				return (state.s1 == 1)
			elif transition == 5:
				return ((state.s1 == 1) and (state.x1 == 30))
			elif transition == 6:
				return ((((state.s1 == 3) and (state.x1 == 2)) and (state.bc1 == 0)) or (state.s1 == 0))
			elif transition == 7:
				return ((state.s1 == 1) and (state.x1 < 30))
			elif transition == 8:
				return ((state.s1 == 3) and (state.x1 < 2))
			elif transition == 9:
				return (((state.s1 == 3) and (state.x1 == 2)) and (state.bc1 > 0))
			elif transition == 10:
				return (state.s1 >= 4)
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
				if True:
					return (1 / 2)
			elif transition == 1:
				if True:
					return (1 / 4)
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
						target_state.s1 = 3
						target_state.bc1 = 0
					elif branch == 1:
						target_state.s1 = 3
						target_state.bc1 = 1
				elif transition == 1:
					if branch == 0:
						target_state.s1 = 3
						target_state.bc1 = 0
					elif branch == 1:
						target_state.s1 = 3
						target_state.bc1 = 1
					elif branch == 2:
						target_state.s1 = 3
						target_state.bc1 = 2
					elif branch == 3:
						target_state.s1 = 3
						target_state.bc1 = 3
				elif transition == 2:
					if branch == 0:
						target_state.s1 = 2
						target_state.x1 = 0
						target_state.cd1 = min(2, (state.cd1 + 1))
				elif transition == 3:
					if branch == 0:
						pass
				elif transition == 4:
					if branch == 0:
						target_state.s1 = 2
						target_state.x1 = 0
						target_state.cd1 = min(2, (state.cd1 + 1))
				elif transition == 5:
					if branch == 0:
						target_state.s1 = 4
						target_state.x1 = 0
				elif transition == 6:
					if branch == 0:
						target_state.s1 = 1
						target_state.x1 = 0
				elif transition == 7:
					if branch == 0:
						target_state.x1 = min((state.x1 + 1), 30)
				elif transition == 8:
					if branch == 0:
						target_state.x1 = (state.x1 + 1)
						if target_state.x1 > 30:
							raise OverflowError("Assigned value of " + str(target_state.x1) + " is greater than the upper bound of 30 for variable \"x1\".")
				elif transition == 9:
					if branch == 0:
						target_state.x1 = 1
						target_state.bc1 = (state.bc1 - 1)
						if target_state.bc1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.bc1) + " is less than the lower bound of 0 for variable \"bc1\".")
				elif transition == 10:
					if branch == 0:
						target_state.x1 = 0

# Automaton: station2
class station2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [11]
		self.transition_labels = [[0, 0, 2, 3, 3, 5, 7, 8, 8, 8, 8]]
		self.branch_counts = [[2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
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
				return ((state.s2 == 2) and (state.cd2 == 1))
			elif transition == 1:
				return ((state.s2 == 2) and (state.cd2 == 2))
			elif transition == 2:
				return ((state.s2 == 0) or (((state.s2 == 3) and (state.x2 == 2)) and (state.bc2 == 0)))
			elif transition == 3:
				return (state.s2 != 1)
			elif transition == 4:
				return (state.s2 == 1)
			elif transition == 5:
				return ((state.s2 == 1) and (state.x2 == 30))
			elif transition == 6:
				return ((((state.s2 == 3) and (state.x2 == 2)) and (state.bc2 == 0)) or (state.s2 == 0))
			elif transition == 7:
				return ((state.s2 == 1) and (state.x2 < 30))
			elif transition == 8:
				return ((state.s2 == 3) and (state.x2 < 2))
			elif transition == 9:
				return (((state.s2 == 3) and (state.x2 == 2)) and (state.bc2 > 0))
			elif transition == 10:
				return (state.s2 >= 4)
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
				if True:
					return (1 / 2)
			elif transition == 1:
				if True:
					return (1 / 4)
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
						target_state.s2 = 3
						target_state.bc2 = 0
					elif branch == 1:
						target_state.s2 = 3
						target_state.bc2 = 1
				elif transition == 1:
					if branch == 0:
						target_state.s2 = 3
						target_state.bc2 = 0
					elif branch == 1:
						target_state.s2 = 3
						target_state.bc2 = 1
					elif branch == 2:
						target_state.s2 = 3
						target_state.bc2 = 2
					elif branch == 3:
						target_state.s2 = 3
						target_state.bc2 = 3
				elif transition == 2:
					if branch == 0:
						target_state.s2 = 2
						target_state.x2 = 0
						target_state.cd2 = min(2, (state.cd2 + 1))
				elif transition == 3:
					if branch == 0:
						pass
				elif transition == 4:
					if branch == 0:
						target_state.s2 = 2
						target_state.x2 = 0
						target_state.cd2 = min(2, (state.cd2 + 1))
				elif transition == 5:
					if branch == 0:
						target_state.s2 = 4
						target_state.x2 = 0
				elif transition == 6:
					if branch == 0:
						target_state.s2 = 1
						target_state.x2 = 0
				elif transition == 7:
					if branch == 0:
						target_state.x2 = min((state.x2 + 1), 30)
				elif transition == 8:
					if branch == 0:
						target_state.x2 = (state.x2 + 1)
						if target_state.x2 > 30:
							raise OverflowError("Assigned value of " + str(target_state.x2) + " is greater than the upper bound of 30 for variable \"x2\".")
				elif transition == 9:
					if branch == 0:
						target_state.x2 = 1
						target_state.bc2 = (state.bc2 - 1)
						if target_state.bc2 < 0:
							raise OverflowError("Assigned value of " + str(target_state.bc2) + " is less than the lower bound of 0 for variable \"bc2\".")
				elif transition == 10:
					if branch == 0:
						target_state.x2 = 0

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_bus", "_aut_station1", "_aut_station2")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ", 1: "busy1", 2: "busy2", 3: "cd", 4: "end1", 5: "end2", 6: "send1", 7: "send2", 8: "time" }
		self.sync_vectors = [[0, -1, -1, 0], [-1, 0, -1, 0], [-1, -1, 0, 0], [1, 1, -1, 1], [2, -1, 2, 2], [3, 3, 3, 3], [4, 4, -1, 4], [5, -1, 5, 5], [6, 6, -1, 6], [7, -1, 7, 7], [8, 8, 8, 8]]
		self.properties = [
			Property("all_before_max", PropertyExpression("p_max", [PropertyExpression("until", [PropertyExpression("ap", [0]), PropertyExpression("ap", [1])])])),
			Property("all_before_min", PropertyExpression("p_min", [PropertyExpression("until", [PropertyExpression("ap", [0]), PropertyExpression("ap", [1])])])),
			Property("some_before", PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [2])])])),
			Property("time_max", PropertyExpression("e_max_s", [3, PropertyExpression("ap", [1])])),
			Property("time_min", PropertyExpression("e_min_s", [3, PropertyExpression("ap", [1])]))
		]
		self.variables = [
			VariableInfo("b", None, "int", 0, 2),
			VariableInfo("y1", None, "int", 0, 2),
			VariableInfo("y2", None, "int", 0, 2),
			VariableInfo("s1", None, "int", 0, 5),
			VariableInfo("x1", None, "int", 0, 30),
			VariableInfo("bc1", None, "int", 0, 3),
			VariableInfo("cd1", None, "int", 0, 2),
			VariableInfo("s2", None, "int", 0, 5),
			VariableInfo("x2", None, "int", 0, 30),
			VariableInfo("bc2", None, "int", 0, 3),
			VariableInfo("cd2", None, "int", 0, 2)
		]
		self._aut_bus = busAutomaton(self)
		self._aut_station1 = station1Automaton(self)
		self._aut_station2 = station2Automaton(self)
		self.components = [self._aut_bus, self._aut_station1, self._aut_station2]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.b = 0
		state.y1 = 0
		state.y2 = 0
		state.s1 = 0
		state.x1 = 0
		state.bc1 = 0
		state.cd1 = 0
		state.s2 = 0
		state.x2 = 0
		state.bc2 = 0
		state.cd2 = 0
		self._aut_bus.set_initial_values(state)
		self._aut_station1.set_initial_values(state)
		self._aut_station2.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.all_delivered = False
		transient.one_delivered = False
		transient.collision_max_backoff = False
		transient.time = 0
		self._aut_bus.set_initial_transient_values(transient)
		self._aut_station1.set_initial_transient_values(transient)
		self._aut_station2.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return (not self.network._get_transient_value(state, "collision_max_backoff"))
		elif expression == 1:
			return self.network._get_transient_value(state, "all_delivered")
		elif expression == 2:
			return (min((state.cd1 if (state.s1 == 4) else 3), (state.cd2 if (state.s2 == 4) else 3)) < 2)
		elif expression == 3:
			return self.network._get_transient_value(state, "time")
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return (not transient.collision_max_backoff)
		elif expression == 1:
			return transient.all_delivered
		elif expression == 2:
			return (min((state.cd1 if (state.s1 == 4) else 3), (state.cd2 if (state.s2 == 4) else 3)) < 2)
		elif expression == 3:
			return transient.time
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_bus.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_station1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_station2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_bus = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_bus.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_bus.get_guard_value(state, i):
				trans_bus[self._aut_bus.get_transition_label(state, i)].append(i)
		trans_station1 = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_station1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_station1.get_guard_value(state, i):
				trans_station1[self._aut_station1.get_transition_label(state, i)].append(i)
		trans_station2 = [[], [], [], [], [], [], [], [], []]
		transition_count = self._aut_station2.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_station2.get_guard_value(state, i):
				trans_station2[self._aut_station2.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1]]
			# bus
			if synced is not None:
				if sv[0] != -1:
					if len(trans_bus[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_bus[sv[0]][0]
						for i in range(1, len(trans_bus[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_bus[sv[0]][i]
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
			branch_count = self._aut_bus.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_bus.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_bus.get_probability_value(state, transition.transitions[0], 0)
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
				self._aut_bus.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_station1.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_station2.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
