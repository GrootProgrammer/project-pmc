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
	__slots__ = ("var0", "var1", "var2", "var3", "var4", "var5", "var6", "var7", "var8", "var9", "var10", "var11", "var12", "var13", "var14", "var15", "var16", "var17", "var18", "var19", "var20", "var21")
	
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
		elif variable == 8:
			return self.var8
		elif variable == 9:
			return self.var9
		elif variable == 10:
			return self.var10
		elif variable == 11:
			return self.var11
		elif variable == 12:
			return self.var12
		elif variable == 13:
			return self.var13
		elif variable == 14:
			return self.var14
		elif variable == 15:
			return self.var15
		elif variable == 16:
			return self.var16
		elif variable == 17:
			return self.var17
		elif variable == 18:
			return self.var18
		elif variable == 19:
			return self.var19
		elif variable == 20:
			return self.var20
		elif variable == 21:
			return self.var21
	
	def copy_to(self, other: State):
		other.var0 = self.var0
		other.var1 = self.var1
		other.var2 = self.var2
		other.var3 = self.var3
		other.var4 = self.var4
		other.var5 = self.var5
		other.var6 = self.var6
		other.var7 = self.var7
		other.var8 = self.var8
		other.var9 = self.var9
		other.var10 = self.var10
		other.var11 = self.var11
		other.var12 = self.var12
		other.var13 = self.var13
		other.var14 = self.var14
		other.var15 = self.var15
		other.var16 = self.var16
		other.var17 = self.var17
		other.var18 = self.var18
		other.var19 = self.var19
		other.var20 = self.var20
		other.var21 = self.var21
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.var0 == other.var0 and self.var1 == other.var1 and self.var2 == other.var2 and self.var3 == other.var3 and self.var4 == other.var4 and self.var5 == other.var5 and self.var6 == other.var6 and self.var7 == other.var7 and self.var8 == other.var8 and self.var9 == other.var9 and self.var10 == other.var10 and self.var11 == other.var11 and self.var12 == other.var12 and self.var13 == other.var13 and self.var14 == other.var14 and self.var15 == other.var15 and self.var16 == other.var16 and self.var17 == other.var17 and self.var18 == other.var18 and self.var19 == other.var19 and self.var20 == other.var20 and self.var21 == other.var21
	
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
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var8)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var9)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var10)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var11)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var12)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var13)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var14)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var15)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var16)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var17)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var18)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var19)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var20)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var21)) & 0xFFFFFFFF
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
		result += ", var8 = " + str(self.var8)
		result += ", var9 = " + str(self.var9)
		result += ", var10 = " + str(self.var10)
		result += ", var11 = " + str(self.var11)
		result += ", var12 = " + str(self.var12)
		result += ", var13 = " + str(self.var13)
		result += ", var14 = " + str(self.var14)
		result += ", var15 = " + str(self.var15)
		result += ", var16 = " + str(self.var16)
		result += ", var17 = " + str(self.var17)
		result += ", var18 = " + str(self.var18)
		result += ", var19 = " + str(self.var19)
		result += ", var20 = " + str(self.var20)
		result += ", var21 = " + str(self.var21)
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

