# zeroconf_dl

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
	__slots__ = ("b_ip7", "b_ip6", "b_ip5", "b_ip4", "b_ip3", "b_ip2", "b_ip1", "b_ip0", "n", "n0", "n1", "b", "z", "ip_mess", "x", "y", "coll", "probes", "mess", "defend", "ip", "l", "t", "host0_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.b_ip7
		elif variable == 1:
			return self.b_ip6
		elif variable == 2:
			return self.b_ip5
		elif variable == 3:
			return self.b_ip4
		elif variable == 4:
			return self.b_ip3
		elif variable == 5:
			return self.b_ip2
		elif variable == 6:
			return self.b_ip1
		elif variable == 7:
			return self.b_ip0
		elif variable == 8:
			return self.n
		elif variable == 9:
			return self.n0
		elif variable == 10:
			return self.n1
		elif variable == 11:
			return self.b
		elif variable == 12:
			return self.z
		elif variable == 13:
			return self.ip_mess
		elif variable == 14:
			return self.x
		elif variable == 15:
			return self.y
		elif variable == 16:
			return self.coll
		elif variable == 17:
			return self.probes
		elif variable == 18:
			return self.mess
		elif variable == 19:
			return self.defend
		elif variable == 20:
			return self.ip
		elif variable == 21:
			return self.l
		elif variable == 22:
			return self.t
		elif variable == 23:
			return self.host0_location
	
	def copy_to(self, other: State):
		other.b_ip7 = self.b_ip7
		other.b_ip6 = self.b_ip6
		other.b_ip5 = self.b_ip5
		other.b_ip4 = self.b_ip4
		other.b_ip3 = self.b_ip3
		other.b_ip2 = self.b_ip2
		other.b_ip1 = self.b_ip1
		other.b_ip0 = self.b_ip0
		other.n = self.n
		other.n0 = self.n0
		other.n1 = self.n1
		other.b = self.b
		other.z = self.z
		other.ip_mess = self.ip_mess
		other.x = self.x
		other.y = self.y
		other.coll = self.coll
		other.probes = self.probes
		other.mess = self.mess
		other.defend = self.defend
		other.ip = self.ip
		other.l = self.l
		other.t = self.t
		other.host0_location = self.host0_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.b_ip7 == other.b_ip7 and self.b_ip6 == other.b_ip6 and self.b_ip5 == other.b_ip5 and self.b_ip4 == other.b_ip4 and self.b_ip3 == other.b_ip3 and self.b_ip2 == other.b_ip2 and self.b_ip1 == other.b_ip1 and self.b_ip0 == other.b_ip0 and self.n == other.n and self.n0 == other.n0 and self.n1 == other.n1 and self.b == other.b and self.z == other.z and self.ip_mess == other.ip_mess and self.x == other.x and self.y == other.y and self.coll == other.coll and self.probes == other.probes and self.mess == other.mess and self.defend == other.defend and self.ip == other.ip and self.l == other.l and self.t == other.t and self.host0_location == other.host0_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b_ip7)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b_ip6)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b_ip5)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b_ip4)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b_ip3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b_ip2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b_ip1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b_ip0)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.n)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.n0)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.n1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.b)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.z)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ip_mess)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.y)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.coll)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.probes)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.mess)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.defend)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ip)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.l)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.t)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.host0_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "b_ip7 = " + str(self.b_ip7)
		result += ", b_ip6 = " + str(self.b_ip6)
		result += ", b_ip5 = " + str(self.b_ip5)
		result += ", b_ip4 = " + str(self.b_ip4)
		result += ", b_ip3 = " + str(self.b_ip3)
		result += ", b_ip2 = " + str(self.b_ip2)
		result += ", b_ip1 = " + str(self.b_ip1)
		result += ", b_ip0 = " + str(self.b_ip0)
		result += ", n = " + str(self.n)
		result += ", n0 = " + str(self.n0)
		result += ", n1 = " + str(self.n1)
		result += ", b = " + str(self.b)
		result += ", z = " + str(self.z)
		result += ", ip_mess = " + str(self.ip_mess)
		result += ", x = " + str(self.x)
		result += ", y = " + str(self.y)
		result += ", coll = " + str(self.coll)
		result += ", probes = " + str(self.probes)
		result += ", mess = " + str(self.mess)
		result += ", defend = " + str(self.defend)
		result += ", ip = " + str(self.ip)
		result += ", l = " + str(self.l)
		result += ", t = " + str(self.t)
		result += ", host0_location = " + str(self.host0_location)
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

