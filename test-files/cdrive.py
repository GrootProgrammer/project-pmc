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
	__slots__ = ("var0", "var1", "var2", "var3", "var4", "var5", "var6", "var7", "var8", "var9", "var10", "var11", "var12", "var13", "var14", "var15", "var16", "var17", "var18", "var19", "var20", "var21", "var22", "var23", "var24", "var25", "var26", "var27", "var28", "var29", "var30", "var31", "var32", "var33", "var34", "var35", "var36", "var37", "var38", "aut_location")
	
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
		elif variable == 22:
			return self.var22
		elif variable == 23:
			return self.var23
		elif variable == 24:
			return self.var24
		elif variable == 25:
			return self.var25
		elif variable == 26:
			return self.var26
		elif variable == 27:
			return self.var27
		elif variable == 28:
			return self.var28
		elif variable == 29:
			return self.var29
		elif variable == 30:
			return self.var30
		elif variable == 31:
			return self.var31
		elif variable == 32:
			return self.var32
		elif variable == 33:
			return self.var33
		elif variable == 34:
			return self.var34
		elif variable == 35:
			return self.var35
		elif variable == 36:
			return self.var36
		elif variable == 37:
			return self.var37
		elif variable == 38:
			return self.var38
		elif variable == 39:
			return self.aut_location
	
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
		other.var22 = self.var22
		other.var23 = self.var23
		other.var24 = self.var24
		other.var25 = self.var25
		other.var26 = self.var26
		other.var27 = self.var27
		other.var28 = self.var28
		other.var29 = self.var29
		other.var30 = self.var30
		other.var31 = self.var31
		other.var32 = self.var32
		other.var33 = self.var33
		other.var34 = self.var34
		other.var35 = self.var35
		other.var36 = self.var36
		other.var37 = self.var37
		other.var38 = self.var38
		other.aut_location = self.aut_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.var0 == other.var0 and self.var1 == other.var1 and self.var2 == other.var2 and self.var3 == other.var3 and self.var4 == other.var4 and self.var5 == other.var5 and self.var6 == other.var6 and self.var7 == other.var7 and self.var8 == other.var8 and self.var9 == other.var9 and self.var10 == other.var10 and self.var11 == other.var11 and self.var12 == other.var12 and self.var13 == other.var13 and self.var14 == other.var14 and self.var15 == other.var15 and self.var16 == other.var16 and self.var17 == other.var17 and self.var18 == other.var18 and self.var19 == other.var19 and self.var20 == other.var20 and self.var21 == other.var21 and self.var22 == other.var22 and self.var23 == other.var23 and self.var24 == other.var24 and self.var25 == other.var25 and self.var26 == other.var26 and self.var27 == other.var27 and self.var28 == other.var28 and self.var29 == other.var29 and self.var30 == other.var30 and self.var31 == other.var31 and self.var32 == other.var32 and self.var33 == other.var33 and self.var34 == other.var34 and self.var35 == other.var35 and self.var36 == other.var36 and self.var37 == other.var37 and self.var38 == other.var38 and self.aut_location == other.aut_location
	
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
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var22)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var23)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var24)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var25)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var26)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var27)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var28)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var29)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var30)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var31)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var32)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var33)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var34)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var35)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var36)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var37)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.var38)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.aut_location)) & 0xFFFFFFFF
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
		result += ", var22 = " + str(self.var22)
		result += ", var23 = " + str(self.var23)
		result += ", var24 = " + str(self.var24)
		result += ", var25 = " + str(self.var25)
		result += ", var26 = " + str(self.var26)
		result += ", var27 = " + str(self.var27)
		result += ", var28 = " + str(self.var28)
		result += ", var29 = " + str(self.var29)
		result += ", var30 = " + str(self.var30)
		result += ", var31 = " + str(self.var31)
		result += ", var32 = " + str(self.var32)
		result += ", var33 = " + str(self.var33)
		result += ", var34 = " + str(self.var34)
		result += ", var35 = " + str(self.var35)
		result += ", var36 = " + str(self.var36)
		result += ", var37 = " + str(self.var37)
		result += ", var38 = " + str(self.var38)
		result += ", aut_location = " + str(self.aut_location)
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
		self.transition_counts = [240, 3, 4, 0]
		self.transition_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0], [0, 0, 0, 0], []]
		self.branch_counts = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [4, 4, 4], [2, 2, 2, 2], []]
	
	def set_initial_values(self, state: State) -> None:
		state.aut_location = 2
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.aut_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.aut_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.aut_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.aut_location
		if location == 0:
			if transition == 0:
				return (((state.var35 == 0) and (state.var9 == 0)) or ((state.var35 == 3) and (state.var9 == 0)))
			elif transition == 1:
				return (((state.var35 == 3) and (state.var10 == 0)) or ((state.var35 == 0) and (state.var10 == 0)))
			elif transition == 2:
				return (((state.var35 == 0) and (state.var19 == 0)) or ((state.var35 == 3) and (state.var19 == 0)))
			elif transition == 3:
				return (((state.var35 == 3) and (state.var23 == 0)) or ((state.var35 == 0) and (state.var23 == 0)))
			elif transition == 4:
				return (((state.var35 == 2) and (state.var23 == 0)) or ((state.var35 == 1) and (state.var23 == 0)))
			elif transition == 5:
				return (((state.var35 == 0) and (state.var20 == 0)) or ((state.var35 == 3) and (state.var20 == 0)))
			elif transition == 6:
				return (((state.var35 == 3) and (state.var6 == 0)) or ((state.var35 == 0) and (state.var6 == 0)))
			elif transition == 7:
				return (((state.var35 == 2) and (state.var6 == 0)) or ((state.var35 == 1) and (state.var6 == 0)))
			elif transition == 8:
				return (((state.var35 == 1) and (state.var31 == 0)) or ((state.var35 == 2) and (state.var31 == 0)))
			elif transition == 9:
				return (((state.var35 == 0) and (state.var27 == 0)) or ((state.var35 == 3) and (state.var27 == 0)))
			elif transition == 10:
				return (((state.var35 == 1) and (state.var13 == 0)) or ((state.var35 == 2) and (state.var13 == 0)))
			elif transition == 11:
				return (((state.var35 == 3) and (state.var13 == 0)) or ((state.var35 == 0) and (state.var13 == 0)))
			elif transition == 12:
				return (((state.var35 == 0) and (state.var12 == 0)) or ((state.var35 == 3) and (state.var12 == 0)))
			elif transition == 13:
				return (((state.var35 == 3) and (state.var26 == 0)) or ((state.var35 == 0) and (state.var26 == 0)))
			elif transition == 14:
				return (((state.var35 == 2) and (state.var34 == 0)) or ((state.var35 == 1) and (state.var34 == 0)))
			elif transition == 15:
				return (((state.var35 == 2) and (state.var15 == 0)) or ((state.var35 == 1) and (state.var15 == 0)))
			elif transition == 16:
				return (((state.var35 == 0) and (state.var7 == 0)) or ((state.var35 == 3) and (state.var7 == 0)))
			elif transition == 17:
				return (((state.var35 == 3) and (state.var21 == 0)) or ((state.var35 == 0) and (state.var21 == 0)))
			elif transition == 18:
				return (((state.var35 == 2) and (state.var21 == 0)) or ((state.var35 == 1) and (state.var21 == 0)))
			elif transition == 19:
				return (((state.var35 == 1) and (state.var30 == 0)) or ((state.var35 == 2) and (state.var30 == 0)))
			elif transition == 20:
				return (((state.var35 == 0) and (state.var30 == 0)) or ((state.var35 == 3) and (state.var30 == 0)))
			elif transition == 21:
				return (((state.var35 == 3) and (state.var22 == 0)) or ((state.var35 == 0) and (state.var22 == 0)))
			elif transition == 22:
				return (((state.var35 == 1) and (state.var17 == 0)) or ((state.var35 == 2) and (state.var17 == 0)))
			elif transition == 23:
				return (((state.var35 == 0) and (state.var2 == 0)) or ((state.var35 == 3) and (state.var2 == 0)))
			elif transition == 24:
				return (((state.var35 == 1) and (state.var8 == 0)) or ((state.var35 == 2) and (state.var8 == 0)))
			elif transition == 25:
				return (((state.var35 == 3) and (state.var8 == 0)) or ((state.var35 == 0) and (state.var8 == 0)))
			elif transition == 26:
				return (((state.var35 == 0) and (state.var8 == 0)) or ((state.var35 == 3) and (state.var8 == 0)))
			elif transition == 27:
				return (((state.var35 == 3) and (state.var14 == 0)) or ((state.var35 == 0) and (state.var14 == 0)))
			elif transition == 28:
				return (((state.var35 == 0) and (state.var3 == 0)) or ((state.var35 == 3) and (state.var3 == 0)))
			elif transition == 29:
				return (((state.var35 == 3) and (state.var9 == 0)) or ((state.var35 == 0) and (state.var9 == 0)))
			elif transition == 30:
				return (((state.var35 == 2) and (state.var10 == 0)) or ((state.var35 == 1) and (state.var10 == 0)))
			elif transition == 31:
				return (((state.var35 == 2) and (state.var5 == 0)) or ((state.var35 == 1) and (state.var5 == 0)))
			elif transition == 32:
				return (((state.var35 == 2) and (state.var4 == 0)) or ((state.var35 == 1) and (state.var4 == 0)))
			elif transition == 33:
				return (((state.var35 == 2) and (state.var19 == 0)) or ((state.var35 == 1) and (state.var19 == 0)))
			elif transition == 34:
				return (((state.var35 == 1) and (state.var24 == 0)) or ((state.var35 == 2) and (state.var24 == 0)))
			elif transition == 35:
				return (((state.var35 == 2) and (state.var24 == 0)) or ((state.var35 == 1) and (state.var24 == 0)))
			elif transition == 36:
				return (((state.var35 == 1) and (state.var20 == 0)) or ((state.var35 == 2) and (state.var20 == 0)))
			elif transition == 37:
				return (((state.var35 == 1) and (state.var11 == 0)) or ((state.var35 == 2) and (state.var11 == 0)))
			elif transition == 38:
				return (((state.var35 == 2) and (state.var11 == 0)) or ((state.var35 == 1) and (state.var11 == 0)))
			elif transition == 39:
				return (((state.var35 == 1) and (state.var25 == 0)) or ((state.var35 == 2) and (state.var25 == 0)))
			elif transition == 40:
				return (((state.var35 == 1) and (state.var32 == 0)) or ((state.var35 == 2) and (state.var32 == 0)))
			elif transition == 41:
				return (((state.var35 == 1) and (state.var12 == 0)) or ((state.var35 == 2) and (state.var12 == 0)))
			elif transition == 42:
				return (((state.var35 == 0) and (state.var26 == 0)) or ((state.var35 == 3) and (state.var26 == 0)))
			elif transition == 43:
				return (((state.var35 == 3) and (state.var33 == 0)) or ((state.var35 == 0) and (state.var33 == 0)))
			elif transition == 44:
				return (((state.var35 == 0) and (state.var33 == 0)) or ((state.var35 == 3) and (state.var33 == 0)))
			elif transition == 45:
				return (((state.var35 == 2) and (state.var33 == 0)) or ((state.var35 == 1) and (state.var33 == 0)))
			elif transition == 46:
				return (((state.var35 == 3) and (state.var34 == 0)) or ((state.var35 == 0) and (state.var34 == 0)))
			elif transition == 47:
				return (((state.var35 == 0) and (state.var21 == 0)) or ((state.var35 == 3) and (state.var21 == 0)))
			elif transition == 48:
				return (((state.var35 == 1) and (state.var29 == 0)) or ((state.var35 == 2) and (state.var29 == 0)))
			elif transition == 49:
				return (((state.var35 == 3) and (state.var29 == 0)) or ((state.var35 == 0) and (state.var29 == 0)))
			elif transition == 50:
				return (((state.var35 == 2) and (state.var29 == 0)) or ((state.var35 == 1) and (state.var29 == 0)))
			elif transition == 51:
				return (((state.var35 == 0) and (state.var22 == 0)) or ((state.var35 == 3) and (state.var22 == 0)))
			elif transition == 52:
				return (((state.var35 == 3) and (state.var17 == 0)) or ((state.var35 == 0) and (state.var17 == 0)))
			elif transition == 53:
				return (((state.var35 == 2) and (state.var17 == 0)) or ((state.var35 == 1) and (state.var17 == 0)))
			elif transition == 54:
				return (((state.var35 == 1) and (state.var14 == 0)) or ((state.var35 == 2) and (state.var14 == 0)))
			elif transition == 55:
				return (((state.var35 == 0) and (state.var14 == 0)) or ((state.var35 == 3) and (state.var14 == 0)))
			elif transition == 56:
				return (((state.var35 == 3) and (state.var16 == 0)) or ((state.var35 == 0) and (state.var16 == 0)))
			elif transition == 57:
				return (((state.var35 == 0) and (state.var18 == 0)) or ((state.var35 == 3) and (state.var18 == 0)))
			elif transition == 58:
				return (((state.var37 == 0) and (state.var35 == 1)) or ((state.var37 == 0) and (state.var35 == 2)))
			elif transition == 59:
				return (((state.var37 == 0) and (state.var35 == 3)) or ((state.var37 == 0) and (state.var35 == 0)))
			elif transition == 60:
				return ((state.var35 == 1) and (state.var3 == 0))
			elif transition == 61:
				return ((state.var35 == 2) and (state.var9 == 0))
			elif transition == 62:
				return ((state.var35 == 0) and (state.var10 == 0))
			elif transition == 63:
				return ((state.var35 == 0) and (state.var5 == 0))
			elif transition == 64:
				return ((state.var35 == 0) and (state.var4 == 0))
			elif transition == 65:
				return ((state.var35 == 0) and (state.var19 == 0))
			elif transition == 66:
				return ((state.var35 == 3) and (state.var24 == 0))
			elif transition == 67:
				return ((state.var35 == 0) and (state.var24 == 0))
			elif transition == 68:
				return ((state.var35 == 3) and (state.var20 == 0))
			elif transition == 69:
				return ((state.var35 == 3) and (state.var11 == 0))
			elif transition == 70:
				return ((state.var35 == 0) and (state.var11 == 0))
			elif transition == 71:
				return ((state.var35 == 3) and (state.var25 == 0))
			elif transition == 72:
				return ((state.var35 == 3) and (state.var32 == 0))
			elif transition == 73:
				return ((state.var35 == 3) and (state.var12 == 0))
			elif transition == 74:
				return ((state.var35 == 1) and (state.var26 == 0))
			elif transition == 75:
				return ((state.var35 == 2) and (state.var33 == 0))
			elif transition == 76:
				return ((state.var35 == 1) and (state.var33 == 0))
			elif transition == 77:
				return ((state.var35 == 0) and (state.var33 == 0))
			elif transition == 78:
				return ((state.var35 == 2) and (state.var34 == 0))
			elif transition == 79:
				return ((state.var35 == 1) and (state.var21 == 0))
			elif transition == 80:
				return ((state.var35 == 3) and (state.var29 == 0))
			elif transition == 81:
				return ((state.var35 == 2) and (state.var29 == 0))
			elif transition == 82:
				return ((state.var35 == 0) and (state.var29 == 0))
			elif transition == 83:
				return ((state.var35 == 1) and (state.var22 == 0))
			elif transition == 84:
				return ((state.var35 == 2) and (state.var17 == 0))
			elif transition == 85:
				return ((state.var35 == 0) and (state.var17 == 0))
			elif transition == 86:
				return ((state.var35 == 3) and (state.var14 == 0))
			elif transition == 87:
				return ((state.var35 == 1) and (state.var14 == 0))
			elif transition == 88:
				return ((state.var35 == 2) and (state.var16 == 0))
			elif transition == 89:
				return ((state.var35 == 1) and (state.var18 == 0))
			elif transition == 90:
				return ((state.var37 == 0) and (state.var35 == 3))
			elif transition == 91:
				return ((state.var37 == 0) and (state.var35 == 2))
			elif transition == 92:
				return (((state.var35 == 0) and (state.var0 == 0)) or ((state.var35 == 3) and (state.var0 == 0)))
			elif transition == 93:
				return (((state.var35 == 2) and (state.var0 == 0)) or ((state.var35 == 1) and (state.var0 == 0)))
			elif transition == 94:
				return (((state.var35 == 3) and (state.var3 == 0)) or ((state.var35 == 0) and (state.var3 == 0)))
			elif transition == 95:
				return (((state.var35 == 2) and (state.var3 == 0)) or ((state.var35 == 1) and (state.var3 == 0)))
			elif transition == 96:
				return (((state.var35 == 2) and (state.var9 == 0)) or ((state.var35 == 1) and (state.var9 == 0)))
			elif transition == 97:
				return (((state.var35 == 0) and (state.var10 == 0)) or ((state.var35 == 3) and (state.var10 == 0)))
			elif transition == 98:
				return (((state.var35 == 3) and (state.var5 == 0)) or ((state.var35 == 0) and (state.var5 == 0)))
			elif transition == 99:
				return (((state.var35 == 0) and (state.var5 == 0)) or ((state.var35 == 3) and (state.var5 == 0)))
			elif transition == 100:
				return (((state.var35 == 3) and (state.var1 == 0)) or ((state.var35 == 0) and (state.var1 == 0)))
			elif transition == 101:
				return (((state.var35 == 2) and (state.var1 == 0)) or ((state.var35 == 1) and (state.var1 == 0)))
			elif transition == 102:
				return (((state.var35 == 1) and (state.var4 == 0)) or ((state.var35 == 2) and (state.var4 == 0)))
			elif transition == 103:
				return (((state.var35 == 0) and (state.var4 == 0)) or ((state.var35 == 3) and (state.var4 == 0)))
			elif transition == 104:
				return (((state.var35 == 1) and (state.var19 == 0)) or ((state.var35 == 2) and (state.var19 == 0)))
			elif transition == 105:
				return (((state.var35 == 3) and (state.var19 == 0)) or ((state.var35 == 0) and (state.var19 == 0)))
			elif transition == 106:
				return (((state.var35 == 1) and (state.var23 == 0)) or ((state.var35 == 2) and (state.var23 == 0)))
			elif transition == 107:
				return (((state.var35 == 0) and (state.var23 == 0)) or ((state.var35 == 3) and (state.var23 == 0)))
			elif transition == 108:
				return (((state.var35 == 3) and (state.var24 == 0)) or ((state.var35 == 0) and (state.var24 == 0)))
			elif transition == 109:
				return (((state.var35 == 0) and (state.var24 == 0)) or ((state.var35 == 3) and (state.var24 == 0)))
			elif transition == 110:
				return (((state.var35 == 3) and (state.var20 == 0)) or ((state.var35 == 0) and (state.var20 == 0)))
			elif transition == 111:
				return (((state.var35 == 2) and (state.var20 == 0)) or ((state.var35 == 1) and (state.var20 == 0)))
			elif transition == 112:
				return (((state.var35 == 1) and (state.var6 == 0)) or ((state.var35 == 2) and (state.var6 == 0)))
			elif transition == 113:
				return (((state.var35 == 0) and (state.var11 == 0)) or ((state.var35 == 3) and (state.var11 == 0)))
			elif transition == 114:
				return (((state.var35 == 3) and (state.var25 == 0)) or ((state.var35 == 0) and (state.var25 == 0)))
			elif transition == 115:
				return (((state.var35 == 0) and (state.var25 == 0)) or ((state.var35 == 3) and (state.var25 == 0)))
			elif transition == 116:
				return (((state.var35 == 2) and (state.var25 == 0)) or ((state.var35 == 1) and (state.var25 == 0)))
			elif transition == 117:
				return (((state.var35 == 3) and (state.var31 == 0)) or ((state.var35 == 0) and (state.var31 == 0)))
			elif transition == 118:
				return (((state.var35 == 0) and (state.var31 == 0)) or ((state.var35 == 3) and (state.var31 == 0)))
			elif transition == 119:
				return (((state.var35 == 2) and (state.var31 == 0)) or ((state.var35 == 1) and (state.var31 == 0)))
			elif transition == 120:
				return (((state.var35 == 3) and (state.var32 == 0)) or ((state.var35 == 0) and (state.var32 == 0)))
			elif transition == 121:
				return (((state.var35 == 0) and (state.var32 == 0)) or ((state.var35 == 3) and (state.var32 == 0)))
			elif transition == 122:
				return (((state.var35 == 2) and (state.var32 == 0)) or ((state.var35 == 1) and (state.var32 == 0)))
			elif transition == 123:
				return (((state.var35 == 1) and (state.var27 == 0)) or ((state.var35 == 2) and (state.var27 == 0)))
			elif transition == 124:
				return (((state.var35 == 3) and (state.var27 == 0)) or ((state.var35 == 0) and (state.var27 == 0)))
			elif transition == 125:
				return (((state.var35 == 2) and (state.var27 == 0)) or ((state.var35 == 1) and (state.var27 == 0)))
			elif transition == 126:
				return (((state.var35 == 2) and (state.var13 == 0)) or ((state.var35 == 1) and (state.var13 == 0)))
			elif transition == 127:
				return (((state.var35 == 2) and (state.var12 == 0)) or ((state.var35 == 1) and (state.var12 == 0)))
			elif transition == 128:
				return (((state.var35 == 1) and (state.var26 == 0)) or ((state.var35 == 2) and (state.var26 == 0)))
			elif transition == 129:
				return (((state.var35 == 2) and (state.var26 == 0)) or ((state.var35 == 1) and (state.var26 == 0)))
			elif transition == 130:
				return (((state.var35 == 1) and (state.var33 == 0)) or ((state.var35 == 2) and (state.var33 == 0)))
			elif transition == 131:
				return (((state.var35 == 1) and (state.var34 == 0)) or ((state.var35 == 2) and (state.var34 == 0)))
			elif transition == 132:
				return (((state.var35 == 0) and (state.var34 == 0)) or ((state.var35 == 3) and (state.var34 == 0)))
			elif transition == 133:
				return (((state.var35 == 1) and (state.var28 == 0)) or ((state.var35 == 2) and (state.var28 == 0)))
			elif transition == 134:
				return (((state.var35 == 3) and (state.var28 == 0)) or ((state.var35 == 0) and (state.var28 == 0)))
			elif transition == 135:
				return (((state.var35 == 0) and (state.var28 == 0)) or ((state.var35 == 3) and (state.var28 == 0)))
			elif transition == 136:
				return (((state.var35 == 2) and (state.var28 == 0)) or ((state.var35 == 1) and (state.var28 == 0)))
			elif transition == 137:
				return (((state.var35 == 1) and (state.var15 == 0)) or ((state.var35 == 2) and (state.var15 == 0)))
			elif transition == 138:
				return (((state.var35 == 3) and (state.var15 == 0)) or ((state.var35 == 0) and (state.var15 == 0)))
			elif transition == 139:
				return (((state.var35 == 1) and (state.var7 == 0)) or ((state.var35 == 2) and (state.var7 == 0)))
			elif transition == 140:
				return (((state.var35 == 2) and (state.var7 == 0)) or ((state.var35 == 1) and (state.var7 == 0)))
			elif transition == 141:
				return (((state.var35 == 1) and (state.var21 == 0)) or ((state.var35 == 2) and (state.var21 == 0)))
			elif transition == 142:
				return (((state.var35 == 0) and (state.var29 == 0)) or ((state.var35 == 3) and (state.var29 == 0)))
			elif transition == 143:
				return (((state.var35 == 3) and (state.var30 == 0)) or ((state.var35 == 0) and (state.var30 == 0)))
			elif transition == 144:
				return (((state.var35 == 2) and (state.var30 == 0)) or ((state.var35 == 1) and (state.var30 == 0)))
			elif transition == 145:
				return (((state.var35 == 1) and (state.var22 == 0)) or ((state.var35 == 2) and (state.var22 == 0)))
			elif transition == 146:
				return (((state.var35 == 2) and (state.var22 == 0)) or ((state.var35 == 1) and (state.var22 == 0)))
			elif transition == 147:
				return (((state.var35 == 1) and (state.var2 == 0)) or ((state.var35 == 2) and (state.var2 == 0)))
			elif transition == 148:
				return (((state.var35 == 1) and (state.var16 == 0)) or ((state.var35 == 2) and (state.var16 == 0)))
			elif transition == 149:
				return (((state.var35 == 0) and (state.var16 == 0)) or ((state.var35 == 3) and (state.var16 == 0)))
			elif transition == 150:
				return (((state.var35 == 1) and (state.var18 == 0)) or ((state.var35 == 2) and (state.var18 == 0)))
			elif transition == 151:
				return (((state.var35 == 3) and (state.var18 == 0)) or ((state.var35 == 0) and (state.var18 == 0)))
			elif transition == 152:
				return ((state.var35 == 1) and (state.var9 == 0))
			elif transition == 153:
				return ((state.var35 == 2) and (state.var10 == 0))
			elif transition == 154:
				return ((state.var35 == 1) and (state.var19 == 0))
			elif transition == 155:
				return ((state.var35 == 2) and (state.var23 == 0))
			elif transition == 156:
				return ((state.var35 == 0) and (state.var23 == 0))
			elif transition == 157:
				return ((state.var35 == 1) and (state.var20 == 0))
			elif transition == 158:
				return ((state.var35 == 2) and (state.var6 == 0))
			elif transition == 159:
				return ((state.var35 == 0) and (state.var6 == 0))
			elif transition == 160:
				return ((state.var35 == 3) and (state.var31 == 0))
			elif transition == 161:
				return ((state.var35 == 1) and (state.var27 == 0))
			elif transition == 162:
				return ((state.var35 == 3) and (state.var13 == 0))
			elif transition == 163:
				return ((state.var35 == 2) and (state.var13 == 0))
			elif transition == 164:
				return ((state.var35 == 1) and (state.var12 == 0))
			elif transition == 165:
				return ((state.var35 == 2) and (state.var26 == 0))
			elif transition == 166:
				return ((state.var35 == 0) and (state.var34 == 0))
			elif transition == 167:
				return ((state.var35 == 0) and (state.var15 == 0))
			elif transition == 168:
				return ((state.var35 == 1) and (state.var7 == 0))
			elif transition == 169:
				return ((state.var35 == 2) and (state.var21 == 0))
			elif transition == 170:
				return ((state.var35 == 0) and (state.var21 == 0))
			elif transition == 171:
				return ((state.var35 == 3) and (state.var30 == 0))
			elif transition == 172:
				return ((state.var35 == 1) and (state.var30 == 0))
			elif transition == 173:
				return ((state.var35 == 2) and (state.var22 == 0))
			elif transition == 174:
				return ((state.var35 == 3) and (state.var17 == 0))
			elif transition == 175:
				return ((state.var35 == 1) and (state.var2 == 0))
			elif transition == 176:
				return ((state.var35 == 3) and (state.var8 == 0))
			elif transition == 177:
				return ((state.var35 == 2) and (state.var8 == 0))
			elif transition == 178:
				return ((state.var35 == 1) and (state.var8 == 0))
			elif transition == 179:
				return ((state.var35 == 2) and (state.var14 == 0))
			elif transition == 180:
				return ((state.var35 == 1) and (state.var0 == 0))
			elif transition == 181:
				return ((state.var35 == 0) and (state.var0 == 0))
			elif transition == 182:
				return ((state.var35 == 2) and (state.var3 == 0))
			elif transition == 183:
				return ((state.var35 == 0) and (state.var3 == 0))
			elif transition == 184:
				return ((state.var35 == 0) and (state.var9 == 0))
			elif transition == 185:
				return ((state.var35 == 1) and (state.var10 == 0))
			elif transition == 186:
				return ((state.var35 == 2) and (state.var5 == 0))
			elif transition == 187:
				return ((state.var35 == 1) and (state.var5 == 0))
			elif transition == 188:
				return ((state.var35 == 2) and (state.var1 == 0))
			elif transition == 189:
				return ((state.var35 == 0) and (state.var1 == 0))
			elif transition == 190:
				return ((state.var35 == 3) and (state.var4 == 0))
			elif transition == 191:
				return ((state.var35 == 1) and (state.var4 == 0))
			elif transition == 192:
				return ((state.var35 == 3) and (state.var19 == 0))
			elif transition == 193:
				return ((state.var35 == 2) and (state.var19 == 0))
			elif transition == 194:
				return ((state.var35 == 3) and (state.var23 == 0))
			elif transition == 195:
				return ((state.var35 == 1) and (state.var23 == 0))
			elif transition == 196:
				return ((state.var35 == 2) and (state.var24 == 0))
			elif transition == 197:
				return ((state.var35 == 1) and (state.var24 == 0))
			elif transition == 198:
				return ((state.var35 == 2) and (state.var20 == 0))
			elif transition == 199:
				return ((state.var35 == 0) and (state.var20 == 0))
			elif transition == 200:
				return ((state.var35 == 3) and (state.var6 == 0))
			elif transition == 201:
				return ((state.var35 == 1) and (state.var11 == 0))
			elif transition == 202:
				return ((state.var35 == 2) and (state.var25 == 0))
			elif transition == 203:
				return ((state.var35 == 1) and (state.var25 == 0))
			elif transition == 204:
				return ((state.var35 == 0) and (state.var25 == 0))
			elif transition == 205:
				return ((state.var35 == 2) and (state.var31 == 0))
			elif transition == 206:
				return ((state.var35 == 1) and (state.var31 == 0))
			elif transition == 207:
				return ((state.var35 == 0) and (state.var31 == 0))
			elif transition == 208:
				return ((state.var35 == 2) and (state.var32 == 0))
			elif transition == 209:
				return ((state.var35 == 1) and (state.var32 == 0))
			elif transition == 210:
				return ((state.var35 == 0) and (state.var32 == 0))
			elif transition == 211:
				return ((state.var35 == 3) and (state.var27 == 0))
			elif transition == 212:
				return ((state.var35 == 2) and (state.var27 == 0))
			elif transition == 213:
				return ((state.var35 == 0) and (state.var27 == 0))
			elif transition == 214:
				return ((state.var35 == 0) and (state.var13 == 0))
			elif transition == 215:
				return ((state.var35 == 0) and (state.var12 == 0))
			elif transition == 216:
				return ((state.var35 == 3) and (state.var26 == 0))
			elif transition == 217:
				return ((state.var35 == 0) and (state.var26 == 0))
			elif transition == 218:
				return ((state.var35 == 3) and (state.var33 == 0))
			elif transition == 219:
				return ((state.var35 == 3) and (state.var34 == 0))
			elif transition == 220:
				return ((state.var35 == 1) and (state.var34 == 0))
			elif transition == 221:
				return ((state.var35 == 3) and (state.var28 == 0))
			elif transition == 222:
				return ((state.var35 == 2) and (state.var28 == 0))
			elif transition == 223:
				return ((state.var35 == 1) and (state.var28 == 0))
			elif transition == 224:
				return ((state.var35 == 0) and (state.var28 == 0))
			elif transition == 225:
				return ((state.var35 == 3) and (state.var15 == 0))
			elif transition == 226:
				return ((state.var35 == 2) and (state.var15 == 0))
			elif transition == 227:
				return ((state.var35 == 3) and (state.var7 == 0))
			elif transition == 228:
				return ((state.var35 == 0) and (state.var7 == 0))
			elif transition == 229:
				return ((state.var35 == 3) and (state.var21 == 0))
			elif transition == 230:
				return ((state.var35 == 1) and (state.var29 == 0))
			elif transition == 231:
				return ((state.var35 == 2) and (state.var30 == 0))
			elif transition == 232:
				return ((state.var35 == 0) and (state.var30 == 0))
			elif transition == 233:
				return ((state.var35 == 3) and (state.var22 == 0))
			elif transition == 234:
				return ((state.var35 == 0) and (state.var22 == 0))
			elif transition == 235:
				return ((state.var35 == 3) and (state.var2 == 0))
			elif transition == 236:
				return ((state.var35 == 3) and (state.var16 == 0))
			elif transition == 237:
				return ((state.var35 == 1) and (state.var16 == 0))
			elif transition == 238:
				return ((state.var35 == 3) and (state.var18 == 0))
			elif transition == 239:
				return ((state.var35 == 2) and (state.var18 == 0))
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return ((((((((((((((((((state.var0 == 0) or (state.var3 == 0)) or (state.var9 == 0)) or (state.var5 == 0)) or (state.var1 == 0)) or (state.var4 == 0)) or (state.var19 == 0)) or (state.var31 == 0)) or (state.var13 == 0)) or (state.var26 == 0)) or (state.var33 == 0)) or (state.var34 == 0)) or (state.var7 == 0)) or (state.var21 == 0)) or (state.var2 == 0)) or (state.var8 == 0)) or (state.var14 == 0)) or (state.var16 == 0))
			elif transition == 1:
				return ((((((((((state.var10 == 0) or (state.var24 == 0)) or (state.var20 == 0)) or (state.var25 == 0)) or (state.var12 == 0)) or (state.var28 == 0)) or (state.var15 == 0)) or (state.var22 == 0)) or (state.var17 == 0)) or (state.var37 == 0))
			elif transition == 2:
				return ((((((((((((((((((state.var0 == 0) or (state.var3 == 0)) or (state.var9 == 0)) or (state.var5 == 0)) or (state.var1 == 0)) or (state.var4 == 0)) or (state.var19 == 0)) or (state.var31 == 0)) or (state.var13 == 0)) or (state.var26 == 0)) or (state.var33 == 0)) or (state.var34 == 0)) or (state.var7 == 0)) or (state.var21 == 0)) or (state.var2 == 0)) or (state.var8 == 0)) or (state.var14 == 0)) or (state.var16 == 0))
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return ((((((((((((((((((((((((((((((((((((((state.var35 == 0) and (state.var3 == 0)) or ((state.var35 == 0) and (state.var9 == 0))) or ((state.var35 == 0) and (state.var24 == 0))) or ((state.var35 == 0) and (state.var20 == 0))) or ((state.var35 == 0) and (state.var31 == 0))) or ((state.var35 == 0) and (state.var27 == 0))) or ((state.var35 == 0) and (state.var26 == 0))) or ((state.var35 == 0) and (state.var34 == 0))) or ((state.var35 == 0) and (state.var7 == 0))) or ((state.var37 == 0) and (state.var35 == 0))) or ((state.var35 == 1) and (state.var0 == 0))) or ((state.var35 == 1) and (state.var5 == 0))) or ((state.var35 == 1) and (state.var4 == 0))) or ((state.var35 == 1) and (state.var19 == 0))) or ((state.var35 == 1) and (state.var23 == 0))) or ((state.var35 == 1) and (state.var6 == 0))) or ((state.var35 == 1) and (state.var11 == 0))) or ((state.var35 == 1) and (state.var32 == 0))) or ((state.var35 == 1) and (state.var12 == 0))) or ((state.var35 == 1) and (state.var33 == 0))) or ((state.var35 == 1) and (state.var28 == 0))) or ((state.var35 == 1) and (state.var15 == 0))) or ((state.var35 == 1) and (state.var29 == 0))) or ((state.var35 == 1) and (state.var22 == 0))) or ((state.var35 == 1) and (state.var2 == 0))) or ((state.var35 == 1) and (state.var8 == 0))) or ((state.var35 == 1) and (state.var14 == 0))) or ((state.var35 == 3) and (state.var3 == 0))) or ((state.var35 == 3) and (state.var9 == 0))) or ((state.var35 == 3) and (state.var24 == 0))) or ((state.var35 == 3) and (state.var20 == 0))) or ((state.var35 == 3) and (state.var31 == 0))) or ((state.var35 == 3) and (state.var27 == 0))) or ((state.var35 == 3) and (state.var26 == 0))) or ((state.var35 == 3) and (state.var34 == 0))) or ((state.var35 == 3) and (state.var7 == 0))) or ((state.var37 == 0) and (state.var35 == 3)))
			elif transition == 1:
				return (((((((((((((((((((((((((((((((((((((((((((((((((((((((state.var35 == 0) and (state.var0 == 0)) or ((state.var35 == 0) and (state.var5 == 0))) or ((state.var35 == 0) and (state.var4 == 0))) or ((state.var35 == 0) and (state.var19 == 0))) or ((state.var35 == 0) and (state.var23 == 0))) or ((state.var35 == 0) and (state.var6 == 0))) or ((state.var35 == 0) and (state.var11 == 0))) or ((state.var35 == 0) and (state.var32 == 0))) or ((state.var35 == 0) and (state.var12 == 0))) or ((state.var35 == 0) and (state.var33 == 0))) or ((state.var35 == 0) and (state.var28 == 0))) or ((state.var35 == 0) and (state.var15 == 0))) or ((state.var35 == 0) and (state.var29 == 0))) or ((state.var35 == 0) and (state.var22 == 0))) or ((state.var35 == 0) and (state.var2 == 0))) or ((state.var35 == 0) and (state.var8 == 0))) or ((state.var35 == 0) and (state.var14 == 0))) or ((state.var35 == 1) and (state.var3 == 0))) or ((state.var35 == 1) and (state.var9 == 0))) or ((state.var35 == 1) and (state.var24 == 0))) or ((state.var35 == 1) and (state.var20 == 0))) or ((state.var35 == 1) and (state.var31 == 0))) or ((state.var35 == 1) and (state.var27 == 0))) or ((state.var35 == 1) and (state.var26 == 0))) or ((state.var35 == 1) and (state.var34 == 0))) or ((state.var35 == 1) and (state.var7 == 0))) or ((state.var37 == 0) and (state.var35 == 1))) or ((state.var35 == 2) and (state.var3 == 0))) or ((state.var35 == 2) and (state.var9 == 0))) or ((state.var35 == 2) and (state.var24 == 0))) or ((state.var35 == 2) and (state.var20 == 0))) or ((state.var35 == 2) and (state.var31 == 0))) or ((state.var35 == 2) and (state.var27 == 0))) or ((state.var35 == 2) and (state.var26 == 0))) or ((state.var35 == 2) and (state.var34 == 0))) or ((state.var35 == 2) and (state.var7 == 0))) or ((state.var37 == 0) and (state.var35 == 2))) or ((state.var35 == 3) and (state.var0 == 0))) or ((state.var35 == 3) and (state.var5 == 0))) or ((state.var35 == 3) and (state.var4 == 0))) or ((state.var35 == 3) and (state.var19 == 0))) or ((state.var35 == 3) and (state.var23 == 0))) or ((state.var35 == 3) and (state.var6 == 0))) or ((state.var35 == 3) and (state.var11 == 0))) or ((state.var35 == 3) and (state.var32 == 0))) or ((state.var35 == 3) and (state.var12 == 0))) or ((state.var35 == 3) and (state.var33 == 0))) or ((state.var35 == 3) and (state.var28 == 0))) or ((state.var35 == 3) and (state.var15 == 0))) or ((state.var35 == 3) and (state.var29 == 0))) or ((state.var35 == 3) and (state.var22 == 0))) or ((state.var35 == 3) and (state.var2 == 0))) or ((state.var35 == 3) and (state.var8 == 0))) or ((state.var35 == 3) and (state.var14 == 0)))
			elif transition == 2:
				return ((((((((((((((((((state.var35 == 2) and (state.var0 == 0)) or ((state.var35 == 2) and (state.var5 == 0))) or ((state.var35 == 2) and (state.var4 == 0))) or ((state.var35 == 2) and (state.var19 == 0))) or ((state.var35 == 2) and (state.var23 == 0))) or ((state.var35 == 2) and (state.var6 == 0))) or ((state.var35 == 2) and (state.var11 == 0))) or ((state.var35 == 2) and (state.var32 == 0))) or ((state.var35 == 2) and (state.var12 == 0))) or ((state.var35 == 2) and (state.var33 == 0))) or ((state.var35 == 2) and (state.var28 == 0))) or ((state.var35 == 2) and (state.var15 == 0))) or ((state.var35 == 2) and (state.var29 == 0))) or ((state.var35 == 2) and (state.var22 == 0))) or ((state.var35 == 2) and (state.var2 == 0))) or ((state.var35 == 2) and (state.var8 == 0))) or ((state.var35 == 2) and (state.var14 == 0)))
			elif transition == 3:
				return (((((((((state.var10 == 0) or (state.var1 == 0)) or (state.var25 == 0)) or (state.var13 == 0)) or (state.var21 == 0)) or (state.var30 == 0)) or (state.var17 == 0)) or (state.var16 == 0)) or (state.var18 == 0))
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.aut_location
		if location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.aut_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.aut_location
		if location == 0:
			if transition == 0:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 1:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 2:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 3:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 4:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 5:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 6:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 7:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 8:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 9:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 10:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 11:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 12:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 13:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 14:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 15:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 16:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 17:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 18:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 19:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 20:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 21:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 22:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 23:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 24:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 25:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 26:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 27:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 28:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 29:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 30:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 31:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 32:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 33:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 34:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 35:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 36:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 37:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 38:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 39:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 40:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 41:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 42:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 43:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 44:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 45:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 46:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 47:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 48:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 49:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 50:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 51:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 52:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 53:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 54:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 55:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 56:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 57:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 58:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 59:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 60:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 61:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 62:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 63:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 64:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 65:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 66:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 67:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 68:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 69:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 70:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 71:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 72:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 73:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 74:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 75:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 76:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 77:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 78:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 79:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 80:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 81:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 82:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 83:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 84:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 85:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 86:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 87:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 88:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 89:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 90:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 91:
				if branch == 0:
					return (5 / 100)
				elif branch == 1:
					return (95 / 100)
			elif transition == 92:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 93:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 94:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 95:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 96:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 97:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 98:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 99:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 100:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 101:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 102:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 103:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 104:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 105:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 106:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 107:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 108:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 109:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 110:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 111:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 112:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 113:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 114:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 115:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 116:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 117:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 118:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 119:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 120:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 121:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 122:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 123:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 124:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 125:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 126:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 127:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 128:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 129:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 130:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 131:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 132:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 133:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 134:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 135:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 136:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 137:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 138:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 139:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 140:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 141:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 142:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 143:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 144:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 145:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 146:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 147:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 148:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 149:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 150:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 151:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 152:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 153:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 154:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 155:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 156:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 157:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 158:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 159:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 160:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 161:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 162:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 163:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 164:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 165:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 166:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 167:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 168:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 169:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 170:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 171:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 172:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 173:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 174:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 175:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 176:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 177:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 178:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 179:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 180:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 181:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 182:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 183:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 184:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 185:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 186:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 187:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 188:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 189:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 190:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 191:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 192:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 193:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 194:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 195:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 196:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 197:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 198:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 199:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 200:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 201:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 202:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 203:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 204:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 205:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 206:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 207:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 208:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 209:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 210:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 211:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 212:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 213:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 214:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 215:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 216:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 217:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 218:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 219:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 220:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 221:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 222:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 223:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 224:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 225:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 226:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 227:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 228:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 229:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 230:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 231:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 232:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 233:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 234:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 235:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 236:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 237:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 238:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			elif transition == 239:
				if branch == 0:
					return (2 / 100)
				elif branch == 1:
					return (98 / 100)
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				if branch == 0:
					return (1 / 1000)
				elif branch == 1:
					return (99 / 1000)
				elif branch == 2:
					return (9 / 1000)
				elif branch == 3:
					return (891 / 1000)
			elif transition == 1:
				if branch == 0:
					return (2 / 1000)
				elif branch == 1:
					return (198 / 1000)
				elif branch == 2:
					return (8 / 1000)
				elif branch == 3:
					return (792 / 1000)
			elif transition == 2:
				if branch == 0:
					return (5 / 1000)
				elif branch == 1:
					return (495 / 1000)
				elif branch == 2:
					return (5 / 1000)
				elif branch == 3:
					return (495 / 1000)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			elif transition == 1:
				if branch == 0:
					return (1 / 10)
				elif branch == 1:
					return (9 / 10)
			elif transition == 2:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			elif transition == 3:
				if True:
					return (5 / 10)
			else:
				raise IndexError
		elif location == 3:
			raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.aut_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.var9 = 1
						target_state.var10 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var9 = 1
						target_state.var10 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.var9 = 0
						target_state.var10 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var9 = 0
						target_state.var10 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.var19 = 1
						target_state.var23 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var19 = 1
						target_state.var23 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 3:
					if branch == 0:
						target_state.var19 = 0
						target_state.var23 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var19 = 0
						target_state.var23 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 4:
					if branch == 0:
						target_state.var23 = 1
						target_state.var31 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var23 = 1
						target_state.var31 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 5:
					if branch == 0:
						target_state.var6 = 0
						target_state.var20 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var6 = 0
						target_state.var20 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 6:
					if branch == 0:
						target_state.var6 = 1
						target_state.var20 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var6 = 1
						target_state.var20 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 7:
					if branch == 0:
						target_state.var6 = 1
						target_state.var13 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var6 = 1
						target_state.var13 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 8:
					if branch == 0:
						target_state.var23 = 0
						target_state.var31 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var23 = 0
						target_state.var31 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 9:
					if branch == 0:
						target_state.var13 = 0
						target_state.var27 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var13 = 0
						target_state.var27 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 10:
					if branch == 0:
						target_state.var6 = 0
						target_state.var13 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var6 = 0
						target_state.var13 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 11:
					if branch == 0:
						target_state.var13 = 1
						target_state.var27 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var13 = 1
						target_state.var27 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 12:
					if branch == 0:
						target_state.var12 = 1
						target_state.var26 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var12 = 1
						target_state.var26 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 13:
					if branch == 0:
						target_state.var12 = 0
						target_state.var26 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var12 = 0
						target_state.var26 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 14:
					if branch == 0:
						target_state.var30 = 0
						target_state.var34 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var30 = 0
						target_state.var34 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 15:
					if branch == 0:
						target_state.var15 = 1
						target_state.var17 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var15 = 1
						target_state.var17 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 16:
					if branch == 0:
						target_state.var7 = 1
						target_state.var21 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var7 = 1
						target_state.var21 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 17:
					if branch == 0:
						target_state.var7 = 0
						target_state.var21 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var7 = 0
						target_state.var21 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 18:
					if branch == 0:
						target_state.var8 = 0
						target_state.var21 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var8 = 0
						target_state.var21 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 19:
					if branch == 0:
						target_state.var30 = 1
						target_state.var34 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var30 = 1
						target_state.var34 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 20:
					if branch == 0:
						target_state.var22 = 0
						target_state.var30 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var22 = 0
						target_state.var30 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 21:
					if branch == 0:
						target_state.var22 = 1
						target_state.var30 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var22 = 1
						target_state.var30 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 22:
					if branch == 0:
						target_state.var15 = 0
						target_state.var17 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var15 = 0
						target_state.var17 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 23:
					if branch == 0:
						target_state.var2 = 1
						target_state.var8 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var2 = 1
						target_state.var8 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 24:
					if branch == 0:
						target_state.var8 = 1
						target_state.var21 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var8 = 1
						target_state.var21 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 25:
					if branch == 0:
						target_state.var2 = 0
						target_state.var8 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var2 = 0
						target_state.var8 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 26:
					if branch == 0:
						target_state.var8 = 1
						target_state.var14 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var8 = 1
						target_state.var14 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 27:
					if branch == 0:
						target_state.var8 = 0
						target_state.var14 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var8 = 0
						target_state.var14 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 28:
					if branch == 0:
						target_state.var3 = 1
						target_state.var9 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var3 = 1
						target_state.var9 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 29:
					if branch == 0:
						target_state.var3 = 0
						target_state.var9 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var3 = 0
						target_state.var9 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 30:
					if branch == 0:
						target_state.var10 = 1
						target_state.var24 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var10 = 1
						target_state.var24 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 31:
					if branch == 0:
						target_state.var5 = 1
						target_state.var20 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var5 = 1
						target_state.var20 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 32:
					if branch == 0:
						target_state.var4 = 1
						target_state.var11 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var4 = 1
						target_state.var11 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 33:
					if branch == 0:
						target_state.var19 = 1
						target_state.var25 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var19 = 1
						target_state.var25 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 34:
					if branch == 0:
						target_state.var10 = 0
						target_state.var24 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var10 = 0
						target_state.var24 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 35:
					if branch == 0:
						target_state.var24 = 1
						target_state.var32 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var24 = 1
						target_state.var32 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 36:
					if branch == 0:
						target_state.var5 = 0
						target_state.var20 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var5 = 0
						target_state.var20 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 37:
					if branch == 0:
						target_state.var4 = 0
						target_state.var11 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var4 = 0
						target_state.var11 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 38:
					if branch == 0:
						target_state.var11 = 1
						target_state.var12 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var11 = 1
						target_state.var12 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 39:
					if branch == 0:
						target_state.var19 = 0
						target_state.var25 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var19 = 0
						target_state.var25 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 40:
					if branch == 0:
						target_state.var24 = 0
						target_state.var32 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var24 = 0
						target_state.var32 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 41:
					if branch == 0:
						target_state.var11 = 0
						target_state.var12 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var11 = 0
						target_state.var12 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 42:
					if branch == 0:
						target_state.var26 = 1
						target_state.var33 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var26 = 1
						target_state.var33 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 43:
					if branch == 0:
						target_state.var26 = 0
						target_state.var33 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var26 = 0
						target_state.var33 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 44:
					if branch == 0:
						target_state.var33 = 1
						target_state.var34 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var33 = 1
						target_state.var34 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 45:
					if branch == 0:
						target_state.var29 = 0
						target_state.var33 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var29 = 0
						target_state.var33 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 46:
					if branch == 0:
						target_state.var33 = 0
						target_state.var34 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var33 = 0
						target_state.var34 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 47:
					if branch == 0:
						target_state.var21 = 1
						target_state.var29 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var21 = 1
						target_state.var29 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 48:
					if branch == 0:
						target_state.var29 = 1
						target_state.var33 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var29 = 1
						target_state.var33 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 49:
					if branch == 0:
						target_state.var21 = 0
						target_state.var29 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var21 = 0
						target_state.var29 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 50:
					if branch == 0:
						target_state.var14 = 0
						target_state.var29 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var14 = 0
						target_state.var29 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 51:
					if branch == 0:
						target_state.var17 = 0
						target_state.var22 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var17 = 0
						target_state.var22 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 52:
					if branch == 0:
						target_state.var17 = 1
						target_state.var22 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var17 = 1
						target_state.var22 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 53:
					if branch == 0:
						target_state.var17 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var37 = 0
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var17 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var37 = 0
						target_state.aut_location = 2
				elif transition == 54:
					if branch == 0:
						target_state.var14 = 1
						target_state.var29 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var14 = 1
						target_state.var29 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 55:
					if branch == 0:
						target_state.var14 = 1
						target_state.var16 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var14 = 1
						target_state.var16 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 56:
					if branch == 0:
						target_state.var14 = 0
						target_state.var16 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var14 = 0
						target_state.var16 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 57:
					if branch == 0:
						target_state.var18 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var37 = 0
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var18 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var37 = 0
						target_state.aut_location = 2
				elif transition == 58:
					if branch == 0:
						target_state.var17 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var37 = 1
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var17 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var37 = 1
						target_state.aut_location = 2
				elif transition == 59:
					if branch == 0:
						target_state.var18 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var37 = 1
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var18 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var37 = 1
						target_state.aut_location = 2
				elif transition == 60:
					if branch == 0:
						target_state.var3 = 1
						target_state.var9 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var3 = 1
						target_state.var9 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 61:
					if branch == 0:
						target_state.var3 = 0
						target_state.var9 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var3 = 0
						target_state.var9 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 62:
					if branch == 0:
						target_state.var10 = 1
						target_state.var24 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var10 = 1
						target_state.var24 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 63:
					if branch == 0:
						target_state.var5 = 1
						target_state.var20 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var5 = 1
						target_state.var20 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 64:
					if branch == 0:
						target_state.var4 = 1
						target_state.var11 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var4 = 1
						target_state.var11 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 65:
					if branch == 0:
						target_state.var19 = 1
						target_state.var25 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var19 = 1
						target_state.var25 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 66:
					if branch == 0:
						target_state.var10 = 0
						target_state.var24 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var10 = 0
						target_state.var24 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 67:
					if branch == 0:
						target_state.var24 = 1
						target_state.var32 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var24 = 1
						target_state.var32 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 68:
					if branch == 0:
						target_state.var5 = 0
						target_state.var20 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var5 = 0
						target_state.var20 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 69:
					if branch == 0:
						target_state.var4 = 0
						target_state.var11 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var4 = 0
						target_state.var11 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 70:
					if branch == 0:
						target_state.var11 = 1
						target_state.var12 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var11 = 1
						target_state.var12 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 71:
					if branch == 0:
						target_state.var19 = 0
						target_state.var25 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var19 = 0
						target_state.var25 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 72:
					if branch == 0:
						target_state.var24 = 0
						target_state.var32 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var24 = 0
						target_state.var32 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 73:
					if branch == 0:
						target_state.var11 = 0
						target_state.var12 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var11 = 0
						target_state.var12 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 74:
					if branch == 0:
						target_state.var26 = 1
						target_state.var33 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var26 = 1
						target_state.var33 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 75:
					if branch == 0:
						target_state.var26 = 0
						target_state.var33 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var26 = 0
						target_state.var33 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 76:
					if branch == 0:
						target_state.var33 = 1
						target_state.var34 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var33 = 1
						target_state.var34 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 77:
					if branch == 0:
						target_state.var29 = 0
						target_state.var33 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var29 = 0
						target_state.var33 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 78:
					if branch == 0:
						target_state.var33 = 0
						target_state.var34 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var33 = 0
						target_state.var34 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 79:
					if branch == 0:
						target_state.var21 = 1
						target_state.var29 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var21 = 1
						target_state.var29 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 80:
					if branch == 0:
						target_state.var29 = 1
						target_state.var33 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var29 = 1
						target_state.var33 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 81:
					if branch == 0:
						target_state.var21 = 0
						target_state.var29 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var21 = 0
						target_state.var29 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 82:
					if branch == 0:
						target_state.var14 = 0
						target_state.var29 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var14 = 0
						target_state.var29 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 83:
					if branch == 0:
						target_state.var17 = 0
						target_state.var22 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var17 = 0
						target_state.var22 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 84:
					if branch == 0:
						target_state.var17 = 1
						target_state.var22 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var17 = 1
						target_state.var22 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 85:
					if branch == 0:
						target_state.var17 = 1
						target_state.var36 = 2
						target_state.var37 = 0
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var17 = 1
						target_state.var36 = 2
						target_state.var37 = 0
						target_state.aut_location = 2
				elif transition == 86:
					if branch == 0:
						target_state.var14 = 1
						target_state.var29 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var14 = 1
						target_state.var29 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 87:
					if branch == 0:
						target_state.var14 = 1
						target_state.var16 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var14 = 1
						target_state.var16 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 88:
					if branch == 0:
						target_state.var14 = 0
						target_state.var16 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var14 = 0
						target_state.var16 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 89:
					if branch == 0:
						target_state.var18 = 1
						target_state.var36 = 2
						target_state.var37 = 0
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var18 = 1
						target_state.var36 = 2
						target_state.var37 = 0
						target_state.aut_location = 2
				elif transition == 90:
					if branch == 0:
						target_state.var17 = 0
						target_state.var36 = 2
						target_state.var37 = 1
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var17 = 0
						target_state.var36 = 2
						target_state.var37 = 1
						target_state.aut_location = 2
				elif transition == 91:
					if branch == 0:
						target_state.var18 = 0
						target_state.var36 = 2
						target_state.var37 = 1
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var18 = 0
						target_state.var36 = 2
						target_state.var37 = 1
						target_state.aut_location = 2
				elif transition == 92:
					if branch == 0:
						target_state.var0 = 1
						target_state.var3 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 1
						target_state.var3 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 93:
					if branch == 0:
						target_state.var0 = 1
						target_state.var4 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 1
						target_state.var4 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 94:
					if branch == 0:
						target_state.var0 = 0
						target_state.var3 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.var3 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 95:
					if branch == 0:
						target_state.var3 = 1
						target_state.var19 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var3 = 1
						target_state.var19 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 96:
					if branch == 0:
						target_state.var9 = 1
						target_state.var23 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var9 = 1
						target_state.var23 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 97:
					if branch == 0:
						target_state.var5 = 0
						target_state.var10 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var5 = 0
						target_state.var10 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 98:
					if branch == 0:
						target_state.var5 = 1
						target_state.var10 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var5 = 1
						target_state.var10 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 99:
					if branch == 0:
						target_state.var1 = 0
						target_state.var5 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var1 = 0
						target_state.var5 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 100:
					if branch == 0:
						target_state.var1 = 1
						target_state.var5 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var1 = 1
						target_state.var5 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 101:
					if branch == 0:
						target_state.var1 = 1
						target_state.var6 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var1 = 1
						target_state.var6 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 102:
					if branch == 0:
						target_state.var0 = 0
						target_state.var4 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.var4 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 103:
					if branch == 0:
						target_state.var4 = 1
						target_state.var19 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var4 = 1
						target_state.var19 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 104:
					if branch == 0:
						target_state.var3 = 0
						target_state.var19 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var3 = 0
						target_state.var19 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 105:
					if branch == 0:
						target_state.var4 = 0
						target_state.var19 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var4 = 0
						target_state.var19 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 106:
					if branch == 0:
						target_state.var9 = 0
						target_state.var23 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var9 = 0
						target_state.var23 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 107:
					if branch == 0:
						target_state.var23 = 1
						target_state.var24 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var23 = 1
						target_state.var24 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 108:
					if branch == 0:
						target_state.var23 = 0
						target_state.var24 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var23 = 0
						target_state.var24 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 109:
					if branch == 0:
						target_state.var20 = 0
						target_state.var24 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var20 = 0
						target_state.var24 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 110:
					if branch == 0:
						target_state.var20 = 1
						target_state.var24 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var20 = 1
						target_state.var24 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 111:
					if branch == 0:
						target_state.var20 = 1
						target_state.var27 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var20 = 1
						target_state.var27 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 112:
					if branch == 0:
						target_state.var1 = 0
						target_state.var6 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var1 = 0
						target_state.var6 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 113:
					if branch == 0:
						target_state.var11 = 1
						target_state.var25 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var11 = 1
						target_state.var25 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 114:
					if branch == 0:
						target_state.var11 = 0
						target_state.var25 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var11 = 0
						target_state.var25 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 115:
					if branch == 0:
						target_state.var25 = 1
						target_state.var31 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var25 = 1
						target_state.var31 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 116:
					if branch == 0:
						target_state.var25 = 1
						target_state.var26 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var25 = 1
						target_state.var26 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 117:
					if branch == 0:
						target_state.var25 = 0
						target_state.var31 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var25 = 0
						target_state.var31 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 118:
					if branch == 0:
						target_state.var31 = 1
						target_state.var32 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var31 = 1
						target_state.var32 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 119:
					if branch == 0:
						target_state.var31 = 1
						target_state.var33 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var31 = 1
						target_state.var33 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 120:
					if branch == 0:
						target_state.var31 = 0
						target_state.var32 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var31 = 0
						target_state.var32 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 121:
					if branch == 0:
						target_state.var27 = 0
						target_state.var32 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var27 = 0
						target_state.var32 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 122:
					if branch == 0:
						target_state.var32 = 1
						target_state.var34 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var32 = 1
						target_state.var34 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 123:
					if branch == 0:
						target_state.var20 = 0
						target_state.var27 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var20 = 0
						target_state.var27 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 124:
					if branch == 0:
						target_state.var27 = 1
						target_state.var32 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var27 = 1
						target_state.var32 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 125:
					if branch == 0:
						target_state.var27 = 1
						target_state.var28 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var27 = 1
						target_state.var28 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 126:
					if branch == 0:
						target_state.var13 = 1
						target_state.var15 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var13 = 1
						target_state.var15 = 0
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 127:
					if branch == 0:
						target_state.var7 = 0
						target_state.var12 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var7 = 0
						target_state.var12 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 128:
					if branch == 0:
						target_state.var25 = 0
						target_state.var26 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var25 = 0
						target_state.var26 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 129:
					if branch == 0:
						target_state.var21 = 0
						target_state.var26 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var21 = 0
						target_state.var26 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 130:
					if branch == 0:
						target_state.var31 = 0
						target_state.var33 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var31 = 0
						target_state.var33 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 131:
					if branch == 0:
						target_state.var32 = 0
						target_state.var34 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var32 = 0
						target_state.var34 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 132:
					if branch == 0:
						target_state.var28 = 0
						target_state.var34 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var28 = 0
						target_state.var34 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 133:
					if branch == 0:
						target_state.var27 = 0
						target_state.var28 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var27 = 0
						target_state.var28 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 134:
					if branch == 0:
						target_state.var28 = 1
						target_state.var34 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var28 = 1
						target_state.var34 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 135:
					if branch == 0:
						target_state.var15 = 0
						target_state.var28 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var15 = 0
						target_state.var28 = 1
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 136:
					if branch == 0:
						target_state.var22 = 0
						target_state.var28 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var22 = 0
						target_state.var28 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 137:
					if branch == 0:
						target_state.var13 = 0
						target_state.var15 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var13 = 0
						target_state.var15 = 1
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 138:
					if branch == 0:
						target_state.var15 = 1
						target_state.var28 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var15 = 1
						target_state.var28 = 0
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 139:
					if branch == 0:
						target_state.var7 = 1
						target_state.var12 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var7 = 1
						target_state.var12 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 140:
					if branch == 0:
						target_state.var2 = 0
						target_state.var7 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var2 = 0
						target_state.var7 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 141:
					if branch == 0:
						target_state.var21 = 1
						target_state.var26 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var21 = 1
						target_state.var26 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 142:
					if branch == 0:
						target_state.var29 = 1
						target_state.var30 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var29 = 1
						target_state.var30 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 143:
					if branch == 0:
						target_state.var29 = 0
						target_state.var30 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var29 = 0
						target_state.var30 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 144:
					if branch == 0:
						target_state.var16 = 0
						target_state.var30 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var16 = 0
						target_state.var30 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 145:
					if branch == 0:
						target_state.var22 = 1
						target_state.var28 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var22 = 1
						target_state.var28 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 146:
					if branch == 0:
						target_state.var18 = 0
						target_state.var22 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var18 = 0
						target_state.var22 = 1
						target_state.var35 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 147:
					if branch == 0:
						target_state.var2 = 1
						target_state.var7 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var2 = 1
						target_state.var7 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 148:
					if branch == 0:
						target_state.var16 = 1
						target_state.var30 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var16 = 1
						target_state.var30 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 149:
					if branch == 0:
						target_state.var16 = 1
						target_state.var18 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var16 = 1
						target_state.var18 = 0
						target_state.var35 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 150:
					if branch == 0:
						target_state.var18 = 1
						target_state.var22 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var18 = 1
						target_state.var22 = 0
						target_state.var35 = 3
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 151:
					if branch == 0:
						target_state.var16 = 0
						target_state.var18 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var16 = 0
						target_state.var18 = 1
						target_state.var35 = 2
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 152:
					if branch == 0:
						target_state.var9 = 1
						target_state.var10 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var9 = 1
						target_state.var10 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 153:
					if branch == 0:
						target_state.var9 = 0
						target_state.var10 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var9 = 0
						target_state.var10 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 154:
					if branch == 0:
						target_state.var19 = 1
						target_state.var23 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var19 = 1
						target_state.var23 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 155:
					if branch == 0:
						target_state.var19 = 0
						target_state.var23 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var19 = 0
						target_state.var23 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 156:
					if branch == 0:
						target_state.var23 = 1
						target_state.var31 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var23 = 1
						target_state.var31 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 157:
					if branch == 0:
						target_state.var6 = 0
						target_state.var20 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var6 = 0
						target_state.var20 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 158:
					if branch == 0:
						target_state.var6 = 1
						target_state.var20 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var6 = 1
						target_state.var20 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 159:
					if branch == 0:
						target_state.var6 = 1
						target_state.var13 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var6 = 1
						target_state.var13 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 160:
					if branch == 0:
						target_state.var23 = 0
						target_state.var31 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var23 = 0
						target_state.var31 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 161:
					if branch == 0:
						target_state.var13 = 0
						target_state.var27 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var13 = 0
						target_state.var27 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 162:
					if branch == 0:
						target_state.var6 = 0
						target_state.var13 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var6 = 0
						target_state.var13 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 163:
					if branch == 0:
						target_state.var13 = 1
						target_state.var27 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var13 = 1
						target_state.var27 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 164:
					if branch == 0:
						target_state.var12 = 1
						target_state.var26 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var12 = 1
						target_state.var26 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 165:
					if branch == 0:
						target_state.var12 = 0
						target_state.var26 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var12 = 0
						target_state.var26 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 166:
					if branch == 0:
						target_state.var30 = 0
						target_state.var34 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var30 = 0
						target_state.var34 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 167:
					if branch == 0:
						target_state.var15 = 1
						target_state.var17 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var15 = 1
						target_state.var17 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 168:
					if branch == 0:
						target_state.var7 = 1
						target_state.var21 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var7 = 1
						target_state.var21 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 169:
					if branch == 0:
						target_state.var7 = 0
						target_state.var21 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var7 = 0
						target_state.var21 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 170:
					if branch == 0:
						target_state.var8 = 0
						target_state.var21 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var8 = 0
						target_state.var21 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 171:
					if branch == 0:
						target_state.var30 = 1
						target_state.var34 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var30 = 1
						target_state.var34 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 172:
					if branch == 0:
						target_state.var22 = 0
						target_state.var30 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var22 = 0
						target_state.var30 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 173:
					if branch == 0:
						target_state.var22 = 1
						target_state.var30 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var22 = 1
						target_state.var30 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 174:
					if branch == 0:
						target_state.var15 = 0
						target_state.var17 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var15 = 0
						target_state.var17 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 175:
					if branch == 0:
						target_state.var2 = 1
						target_state.var8 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var2 = 1
						target_state.var8 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 176:
					if branch == 0:
						target_state.var8 = 1
						target_state.var21 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var8 = 1
						target_state.var21 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 177:
					if branch == 0:
						target_state.var2 = 0
						target_state.var8 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var2 = 0
						target_state.var8 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 178:
					if branch == 0:
						target_state.var8 = 1
						target_state.var14 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var8 = 1
						target_state.var14 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 179:
					if branch == 0:
						target_state.var8 = 0
						target_state.var14 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var8 = 0
						target_state.var14 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 180:
					if branch == 0:
						target_state.var0 = 1
						target_state.var3 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 1
						target_state.var3 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 181:
					if branch == 0:
						target_state.var0 = 1
						target_state.var4 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 1
						target_state.var4 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 182:
					if branch == 0:
						target_state.var0 = 0
						target_state.var3 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.var3 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 183:
					if branch == 0:
						target_state.var3 = 1
						target_state.var19 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var3 = 1
						target_state.var19 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 184:
					if branch == 0:
						target_state.var9 = 1
						target_state.var23 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var9 = 1
						target_state.var23 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 185:
					if branch == 0:
						target_state.var5 = 0
						target_state.var10 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var5 = 0
						target_state.var10 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 186:
					if branch == 0:
						target_state.var5 = 1
						target_state.var10 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var5 = 1
						target_state.var10 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 187:
					if branch == 0:
						target_state.var1 = 0
						target_state.var5 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var1 = 0
						target_state.var5 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 188:
					if branch == 0:
						target_state.var1 = 1
						target_state.var5 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var1 = 1
						target_state.var5 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 189:
					if branch == 0:
						target_state.var1 = 1
						target_state.var6 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var1 = 1
						target_state.var6 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 190:
					if branch == 0:
						target_state.var0 = 0
						target_state.var4 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var0 = 0
						target_state.var4 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 191:
					if branch == 0:
						target_state.var4 = 1
						target_state.var19 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var4 = 1
						target_state.var19 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 192:
					if branch == 0:
						target_state.var3 = 0
						target_state.var19 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var3 = 0
						target_state.var19 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 193:
					if branch == 0:
						target_state.var4 = 0
						target_state.var19 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var4 = 0
						target_state.var19 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 194:
					if branch == 0:
						target_state.var9 = 0
						target_state.var23 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var9 = 0
						target_state.var23 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 195:
					if branch == 0:
						target_state.var23 = 1
						target_state.var24 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var23 = 1
						target_state.var24 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 196:
					if branch == 0:
						target_state.var23 = 0
						target_state.var24 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var23 = 0
						target_state.var24 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 197:
					if branch == 0:
						target_state.var20 = 0
						target_state.var24 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var20 = 0
						target_state.var24 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 198:
					if branch == 0:
						target_state.var20 = 1
						target_state.var24 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var20 = 1
						target_state.var24 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 199:
					if branch == 0:
						target_state.var20 = 1
						target_state.var27 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var20 = 1
						target_state.var27 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 200:
					if branch == 0:
						target_state.var1 = 0
						target_state.var6 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var1 = 0
						target_state.var6 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 201:
					if branch == 0:
						target_state.var11 = 1
						target_state.var25 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var11 = 1
						target_state.var25 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 202:
					if branch == 0:
						target_state.var11 = 0
						target_state.var25 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var11 = 0
						target_state.var25 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 203:
					if branch == 0:
						target_state.var25 = 1
						target_state.var31 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var25 = 1
						target_state.var31 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 204:
					if branch == 0:
						target_state.var25 = 1
						target_state.var26 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var25 = 1
						target_state.var26 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 205:
					if branch == 0:
						target_state.var25 = 0
						target_state.var31 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var25 = 0
						target_state.var31 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 206:
					if branch == 0:
						target_state.var31 = 1
						target_state.var32 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var31 = 1
						target_state.var32 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 207:
					if branch == 0:
						target_state.var31 = 1
						target_state.var33 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var31 = 1
						target_state.var33 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 208:
					if branch == 0:
						target_state.var31 = 0
						target_state.var32 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var31 = 0
						target_state.var32 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 209:
					if branch == 0:
						target_state.var27 = 0
						target_state.var32 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var27 = 0
						target_state.var32 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 210:
					if branch == 0:
						target_state.var32 = 1
						target_state.var34 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var32 = 1
						target_state.var34 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 211:
					if branch == 0:
						target_state.var20 = 0
						target_state.var27 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var20 = 0
						target_state.var27 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 212:
					if branch == 0:
						target_state.var27 = 1
						target_state.var32 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var27 = 1
						target_state.var32 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 213:
					if branch == 0:
						target_state.var27 = 1
						target_state.var28 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var27 = 1
						target_state.var28 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 214:
					if branch == 0:
						target_state.var13 = 1
						target_state.var15 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var13 = 1
						target_state.var15 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 215:
					if branch == 0:
						target_state.var7 = 0
						target_state.var12 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var7 = 0
						target_state.var12 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 216:
					if branch == 0:
						target_state.var25 = 0
						target_state.var26 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var25 = 0
						target_state.var26 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 217:
					if branch == 0:
						target_state.var21 = 0
						target_state.var26 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var21 = 0
						target_state.var26 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 218:
					if branch == 0:
						target_state.var31 = 0
						target_state.var33 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var31 = 0
						target_state.var33 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 219:
					if branch == 0:
						target_state.var32 = 0
						target_state.var34 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var32 = 0
						target_state.var34 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 220:
					if branch == 0:
						target_state.var28 = 0
						target_state.var34 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var28 = 0
						target_state.var34 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 221:
					if branch == 0:
						target_state.var27 = 0
						target_state.var28 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var27 = 0
						target_state.var28 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 222:
					if branch == 0:
						target_state.var28 = 1
						target_state.var34 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var28 = 1
						target_state.var34 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 223:
					if branch == 0:
						target_state.var15 = 0
						target_state.var28 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var15 = 0
						target_state.var28 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 224:
					if branch == 0:
						target_state.var22 = 0
						target_state.var28 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var22 = 0
						target_state.var28 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 225:
					if branch == 0:
						target_state.var13 = 0
						target_state.var15 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var13 = 0
						target_state.var15 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 226:
					if branch == 0:
						target_state.var15 = 1
						target_state.var28 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var15 = 1
						target_state.var28 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 227:
					if branch == 0:
						target_state.var7 = 1
						target_state.var12 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var7 = 1
						target_state.var12 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 228:
					if branch == 0:
						target_state.var2 = 0
						target_state.var7 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var2 = 0
						target_state.var7 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 229:
					if branch == 0:
						target_state.var21 = 1
						target_state.var26 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var21 = 1
						target_state.var26 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 230:
					if branch == 0:
						target_state.var29 = 1
						target_state.var30 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var29 = 1
						target_state.var30 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 231:
					if branch == 0:
						target_state.var29 = 0
						target_state.var30 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var29 = 0
						target_state.var30 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 232:
					if branch == 0:
						target_state.var16 = 0
						target_state.var30 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var16 = 0
						target_state.var30 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 233:
					if branch == 0:
						target_state.var22 = 1
						target_state.var28 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var22 = 1
						target_state.var28 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 234:
					if branch == 0:
						target_state.var18 = 0
						target_state.var22 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var18 = 0
						target_state.var22 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 235:
					if branch == 0:
						target_state.var2 = 1
						target_state.var7 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var2 = 1
						target_state.var7 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 236:
					if branch == 0:
						target_state.var16 = 1
						target_state.var30 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var16 = 1
						target_state.var30 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 237:
					if branch == 0:
						target_state.var16 = 1
						target_state.var18 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var16 = 1
						target_state.var18 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 238:
					if branch == 0:
						target_state.var18 = 1
						target_state.var22 = 0
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var18 = 1
						target_state.var22 = 0
						target_state.var36 = 2
						target_state.aut_location = 2
				elif transition == 239:
					if branch == 0:
						target_state.var16 = 0
						target_state.var18 = 1
						target_state.var36 = 2
						target_state.var38 = 1
						target_state.aut_location = 2
					elif branch == 1:
						target_state.var16 = 0
						target_state.var18 = 1
						target_state.var36 = 2
						target_state.aut_location = 2
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.var36 = 0
						target_state.var38 = 1
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var36 = 0
						target_state.aut_location = 0
					elif branch == 2:
						target_state.var38 = 1
						target_state.aut_location = 1
					elif branch == 3:
						target_state.aut_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.var36 = 0
						target_state.var38 = 1
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var36 = 0
						target_state.aut_location = 0
					elif branch == 2:
						target_state.var38 = 1
						target_state.aut_location = 1
					elif branch == 3:
						target_state.aut_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.var36 = 0
						target_state.var38 = 1
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var36 = 0
						target_state.aut_location = 0
					elif branch == 2:
						target_state.var38 = 1
						target_state.aut_location = 1
					elif branch == 3:
						target_state.aut_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.var36 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var36 = 1
						target_state.aut_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.var36 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var36 = 1
						target_state.aut_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.var36 = 3
						target_state.aut_location = 3
					elif branch == 1:
						target_state.var36 = 1
						target_state.aut_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.var36 = 0
						target_state.aut_location = 0
					elif branch == 1:
						target_state.var36 = 1
						target_state.aut_location = 1

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
			VariableInfo("var11", None, "int", 0, 2),
			VariableInfo("var12", None, "int", 0, 2),
			VariableInfo("var13", None, "int", 0, 2),
			VariableInfo("var14", None, "int", 0, 2),
			VariableInfo("var15", None, "int", 0, 2),
			VariableInfo("var16", None, "int", 0, 2),
			VariableInfo("var17", None, "int", 0, 2),
			VariableInfo("var18", None, "int", 0, 2),
			VariableInfo("var19", None, "int", 0, 2),
			VariableInfo("var20", None, "int", 0, 2),
			VariableInfo("var21", None, "int", 0, 2),
			VariableInfo("var22", None, "int", 0, 2),
			VariableInfo("var23", None, "int", 0, 2),
			VariableInfo("var24", None, "int", 0, 2),
			VariableInfo("var25", None, "int", 0, 2),
			VariableInfo("var26", None, "int", 0, 2),
			VariableInfo("var27", None, "int", 0, 2),
			VariableInfo("var28", None, "int", 0, 2),
			VariableInfo("var29", None, "int", 0, 2),
			VariableInfo("var30", None, "int", 0, 2),
			VariableInfo("var31", None, "int", 0, 2),
			VariableInfo("var32", None, "int", 0, 2),
			VariableInfo("var33", None, "int", 0, 2),
			VariableInfo("var34", None, "int", 0, 2),
			VariableInfo("var35", None, "int", 0, 4),
			VariableInfo("var36", None, "int", 0, 4),
			VariableInfo("var37", None, "int", 0, 2),
			VariableInfo("var38", None, "int", 0, 2),
			VariableInfo("aut_location", 0, "int", 0, 3)
		]
		self._aut_aut = autAutomaton(self)
		self.components = [self._aut_aut]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.var0 = 0
		state.var1 = 1
		state.var2 = 1
		state.var3 = 1
		state.var4 = 1
		state.var5 = 1
		state.var6 = 1
		state.var7 = 1
		state.var8 = 1
		state.var9 = 1
		state.var10 = 1
		state.var11 = 1
		state.var12 = 1
		state.var13 = 1
		state.var14 = 1
		state.var15 = 1
		state.var16 = 1
		state.var17 = 1
		state.var18 = 1
		state.var19 = 1
		state.var20 = 1
		state.var21 = 1
		state.var22 = 1
		state.var23 = 1
		state.var24 = 1
		state.var25 = 1
		state.var26 = 1
		state.var27 = 1
		state.var28 = 1
		state.var29 = 1
		state.var30 = 1
		state.var31 = 1
		state.var32 = 1
		state.var33 = 1
		state.var34 = 1
		state.var35 = 1
		state.var36 = 2
		state.var37 = 1
		state.var38 = 0
		self._aut_aut.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_aut.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return ((state.var38 == 0) and (state.var37 == 0))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return ((state.var38 == 0) and (state.var37 == 0))
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