# Automaton: aut
class autAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [75]
		self.transition_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
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
				return ((((state.var19 == 0) and (state.var14 == 0)) and (state.var13 == 1)) and (state.var2 == 0))
			elif transition == 1:
				return ((((state.var19 == 0) and (state.var14 == 0)) and (state.var13 == 2)) and (state.var2 == 0))
			elif transition == 2:
				return ((((state.var19 == 0) and (state.var14 == 0)) and (state.var13 == 3)) and (state.var2 == 0))
			elif transition == 3:
				return ((((state.var19 == 0) and (state.var14 == 0)) and (state.var13 == 4)) and (state.var2 == 0))
			elif transition == 4:
				return ((((state.var20 == 1) and (state.var19 == 0)) and (state.var17 == 0)) and (state.var1 == 0))
			elif transition == 5:
				return ((((state.var20 == 2) and (state.var19 == 0)) and (state.var17 == 0)) and (state.var1 == 0))
			elif transition == 6:
				return ((((state.var20 == 3) and (state.var19 == 0)) and (state.var17 == 0)) and (state.var1 == 0))
			elif transition == 7:
				return ((((state.var20 == 4) and (state.var19 == 0)) and (state.var17 == 0)) and (state.var1 == 0))
			elif transition == 8:
				return ((((state.var19 == 0) and (state.var15 == 0)) and (state.var11 == 1)) and (state.var7 == 0))
			elif transition == 9:
				return ((((state.var19 == 0) and (state.var15 == 0)) and (state.var11 == 2)) and (state.var7 == 0))
			elif transition == 10:
				return ((((state.var19 == 0) and (state.var15 == 0)) and (state.var11 == 3)) and (state.var7 == 0))
			elif transition == 11:
				return ((((state.var19 == 0) and (state.var15 == 0)) and (state.var11 == 4)) and (state.var7 == 0))
			elif transition == 12:
				return ((((state.var21 == 1) and (state.var19 == 0)) and (state.var18 == 0)) and (state.var8 == 0))
			elif transition == 13:
				return ((((state.var21 == 2) and (state.var19 == 0)) and (state.var18 == 0)) and (state.var8 == 0))
			elif transition == 14:
				return ((((state.var21 == 3) and (state.var19 == 0)) and (state.var18 == 0)) and (state.var8 == 0))
			elif transition == 15:
				return ((((state.var21 == 4) and (state.var19 == 0)) and (state.var18 == 0)) and (state.var8 == 0))
			elif transition == 16:
				return ((((state.var19 == 0) and (state.var16 == 0)) and (state.var12 == 1)) and (state.var5 == 0))
			elif transition == 17:
				return ((((state.var19 == 0) and (state.var16 == 0)) and (state.var12 == 2)) and (state.var5 == 0))
			elif transition == 18:
				return ((((state.var19 == 0) and (state.var16 == 0)) and (state.var12 == 3)) and (state.var5 == 0))
			elif transition == 19:
				return ((((state.var19 == 0) and (state.var16 == 0)) and (state.var12 == 4)) and (state.var5 == 0))
			elif transition == 20:
				return ((((state.var19 == 0) and (state.var14 == 0)) and (state.var13 == 5)) and (state.var2 == 0))
			elif transition == 21:
				return ((((state.var20 == 5) and (state.var19 == 0)) and (state.var17 == 0)) and (state.var1 == 0))
			elif transition == 22:
				return ((((state.var19 == 0) and (state.var15 == 0)) and (state.var11 == 5)) and (state.var7 == 0))
			elif transition == 23:
				return ((((state.var21 == 5) and (state.var19 == 0)) and (state.var18 == 0)) and (state.var8 == 0))
			elif transition == 24:
				return ((((state.var19 == 0) and (state.var16 == 0)) and (state.var12 == 5)) and (state.var5 == 0))
			elif transition == 25:
				return (((state.var13 == 0) and (state.var9 == 0)) and (state.var0 == 0))
			elif transition == 26:
				return (((state.var20 == 0) and (state.var10 == 0)) and (state.var0 == 0))
			elif transition == 27:
				return (((state.var11 == 0) and (state.var3 == 0)) and (state.var0 == 0))
			elif transition == 28:
				return (((state.var21 == 0) and (state.var4 == 0)) and (state.var0 == 0))
			elif transition == 29:
				return (((state.var12 == 0) and (state.var6 == 0)) and (state.var0 == 0))
			elif transition == 30:
				return (((state.var13 == 0) and (state.var9 == 1)) and (state.var0 == 0))
			elif transition == 31:
				return (((state.var20 == 0) and (state.var10 == 1)) and (state.var0 == 0))
			elif transition == 32:
				return (((state.var11 == 0) and (state.var3 == 1)) and (state.var0 == 0))
			elif transition == 33:
				return (((state.var21 == 0) and (state.var4 == 1)) and (state.var0 == 0))
			elif transition == 34:
				return (((state.var12 == 0) and (state.var6 == 1)) and (state.var0 == 0))
			elif transition == 35:
				return ((((state.var17 == 0) and (state.var13 == 0)) and (state.var9 == 0)) and (state.var1 == 0))
			elif transition == 36:
				return ((((state.var15 == 0) and (state.var13 == 0)) and (state.var9 == 0)) and (state.var7 == 0))
			elif transition == 37:
				return ((((state.var18 == 0) and (state.var13 == 0)) and (state.var9 == 0)) and (state.var8 == 0))
			elif transition == 38:
				return ((((state.var16 == 0) and (state.var13 == 0)) and (state.var9 == 0)) and (state.var5 == 0))
			elif transition == 39:
				return ((((state.var20 == 0) and (state.var14 == 0)) and (state.var10 == 0)) and (state.var2 == 0))
			elif transition == 40:
				return ((((state.var20 == 0) and (state.var15 == 0)) and (state.var10 == 0)) and (state.var7 == 0))
			elif transition == 41:
				return ((((state.var20 == 0) and (state.var18 == 0)) and (state.var10 == 0)) and (state.var8 == 0))
			elif transition == 42:
				return ((((state.var20 == 0) and (state.var16 == 0)) and (state.var10 == 0)) and (state.var5 == 0))
			elif transition == 43:
				return ((((state.var14 == 0) and (state.var11 == 0)) and (state.var3 == 0)) and (state.var2 == 0))
			elif transition == 44:
				return ((((state.var17 == 0) and (state.var11 == 0)) and (state.var3 == 0)) and (state.var1 == 0))
			elif transition == 45:
				return ((((state.var18 == 0) and (state.var11 == 0)) and (state.var8 == 0)) and (state.var3 == 0))
			elif transition == 46:
				return ((((state.var16 == 0) and (state.var11 == 0)) and (state.var5 == 0)) and (state.var3 == 0))
			elif transition == 47:
				return ((((state.var21 == 0) and (state.var14 == 0)) and (state.var4 == 0)) and (state.var2 == 0))
			elif transition == 48:
				return ((((state.var21 == 0) and (state.var17 == 0)) and (state.var4 == 0)) and (state.var1 == 0))
			elif transition == 49:
				return ((((state.var21 == 0) and (state.var15 == 0)) and (state.var7 == 0)) and (state.var4 == 0))
			elif transition == 50:
				return ((((state.var21 == 0) and (state.var16 == 0)) and (state.var5 == 0)) and (state.var4 == 0))
			elif transition == 51:
				return ((((state.var14 == 0) and (state.var12 == 0)) and (state.var6 == 0)) and (state.var2 == 0))
			elif transition == 52:
				return ((((state.var17 == 0) and (state.var12 == 0)) and (state.var6 == 0)) and (state.var1 == 0))
			elif transition == 53:
				return ((((state.var15 == 0) and (state.var12 == 0)) and (state.var7 == 0)) and (state.var6 == 0))
			elif transition == 54:
				return ((((state.var18 == 0) and (state.var12 == 0)) and (state.var8 == 0)) and (state.var6 == 0))
			elif transition == 55:
				return ((((state.var17 == 0) and (state.var13 == 0)) and (state.var9 == 1)) and (state.var1 == 0))
			elif transition == 56:
				return ((((state.var15 == 0) and (state.var13 == 0)) and (state.var9 == 1)) and (state.var7 == 0))
			elif transition == 57:
				return ((((state.var18 == 0) and (state.var13 == 0)) and (state.var9 == 1)) and (state.var8 == 0))
			elif transition == 58:
				return ((((state.var16 == 0) and (state.var13 == 0)) and (state.var9 == 1)) and (state.var5 == 0))
			elif transition == 59:
				return ((((state.var20 == 0) and (state.var14 == 0)) and (state.var10 == 1)) and (state.var2 == 0))
			elif transition == 60:
				return ((((state.var20 == 0) and (state.var15 == 0)) and (state.var10 == 1)) and (state.var7 == 0))
			elif transition == 61:
				return ((((state.var20 == 0) and (state.var18 == 0)) and (state.var10 == 1)) and (state.var8 == 0))
			elif transition == 62:
				return ((((state.var20 == 0) and (state.var16 == 0)) and (state.var10 == 1)) and (state.var5 == 0))
			elif transition == 63:
				return ((((state.var14 == 0) and (state.var11 == 0)) and (state.var3 == 1)) and (state.var2 == 0))
			elif transition == 64:
				return ((((state.var17 == 0) and (state.var11 == 0)) and (state.var3 == 1)) and (state.var1 == 0))
			elif transition == 65:
				return ((((state.var18 == 0) and (state.var11 == 0)) and (state.var8 == 0)) and (state.var3 == 1))
			elif transition == 66:
				return ((((state.var16 == 0) and (state.var11 == 0)) and (state.var5 == 0)) and (state.var3 == 1))
			elif transition == 67:
				return ((((state.var21 == 0) and (state.var14 == 0)) and (state.var4 == 1)) and (state.var2 == 0))
			elif transition == 68:
				return ((((state.var21 == 0) and (state.var17 == 0)) and (state.var4 == 1)) and (state.var1 == 0))
			elif transition == 69:
				return ((((state.var21 == 0) and (state.var15 == 0)) and (state.var7 == 0)) and (state.var4 == 1))
			elif transition == 70:
				return ((((state.var21 == 0) and (state.var16 == 0)) and (state.var5 == 0)) and (state.var4 == 1))
			elif transition == 71:
				return ((((state.var14 == 0) and (state.var12 == 0)) and (state.var6 == 1)) and (state.var2 == 0))
			elif transition == 72:
				return ((((state.var17 == 0) and (state.var12 == 0)) and (state.var6 == 1)) and (state.var1 == 0))
			elif transition == 73:
				return ((((state.var15 == 0) and (state.var12 == 0)) and (state.var7 == 0)) and (state.var6 == 1))
			elif transition == 74:
				return ((((state.var18 == 0) and (state.var12 == 0)) and (state.var8 == 0)) and (state.var6 == 1))
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
				if branch == 0:
					return (4 / 10)
				elif branch == 1:
					return (6 / 10)
			elif transition == 26:
				if branch == 0:
					return (4 / 10)
				elif branch == 1:
					return (6 / 10)
			elif transition == 27:
				if branch == 0:
					return (4 / 10)
				elif branch == 1:
					return (6 / 10)
			elif transition == 28:
				if branch == 0:
					return (4 / 10)
				elif branch == 1:
					return (6 / 10)
			elif transition == 29:
				if branch == 0:
					return (4 / 10)
				elif branch == 1:
					return (6 / 10)
			elif transition == 30:
				return 1
			elif transition == 31:
				return 1
			elif transition == 32:
				return 1
			elif transition == 33:
				return 1
			elif transition == 34:
				return 1
			elif transition == 35:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 36:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 37:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 38:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 39:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 40:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 41:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 42:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 43:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 44:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 45:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 46:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 47:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 48:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 49:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 50:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 51:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 52:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 53:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 54:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 55:
				return 1
			elif transition == 56:
				return 1
			elif transition == 57:
				return 1
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
			elif transition == 67:
				return 1
			elif transition == 68:
				return 1
			elif transition == 69:
				return 1
			elif transition == 70:
				return 1
			elif transition == 71:
				return 1
			elif transition == 72:
				return 1
			elif transition == 73:
				return 1
			elif transition == 74:
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
						target_state.var13 = 0
						target_state.var14 = 1
						target_state.var17 = 0
						target_state.var19 = 1
				elif transition == 1:
					if branch == 0:
						target_state.var13 = 0
						target_state.var14 = 1
						target_state.var15 = 0
						target_state.var19 = 1
				elif transition == 2:
					if branch == 0:
						target_state.var13 = 0
						target_state.var14 = 1
						target_state.var18 = 0
						target_state.var19 = 1
				elif transition == 3:
					if branch == 0:
						target_state.var13 = 0
						target_state.var14 = 1
						target_state.var16 = 0
						target_state.var19 = 1
				elif transition == 4:
					if branch == 0:
						target_state.var14 = 0
						target_state.var17 = 1
						target_state.var19 = 1
						target_state.var20 = 0
				elif transition == 5:
					if branch == 0:
						target_state.var15 = 0
						target_state.var17 = 1
						target_state.var19 = 1
						target_state.var20 = 0
				elif transition == 6:
					if branch == 0:
						target_state.var17 = 1
						target_state.var18 = 0
						target_state.var19 = 1
						target_state.var20 = 0
				elif transition == 7:
					if branch == 0:
						target_state.var16 = 0
						target_state.var17 = 1
						target_state.var19 = 1
						target_state.var20 = 0
				elif transition == 8:
					if branch == 0:
						target_state.var11 = 0
						target_state.var14 = 0
						target_state.var15 = 1
						target_state.var19 = 1
				elif transition == 9:
					if branch == 0:
						target_state.var11 = 0
						target_state.var15 = 1
						target_state.var17 = 0
						target_state.var19 = 1
				elif transition == 10:
					if branch == 0:
						target_state.var11 = 0
						target_state.var15 = 1
						target_state.var18 = 0
						target_state.var19 = 1
				elif transition == 11:
					if branch == 0:
						target_state.var11 = 0
						target_state.var15 = 1
						target_state.var16 = 0
						target_state.var19 = 1
				elif transition == 12:
					if branch == 0:
						target_state.var14 = 0
						target_state.var18 = 1
						target_state.var19 = 1
						target_state.var21 = 0
				elif transition == 13:
					if branch == 0:
						target_state.var17 = 0
						target_state.var18 = 1
						target_state.var19 = 1
						target_state.var21 = 0
				elif transition == 14:
					if branch == 0:
						target_state.var15 = 0
						target_state.var18 = 1
						target_state.var19 = 1
						target_state.var21 = 0
				elif transition == 15:
					if branch == 0:
						target_state.var16 = 0
						target_state.var18 = 1
						target_state.var19 = 1
						target_state.var21 = 0
				elif transition == 16:
					if branch == 0:
						target_state.var12 = 0
						target_state.var14 = 0
						target_state.var16 = 1
						target_state.var19 = 1
				elif transition == 17:
					if branch == 0:
						target_state.var12 = 0
						target_state.var16 = 1
						target_state.var17 = 0
						target_state.var19 = 1
				elif transition == 18:
					if branch == 0:
						target_state.var12 = 0
						target_state.var15 = 0
						target_state.var16 = 1
						target_state.var19 = 1
				elif transition == 19:
					if branch == 0:
						target_state.var12 = 0
						target_state.var16 = 1
						target_state.var18 = 0
						target_state.var19 = 1
				elif transition == 20:
					if branch == 0:
						target_state.var13 = 0
						target_state.var14 = 1
						target_state.var19 = 1
				elif transition == 21:
					if branch == 0:
						target_state.var17 = 1
						target_state.var19 = 1
						target_state.var20 = 0
				elif transition == 22:
					if branch == 0:
						target_state.var11 = 0
						target_state.var15 = 1
						target_state.var19 = 1
				elif transition == 23:
					if branch == 0:
						target_state.var18 = 1
						target_state.var19 = 1
						target_state.var21 = 0
				elif transition == 24:
					if branch == 0:
						target_state.var12 = 0
						target_state.var16 = 1
						target_state.var19 = 1
				elif transition == 25:
					if branch == 0:
						target_state.var0 = 1
						target_state.var9 = 1
						target_state.var13 = 5
						target_state.var14 = 0
						target_state.var19 = 0
					elif branch == 1:
						target_state.var13 = 5
						target_state.var14 = 0
						target_state.var19 = 0
				elif transition == 26:
					if branch == 0:
						target_state.var0 = 1
						target_state.var10 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 5
					elif branch == 1:
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 5
				elif transition == 27:
					if branch == 0:
						target_state.var0 = 1
						target_state.var3 = 1
						target_state.var11 = 5
						target_state.var15 = 0
						target_state.var19 = 0
					elif branch == 1:
						target_state.var11 = 5
						target_state.var15 = 0
						target_state.var19 = 0
				elif transition == 28:
					if branch == 0:
						target_state.var0 = 1
						target_state.var4 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 5
					elif branch == 1:
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 5
				elif transition == 29:
					if branch == 0:
						target_state.var0 = 1
						target_state.var6 = 1
						target_state.var12 = 5
						target_state.var16 = 0
						target_state.var19 = 0
					elif branch == 1:
						target_state.var12 = 5
						target_state.var16 = 0
						target_state.var19 = 0
				elif transition == 30:
					if branch == 0:
						target_state.var13 = 5
						target_state.var14 = 0
						target_state.var19 = 0
				elif transition == 31:
					if branch == 0:
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 5
				elif transition == 32:
					if branch == 0:
						target_state.var11 = 5
						target_state.var15 = 0
						target_state.var19 = 0
				elif transition == 33:
					if branch == 0:
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 5
				elif transition == 34:
					if branch == 0:
						target_state.var12 = 5
						target_state.var16 = 0
						target_state.var19 = 0
				elif transition == 35:
					if branch == 0:
						target_state.var1 = 1
						target_state.var9 = 1
						target_state.var13 = 1
						target_state.var14 = 0
						target_state.var17 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var13 = 1
						target_state.var14 = 0
						target_state.var17 = 1
						target_state.var19 = 0
				elif transition == 36:
					if branch == 0:
						target_state.var7 = 1
						target_state.var9 = 1
						target_state.var13 = 2
						target_state.var14 = 0
						target_state.var15 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var13 = 2
						target_state.var14 = 0
						target_state.var15 = 1
						target_state.var19 = 0
				elif transition == 37:
					if branch == 0:
						target_state.var8 = 1
						target_state.var9 = 1
						target_state.var13 = 3
						target_state.var14 = 0
						target_state.var18 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var13 = 3
						target_state.var14 = 0
						target_state.var18 = 1
						target_state.var19 = 0
				elif transition == 38:
					if branch == 0:
						target_state.var5 = 1
						target_state.var9 = 1
						target_state.var13 = 4
						target_state.var14 = 0
						target_state.var16 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var13 = 4
						target_state.var14 = 0
						target_state.var16 = 1
						target_state.var19 = 0
				elif transition == 39:
					if branch == 0:
						target_state.var2 = 1
						target_state.var10 = 1
						target_state.var14 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 1
					elif branch == 1:
						target_state.var14 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 1
				elif transition == 40:
					if branch == 0:
						target_state.var7 = 1
						target_state.var10 = 1
						target_state.var15 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 2
					elif branch == 1:
						target_state.var15 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 2
				elif transition == 41:
					if branch == 0:
						target_state.var8 = 1
						target_state.var10 = 1
						target_state.var17 = 0
						target_state.var18 = 1
						target_state.var19 = 0
						target_state.var20 = 3
					elif branch == 1:
						target_state.var17 = 0
						target_state.var18 = 1
						target_state.var19 = 0
						target_state.var20 = 3
				elif transition == 42:
					if branch == 0:
						target_state.var5 = 1
						target_state.var10 = 1
						target_state.var16 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 4
					elif branch == 1:
						target_state.var16 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 4
				elif transition == 43:
					if branch == 0:
						target_state.var2 = 1
						target_state.var3 = 1
						target_state.var11 = 1
						target_state.var14 = 1
						target_state.var15 = 0
						target_state.var19 = 0
					elif branch == 1:
						target_state.var11 = 1
						target_state.var14 = 1
						target_state.var15 = 0
						target_state.var19 = 0
				elif transition == 44:
					if branch == 0:
						target_state.var1 = 1
						target_state.var3 = 1
						target_state.var11 = 2
						target_state.var15 = 0
						target_state.var17 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var11 = 2
						target_state.var15 = 0
						target_state.var17 = 1
						target_state.var19 = 0
				elif transition == 45:
					if branch == 0:
						target_state.var3 = 1
						target_state.var8 = 1
						target_state.var11 = 3
						target_state.var15 = 0
						target_state.var18 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var11 = 3
						target_state.var15 = 0
						target_state.var18 = 1
						target_state.var19 = 0
				elif transition == 46:
					if branch == 0:
						target_state.var3 = 1
						target_state.var5 = 1
						target_state.var11 = 4
						target_state.var15 = 0
						target_state.var16 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var11 = 4
						target_state.var15 = 0
						target_state.var16 = 1
						target_state.var19 = 0
				elif transition == 47:
					if branch == 0:
						target_state.var2 = 1
						target_state.var4 = 1
						target_state.var14 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 1
					elif branch == 1:
						target_state.var14 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 1
				elif transition == 48:
					if branch == 0:
						target_state.var1 = 1
						target_state.var4 = 1
						target_state.var17 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 2
					elif branch == 1:
						target_state.var17 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 2
				elif transition == 49:
					if branch == 0:
						target_state.var4 = 1
						target_state.var7 = 1
						target_state.var15 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 3
					elif branch == 1:
						target_state.var15 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 3
				elif transition == 50:
					if branch == 0:
						target_state.var4 = 1
						target_state.var5 = 1
						target_state.var16 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 4
					elif branch == 1:
						target_state.var16 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 4
				elif transition == 51:
					if branch == 0:
						target_state.var2 = 1
						target_state.var6 = 1
						target_state.var12 = 1
						target_state.var14 = 1
						target_state.var16 = 0
						target_state.var19 = 0
					elif branch == 1:
						target_state.var12 = 1
						target_state.var14 = 1
						target_state.var16 = 0
						target_state.var19 = 0
				elif transition == 52:
					if branch == 0:
						target_state.var1 = 1
						target_state.var6 = 1
						target_state.var12 = 2
						target_state.var16 = 0
						target_state.var17 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var12 = 2
						target_state.var16 = 0
						target_state.var17 = 1
						target_state.var19 = 0
				elif transition == 53:
					if branch == 0:
						target_state.var6 = 1
						target_state.var7 = 1
						target_state.var12 = 3
						target_state.var15 = 1
						target_state.var16 = 0
						target_state.var19 = 0
					elif branch == 1:
						target_state.var12 = 3
						target_state.var15 = 1
						target_state.var16 = 0
						target_state.var19 = 0
				elif transition == 54:
					if branch == 0:
						target_state.var6 = 1
						target_state.var8 = 1
						target_state.var12 = 4
						target_state.var16 = 0
						target_state.var18 = 1
						target_state.var19 = 0
					elif branch == 1:
						target_state.var12 = 4
						target_state.var16 = 0
						target_state.var18 = 1
						target_state.var19 = 0
				elif transition == 55:
					if branch == 0:
						target_state.var13 = 1
						target_state.var14 = 0
						target_state.var17 = 1
						target_state.var19 = 0
				elif transition == 56:
					if branch == 0:
						target_state.var13 = 2
						target_state.var14 = 0
						target_state.var15 = 1
						target_state.var19 = 0
				elif transition == 57:
					if branch == 0:
						target_state.var13 = 3
						target_state.var14 = 0
						target_state.var18 = 1
						target_state.var19 = 0
				elif transition == 58:
					if branch == 0:
						target_state.var13 = 4
						target_state.var14 = 0
						target_state.var16 = 1
						target_state.var19 = 0
				elif transition == 59:
					if branch == 0:
						target_state.var14 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 1
				elif transition == 60:
					if branch == 0:
						target_state.var15 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 2
				elif transition == 61:
					if branch == 0:
						target_state.var17 = 0
						target_state.var18 = 1
						target_state.var19 = 0
						target_state.var20 = 3
				elif transition == 62:
					if branch == 0:
						target_state.var16 = 1
						target_state.var17 = 0
						target_state.var19 = 0
						target_state.var20 = 4
				elif transition == 63:
					if branch == 0:
						target_state.var11 = 1
						target_state.var14 = 1
						target_state.var15 = 0
						target_state.var19 = 0
				elif transition == 64:
					if branch == 0:
						target_state.var11 = 2
						target_state.var15 = 0
						target_state.var17 = 1
						target_state.var19 = 0
				elif transition == 65:
					if branch == 0:
						target_state.var11 = 3
						target_state.var15 = 0
						target_state.var18 = 1
						target_state.var19 = 0
				elif transition == 66:
					if branch == 0:
						target_state.var11 = 4
						target_state.var15 = 0
						target_state.var16 = 1
						target_state.var19 = 0
				elif transition == 67:
					if branch == 0:
						target_state.var14 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 1
				elif transition == 68:
					if branch == 0:
						target_state.var17 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 2
				elif transition == 69:
					if branch == 0:
						target_state.var15 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 3
				elif transition == 70:
					if branch == 0:
						target_state.var16 = 1
						target_state.var18 = 0
						target_state.var19 = 0
						target_state.var21 = 4
				elif transition == 71:
					if branch == 0:
						target_state.var12 = 1
						target_state.var14 = 1
						target_state.var16 = 0
						target_state.var19 = 0
				elif transition == 72:
					if branch == 0:
						target_state.var12 = 2
						target_state.var16 = 0
						target_state.var17 = 1
						target_state.var19 = 0
				elif transition == 73:
					if branch == 0:
						target_state.var12 = 3
						target_state.var15 = 1
						target_state.var16 = 0
						target_state.var19 = 0
				elif transition == 74:
					if branch == 0:
						target_state.var12 = 4
						target_state.var16 = 0
						target_state.var18 = 1
						target_state.var19 = 0

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
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_aut")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ" }
		self.sync_vectors = [[0, 0]]
		self.properties = [
			Property("goal", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))
		]
		self.variables = [
			VariableInfo("var0", None, "int", 0, 2),
			VariableInfo("var1", None, "int", 0, 2),
			VariableInfo("var2", None, "int", 0, 2),
			VariableInfo("var3", None, "int", 0, 2),
			VariableInfo("var4", None, "int", 0, 2),
			VariableInfo("var5", None, "int", 0, 2),
			VariableInfo("var6", None, "int", 0, 2),
			VariableInfo("var7", None, "int", 0, 2),
			VariableInfo("var8", None, "int", 0, 2),
			VariableInfo("var9", None, "int", 0, 2),
			VariableInfo("var10", None, "int", 0, 2),
			VariableInfo("var11", None, "int", 0, 6),
			VariableInfo("var12", None, "int", 0, 6),
			VariableInfo("var13", None, "int", 0, 6),
			VariableInfo("var14", None, "int", 0, 2),
			VariableInfo("var15", None, "int", 0, 2),
			VariableInfo("var16", None, "int", 0, 2),
			VariableInfo("var17", None, "int", 0, 2),
			VariableInfo("var18", None, "int", 0, 2),
			VariableInfo("var19", None, "int", 0, 2),
			VariableInfo("var20", None, "int", 0, 6),
			VariableInfo("var21", None, "int", 0, 6)
		]
		self._aut_aut = autAutomaton(self)
		self.components = [self._aut_aut]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.var0 = 0
		state.var1 = 0
		state.var2 = 0
		state.var3 = 0
		state.var4 = 0
		state.var5 = 0
		state.var6 = 0
		state.var7 = 0
		state.var8 = 0
		state.var9 = 0
		state.var10 = 0
		state.var11 = 2
		state.var12 = 5
		state.var13 = 3
		state.var14 = 0
		state.var15 = 0
		state.var16 = 1
		state.var17 = 1
		state.var18 = 1
		state.var19 = 0
		state.var20 = 5
		state.var21 = 4
		self._aut_aut.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_aut.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return ((state.var21 == 5) and (state.var20 == 3))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return ((state.var21 == 5) and (state.var20 == 3))
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_aut.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_aut = [[]]
		transition_count = self._aut_aut.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_aut.get_guard_value(state, i):
				trans_aut[self._aut_aut.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1]]
			# aut
			if synced is not None:
				if sv[0] != -1:
					if len(trans_aut[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_aut[sv[0]][0]
						for i in range(1, len(trans_aut[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_aut[sv[0]][i]
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
			branch_count = self._aut_aut.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_aut.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_aut.get_probability_value(state, transition.transitions[0], 0)
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
				self._aut_aut.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