# Automaton: environment
class environmentAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [19]
		self.transition_labels = [[0, 0, 0, 0, 0, 0, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5]]
		self.branch_counts = [[2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
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
				return (((state.l > 0) and (state.b == 0)) and (state.n > 0))
			elif transition == 1:
				return (((state.l > 0) and (state.b == 0)) and (state.n0 > 0))
			elif transition == 2:
				return (((state.l > 0) and (state.b == 0)) and (state.n1 > 0))
			elif transition == 3:
				return (((state.l > 0) and (state.b == 1)) and (state.ip_mess == 0))
			elif transition == 4:
				return (((state.l > 0) and (state.b == 1)) and (state.ip_mess == 1))
			elif transition == 5:
				return (((state.l > 0) and (state.b == 1)) and (state.ip_mess == 2))
			elif transition == 6:
				return ((state.l > 0) and (state.b == 2))
			elif transition == 7:
				return True
			elif transition == 8:
				return ((state.l > 0) and (state.n == 4))
			elif transition == 9:
				return ((state.l > 0) and (state.n == 2))
			elif transition == 10:
				return ((state.l > 0) and (state.n == 5))
			elif transition == 11:
				return ((state.l > 0) and (state.n == 6))
			elif transition == 12:
				return ((state.l > 0) and (state.n == 1))
			elif transition == 13:
				return ((state.l > 0) and (state.n == 7))
			elif transition == 14:
				return ((state.l > 0) and (state.n == 3))
			elif transition == 15:
				return ((state.l > 0) and (state.n == 8))
			elif transition == 16:
				return ((state.l > 0) and (state.n == 0))
			elif transition == 17:
				return (((state.l > 0) and (state.b > 0)) and (state.z < 1))
			elif transition == 18:
				return ((((state.n1 == 0) and (state.b == 0)) and (state.n == 0)) and ((state.n0 == 0) and (state.l > 0)))
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
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			elif transition == 1:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			elif transition == 2:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
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
						target_state.b_ip7 = 0
						target_state.b_ip6 = state.b_ip7
						target_state.b_ip5 = state.b_ip6
						target_state.b_ip4 = state.b_ip5
						target_state.b_ip3 = state.b_ip4
						target_state.b_ip2 = state.b_ip3
						target_state.b_ip1 = state.b_ip2
						target_state.b_ip0 = state.b_ip1
						target_state.n = (state.n - 1)
						if target_state.n < 0:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is less than the lower bound of 0 for variable \"n\".")
						target_state.b = 1
						target_state.ip_mess = state.b_ip0
					elif branch == 1:
						target_state.b_ip7 = 0
						target_state.b_ip6 = state.b_ip7
						target_state.b_ip5 = state.b_ip6
						target_state.b_ip4 = state.b_ip5
						target_state.b_ip3 = state.b_ip4
						target_state.b_ip2 = state.b_ip3
						target_state.b_ip1 = state.b_ip2
						target_state.b_ip0 = state.b_ip1
						target_state.n = (state.n - 1)
						if target_state.n < 0:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is less than the lower bound of 0 for variable \"n\".")
				elif transition == 1:
					if branch == 0:
						target_state.n0 = (state.n0 - 1)
						if target_state.n0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.n0) + " is less than the lower bound of 0 for variable \"n0\".")
						target_state.b = 2
						target_state.ip_mess = 0
					elif branch == 1:
						target_state.n0 = (state.n0 - 1)
						if target_state.n0 < 0:
							raise OverflowError("Assigned value of " + str(target_state.n0) + " is less than the lower bound of 0 for variable \"n0\".")
				elif transition == 2:
					if branch == 0:
						target_state.n1 = (state.n1 - 1)
						if target_state.n1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.n1) + " is less than the lower bound of 0 for variable \"n1\".")
						target_state.b = 2
						target_state.ip_mess = 1
					elif branch == 1:
						target_state.n1 = (state.n1 - 1)
						if target_state.n1 < 0:
							raise OverflowError("Assigned value of " + str(target_state.n1) + " is less than the lower bound of 0 for variable \"n1\".")
				elif transition == 3:
					if branch == 0:
						target_state.n0 = min((state.n0 + 1), 20)
						target_state.b = 0
						target_state.z = 0
						target_state.ip_mess = 0
				elif transition == 4:
					if branch == 0:
						target_state.n1 = min((state.n1 + 1), 8)
						target_state.b = 0
						target_state.z = 0
						target_state.ip_mess = 0
				elif transition == 5:
					if branch == 0:
						target_state.b = 0
						target_state.z = 0
						target_state.ip_mess = 0
				elif transition == 6:
					if branch == 0:
						target_state.b = 0
						target_state.z = 0
						target_state.ip_mess = 0
				elif transition == 7:
					if branch == 0:
						target_state.b_ip7 = 0
						target_state.b_ip6 = 0
						target_state.b_ip5 = 0
						target_state.b_ip4 = 0
						target_state.b_ip3 = 0
						target_state.b_ip2 = 0
						target_state.b_ip1 = 0
						target_state.b_ip0 = 0
						target_state.n = 0
						target_state.n0 = min(20, (state.n0 + state.n1))
						target_state.n1 = 0
						target_state.ip_mess = 0
				elif transition == 8:
					if branch == 0:
						target_state.b_ip4 = state.ip
						target_state.n = (state.n + 1)
						if target_state.n > 8:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is greater than the upper bound of 8 for variable \"n\".")
				elif transition == 9:
					if branch == 0:
						target_state.b_ip2 = state.ip
						target_state.n = (state.n + 1)
						if target_state.n > 8:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is greater than the upper bound of 8 for variable \"n\".")
				elif transition == 10:
					if branch == 0:
						target_state.b_ip5 = state.ip
						target_state.n = (state.n + 1)
						if target_state.n > 8:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is greater than the upper bound of 8 for variable \"n\".")
				elif transition == 11:
					if branch == 0:
						target_state.b_ip6 = state.ip
						target_state.n = (state.n + 1)
						if target_state.n > 8:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is greater than the upper bound of 8 for variable \"n\".")
				elif transition == 12:
					if branch == 0:
						target_state.b_ip1 = state.ip
						target_state.n = (state.n + 1)
						if target_state.n > 8:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is greater than the upper bound of 8 for variable \"n\".")
				elif transition == 13:
					if branch == 0:
						target_state.b_ip7 = state.ip
						target_state.n = (state.n + 1)
						if target_state.n > 8:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is greater than the upper bound of 8 for variable \"n\".")
				elif transition == 14:
					if branch == 0:
						target_state.b_ip3 = state.ip
						target_state.n = (state.n + 1)
						if target_state.n > 8:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is greater than the upper bound of 8 for variable \"n\".")
				elif transition == 15:
					if branch == 0:
						pass
				elif transition == 16:
					if branch == 0:
						target_state.b_ip0 = state.ip
						target_state.n = (state.n + 1)
						if target_state.n > 8:
							raise OverflowError("Assigned value of " + str(target_state.n) + " is greater than the upper bound of 8 for variable \"n\".")
				elif transition == 17:
					if branch == 0:
						target_state.z = min((state.z + 1), 1)
				elif transition == 18:
					if branch == 0:
						pass

