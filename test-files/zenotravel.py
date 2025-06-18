# jani_from_ppddl

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
	__slots__ = ("var0", "var1", "var2", "var3", "var4", "var5", "var6", "var7")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.var0
		elif variable == 1:
			return self.var1
		elif variable == 2:
			return self.var2
		elif variable == 3:
			return self.var3
		elif variable == 4:
			return self.var4
		elif variable == 5:
			return self.var5
		elif variable == 6:
			return self.var6
		elif variable == 7:
			return self.var7
	
	def copy_to(self, other: State):
		other.var0 = self.var0
		other.var1 = self.var1
		other.var2 = self.var2
		other.var3 = self.var3
		other.var4 = self.var4
		other.var5 = self.var5
		other.var6 = self.var6
		other.var7 = self.var7
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.var0 == other.var0 and self.var1 == other.var1 and self.var2 == other.var2 and self.var3 == other.var3 and self.var4 == other.var4 and self.var5 == other.var5 and self.var6 == other.var6 and self.var7 == other.var7
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var0)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var4)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var5)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var6)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var7)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "var0 = " + str(self.var0)
		result += ", var1 = " + str(self.var1)
		result += ", var2 = " + str(self.var2)
		result += ", var3 = " + str(self.var3)
		result += ", var4 = " + str(self.var4)
		result += ", var5 = " + str(self.var5)
		result += ", var6 = " + str(self.var6)
		result += ", var7 = " + str(self.var7)
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

# Automaton: main
class mainAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [110]
		self.transition_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		self.branch_counts = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
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
				return (((((state.var7 == 4) and (state.var5 == 0)) or ((state.var7 == 4) and (state.var5 == 1))) or ((state.var7 == 4) and (state.var5 == 2))) or ((state.var7 == 4) and (state.var5 == 3)))
			elif transition == 1:
				return (((((state.var7 == 5) and (state.var2 == 0)) or ((state.var7 == 5) and (state.var2 == 1))) or ((state.var7 == 5) and (state.var2 == 2))) or ((state.var7 == 5) and (state.var2 == 3)))
			elif transition == 2:
				return (((((state.var6 == 4) and (state.var5 == 0)) or ((state.var6 == 4) and (state.var5 == 1))) or ((state.var6 == 4) and (state.var5 == 2))) or ((state.var6 == 4) and (state.var5 == 3)))
			elif transition == 3:
				return (((((state.var6 == 5) and (state.var2 == 0)) or ((state.var6 == 5) and (state.var2 == 1))) or ((state.var6 == 5) and (state.var2 == 2))) or ((state.var6 == 5) and (state.var2 == 3)))
			elif transition == 4:
				return (((state.var7 == 6) and (state.var5 == 0)) or ((state.var7 == 7) and (state.var2 == 0)))
			elif transition == 5:
				return (((state.var7 == 6) and (state.var5 == 1)) or ((state.var7 == 7) and (state.var2 == 1)))
			elif transition == 6:
				return (((state.var7 == 6) and (state.var5 == 2)) or ((state.var7 == 7) and (state.var2 == 2)))
			elif transition == 7:
				return (((state.var7 == 6) and (state.var5 == 3)) or ((state.var7 == 7) and (state.var2 == 3)))
			elif transition == 8:
				return (((state.var6 == 6) and (state.var5 == 0)) or ((state.var6 == 7) and (state.var2 == 0)))
			elif transition == 9:
				return (((state.var6 == 6) and (state.var5 == 1)) or ((state.var6 == 7) and (state.var2 == 1)))
			elif transition == 10:
				return (((state.var6 == 6) and (state.var5 == 2)) or ((state.var6 == 7) and (state.var2 == 2)))
			elif transition == 11:
				return (((state.var6 == 6) and (state.var5 == 3)) or ((state.var6 == 7) and (state.var2 == 3)))
			elif transition == 12:
				return ((state.var5 == 4) and (state.var3 == 1))
			elif transition == 13:
				return ((state.var5 == 4) and (state.var3 == 2))
			elif transition == 14:
				return ((state.var5 == 4) and (state.var3 == 3))
			elif transition == 15:
				return ((state.var5 == 4) and (state.var3 == 4))
			elif transition == 16:
				return ((state.var5 == 5) and (state.var3 == 1))
			elif transition == 17:
				return ((state.var5 == 5) and (state.var3 == 2))
			elif transition == 18:
				return ((state.var5 == 5) and (state.var3 == 3))
			elif transition == 19:
				return ((state.var5 == 5) and (state.var3 == 4))
			elif transition == 20:
				return ((state.var5 == 6) and (state.var3 == 1))
			elif transition == 21:
				return ((state.var5 == 6) and (state.var3 == 2))
			elif transition == 22:
				return ((state.var5 == 6) and (state.var3 == 3))
			elif transition == 23:
				return ((state.var5 == 6) and (state.var3 == 4))
			elif transition == 24:
				return ((state.var5 == 7) and (state.var3 == 1))
			elif transition == 25:
				return ((state.var5 == 7) and (state.var3 == 2))
			elif transition == 26:
				return ((state.var5 == 7) and (state.var3 == 3))
			elif transition == 27:
				return ((state.var5 == 7) and (state.var3 == 4))
			elif transition == 28:
				return ((state.var2 == 4) and (state.var0 == 1))
			elif transition == 29:
				return ((state.var2 == 4) and (state.var0 == 2))
			elif transition == 30:
				return ((state.var2 == 4) and (state.var0 == 3))
			elif transition == 31:
				return ((state.var2 == 4) and (state.var0 == 4))
			elif transition == 32:
				return ((state.var2 == 5) and (state.var0 == 1))
			elif transition == 33:
				return ((state.var2 == 5) and (state.var0 == 2))
			elif transition == 34:
				return ((state.var2 == 5) and (state.var0 == 3))
			elif transition == 35:
				return ((state.var2 == 5) and (state.var0 == 4))
			elif transition == 36:
				return ((state.var2 == 6) and (state.var0 == 1))
			elif transition == 37:
				return ((state.var2 == 6) and (state.var0 == 2))
			elif transition == 38:
				return ((state.var2 == 6) and (state.var0 == 3))
			elif transition == 39:
				return ((state.var2 == 6) and (state.var0 == 4))
			elif transition == 40:
				return ((state.var2 == 7) and (state.var0 == 1))
			elif transition == 41:
				return ((state.var2 == 7) and (state.var0 == 2))
			elif transition == 42:
				return ((state.var2 == 7) and (state.var0 == 3))
			elif transition == 43:
				return ((state.var2 == 7) and (state.var0 == 4))
			elif transition == 44:
				return ((state.var4 == 1) and (state.var3 == 0))
			elif transition == 45:
				return ((state.var4 == 1) and (state.var3 == 1))
			elif transition == 46:
				return ((state.var4 == 1) and (state.var3 == 2))
			elif transition == 47:
				return ((state.var4 == 1) and (state.var3 == 3))
			elif transition == 48:
				return ((state.var1 == 1) and (state.var0 == 0))
			elif transition == 49:
				return ((state.var1 == 1) and (state.var0 == 1))
			elif transition == 50:
				return ((state.var1 == 1) and (state.var0 == 2))
			elif transition == 51:
				return ((state.var1 == 1) and (state.var0 == 3))
			elif transition == 52:
				return ((state.var5 == 8) and (state.var3 == 1))
			elif transition == 53:
				return ((state.var5 == 8) and (state.var3 == 2))
			elif transition == 54:
				return ((state.var5 == 8) and (state.var3 == 3))
			elif transition == 55:
				return ((state.var5 == 8) and (state.var3 == 4))
			elif transition == 56:
				return ((state.var5 == 9) and (state.var3 == 1))
			elif transition == 57:
				return ((state.var5 == 9) and (state.var3 == 2))
			elif transition == 58:
				return ((state.var5 == 9) and (state.var3 == 3))
			elif transition == 59:
				return ((state.var5 == 9) and (state.var3 == 4))
			elif transition == 60:
				return ((state.var5 == 10) and (state.var3 == 1))
			elif transition == 61:
				return ((state.var5 == 10) and (state.var3 == 2))
			elif transition == 62:
				return ((state.var5 == 10) and (state.var3 == 3))
			elif transition == 63:
				return ((state.var5 == 10) and (state.var3 == 4))
			elif transition == 64:
				return ((state.var5 == 11) and (state.var3 == 1))
			elif transition == 65:
				return ((state.var5 == 11) and (state.var3 == 2))
			elif transition == 66:
				return ((state.var5 == 11) and (state.var3 == 3))
			elif transition == 67:
				return ((state.var5 == 11) and (state.var3 == 4))
			elif transition == 68:
				return ((state.var2 == 8) and (state.var0 == 1))
			elif transition == 69:
				return ((state.var2 == 8) and (state.var0 == 2))
			elif transition == 70:
				return ((state.var2 == 8) and (state.var0 == 3))
			elif transition == 71:
				return ((state.var2 == 8) and (state.var0 == 4))
			elif transition == 72:
				return ((state.var2 == 9) and (state.var0 == 1))
			elif transition == 73:
				return ((state.var2 == 9) and (state.var0 == 2))
			elif transition == 74:
				return ((state.var2 == 9) and (state.var0 == 3))
			elif transition == 75:
				return ((state.var2 == 9) and (state.var0 == 4))
			elif transition == 76:
				return ((state.var2 == 10) and (state.var0 == 1))
			elif transition == 77:
				return ((state.var2 == 10) and (state.var0 == 2))
			elif transition == 78:
				return ((state.var2 == 10) and (state.var0 == 3))
			elif transition == 79:
				return ((state.var2 == 10) and (state.var0 == 4))
			elif transition == 80:
				return ((state.var2 == 11) and (state.var0 == 1))
			elif transition == 81:
				return ((state.var2 == 11) and (state.var0 == 2))
			elif transition == 82:
				return ((state.var2 == 11) and (state.var0 == 3))
			elif transition == 83:
				return ((state.var2 == 11) and (state.var0 == 4))
			elif transition == 84:
				return (((((state.var7 == 0) and (state.var5 == 0)) or ((state.var7 == 1) and (state.var5 == 1))) or ((state.var7 == 2) and (state.var5 == 2))) or ((state.var7 == 3) and (state.var5 == 3)))
			elif transition == 85:
				return (((((state.var7 == 0) and (state.var2 == 0)) or ((state.var7 == 1) and (state.var2 == 1))) or ((state.var7 == 2) and (state.var2 == 2))) or ((state.var7 == 3) and (state.var2 == 3)))
			elif transition == 86:
				return (((((state.var6 == 0) and (state.var5 == 0)) or ((state.var6 == 1) and (state.var5 == 1))) or ((state.var6 == 2) and (state.var5 == 2))) or ((state.var6 == 3) and (state.var5 == 3)))
			elif transition == 87:
				return (((((state.var6 == 0) and (state.var2 == 0)) or ((state.var6 == 1) and (state.var2 == 1))) or ((state.var6 == 2) and (state.var2 == 2))) or ((state.var6 == 3) and (state.var2 == 3)))
			elif transition == 88:
				return (((((state.var7 == 8) and (state.var5 == 0)) or ((state.var7 == 8) and (state.var5 == 1))) or ((state.var7 == 8) and (state.var5 == 2))) or ((state.var7 == 8) and (state.var5 == 3)))
			elif transition == 89:
				return (((((state.var7 == 9) and (state.var2 == 0)) or ((state.var7 == 9) and (state.var2 == 1))) or ((state.var7 == 9) and (state.var2 == 2))) or ((state.var7 == 9) and (state.var2 == 3)))
			elif transition == 90:
				return (((((state.var6 == 8) and (state.var5 == 0)) or ((state.var6 == 8) and (state.var5 == 1))) or ((state.var6 == 8) and (state.var5 == 2))) or ((state.var6 == 8) and (state.var5 == 3)))
			elif transition == 91:
				return (((((state.var6 == 9) and (state.var2 == 0)) or ((state.var6 == 9) and (state.var2 == 1))) or ((state.var6 == 9) and (state.var2 == 2))) or ((state.var6 == 9) and (state.var2 == 3)))
			elif transition >= 92 and transition < 96:
				return ((((((((((((((((((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 1)) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 4))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 4))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 4))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 4)))
			elif transition >= 96 and transition < 100:
				return ((((((((((((((((((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 1)) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 4))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 4))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 4))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 4)))
			elif transition == 100:
				return ((((((((((((((((((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 0)) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 0))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 0))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 0))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 3)))
			elif transition == 101:
				return ((((((((((((((((((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 0)) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 0))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 0))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 0))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 3)))
			elif transition >= 102 and transition < 106:
				return ((((((((((((((((((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 1)) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 0) and (state.var4 == 0)) and (state.var3 == 4))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 1) and (state.var4 == 0)) and (state.var3 == 4))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 2) and (state.var4 == 0)) and (state.var3 == 4))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 1))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 2))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 3))) or (((state.var5 == 3) and (state.var4 == 0)) and (state.var3 == 4)))
			elif transition >= 106:
				return ((((((((((((((((((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 1)) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 0) and (state.var1 == 0)) and (state.var0 == 4))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 1) and (state.var1 == 0)) and (state.var0 == 4))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 2) and (state.var1 == 0)) and (state.var0 == 4))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 1))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 2))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 3))) or (((state.var2 == 3) and (state.var1 == 0)) and (state.var0 == 4)))
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
					return (5 / 10)
			elif transition == 1:
				if True:
					return (5 / 10)
			elif transition == 2:
				if True:
					return (5 / 10)
			elif transition == 3:
				if True:
					return (5 / 10)
			elif transition == 4:
				if branch == 0:
					return (25 / 100)
				elif branch == 1:
					return (75 / 100)
			elif transition == 5:
				if branch == 0:
					return (25 / 100)
				elif branch == 1:
					return (75 / 100)
			elif transition == 6:
				if branch == 0:
					return (25 / 100)
				elif branch == 1:
					return (75 / 100)
			elif transition == 7:
				if branch == 0:
					return (25 / 100)
				elif branch == 1:
					return (75 / 100)
			elif transition == 8:
				if branch == 0:
					return (25 / 100)
				elif branch == 1:
					return (75 / 100)
			elif transition == 9:
				if branch == 0:
					return (25 / 100)
				elif branch == 1:
					return (75 / 100)
			elif transition == 10:
				if branch == 0:
					return (25 / 100)
				elif branch == 1:
					return (75 / 100)
			elif transition == 11:
				if branch == 0:
					return (25 / 100)
				elif branch == 1:
					return (75 / 100)
			elif transition == 12:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 13:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 14:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 15:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 16:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 17:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 18:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 19:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 20:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 21:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 22:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 23:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 24:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 25:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 26:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 27:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 28:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 29:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 30:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 31:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 32:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 33:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 34:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 35:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 36:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 37:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 38:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 39:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 40:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 41:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 42:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 43:
				if branch == 0:
					return (4 / 100)
				elif branch == 1:
					return (96 / 100)
			elif transition == 44:
				if branch == 0:
					return (14286 / 100000)
				elif branch == 1:
					return (85714 / 100000)
			elif transition == 45:
				if branch == 0:
					return (14286 / 100000)
				elif branch == 1:
					return (85714 / 100000)
			elif transition == 46:
				if branch == 0:
					return (14286 / 100000)
				elif branch == 1:
					return (85714 / 100000)
			elif transition == 47:
				if branch == 0:
					return (14286 / 100000)
				elif branch == 1:
					return (85714 / 100000)
			elif transition == 48:
				if branch == 0:
					return (14286 / 100000)
				elif branch == 1:
					return (85714 / 100000)
			elif transition == 49:
				if branch == 0:
					return (14286 / 100000)
				elif branch == 1:
					return (85714 / 100000)
			elif transition == 50:
				if branch == 0:
					return (14286 / 100000)
				elif branch == 1:
					return (85714 / 100000)
			elif transition == 51:
				if branch == 0:
					return (14286 / 100000)
				elif branch == 1:
					return (85714 / 100000)
			elif transition == 52:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 53:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 54:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 55:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 56:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 57:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 58:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 59:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 60:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 61:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 62:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 63:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 64:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 65:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 66:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 67:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 68:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 69:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 70:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 71:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 72:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 73:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 74:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 75:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 76:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 77:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 78:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 79:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 80:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 81:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 82:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 83:
				if branch == 0:
					return (666667 / 10000000)
				elif branch == 1:
					return (9333333 / 10000000)
			elif transition == 84:
				return 1
			elif transition == 85:
				return 1
			elif transition == 86:
				return 1
			elif transition == 87:
				return 1
			elif transition == 88:
				return 1
			elif transition == 89:
				return 1
			elif transition == 90:
				return 1
			elif transition == 91:
				return 1
			elif transition == 92:
				return 1
			elif transition == 93:
				return 1
			elif transition == 94:
				return 1
			elif transition == 95:
				return 1
			elif transition == 96:
				return 1
			elif transition == 97:
				return 1
			elif transition == 98:
				return 1
			elif transition == 99:
				return 1
			elif transition == 100:
				return 1
			elif transition == 101:
				return 1
			elif transition == 102:
				return 1
			elif transition == 103:
				return 1
			elif transition == 104:
				return 1
			elif transition == 105:
				return 1
			elif transition == 106:
				return 1
			elif transition == 107:
				return 1
			elif transition == 108:
				return 1
			elif transition == 109:
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
						target_state.var7 = 8
					elif branch == 1:
						pass
				elif transition == 1:
					if branch == 0:
						target_state.var7 = 9
					elif branch == 1:
						pass
				elif transition == 2:
					if branch == 0:
						target_state.var6 = 8
					elif branch == 1:
						pass
				elif transition == 3:
					if branch == 0:
						target_state.var6 = 9
					elif branch == 1:
						pass
				elif transition == 4:
					if branch == 0:
						target_state.var7 = 0
					elif branch == 1:
						pass
				elif transition == 5:
					if branch == 0:
						target_state.var7 = 1
					elif branch == 1:
						pass
				elif transition == 6:
					if branch == 0:
						target_state.var7 = 2
					elif branch == 1:
						pass
				elif transition == 7:
					if branch == 0:
						target_state.var7 = 3
					elif branch == 1:
						pass
				elif transition == 8:
					if branch == 0:
						target_state.var6 = 0
					elif branch == 1:
						pass
				elif transition == 9:
					if branch == 0:
						target_state.var6 = 1
					elif branch == 1:
						pass
				elif transition == 10:
					if branch == 0:
						target_state.var6 = 2
					elif branch == 1:
						pass
				elif transition == 11:
					if branch == 0:
						target_state.var6 = 3
					elif branch == 1:
						pass
				elif transition == 12:
					if branch == 0:
						target_state.var3 = 0
						target_state.var5 = 0
					elif branch == 1:
						pass
				elif transition == 13:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 0
					elif branch == 1:
						pass
				elif transition == 14:
					if branch == 0:
						target_state.var3 = 2
						target_state.var5 = 0
					elif branch == 1:
						pass
				elif transition == 15:
					if branch == 0:
						target_state.var3 = 3
						target_state.var5 = 0
					elif branch == 1:
						pass
				elif transition == 16:
					if branch == 0:
						target_state.var3 = 0
						target_state.var5 = 1
					elif branch == 1:
						pass
				elif transition == 17:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 1
					elif branch == 1:
						pass
				elif transition == 18:
					if branch == 0:
						target_state.var3 = 2
						target_state.var5 = 1
					elif branch == 1:
						pass
				elif transition == 19:
					if branch == 0:
						target_state.var3 = 3
						target_state.var5 = 1
					elif branch == 1:
						pass
				elif transition == 20:
					if branch == 0:
						target_state.var3 = 0
						target_state.var5 = 2
					elif branch == 1:
						pass
				elif transition == 21:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 2
					elif branch == 1:
						pass
				elif transition == 22:
					if branch == 0:
						target_state.var3 = 2
						target_state.var5 = 2
					elif branch == 1:
						pass
				elif transition == 23:
					if branch == 0:
						target_state.var3 = 3
						target_state.var5 = 2
					elif branch == 1:
						pass
				elif transition == 24:
					if branch == 0:
						target_state.var3 = 0
						target_state.var5 = 3
					elif branch == 1:
						pass
				elif transition == 25:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 3
					elif branch == 1:
						pass
				elif transition == 26:
					if branch == 0:
						target_state.var3 = 2
						target_state.var5 = 3
					elif branch == 1:
						pass
				elif transition == 27:
					if branch == 0:
						target_state.var3 = 3
						target_state.var5 = 3
					elif branch == 1:
						pass
				elif transition == 28:
					if branch == 0:
						target_state.var0 = 0
						target_state.var2 = 0
					elif branch == 1:
						pass
				elif transition == 29:
					if branch == 0:
						target_state.var0 = 1
						target_state.var2 = 0
					elif branch == 1:
						pass
				elif transition == 30:
					if branch == 0:
						target_state.var0 = 2
						target_state.var2 = 0
					elif branch == 1:
						pass
				elif transition == 31:
					if branch == 0:
						target_state.var0 = 3
						target_state.var2 = 0
					elif branch == 1:
						pass
				elif transition == 32:
					if branch == 0:
						target_state.var0 = 0
						target_state.var2 = 1
					elif branch == 1:
						pass
				elif transition == 33:
					if branch == 0:
						target_state.var0 = 1
						target_state.var2 = 1
					elif branch == 1:
						pass
				elif transition == 34:
					if branch == 0:
						target_state.var0 = 2
						target_state.var2 = 1
					elif branch == 1:
						pass
				elif transition == 35:
					if branch == 0:
						target_state.var0 = 3
						target_state.var2 = 1
					elif branch == 1:
						pass
				elif transition == 36:
					if branch == 0:
						target_state.var0 = 0
						target_state.var2 = 2
					elif branch == 1:
						pass
				elif transition == 37:
					if branch == 0:
						target_state.var0 = 1
						target_state.var2 = 2
					elif branch == 1:
						pass
				elif transition == 38:
					if branch == 0:
						target_state.var0 = 2
						target_state.var2 = 2
					elif branch == 1:
						pass
				elif transition == 39:
					if branch == 0:
						target_state.var0 = 3
						target_state.var2 = 2
					elif branch == 1:
						pass
				elif transition == 40:
					if branch == 0:
						target_state.var0 = 0
						target_state.var2 = 3
					elif branch == 1:
						pass
				elif transition == 41:
					if branch == 0:
						target_state.var0 = 1
						target_state.var2 = 3
					elif branch == 1:
						pass
				elif transition == 42:
					if branch == 0:
						target_state.var0 = 2
						target_state.var2 = 3
					elif branch == 1:
						pass
				elif transition == 43:
					if branch == 0:
						target_state.var0 = 3
						target_state.var2 = 3
					elif branch == 1:
						pass
				elif transition == 44:
					if branch == 0:
						target_state.var3 = 1
						target_state.var4 = 0
					elif branch == 1:
						pass
				elif transition == 45:
					if branch == 0:
						target_state.var3 = 2
						target_state.var4 = 0
					elif branch == 1:
						pass
				elif transition == 46:
					if branch == 0:
						target_state.var3 = 3
						target_state.var4 = 0
					elif branch == 1:
						pass
				elif transition == 47:
					if branch == 0:
						target_state.var3 = 4
						target_state.var4 = 0
					elif branch == 1:
						pass
				elif transition == 48:
					if branch == 0:
						target_state.var0 = 1
						target_state.var1 = 0
					elif branch == 1:
						pass
				elif transition == 49:
					if branch == 0:
						target_state.var0 = 2
						target_state.var1 = 0
					elif branch == 1:
						pass
				elif transition == 50:
					if branch == 0:
						target_state.var0 = 3
						target_state.var1 = 0
					elif branch == 1:
						pass
				elif transition == 51:
					if branch == 0:
						target_state.var0 = 4
						target_state.var1 = 0
					elif branch == 1:
						pass
				elif transition == 52:
					if branch == 0:
						target_state.var3 = 0
						target_state.var5 = 0
					elif branch == 1:
						pass
				elif transition == 53:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 0
					elif branch == 1:
						pass
				elif transition == 54:
					if branch == 0:
						target_state.var3 = 2
						target_state.var5 = 0
					elif branch == 1:
						pass
				elif transition == 55:
					if branch == 0:
						target_state.var3 = 3
						target_state.var5 = 0
					elif branch == 1:
						pass
				elif transition == 56:
					if branch == 0:
						target_state.var3 = 0
						target_state.var5 = 1
					elif branch == 1:
						pass
				elif transition == 57:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 1
					elif branch == 1:
						pass
				elif transition == 58:
					if branch == 0:
						target_state.var3 = 2
						target_state.var5 = 1
					elif branch == 1:
						pass
				elif transition == 59:
					if branch == 0:
						target_state.var3 = 3
						target_state.var5 = 1
					elif branch == 1:
						pass
				elif transition == 60:
					if branch == 0:
						target_state.var3 = 0
						target_state.var5 = 2
					elif branch == 1:
						pass
				elif transition == 61:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 2
					elif branch == 1:
						pass
				elif transition == 62:
					if branch == 0:
						target_state.var3 = 2
						target_state.var5 = 2
					elif branch == 1:
						pass
				elif transition == 63:
					if branch == 0:
						target_state.var3 = 3
						target_state.var5 = 2
					elif branch == 1:
						pass
				elif transition == 64:
					if branch == 0:
						target_state.var3 = 0
						target_state.var5 = 3
					elif branch == 1:
						pass
				elif transition == 65:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 3
					elif branch == 1:
						pass
				elif transition == 66:
					if branch == 0:
						target_state.var3 = 2
						target_state.var5 = 3
					elif branch == 1:
						pass
				elif transition == 67:
					if branch == 0:
						target_state.var3 = 3
						target_state.var5 = 3
					elif branch == 1:
						pass
				elif transition == 68:
					if branch == 0:
						target_state.var0 = 0
						target_state.var2 = 0
					elif branch == 1:
						pass
				elif transition == 69:
					if branch == 0:
						target_state.var0 = 1
						target_state.var2 = 0
					elif branch == 1:
						pass
				elif transition == 70:
					if branch == 0:
						target_state.var0 = 2
						target_state.var2 = 0
					elif branch == 1:
						pass
				elif transition == 71:
					if branch == 0:
						target_state.var0 = 3
						target_state.var2 = 0
					elif branch == 1:
						pass
				elif transition == 72:
					if branch == 0:
						target_state.var0 = 0
						target_state.var2 = 1
					elif branch == 1:
						pass
				elif transition == 73:
					if branch == 0:
						target_state.var0 = 1
						target_state.var2 = 1
					elif branch == 1:
						pass
				elif transition == 74:
					if branch == 0:
						target_state.var0 = 2
						target_state.var2 = 1
					elif branch == 1:
						pass
				elif transition == 75:
					if branch == 0:
						target_state.var0 = 3
						target_state.var2 = 1
					elif branch == 1:
						pass
				elif transition == 76:
					if branch == 0:
						target_state.var0 = 0
						target_state.var2 = 2
					elif branch == 1:
						pass
				elif transition == 77:
					if branch == 0:
						target_state.var0 = 1
						target_state.var2 = 2
					elif branch == 1:
						pass
				elif transition == 78:
					if branch == 0:
						target_state.var0 = 2
						target_state.var2 = 2
					elif branch == 1:
						pass
				elif transition == 79:
					if branch == 0:
						target_state.var0 = 3
						target_state.var2 = 2
					elif branch == 1:
						pass
				elif transition == 80:
					if branch == 0:
						target_state.var0 = 0
						target_state.var2 = 3
					elif branch == 1:
						pass
				elif transition == 81:
					if branch == 0:
						target_state.var0 = 1
						target_state.var2 = 3
					elif branch == 1:
						pass
				elif transition == 82:
					if branch == 0:
						target_state.var0 = 2
						target_state.var2 = 3
					elif branch == 1:
						pass
				elif transition == 83:
					if branch == 0:
						target_state.var0 = 3
						target_state.var2 = 3
					elif branch == 1:
						pass
				elif transition == 84:
					if branch == 0:
						target_state.var7 = 4
				elif transition == 85:
					if branch == 0:
						target_state.var7 = 5
				elif transition == 86:
					if branch == 0:
						target_state.var6 = 4
				elif transition == 87:
					if branch == 0:
						target_state.var6 = 5
				elif transition == 88:
					if branch == 0:
						target_state.var7 = 6
				elif transition == 89:
					if branch == 0:
						target_state.var7 = 7
				elif transition == 90:
					if branch == 0:
						target_state.var6 = 6
				elif transition == 91:
					if branch == 0:
						target_state.var6 = 7
				elif transition == 92:
					if branch == 0:
						target_state.var5 = 4
				elif transition == 93:
					if branch == 0:
						target_state.var5 = 5
				elif transition == 94:
					if branch == 0:
						target_state.var5 = 6
				elif transition == 95:
					if branch == 0:
						target_state.var5 = 7
				elif transition == 96:
					if branch == 0:
						target_state.var2 = 4
				elif transition == 97:
					if branch == 0:
						target_state.var2 = 5
				elif transition == 98:
					if branch == 0:
						target_state.var2 = 6
				elif transition == 99:
					if branch == 0:
						target_state.var2 = 7
				elif transition == 100:
					if branch == 0:
						target_state.var4 = 1
				elif transition == 101:
					if branch == 0:
						target_state.var1 = 1
				elif transition == 102:
					if branch == 0:
						target_state.var5 = 8
				elif transition == 103:
					if branch == 0:
						target_state.var5 = 9
				elif transition == 104:
					if branch == 0:
						target_state.var5 = 10
				elif transition == 105:
					if branch == 0:
						target_state.var5 = 11
				elif transition == 106:
					if branch == 0:
						target_state.var2 = 8
				elif transition == 107:
					if branch == 0:
						target_state.var2 = 9
				elif transition == 108:
					if branch == 0:
						target_state.var2 = 10
				elif transition == 109:
					if branch == 0:
						target_state.var2 = 11

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_main")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ" }
		self.sync_vectors = [[0, 0]]
		self.properties = [
			Property("goal", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("var0", None, "int", 0, 5),
			VariableInfo("var1", None, "int", 0, 2),
			VariableInfo("var2", None, "int", 0, 12),
			VariableInfo("var3", None, "int", 0, 5),
			VariableInfo("var4", None, "int", 0, 2),
			VariableInfo("var5", None, "int", 0, 12),
			VariableInfo("var6", None, "int", 0, 10),
			VariableInfo("var7", None, "int", 0, 10)
		]
		self._aut_main = mainAutomaton(self)
		self.components = [self._aut_main]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.var0 = 1
		state.var1 = 0
		state.var2 = 3
		state.var3 = 3
		state.var4 = 0
		state.var5 = 3
		state.var6 = 0
		state.var7 = 1
		self._aut_main.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_main.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return ((state.var7 == 1) and (state.var6 == 2))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return ((state.var7 == 1) and (state.var6 == 2))
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_main.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_main = [[]]
		transition_count = self._aut_main.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_main.get_guard_value(state, i):
				trans_main[self._aut_main.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1]]
			# main
			if synced is not None:
				if sv[0] != -1:
					if len(trans_main[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_main[sv[0]][0]
						for i in range(1, len(trans_main[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_main[sv[0]][i]
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
		combs = [[-1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_main.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_main.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_main.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
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
				self._aut_main.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