# Automaton: host0
class host0Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1, 3, 5, 8, 1]
		self.transition_labels = [[3], [0, 2, 5], [0, 2, 2, 4, 5], [2, 2, 2, 4, 4, 4, 5, 5], [0]]
		self.branch_counts = [[1], [6, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.host0_location = 1
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.host0_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.host0_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.host0_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.host0_location
		if location == 0 or location == 4:
			return True
		elif location == 1:
			if transition == 0:
				return ((state.coll < 10) or ((state.coll == 10) and (state.x == 60)))
			elif transition == 1:
				return True
			elif transition == 2:
				return ((state.coll == 10) and (state.x < 60))
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return ((state.x == 2) and (state.probes == 1))
			elif transition == 1:
				return (state.ip_mess != state.ip)
			elif transition == 2:
				return (state.ip_mess == state.ip)
			elif transition == 3:
				return ((state.x == 2) and (state.probes < 1))
			elif transition == 4:
				return (state.x < 2)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return ((((state.defend == 0) or (state.y >= 10)) and (state.mess == 0)) and (state.ip_mess == state.ip))
			elif transition == 1:
				return ((((state.defend == 0) or (state.y < 10)) and (state.mess == 0)) and (state.ip_mess == state.ip))
			elif transition == 2:
				return ((state.mess == 0) and (state.ip_mess != state.ip))
			elif transition == 3:
				return (((state.probes < 1) and (state.mess == 0)) and (state.x == 2))
			elif transition == 4:
				return (((state.probes == 1) and (state.mess == 0)) and (state.x == 2))
			elif transition == 5:
				return (state.mess == 1)
			elif transition == 6:
				return (((state.x < 2) and (state.mess == 0)) and (state.defend == 0))
			elif transition == 7:
				return (((state.x < 2) and (state.mess == 0)) and (state.defend == 1))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.host0_location
		if location == 0 or location == 4:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.host0_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.host0_location
		if location == 0:
			if transition == 0:
				return 1
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				if branch < 3:
					return (125 / 24384)
				elif branch >= 3:
					return (8003 / 24384)
			elif transition == 1:
				return 1
			elif transition == 2:
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
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.host0_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.l = 1
						target_state.host0_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.x = 0
						target_state.ip = 1
						target_state.l = 2
						target_state.host0_location = 2
					elif branch == 1:
						target_state.x = 1
						target_state.ip = 1
						target_state.l = 2
						target_state.host0_location = 2
					elif branch == 2:
						target_state.x = 2
						target_state.ip = 1
						target_state.l = 2
						target_state.host0_location = 2
					elif branch == 3:
						target_state.x = 0
						target_state.ip = 2
						target_state.l = 2
						target_state.host0_location = 2
					elif branch == 4:
						target_state.x = 1
						target_state.ip = 2
						target_state.l = 2
						target_state.host0_location = 2
					elif branch == 5:
						target_state.x = 2
						target_state.ip = 2
						target_state.l = 2
						target_state.host0_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.host0_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.x = min((state.x + 1), 60)
						target_state.host0_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.x = 0
						target_state.coll = 0
						target_state.probes = 0
						target_state.l = 3
						target_state.host0_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.host0_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.x = 0
						target_state.coll = min((state.coll + 1), 10)
						target_state.probes = 0
						target_state.l = 0
						target_state.host0_location = 0
				elif transition == 3:
					if branch == 0:
						target_state.x = 0
						target_state.probes = (state.probes + 1)
						if target_state.probes > 1:
							raise OverflowError("Assigned value of " + str(target_state.probes) + " is greater than the upper bound of 1 for variable \"probes\".")
						target_state.host0_location = 2
				elif transition == 4:
					if branch == 0:
						target_state.x = min((state.x + 1), 2)
						target_state.host0_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.y = 0
						target_state.mess = 1
						target_state.defend = 1
						target_state.host0_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.x = 0
						target_state.y = 0
						target_state.probes = 0
						target_state.defend = 0
						target_state.l = 0
						target_state.host0_location = 0
				elif transition == 2:
					if branch == 0:
						target_state.host0_location = 3
				elif transition == 3:
					if branch == 0:
						target_state.x = 0
						target_state.probes = (state.probes + 1)
						if target_state.probes > 1:
							raise OverflowError("Assigned value of " + str(target_state.probes) + " is greater than the upper bound of 1 for variable \"probes\".")
						target_state.host0_location = 3
				elif transition == 4:
					if branch == 0:
						target_state.x = 0
						target_state.y = 0
						target_state.probes = 0
						target_state.l = 4
						target_state.host0_location = 4
				elif transition == 5:
					if branch == 0:
						target_state.mess = 0
						target_state.host0_location = 3
				elif transition == 6:
					if branch == 0:
						target_state.x = min((state.x + 1), 60)
						target_state.host0_location = 3
				elif transition == 7:
					if branch == 0:
						target_state.x = min((state.x + 1), 60)
						target_state.y = min((state.y + 1), 10)
						target_state.host0_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.host0_location = 4

# Automaton: timer
class timerAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[1, 5]]
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
				return (state.l == 4)
			elif transition == 1:
				return (state.t <= 10)
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
						target_state.t = 11
				elif transition == 1:
					if branch == 0:
						target_state.t = min((state.t + 1), 11)

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_environment", "_aut_host0", "_aut_timer")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ", 1: "done", 2: "rec", 3: "reset", 4: "send", 5: "time" }
		self.sync_vectors = [[0, -1, -1, 0], [-1, 0, -1, 0], [-1, -1, 0, 0], [-1, -1, 1, 1], [2, 2, -1, 2], [3, 3, -1, 3], [4, 4, -1, 4], [5, 5, 5, 5]]
		self.properties = [
			Property("deadline_max", PropertyExpression("p_max", [PropertyExpression("until", [PropertyExpression("ap", [0]), PropertyExpression("ap", [1])])])),
			Property("deadline_min", PropertyExpression("p_min", [PropertyExpression("until", [PropertyExpression("ap", [0]), PropertyExpression("ap", [1])])]))
		]
		self.variables = [
			VariableInfo("b_ip7", None, "int", 0, 2),
			VariableInfo("b_ip6", None, "int", 0, 2),
			VariableInfo("b_ip5", None, "int", 0, 2),
			VariableInfo("b_ip4", None, "int", 0, 2),
			VariableInfo("b_ip3", None, "int", 0, 2),
			VariableInfo("b_ip2", None, "int", 0, 2),
			VariableInfo("b_ip1", None, "int", 0, 2),
			VariableInfo("b_ip0", None, "int", 0, 2),
			VariableInfo("n", None, "int", 0, 8),
			VariableInfo("n0", None, "int", 0, 20),
			VariableInfo("n1", None, "int", 0, 8),
			VariableInfo("b", None, "int", 0, 2),
			VariableInfo("z", None, "int", 0, 1),
			VariableInfo("ip_mess", None, "int", 0, 2),
			VariableInfo("x", None, "int", 0, 60),
			VariableInfo("y", None, "int", 0, 10),
			VariableInfo("coll", None, "int", 0, 10),
			VariableInfo("probes", None, "int", 0, 1),
			VariableInfo("mess", None, "int", 0, 1),
			VariableInfo("defend", None, "int", 0, 1),
			VariableInfo("ip", None, "int", 1, 2),
			VariableInfo("l", None, "int", 0, 4),
			VariableInfo("t", None, "int", 0, 11),
			VariableInfo("host0_location", 1, "int", 0, 4)
		]
		self._aut_environment = environmentAutomaton(self)
		self._aut_host0 = host0Automaton(self)
		self._aut_timer = timerAutomaton(self)
		self.components = [self._aut_environment, self._aut_host0, self._aut_timer]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.b_ip7 = 0
		state.b_ip6 = 0
		state.b_ip5 = 0
		state.b_ip4 = 0
		state.b_ip3 = 0
		state.b_ip2 = 0
		state.b_ip1 = 0
		state.b_ip0 = 0
		state.n = 0
		state.n0 = 0
		state.n1 = 0
		state.b = 0
		state.z = 0
		state.ip_mess = 0
		state.x = 0
		state.y = 0
		state.coll = 0
		state.probes = 0
		state.mess = 0
		state.defend = 0
		state.ip = 1
		state.l = 1
		state.t = 0
		self._aut_environment.set_initial_values(state)
		self._aut_host0.set_initial_values(state)
		self._aut_timer.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_environment.set_initial_transient_values(transient)
		self._aut_host0.set_initial_transient_values(transient)
		self._aut_timer.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return (not ((state.l == 4) and (state.ip == 2)))
		elif expression == 1:
			return (state.t >= 10)
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return (not ((state.l == 4) and (state.ip == 2)))
		elif expression == 1:
			return (state.t >= 10)
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_environment.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_host0.get_transient_value(state, transient_variable)
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
		trans_environment = [[], [], [], [], [], []]
		transition_count = self._aut_environment.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_environment.get_guard_value(state, i):
				trans_environment[self._aut_environment.get_transition_label(state, i)].append(i)
		trans_host0 = [[], [], [], [], [], []]
		transition_count = self._aut_host0.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_host0.get_guard_value(state, i):
				trans_host0[self._aut_host0.get_transition_label(state, i)].append(i)
		trans_timer = [[], [], [], [], [], []]
		transition_count = self._aut_timer.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_timer.get_guard_value(state, i):
				trans_timer[self._aut_timer.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1]]
			# environment
			if synced is not None:
				if sv[0] != -1:
					if len(trans_environment[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_environment[sv[0]][0]
						for i in range(1, len(trans_environment[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_environment[sv[0]][i]
			# host0
			if synced is not None:
				if sv[1] != -1:
					if len(trans_host0[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_host0[sv[1]][0]
						for i in range(1, len(trans_host0[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_host0[sv[1]][i]
			# timer
			if synced is not None:
				if sv[2] != -1:
					if len(trans_timer[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_timer[sv[2]][0]
						for i in range(1, len(trans_timer[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_timer[sv[2]][i]
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
			branch_count = self._aut_environment.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_environment.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_environment.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_host0.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_host0.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_host0.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_timer.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_timer.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_timer.get_probability_value(state, transition.transitions[2], 0)
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
				self._aut_environment.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_host0.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_timer.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
