# echoring

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
	__slots__ = ("msg_sender", "msg_receiver", "msg_type", "msg_ring", "deliverClock", "failed", "is_offline_1", "is_offline_2", "is_offline_3", "iter", "c", "Station_location", "is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1", "rcvTokenFrom_retries_1_errmode_1", "receives_currentlySending", "stationClock_retries", "safe_initToken", "errmode_rcvTokenFrom_1", "cRcvInt", "ring", "Station_1_location", "initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1", "rcvTokenFrom_retries_1_errmode_1_1", "receives_currentlySending_1", "stationClock_retries_1", "errmode_rcvTokenFrom_1_1", "cRcvInt_1", "ring_1", "safe", "itd", "Station_2_location", "initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1", "rcvTokenFrom_retries_1_errmode_1_2", "receives_currentlySending_2", "stationClock_retries_2", "errmode_rcvTokenFrom_1_2", "cRcvInt_2", "ring_2", "safe_1", "itd_1", "Uplinks3_location", "Channels3_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.msg_sender
		elif variable == 1:
			return self.msg_receiver
		elif variable == 2:
			return self.msg_type
		elif variable == 3:
			return self.msg_ring
		elif variable == 4:
			return self.deliverClock
		elif variable == 5:
			return self.failed
		elif variable == 6:
			return self.is_offline_1
		elif variable == 7:
			return self.is_offline_2
		elif variable == 8:
			return self.is_offline_3
		elif variable == 9:
			return self.iter
		elif variable == 10:
			return self.c
		elif variable == 11:
			return self.Station_location
		elif variable == 12:
			return self.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1
		elif variable == 13:
			return self.rcvTokenFrom_retries_1_errmode_1
		elif variable == 14:
			return self.receives_currentlySending
		elif variable == 15:
			return self.stationClock_retries
		elif variable == 16:
			return self.safe_initToken
		elif variable == 17:
			return self.errmode_rcvTokenFrom_1
		elif variable == 18:
			return self.cRcvInt
		elif variable == 19:
			return self.ring
		elif variable == 20:
			return self.Station_1_location
		elif variable == 21:
			return self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1
		elif variable == 22:
			return self.rcvTokenFrom_retries_1_errmode_1_1
		elif variable == 23:
			return self.receives_currentlySending_1
		elif variable == 24:
			return self.stationClock_retries_1
		elif variable == 25:
			return self.errmode_rcvTokenFrom_1_1
		elif variable == 26:
			return self.cRcvInt_1
		elif variable == 27:
			return self.ring_1
		elif variable == 28:
			return self.safe
		elif variable == 29:
			return self.itd
		elif variable == 30:
			return self.Station_2_location
		elif variable == 31:
			return self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1
		elif variable == 32:
			return self.rcvTokenFrom_retries_1_errmode_1_2
		elif variable == 33:
			return self.receives_currentlySending_2
		elif variable == 34:
			return self.stationClock_retries_2
		elif variable == 35:
			return self.errmode_rcvTokenFrom_1_2
		elif variable == 36:
			return self.cRcvInt_2
		elif variable == 37:
			return self.ring_2
		elif variable == 38:
			return self.safe_1
		elif variable == 39:
			return self.itd_1
		elif variable == 40:
			return self.Uplinks3_location
		elif variable == 41:
			return self.Channels3_location
	
	def copy_to(self, other: State):
		other.msg_sender = self.msg_sender
		other.msg_receiver = self.msg_receiver
		other.msg_type = self.msg_type
		other.msg_ring = self.msg_ring
		other.deliverClock = self.deliverClock
		other.failed = self.failed
		other.is_offline_1 = self.is_offline_1
		other.is_offline_2 = self.is_offline_2
		other.is_offline_3 = self.is_offline_3
		other.iter = self.iter
		other.c = self.c
		other.Station_location = self.Station_location
		other.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = self.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1
		other.rcvTokenFrom_retries_1_errmode_1 = self.rcvTokenFrom_retries_1_errmode_1
		other.receives_currentlySending = self.receives_currentlySending
		other.stationClock_retries = self.stationClock_retries
		other.safe_initToken = self.safe_initToken
		other.errmode_rcvTokenFrom_1 = self.errmode_rcvTokenFrom_1
		other.cRcvInt = self.cRcvInt
		other.ring = self.ring
		other.Station_1_location = self.Station_1_location
		other.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1
		other.rcvTokenFrom_retries_1_errmode_1_1 = self.rcvTokenFrom_retries_1_errmode_1_1
		other.receives_currentlySending_1 = self.receives_currentlySending_1
		other.stationClock_retries_1 = self.stationClock_retries_1
		other.errmode_rcvTokenFrom_1_1 = self.errmode_rcvTokenFrom_1_1
		other.cRcvInt_1 = self.cRcvInt_1
		other.ring_1 = self.ring_1
		other.safe = self.safe
		other.itd = self.itd
		other.Station_2_location = self.Station_2_location
		other.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1
		other.rcvTokenFrom_retries_1_errmode_1_2 = self.rcvTokenFrom_retries_1_errmode_1_2
		other.receives_currentlySending_2 = self.receives_currentlySending_2
		other.stationClock_retries_2 = self.stationClock_retries_2
		other.errmode_rcvTokenFrom_1_2 = self.errmode_rcvTokenFrom_1_2
		other.cRcvInt_2 = self.cRcvInt_2
		other.ring_2 = self.ring_2
		other.safe_1 = self.safe_1
		other.itd_1 = self.itd_1
		other.Uplinks3_location = self.Uplinks3_location
		other.Channels3_location = self.Channels3_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.msg_sender == other.msg_sender and self.msg_receiver == other.msg_receiver and self.msg_type == other.msg_type and self.msg_ring == other.msg_ring and self.deliverClock == other.deliverClock and self.failed == other.failed and self.is_offline_1 == other.is_offline_1 and self.is_offline_2 == other.is_offline_2 and self.is_offline_3 == other.is_offline_3 and self.iter == other.iter and self.c == other.c and self.Station_location == other.Station_location and self.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 == other.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 and self.rcvTokenFrom_retries_1_errmode_1 == other.rcvTokenFrom_retries_1_errmode_1 and self.receives_currentlySending == other.receives_currentlySending and self.stationClock_retries == other.stationClock_retries and self.safe_initToken == other.safe_initToken and self.errmode_rcvTokenFrom_1 == other.errmode_rcvTokenFrom_1 and self.cRcvInt == other.cRcvInt and self.ring == other.ring and self.Station_1_location == other.Station_1_location and self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 == other.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 and self.rcvTokenFrom_retries_1_errmode_1_1 == other.rcvTokenFrom_retries_1_errmode_1_1 and self.receives_currentlySending_1 == other.receives_currentlySending_1 and self.stationClock_retries_1 == other.stationClock_retries_1 and self.errmode_rcvTokenFrom_1_1 == other.errmode_rcvTokenFrom_1_1 and self.cRcvInt_1 == other.cRcvInt_1 and self.ring_1 == other.ring_1 and self.safe == other.safe and self.itd == other.itd and self.Station_2_location == other.Station_2_location and self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 == other.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 and self.rcvTokenFrom_retries_1_errmode_1_2 == other.rcvTokenFrom_retries_1_errmode_1_2 and self.receives_currentlySending_2 == other.receives_currentlySending_2 and self.stationClock_retries_2 == other.stationClock_retries_2 and self.errmode_rcvTokenFrom_1_2 == other.errmode_rcvTokenFrom_1_2 and self.cRcvInt_2 == other.cRcvInt_2 and self.ring_2 == other.ring_2 and self.safe_1 == other.safe_1 and self.itd_1 == other.itd_1 and self.Uplinks3_location == other.Uplinks3_location and self.Channels3_location == other.Channels3_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.msg_sender)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.msg_receiver)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.msg_type)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.msg_ring)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.deliverClock)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.failed)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_offline_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_offline_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_offline_3)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.iter)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Station_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.rcvTokenFrom_retries_1_errmode_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.receives_currentlySending)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.stationClock_retries)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.safe_initToken)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.errmode_rcvTokenFrom_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cRcvInt)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ring)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Station_1_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.rcvTokenFrom_retries_1_errmode_1_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.receives_currentlySending_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.stationClock_retries_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.errmode_rcvTokenFrom_1_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cRcvInt_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ring_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.safe)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.itd)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Station_2_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.rcvTokenFrom_retries_1_errmode_1_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.receives_currentlySending_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.stationClock_retries_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.errmode_rcvTokenFrom_1_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cRcvInt_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.ring_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.safe_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.itd_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Uplinks3_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Channels3_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "msg_sender = " + str(self.msg_sender)
		result += ", msg_receiver = " + str(self.msg_receiver)
		result += ", msg_type = " + str(self.msg_type)
		result += ", msg_ring = " + str(self.msg_ring)
		result += ", deliverClock = " + str(self.deliverClock)
		result += ", failed = " + str(self.failed)
		result += ", is_offline_1 = " + str(self.is_offline_1)
		result += ", is_offline_2 = " + str(self.is_offline_2)
		result += ", is_offline_3 = " + str(self.is_offline_3)
		result += ", iter = " + str(self.iter)
		result += ", c = " + str(self.c)
		result += ", Station_location = " + str(self.Station_location)
		result += ", is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = " + str(self.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
		result += ", rcvTokenFrom_retries_1_errmode_1 = " + str(self.rcvTokenFrom_retries_1_errmode_1)
		result += ", receives_currentlySending = " + str(self.receives_currentlySending)
		result += ", stationClock_retries = " + str(self.stationClock_retries)
		result += ", safe_initToken = " + str(self.safe_initToken)
		result += ", errmode_rcvTokenFrom_1 = " + str(self.errmode_rcvTokenFrom_1)
		result += ", cRcvInt = " + str(self.cRcvInt)
		result += ", ring = " + str(self.ring)
		result += ", Station_1_location = " + str(self.Station_1_location)
		result += ", initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = " + str(self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
		result += ", rcvTokenFrom_retries_1_errmode_1_1 = " + str(self.rcvTokenFrom_retries_1_errmode_1_1)
		result += ", receives_currentlySending_1 = " + str(self.receives_currentlySending_1)
		result += ", stationClock_retries_1 = " + str(self.stationClock_retries_1)
		result += ", errmode_rcvTokenFrom_1_1 = " + str(self.errmode_rcvTokenFrom_1_1)
		result += ", cRcvInt_1 = " + str(self.cRcvInt_1)
		result += ", ring_1 = " + str(self.ring_1)
		result += ", safe = " + str(self.safe)
		result += ", itd = " + str(self.itd)
		result += ", Station_2_location = " + str(self.Station_2_location)
		result += ", initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = " + str(self.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)
		result += ", rcvTokenFrom_retries_1_errmode_1_2 = " + str(self.rcvTokenFrom_retries_1_errmode_1_2)
		result += ", receives_currentlySending_2 = " + str(self.receives_currentlySending_2)
		result += ", stationClock_retries_2 = " + str(self.stationClock_retries_2)
		result += ", errmode_rcvTokenFrom_1_2 = " + str(self.errmode_rcvTokenFrom_1_2)
		result += ", cRcvInt_2 = " + str(self.cRcvInt_2)
		result += ", ring_2 = " + str(self.ring_2)
		result += ", safe_1 = " + str(self.safe_1)
		result += ", itd_1 = " + str(self.itd_1)
		result += ", Uplinks3_location = " + str(self.Uplinks3_location)
		result += ", Channels3_location = " + str(self.Channels3_location)
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

# Automaton: Station
class StationAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 4, 3, 3, 3, 2, 3, 6, 5, 3, 3, 2, 3, 10, 3, 10, 3, 3, 3, 10, 3, 3, 2, 2, 3, 4, 3, 3, 4, 4, 3, 3, 6, 5, 3, 3, 2, 4, 4, 3, 3, 10, 3, 10, 3, 3, 3, 10, 3, 3, 2, 4, 3, 3, 3, 2, 3, 6, 5, 3, 3, 2, 4, 4, 3, 3, 6, 5, 3, 3, 2, 4, 4, 3, 2, 3, 3]
		self.transition_labels = [[0, 1], [0, 1], [0, 0, 1, 35], [1, 2, 35], [1, 3, 35], [1, 4, 35], [0, 1], [0, 1, 2], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 4, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [1, 2, 35], [1, 3, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 1], [0, 1], [0, 1], [0, 1, 35], [0, 1, 5, 35], [1, 2, 35], [1, 3, 35], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 2, 35], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 4, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [1, 2, 35], [1, 3, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 1], [0, 1], [0, 0, 1, 35], [1, 2, 35], [1, 3, 35], [1, 4, 35], [0, 1], [0, 1, 2], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 2, 35], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [0, 1], [1, 2, 35], [1, 3, 35]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Station_location = 0
		state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
		state.rcvTokenFrom_retries_1_errmode_1 = 0
		state.receives_currentlySending = False
		state.stationClock_retries = 0
		state.safe_initToken = True
		state.errmode_rcvTokenFrom_1 = 0
		state.cRcvInt = 0
		state.ring = 1
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Station_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Station_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Station_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Station_location
		if location == 0:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.iter < 3)
			elif transition == 1:
				return (state.iter == 3)
			elif transition == 2:
				return (not state.receives_currentlySending)
			elif transition == 3:
				return (state.cRcvInt < 0)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt < 0)
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return (state.stationClock_retries >= 1)
			elif transition == 2:
				return (state.stationClock_retries < 1)
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (state.stationClock_retries < 1)
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (state.stationClock_retries == 1)
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt == 2))
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (((state.msg_sender == 2) and (state.msg_ring == state.ring)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 2) or (state.msg_ring != state.ring))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt < 2)
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt == 2))
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (((state.msg_sender == 2) and (state.msg_ring == state.ring)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 2) or (state.msg_ring != state.ring))
			elif transition == 4:
				return (state.cRcvInt < 2)
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries < 0)
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.rcvTokenFrom_retries_1_errmode_1 != 2)) and state.safe_initToken)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and ((state.rcvTokenFrom_retries_1_errmode_1 == 2) or (not state.safe_initToken)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.rcvTokenFrom_retries_1_errmode_1 != 2)) and state.safe_initToken)
			elif transition == 3:
				return (not state.receives_currentlySending)
			elif transition == 4:
				return (((state.msg_ring == state.ring) and (state.msg_receiver == 1)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_receiver == 1)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring) and (((state.msg_receiver != 1) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring) and (state.msg_ring != 0)) and (state.msg_ring != 2))
			elif transition == 9:
				return (state.stationClock_retries < 7)
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 16:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.rcvTokenFrom_retries_1_errmode_1 != 2)) and state.safe_initToken)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and ((state.rcvTokenFrom_retries_1_errmode_1 == 2) or (not state.safe_initToken)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.rcvTokenFrom_retries_1_errmode_1 != 2)) and state.safe_initToken)
			elif transition == 3:
				return (not state.receives_currentlySending)
			elif transition == 4:
				return (((state.msg_ring == state.ring) and (state.msg_receiver == 1)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_receiver == 1)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring) and (((state.msg_receiver != 1) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring) and (state.msg_ring != 0)) and (state.msg_ring != 2))
			elif transition == 9:
				return (state.stationClock_retries < 7)
			else:
				raise IndexError
		elif location == 17:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 18:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt < 0)
			else:
				raise IndexError
		elif location == 19:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 20:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.rcvTokenFrom_retries_1_errmode_1 != 2)) and state.safe_initToken)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and ((state.rcvTokenFrom_retries_1_errmode_1 == 2) or (not state.safe_initToken)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.rcvTokenFrom_retries_1_errmode_1 != 2)) and state.safe_initToken)
			elif transition == 3:
				return (not state.receives_currentlySending)
			elif transition == 4:
				return (((state.msg_ring == state.ring) and (state.msg_receiver == 1)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_receiver == 1)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring) and (((state.msg_receiver != 1) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring) and (state.msg_ring != 0)) and (state.msg_ring != 2))
			elif transition == 9:
				return (state.stationClock_retries < 7)
			else:
				raise IndexError
		elif location == 21:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 22:
			if transition == 0:
				return ((state.rcvTokenFrom_retries_1_errmode_1 == 2) or (not state.safe_initToken))
			elif transition == 1:
				return ((state.rcvTokenFrom_retries_1_errmode_1 != 2) and state.safe_initToken)
			elif transition == 2:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 23:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 24:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 25:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (state.stationClock_retries < 0)
			else:
				raise IndexError
		elif location == 26:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition >= 2:
				return True
			else:
				raise IndexError
		elif location == 27:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries < 0)
			else:
				raise IndexError
		elif location == 28:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 29:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 30:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 31:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 32:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt < 0)
			else:
				raise IndexError
		elif location == 33:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt == 2))
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 1)) and (state.msg_ring == state.ring))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 1)) or (state.msg_ring != state.ring))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt < 2)
			else:
				raise IndexError
		elif location == 34:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt == 2))
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 1)) and (state.msg_ring == state.ring))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 1)) or (state.msg_ring != state.ring))
			elif transition == 4:
				return (state.cRcvInt < 2)
			else:
				raise IndexError
		elif location == 35:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 36:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 37:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 38:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 39:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 40:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 41:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries < 0)
			else:
				raise IndexError
		elif location == 42:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.errmode_rcvTokenFrom_1 != 2)) and state.safe_initToken)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and ((state.errmode_rcvTokenFrom_1 == 2) or (not state.safe_initToken)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.errmode_rcvTokenFrom_1 != 2)) and state.safe_initToken)
			elif transition == 3:
				return (not state.receives_currentlySending)
			elif transition == 4:
				return (((state.msg_ring == state.ring) and (state.msg_receiver == 1)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_receiver == 1)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring) and (((state.msg_receiver != 1) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring) and (state.msg_ring != 0)) and (state.msg_ring != 2))
			elif transition == 9:
				return (state.stationClock_retries < 7)
			else:
				raise IndexError
		elif location == 43:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 44:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.errmode_rcvTokenFrom_1 != 2)) and state.safe_initToken)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and ((state.errmode_rcvTokenFrom_1 == 2) or (not state.safe_initToken)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.errmode_rcvTokenFrom_1 != 2)) and state.safe_initToken)
			elif transition == 3:
				return (not state.receives_currentlySending)
			elif transition == 4:
				return (((state.msg_ring == state.ring) and (state.msg_receiver == 1)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_receiver == 1)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring) and (((state.msg_receiver != 1) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring) and (state.msg_ring != 0)) and (state.msg_ring != 2))
			elif transition == 9:
				return (state.stationClock_retries < 7)
			else:
				raise IndexError
		elif location == 45:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 46:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt < 0)
			else:
				raise IndexError
		elif location == 47:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 48:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.errmode_rcvTokenFrom_1 != 2)) and state.safe_initToken)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and ((state.errmode_rcvTokenFrom_1 == 2) or (not state.safe_initToken)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries >= 7)) and (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.errmode_rcvTokenFrom_1 != 2)) and state.safe_initToken)
			elif transition == 3:
				return (not state.receives_currentlySending)
			elif transition == 4:
				return (((state.msg_ring == state.ring) and (state.msg_receiver == 1)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_receiver == 1)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring) and (((state.msg_receiver != 1) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring) or (state.msg_ring == 2)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring) and (state.msg_ring != 0)) and (state.msg_ring != 2))
			elif transition == 9:
				return (state.stationClock_retries < 7)
			else:
				raise IndexError
		elif location == 49:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 50:
			if transition == 0:
				return ((state.errmode_rcvTokenFrom_1 == 2) or (not state.safe_initToken))
			elif transition == 1:
				return ((state.errmode_rcvTokenFrom_1 != 2) and state.safe_initToken)
			elif transition == 2:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 51:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 52:
			if transition == 0:
				return (state.iter < 3)
			elif transition == 1:
				return (state.iter == 3)
			elif transition == 2:
				return (not state.receives_currentlySending)
			elif transition == 3:
				return (state.cRcvInt < 0)
			else:
				raise IndexError
		elif location == 53:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt < 0)
			else:
				raise IndexError
		elif location == 54:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 55:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return (state.stationClock_retries >= 1)
			elif transition == 2:
				return (state.stationClock_retries < 1)
			else:
				raise IndexError
		elif location == 56:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 57:
			if transition == 0:
				return (state.rcvTokenFrom_retries_1_errmode_1 < 1)
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (state.rcvTokenFrom_retries_1_errmode_1 == 1)
			else:
				raise IndexError
		elif location == 58:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt == 2))
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (((state.msg_sender == 2) and (state.msg_ring == state.ring)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 2) or (state.msg_ring != state.ring))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt < 2)
			else:
				raise IndexError
		elif location == 59:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt == 2))
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (((state.msg_sender == 2) and (state.msg_ring == state.ring)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 2) or (state.msg_ring != state.ring))
			elif transition == 4:
				return (state.cRcvInt < 2)
			else:
				raise IndexError
		elif location == 60:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 61:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 62:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 63:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 64:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 65:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 66:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt < 0)
			else:
				raise IndexError
		elif location == 67:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt == 2))
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 1)) and (state.msg_ring == state.ring))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 1)) or (state.msg_ring != state.ring))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt < 2)
			else:
				raise IndexError
		elif location == 68:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt == 2))
			elif transition == 1:
				return (not state.receives_currentlySending)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 1)) and (state.msg_ring == state.ring))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 1)) or (state.msg_ring != state.ring))
			elif transition == 4:
				return (state.cRcvInt < 2)
			else:
				raise IndexError
		elif location == 69:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 70:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 71:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 72:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 73:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 74:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 75:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending)
			else:
				raise IndexError
		elif location == 76:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries < 0)
			else:
				raise IndexError
		elif location == 77:
			if transition == 0:
				return (not state.receives_currentlySending)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Station_location
		if location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 8:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		elif location == 11:
			return None
		elif location == 12:
			return None
		elif location == 13:
			return None
		elif location == 14:
			return None
		elif location == 15:
			return None
		elif location == 16:
			return None
		elif location == 17:
			return None
		elif location == 18:
			return None
		elif location == 19:
			return None
		elif location == 20:
			return None
		elif location == 21:
			return None
		elif location == 22:
			return None
		elif location == 23:
			return None
		elif location == 24:
			return None
		elif location == 25:
			return None
		elif location == 26:
			return None
		elif location == 27:
			return None
		elif location == 28:
			return None
		elif location == 29:
			return None
		elif location == 30:
			return None
		elif location == 31:
			return None
		elif location == 32:
			return None
		elif location == 33:
			return None
		elif location == 34:
			return None
		elif location == 35:
			return None
		elif location == 36:
			return None
		elif location == 37:
			return None
		elif location == 38:
			return None
		elif location == 39:
			return None
		elif location == 40:
			return None
		elif location == 41:
			return None
		elif location == 42:
			return None
		elif location == 43:
			return None
		elif location == 44:
			return None
		elif location == 45:
			return None
		elif location == 46:
			return None
		elif location == 47:
			return None
		elif location == 48:
			return None
		elif location == 49:
			return None
		elif location == 50:
			return None
		elif location == 51:
			return None
		elif location == 52:
			return None
		elif location == 53:
			return None
		elif location == 54:
			return None
		elif location == 55:
			return None
		elif location == 56:
			return None
		elif location == 57:
			return None
		elif location == 58:
			return None
		elif location == 59:
			return None
		elif location == 60:
			return None
		elif location == 61:
			return None
		elif location == 62:
			return None
		elif location == 63:
			return None
		elif location == 64:
			return None
		elif location == 65:
			return None
		elif location == 66:
			return None
		elif location == 67:
			return None
		elif location == 68:
			return None
		elif location == 69:
			return None
		elif location == 70:
			return None
		elif location == 71:
			return None
		elif location == 72:
			return None
		elif location == 73:
			return None
		elif location == 74:
			return None
		elif location == 75:
			return None
		elif location == 76:
			return None
		elif location == 77:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Station_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Station_location
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
			elif transition == 2:
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
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 8:
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
		elif location == 9:
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
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 14:
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
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 16:
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
			else:
				raise IndexError
		elif location == 17:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 18:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 19:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 20:
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
			else:
				raise IndexError
		elif location == 21:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 22:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 23:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 24:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 25:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 26:
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
		elif location == 27:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 28:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 29:
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
		elif location == 30:
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
		elif location == 31:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 32:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 33:
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
		elif location == 34:
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
		elif location == 35:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 36:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 37:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 38:
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
		elif location == 39:
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
		elif location == 40:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 41:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 42:
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
			else:
				raise IndexError
		elif location == 43:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 44:
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
			else:
				raise IndexError
		elif location == 45:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 46:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 47:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 48:
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
			else:
				raise IndexError
		elif location == 49:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 50:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 51:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 52:
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
		elif location == 53:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 54:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 55:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 56:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 57:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 58:
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
		elif location == 59:
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
		elif location == 60:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 61:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 62:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 63:
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
		elif location == 64:
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
		elif location == 65:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 66:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 67:
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
		elif location == 68:
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
		elif location == 69:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 70:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 71:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 72:
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
		elif location == 73:
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
		elif location == 74:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 75:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 76:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 77:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Station_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.iter = (state.iter + 1)
						if target_state.iter > 3:
							raise OverflowError("Assigned value of " + str(target_state.iter) + " is greater than the upper bound of 3 for variable \"iter\".")
						target_state.Station_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 3
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 2
				elif transition == 3:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = 3
						target_state.msg_type = 4
						target_state.msg_ring = state.ring
						target_state.cRcvInt = 0
						target_state.Station_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 5
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 32
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = 2
						target_state.msg_type = 3
						target_state.msg_ring = state.ring
						target_state.stationClock_retries = 0
						target_state.Station_location = 8
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 31
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.cRcvInt = 0
						target_state.Station_location = 30
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 29
				elif transition == 4:
					if branch == 0:
						target_state.Station_location = 9
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
						target_state.cRcvInt = 0
						target_state.Station_location = 12
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.cRcvInt = 0
						target_state.Station_location = 11
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 10
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 11
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 12
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 11
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.safe_initToken = (state.safe_initToken or (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1))
						target_state.Station_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 12
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = (2 if state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 else 0)
						target_state.Station_location = 14
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 13
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.Station_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.stationClock_retries = 0
						target_state.safe_initToken = False
						target_state.ring = 1
						target_state.Station_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.safe_initToken = False
						target_state.Station_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 14
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.Station_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1 = state.msg_sender
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.Station_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_sender
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.Station_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 15
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 16
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 15
			elif location == 16:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.Station_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.stationClock_retries = 0
						target_state.safe_initToken = False
						target_state.ring = 1
						target_state.Station_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.safe_initToken = False
						target_state.Station_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 16
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.Station_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1 = state.msg_sender
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.Station_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_sender
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.Station_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 16
			elif location == 17:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 17
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.cRcvInt = 0
						target_state.Station_location = 18
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 17
			elif location == 18:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 18
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = state.errmode_rcvTokenFrom_1
						target_state.msg_type = 1
						target_state.msg_ring = state.ring
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.cRcvInt = 0
						target_state.Station_location = 19
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 18
			elif location == 19:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 19
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.Station_location = 20
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 19
			elif location == 20:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.Station_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.stationClock_retries = 0
						target_state.safe_initToken = False
						target_state.ring = 1
						target_state.Station_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.safe_initToken = False
						target_state.Station_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 20
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.Station_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1 = state.msg_sender
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.Station_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_sender
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.rcvTokenFrom_retries_1_errmode_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.rcvTokenFrom_retries_1_errmode_1)
						target_state.Station_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 20
			elif location == 21:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 21
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 22
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 21
			elif location == 22:
				if transition == 0:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.safe_initToken = False
						target_state.ring = 1
						target_state.Station_location = 24
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.Station_location = 23
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 22
			elif location == 23:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 23
			elif location == 24:
				if transition == 0:
					if branch == 0:
						target_state.failed = True
						target_state.stationClock_retries = 0
						target_state.Station_location = 25
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 24
			elif location == 25:
				if transition == 0:
					if branch == 0:
						target_state.is_offline_1 = True
						target_state.stationClock_retries = 0
						target_state.Station_location = 26
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 25
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 25
			elif location == 26:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 26
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 26
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 26
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 26
			elif location == 27:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 27
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = 1
						target_state.msg_type = 5
						target_state.msg_ring = state.ring
						target_state.ring = 1
						target_state.Station_location = 28
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 27
			elif location == 28:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 28
				elif transition == 1:
					if branch == 0:
						target_state.ring = 1
						target_state.safe_initToken = False
						target_state.Station_location = 23
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 28
			elif location == 29:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 29
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 10
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 29
			elif location == 30:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 30
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.Station_location = 31
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 11
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 30
			elif location == 31:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 31
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
						target_state.Station_location = 12
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 31
			elif location == 32:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 32
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = 2
						target_state.msg_type = 2
						target_state.msg_ring = state.ring
						target_state.Station_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 32
			elif location == 33:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 40
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.cRcvInt = 0
						target_state.Station_location = 39
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 38
				elif transition == 4:
					if branch == 0:
						target_state.Station_location = 34
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 33
			elif location == 34:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = (state.stationClock_retries + 1)
						if target_state.stationClock_retries > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries) + " is greater than the upper bound of 13 for variable \"stationClock_retries\".")
						target_state.cRcvInt = 0
						target_state.Station_location = 37
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 34
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.cRcvInt = 0
						target_state.Station_location = 36
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 35
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 34
			elif location == 35:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 35
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 34
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 35
			elif location == 36:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 36
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.stationClock_retries = (state.stationClock_retries + 1)
						if target_state.stationClock_retries > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries) + " is greater than the upper bound of 13 for variable \"stationClock_retries\".")
						target_state.Station_location = 37
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 36
			elif location == 37:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 37
			elif location == 38:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 38
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 35
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 38
			elif location == 39:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 39
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 40
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 36
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 39
			elif location == 40:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 40
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries = (state.stationClock_retries + 1)
						if target_state.stationClock_retries > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries) + " is greater than the upper bound of 13 for variable \"stationClock_retries\".")
						target_state.Station_location = 37
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 40
			elif location == 41:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1 = (2 if state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 else 0)
						target_state.Station_location = 42
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 41
			elif location == 42:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.Station_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.safe_initToken = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.ring = 1
						target_state.Station_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.safe_initToken = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.Station_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 42
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.Station_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1 = state.msg_sender
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.Station_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_sender
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.Station_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 42
			elif location == 43:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 43
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 44
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 43
			elif location == 44:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.Station_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.safe_initToken = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.ring = 1
						target_state.Station_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.safe_initToken = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.Station_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 44
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.Station_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1 = state.msg_sender
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.Station_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_sender
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.Station_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 44
			elif location == 45:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 45
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.cRcvInt = 0
						target_state.Station_location = 46
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 45
			elif location == 46:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 46
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = state.rcvTokenFrom_retries_1_errmode_1
						target_state.msg_type = 1
						target_state.msg_ring = state.ring
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.cRcvInt = 0
						target_state.Station_location = 47
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 46
			elif location == 47:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 47
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.Station_location = 48
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 47
			elif location == 48:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.Station_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.safe_initToken = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.ring = 1
						target_state.Station_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.safe_initToken = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.Station_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 48
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.Station_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1 = state.msg_sender
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_ring
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.Station_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.ring = state.msg_sender
						if target_state.ring < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring) + " is less than the lower bound of 1 for variable \"ring\".")
						target_state.errmode_rcvTokenFrom_1 = (min(1, state.errmode_rcvTokenFrom_1) if ((state.msg_ring == 2) or (state.msg_ring == state.ring)) else state.errmode_rcvTokenFrom_1)
						target_state.Station_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 48
			elif location == 49:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 49
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 50
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 49
			elif location == 50:
				if transition == 0:
					if branch == 0:
						target_state.safe_initToken = False
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.ring = 1
						target_state.Station_location = 75
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.errmode_rcvTokenFrom_1 = 0
						target_state.Station_location = 51
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 50
			elif location == 51:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 52
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 51
			elif location == 52:
				if transition == 0:
					if branch == 0:
						target_state.iter = (state.iter + 1)
						if target_state.iter > 3:
							raise OverflowError("Assigned value of " + str(target_state.iter) + " is greater than the upper bound of 3 for variable \"iter\".")
						target_state.Station_location = 53
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 53
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 52
				elif transition == 3:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 52
			elif location == 53:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 53
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = 3
						target_state.msg_type = 4
						target_state.msg_ring = state.ring
						target_state.cRcvInt = 0
						target_state.Station_location = 54
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 53
			elif location == 54:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 54
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 55
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 54
			elif location == 55:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 55
				elif transition == 1:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries = 0
						target_state.Station_location = 56
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 55
			elif location == 56:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 57
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 56
			elif location == 57:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 66
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 57
				elif transition == 2:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = 2
						target_state.msg_type = 3
						target_state.msg_ring = state.ring
						target_state.rcvTokenFrom_retries_1_errmode_1 = 0
						target_state.Station_location = 58
			elif location == 58:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 65
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 58
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.cRcvInt = 0
						target_state.Station_location = 64
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 63
				elif transition == 4:
					if branch == 0:
						target_state.Station_location = 59
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 58
			elif location == 59:
				if transition == 0:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
						target_state.cRcvInt = 0
						target_state.Station_location = 62
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 59
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.cRcvInt = 0
						target_state.Station_location = 61
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 60
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 59
			elif location == 60:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 60
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 59
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 60
			elif location == 61:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 61
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_location = 62
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 61
			elif location == 62:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries = 0
						target_state.safe_initToken = (state.safe_initToken or (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1))
						target_state.Station_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 62
			elif location == 63:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 63
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 58
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 60
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 63
			elif location == 64:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 64
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.Station_location = 65
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 61
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 64
			elif location == 65:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 65
				elif transition == 1:
					if branch == 0:
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = (not state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
						target_state.Station_location = 62
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 65
			elif location == 66:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 66
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = 2
						target_state.msg_type = 2
						target_state.msg_ring = state.ring
						target_state.Station_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 66
			elif location == 67:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 74
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.cRcvInt = 0
						target_state.Station_location = 73
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 72
				elif transition == 4:
					if branch == 0:
						target_state.Station_location = 68
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 67
			elif location == 68:
				if transition == 0:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1 = (state.rcvTokenFrom_retries_1_errmode_1 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1\".")
						target_state.cRcvInt = 0
						target_state.Station_location = 71
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 68
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.cRcvInt = 0
						target_state.Station_location = 70
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending = True
						target_state.Station_location = 69
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 68
			elif location == 69:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 69
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 68
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 69
			elif location == 70:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 70
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.rcvTokenFrom_retries_1_errmode_1 = (state.rcvTokenFrom_retries_1_errmode_1 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1\".")
						target_state.Station_location = 71
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 70
			elif location == 71:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt = 0
						target_state.Station_location = 57
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 71
			elif location == 72:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 72
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 69
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt = min((state.cRcvInt + 1), 3)
						target_state.Station_location = 72
			elif location == 73:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 73
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending = False
						target_state.Station_location = 74
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 70
				elif transition == 3:
					if branch == 0:
						target_state.Station_location = 73
			elif location == 74:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 74
				elif transition == 1:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1 = (state.rcvTokenFrom_retries_1_errmode_1 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1\".")
						target_state.Station_location = 71
				elif transition == 2:
					if branch == 0:
						target_state.Station_location = 74
			elif location == 75:
				if transition == 0:
					if branch == 0:
						target_state.failed = True
						target_state.stationClock_retries = 0
						target_state.Station_location = 25
				elif transition == 1:
					if branch == 0:
						target_state.Station_location = 75
			elif location == 76:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 76
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 1
						target_state.msg_receiver = 1
						target_state.msg_type = 5
						target_state.msg_ring = state.ring
						target_state.ring = 1
						target_state.Station_location = 77
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 76
			elif location == 77:
				if transition == 0:
					if branch == 0:
						target_state.Station_location = 77
				elif transition == 1:
					if branch == 0:
						target_state.ring = 1
						target_state.safe_initToken = False
						target_state.Station_location = 51
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries = min((state.stationClock_retries + 1), 13)
						target_state.Station_location = 77

# Automaton: Station_1
class Station_1Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 3, 3, 3, 3, 2, 3, 6, 5, 3, 3, 2, 3, 10, 3, 10, 3, 3, 3, 10, 3, 3, 2, 2, 3, 4, 3, 3, 4, 4, 3, 3, 6, 5, 3, 3, 2, 4, 4, 3, 3, 10, 3, 10, 3, 3, 3, 10, 3, 3, 2, 3, 3, 3, 3, 2, 3, 6, 5, 3, 3, 2, 4, 4, 3, 3, 6, 5, 3, 3, 2, 4, 4, 3, 2, 3, 3]
		self.transition_labels = [[0, 1], [0, 1], [0, 1, 35], [1, 2, 35], [1, 3, 35], [1, 4, 35], [0, 1], [0, 1, 2], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 4, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [1, 2, 35], [1, 3, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 1], [0, 1], [0, 1], [0, 1, 35], [0, 1, 5, 35], [1, 2, 35], [1, 3, 35], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 2, 35], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 4, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [1, 2, 35], [1, 3, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 1], [0, 1], [0, 1, 35], [1, 2, 35], [1, 3, 35], [1, 4, 35], [0, 1], [0, 1, 2], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 2, 35], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [0, 1], [1, 2, 35], [1, 3, 35]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Station_1_location = 0
		state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
		state.rcvTokenFrom_retries_1_errmode_1_1 = 0
		state.receives_currentlySending_1 = False
		state.stationClock_retries_1 = 0
		state.errmode_rcvTokenFrom_1_1 = 0
		state.cRcvInt_1 = 0
		state.ring_1 = 1
		state.safe = True
		state.itd = 5
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Station_1_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Station_1_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Station_1_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Station_1_location
		if location == 0:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (state.cRcvInt_1 < 0)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_1 < 0)
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return (state.stationClock_retries_1 >= 1)
			elif transition == 2:
				return (state.stationClock_retries_1 < 1)
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (state.stationClock_retries_1 < 1)
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (state.stationClock_retries_1 == 1)
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_1 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (((state.msg_sender == 3) and (state.msg_ring == state.ring_1)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 3) or (state.msg_ring != state.ring_1))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt_1 < 2)
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_1 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (((state.msg_sender == 3) and (state.msg_ring == state.ring_1)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 3) or (state.msg_ring != state.ring_1))
			elif transition == 4:
				return (state.cRcvInt_1 < 2)
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries_1 < 0)
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.rcvTokenFrom_retries_1_errmode_1_1 != 2)) and state.safe)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and ((state.rcvTokenFrom_retries_1_errmode_1_1 == 2) or (not state.safe)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.rcvTokenFrom_retries_1_errmode_1_1 != 2)) and state.safe)
			elif transition == 3:
				return (not state.receives_currentlySending_1)
			elif transition == 4:
				return (((state.msg_ring == state.ring_1) and (state.msg_receiver == 2)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_receiver == 2)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_1) and (((state.msg_receiver != 2) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_1) and (state.msg_ring != 0)) and (state.msg_ring != 3))
			elif transition == 9:
				return (state.stationClock_retries_1 < state.itd)
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 16:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.rcvTokenFrom_retries_1_errmode_1_1 != 2)) and state.safe)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and ((state.rcvTokenFrom_retries_1_errmode_1_1 == 2) or (not state.safe)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.rcvTokenFrom_retries_1_errmode_1_1 != 2)) and state.safe)
			elif transition == 3:
				return (not state.receives_currentlySending_1)
			elif transition == 4:
				return (((state.msg_ring == state.ring_1) and (state.msg_receiver == 2)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_receiver == 2)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_1) and (((state.msg_receiver != 2) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_1) and (state.msg_ring != 0)) and (state.msg_ring != 3))
			elif transition == 9:
				return (state.stationClock_retries_1 < state.itd)
			else:
				raise IndexError
		elif location == 17:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 18:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_1 < 0)
			else:
				raise IndexError
		elif location == 19:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 20:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.rcvTokenFrom_retries_1_errmode_1_1 != 2)) and state.safe)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and ((state.rcvTokenFrom_retries_1_errmode_1_1 == 2) or (not state.safe)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.rcvTokenFrom_retries_1_errmode_1_1 != 2)) and state.safe)
			elif transition == 3:
				return (not state.receives_currentlySending_1)
			elif transition == 4:
				return (((state.msg_ring == state.ring_1) and (state.msg_receiver == 2)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_receiver == 2)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_1) and (((state.msg_receiver != 2) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_1) and (state.msg_ring != 0)) and (state.msg_ring != 3))
			elif transition == 9:
				return (state.stationClock_retries_1 < state.itd)
			else:
				raise IndexError
		elif location == 21:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 22:
			if transition == 0:
				return ((state.rcvTokenFrom_retries_1_errmode_1_1 == 2) or (not state.safe))
			elif transition == 1:
				return ((state.rcvTokenFrom_retries_1_errmode_1_1 != 2) and state.safe)
			elif transition == 2:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 23:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 24:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 25:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (state.stationClock_retries_1 < 0)
			else:
				raise IndexError
		elif location == 26:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition >= 2:
				return True
			else:
				raise IndexError
		elif location == 27:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries_1 < 0)
			else:
				raise IndexError
		elif location == 28:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 29:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 30:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 31:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 32:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_1 < 0)
			else:
				raise IndexError
		elif location == 33:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_1 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 2)) and (state.msg_ring == state.ring_1))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 2)) or (state.msg_ring != state.ring_1))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt_1 < 2)
			else:
				raise IndexError
		elif location == 34:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_1 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 2)) and (state.msg_ring == state.ring_1))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 2)) or (state.msg_ring != state.ring_1))
			elif transition == 4:
				return (state.cRcvInt_1 < 2)
			else:
				raise IndexError
		elif location == 35:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 36:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 37:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 38:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 39:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 40:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 41:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries_1 < 0)
			else:
				raise IndexError
		elif location == 42:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.errmode_rcvTokenFrom_1_1 != 2)) and state.safe)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and ((state.errmode_rcvTokenFrom_1_1 == 2) or (not state.safe)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.errmode_rcvTokenFrom_1_1 != 2)) and state.safe)
			elif transition == 3:
				return (not state.receives_currentlySending_1)
			elif transition == 4:
				return (((state.msg_ring == state.ring_1) and (state.msg_receiver == 2)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_receiver == 2)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_1) and (((state.msg_receiver != 2) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_1) and (state.msg_ring != 0)) and (state.msg_ring != 3))
			elif transition == 9:
				return (state.stationClock_retries_1 < state.itd)
			else:
				raise IndexError
		elif location == 43:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 44:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.errmode_rcvTokenFrom_1_1 != 2)) and state.safe)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and ((state.errmode_rcvTokenFrom_1_1 == 2) or (not state.safe)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.errmode_rcvTokenFrom_1_1 != 2)) and state.safe)
			elif transition == 3:
				return (not state.receives_currentlySending_1)
			elif transition == 4:
				return (((state.msg_ring == state.ring_1) and (state.msg_receiver == 2)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_receiver == 2)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_1) and (((state.msg_receiver != 2) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_1) and (state.msg_ring != 0)) and (state.msg_ring != 3))
			elif transition == 9:
				return (state.stationClock_retries_1 < state.itd)
			else:
				raise IndexError
		elif location == 45:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 46:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_1 < 0)
			else:
				raise IndexError
		elif location == 47:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 48:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1) and (state.errmode_rcvTokenFrom_1_1 != 2)) and state.safe)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and ((state.errmode_rcvTokenFrom_1_1 == 2) or (not state.safe)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_1 >= state.itd)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)) and (state.errmode_rcvTokenFrom_1_1 != 2)) and state.safe)
			elif transition == 3:
				return (not state.receives_currentlySending_1)
			elif transition == 4:
				return (((state.msg_ring == state.ring_1) and (state.msg_receiver == 2)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_receiver == 2)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_1) and (((state.msg_receiver != 2) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_1) or (state.msg_ring == 3)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_1) and (state.msg_ring != 0)) and (state.msg_ring != 3))
			elif transition == 9:
				return (state.stationClock_retries_1 < state.itd)
			else:
				raise IndexError
		elif location == 49:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 50:
			if transition == 0:
				return ((state.errmode_rcvTokenFrom_1_1 == 2) or (not state.safe))
			elif transition == 1:
				return ((state.errmode_rcvTokenFrom_1_1 != 2) and state.safe)
			elif transition == 2:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 51:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 52:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (state.cRcvInt_1 < 0)
			else:
				raise IndexError
		elif location == 53:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_1 < 0)
			else:
				raise IndexError
		elif location == 54:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 55:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return (state.stationClock_retries_1 >= 1)
			elif transition == 2:
				return (state.stationClock_retries_1 < 1)
			else:
				raise IndexError
		elif location == 56:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 57:
			if transition == 0:
				return (state.rcvTokenFrom_retries_1_errmode_1_1 < 1)
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (state.rcvTokenFrom_retries_1_errmode_1_1 == 1)
			else:
				raise IndexError
		elif location == 58:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_1 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (((state.msg_sender == 3) and (state.msg_ring == state.ring_1)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 3) or (state.msg_ring != state.ring_1))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt_1 < 2)
			else:
				raise IndexError
		elif location == 59:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_1 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (((state.msg_sender == 3) and (state.msg_ring == state.ring_1)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 3) or (state.msg_ring != state.ring_1))
			elif transition == 4:
				return (state.cRcvInt_1 < 2)
			else:
				raise IndexError
		elif location == 60:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 61:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 62:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 63:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 64:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 65:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 66:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_1 < 0)
			else:
				raise IndexError
		elif location == 67:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_1 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 2)) and (state.msg_ring == state.ring_1))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 2)) or (state.msg_ring != state.ring_1))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt_1 < 2)
			else:
				raise IndexError
		elif location == 68:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_1 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 2)) and (state.msg_ring == state.ring_1))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 2)) or (state.msg_ring != state.ring_1))
			elif transition == 4:
				return (state.cRcvInt_1 < 2)
			else:
				raise IndexError
		elif location == 69:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 70:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 71:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 72:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 73:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 74:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 75:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_1)
			else:
				raise IndexError
		elif location == 76:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries_1 < 0)
			else:
				raise IndexError
		elif location == 77:
			if transition == 0:
				return (not state.receives_currentlySending_1)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Station_1_location
		if location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 8:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		elif location == 11:
			return None
		elif location == 12:
			return None
		elif location == 13:
			return None
		elif location == 14:
			return None
		elif location == 15:
			return None
		elif location == 16:
			return None
		elif location == 17:
			return None
		elif location == 18:
			return None
		elif location == 19:
			return None
		elif location == 20:
			return None
		elif location == 21:
			return None
		elif location == 22:
			return None
		elif location == 23:
			return None
		elif location == 24:
			return None
		elif location == 25:
			return None
		elif location == 26:
			return None
		elif location == 27:
			return None
		elif location == 28:
			return None
		elif location == 29:
			return None
		elif location == 30:
			return None
		elif location == 31:
			return None
		elif location == 32:
			return None
		elif location == 33:
			return None
		elif location == 34:
			return None
		elif location == 35:
			return None
		elif location == 36:
			return None
		elif location == 37:
			return None
		elif location == 38:
			return None
		elif location == 39:
			return None
		elif location == 40:
			return None
		elif location == 41:
			return None
		elif location == 42:
			return None
		elif location == 43:
			return None
		elif location == 44:
			return None
		elif location == 45:
			return None
		elif location == 46:
			return None
		elif location == 47:
			return None
		elif location == 48:
			return None
		elif location == 49:
			return None
		elif location == 50:
			return None
		elif location == 51:
			return None
		elif location == 52:
			return None
		elif location == 53:
			return None
		elif location == 54:
			return None
		elif location == 55:
			return None
		elif location == 56:
			return None
		elif location == 57:
			return None
		elif location == 58:
			return None
		elif location == 59:
			return None
		elif location == 60:
			return None
		elif location == 61:
			return None
		elif location == 62:
			return None
		elif location == 63:
			return None
		elif location == 64:
			return None
		elif location == 65:
			return None
		elif location == 66:
			return None
		elif location == 67:
			return None
		elif location == 68:
			return None
		elif location == 69:
			return None
		elif location == 70:
			return None
		elif location == 71:
			return None
		elif location == 72:
			return None
		elif location == 73:
			return None
		elif location == 74:
			return None
		elif location == 75:
			return None
		elif location == 76:
			return None
		elif location == 77:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Station_1_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Station_1_location
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
			elif transition == 2:
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
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 8:
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
		elif location == 9:
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
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 14:
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
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 16:
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
			else:
				raise IndexError
		elif location == 17:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 18:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 19:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 20:
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
			else:
				raise IndexError
		elif location == 21:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 22:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 23:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 24:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 25:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 26:
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
		elif location == 27:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 28:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 29:
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
		elif location == 30:
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
		elif location == 31:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 32:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 33:
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
		elif location == 34:
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
		elif location == 35:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 36:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 37:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 38:
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
		elif location == 39:
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
		elif location == 40:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 41:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 42:
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
			else:
				raise IndexError
		elif location == 43:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 44:
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
			else:
				raise IndexError
		elif location == 45:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 46:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 47:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 48:
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
			else:
				raise IndexError
		elif location == 49:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 50:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 51:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 52:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 53:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 54:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 55:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 56:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 57:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 58:
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
		elif location == 59:
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
		elif location == 60:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 61:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 62:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 63:
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
		elif location == 64:
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
		elif location == 65:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 66:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 67:
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
		elif location == 68:
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
		elif location == 69:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 70:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 71:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 72:
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
		elif location == 73:
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
		elif location == 74:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 75:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 76:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 77:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Station_1_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.safe = (state.safe or (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1))
						target_state.Station_1_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.safe = (state.safe or (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1))
						target_state.Station_1_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = 1
						target_state.msg_type = 4
						target_state.msg_ring = state.ring_1
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 5
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 32
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = 3
						target_state.msg_type = 3
						target_state.msg_ring = state.ring_1
						target_state.stationClock_retries_1 = 0
						target_state.Station_1_location = 8
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 31
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 30
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 29
				elif transition == 4:
					if branch == 0:
						target_state.Station_1_location = 9
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 12
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 11
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 10
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 11
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 12
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 11
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.safe = (state.safe or (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1))
						target_state.Station_1_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 12
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (2 if state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 else 0)
						target_state.Station_1_location = 14
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 13
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.stationClock_retries_1 = 0
						target_state.ring_1 = 1
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 14
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1_1 = state.msg_sender
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.Station_1_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_sender
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.Station_1_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 15
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 16
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 15
			elif location == 16:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.stationClock_retries_1 = 0
						target_state.ring_1 = 1
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 16
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1_1 = state.msg_sender
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.Station_1_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_sender
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.Station_1_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 16
			elif location == 17:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 17
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 18
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 17
			elif location == 18:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 18
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = state.errmode_rcvTokenFrom_1_1
						target_state.msg_type = 1
						target_state.msg_ring = state.ring_1
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 19
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 18
			elif location == 19:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 19
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.Station_1_location = 20
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 19
			elif location == 20:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.stationClock_retries_1 = 0
						target_state.ring_1 = 1
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 20
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1_1 = state.msg_sender
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.Station_1_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_sender
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.rcvTokenFrom_retries_1_errmode_1_1)
						target_state.Station_1_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 20
			elif location == 21:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 21
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 22
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 21
			elif location == 22:
				if transition == 0:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.ring_1 = 1
						target_state.safe = False
						target_state.Station_1_location = 24
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.Station_1_location = 23
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 22
			elif location == 23:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.itd = 7
						target_state.Station_1_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 23
			elif location == 24:
				if transition == 0:
					if branch == 0:
						target_state.failed = True
						target_state.stationClock_retries_1 = 0
						target_state.Station_1_location = 25
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 24
			elif location == 25:
				if transition == 0:
					if branch == 0:
						target_state.is_offline_2 = True
						target_state.stationClock_retries_1 = 0
						target_state.Station_1_location = 26
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 25
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 25
			elif location == 26:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 26
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 26
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 26
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 26
			elif location == 27:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 27
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = 2
						target_state.msg_type = 5
						target_state.msg_ring = state.ring_1
						target_state.ring_1 = 1
						target_state.Station_1_location = 28
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 27
			elif location == 28:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 28
				elif transition == 1:
					if branch == 0:
						target_state.ring_1 = 2
						target_state.safe = False
						target_state.Station_1_location = 23
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 28
			elif location == 29:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 29
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 10
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 29
			elif location == 30:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 30
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.Station_1_location = 31
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 11
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 30
			elif location == 31:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 31
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
						target_state.Station_1_location = 12
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 31
			elif location == 32:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 32
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = 3
						target_state.msg_type = 2
						target_state.msg_ring = state.ring_1
						target_state.Station_1_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 32
			elif location == 33:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 40
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 39
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 38
				elif transition == 4:
					if branch == 0:
						target_state.Station_1_location = 34
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 33
			elif location == 34:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = (state.stationClock_retries_1 + 1)
						if target_state.stationClock_retries_1 > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries_1) + " is greater than the upper bound of 13 for variable \"stationClock_retries_1\".")
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 37
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 34
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 36
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 35
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 34
			elif location == 35:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 35
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 34
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 35
			elif location == 36:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 36
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.stationClock_retries_1 = (state.stationClock_retries_1 + 1)
						if target_state.stationClock_retries_1 > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries_1) + " is greater than the upper bound of 13 for variable \"stationClock_retries_1\".")
						target_state.Station_1_location = 37
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 36
			elif location == 37:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 37
			elif location == 38:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 38
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 35
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 38
			elif location == 39:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 39
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 40
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 36
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 39
			elif location == 40:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 40
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries_1 = (state.stationClock_retries_1 + 1)
						if target_state.stationClock_retries_1 > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries_1) + " is greater than the upper bound of 13 for variable \"stationClock_retries_1\".")
						target_state.Station_1_location = 37
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 40
			elif location == 41:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1_1 = (2 if state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 else 0)
						target_state.Station_1_location = 42
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 41
			elif location == 42:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.ring_1 = 1
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 42
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = state.msg_sender
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.Station_1_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_sender
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.Station_1_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 42
			elif location == 43:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 43
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 44
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 43
			elif location == 44:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.ring_1 = 1
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 44
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = state.msg_sender
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.Station_1_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_sender
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.Station_1_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 44
			elif location == 45:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 45
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 46
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 45
			elif location == 46:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 46
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = state.rcvTokenFrom_retries_1_errmode_1_1
						target_state.msg_type = 1
						target_state.msg_ring = state.ring_1
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 47
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 46
			elif location == 47:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 47
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.Station_1_location = 48
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 47
			elif location == 48:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.ring_1 = 1
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.safe = False
						target_state.itd = 0
						target_state.Station_1_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 48
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.itd = 0
						target_state.Station_1_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = state.msg_sender
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_ring
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.Station_1_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.ring_1 = state.msg_sender
						if target_state.ring_1 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_1) + " is less than the lower bound of 1 for variable \"ring_1\".")
						target_state.errmode_rcvTokenFrom_1_1 = (min(1, state.errmode_rcvTokenFrom_1_1) if ((state.msg_ring == 3) or (state.msg_ring == state.ring_1)) else state.errmode_rcvTokenFrom_1_1)
						target_state.Station_1_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 48
			elif location == 49:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 49
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 50
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 49
			elif location == 50:
				if transition == 0:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.ring_1 = 1
						target_state.safe = False
						target_state.Station_1_location = 75
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.errmode_rcvTokenFrom_1_1 = 0
						target_state.Station_1_location = 51
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 50
			elif location == 51:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.itd = 7
						target_state.Station_1_location = 52
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 51
			elif location == 52:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 53
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 52
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 52
			elif location == 53:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 53
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = 1
						target_state.msg_type = 4
						target_state.msg_ring = state.ring_1
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 54
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 53
			elif location == 54:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 54
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 55
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 54
			elif location == 55:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 55
				elif transition == 1:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.stationClock_retries_1 = 0
						target_state.Station_1_location = 56
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 55
			elif location == 56:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 57
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 56
			elif location == 57:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 66
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 57
				elif transition == 2:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = 3
						target_state.msg_type = 3
						target_state.msg_ring = state.ring_1
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = 0
						target_state.Station_1_location = 58
			elif location == 58:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 65
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 58
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 64
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 63
				elif transition == 4:
					if branch == 0:
						target_state.Station_1_location = 59
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 58
			elif location == 59:
				if transition == 0:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 62
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 59
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 61
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 60
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 59
			elif location == 60:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 60
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 59
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 60
			elif location == 61:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 61
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = False
						target_state.Station_1_location = 62
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 61
			elif location == 62:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_1 = 0
						target_state.safe = (state.safe or (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1))
						target_state.Station_1_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 62
			elif location == 63:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 63
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 58
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 60
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 63
			elif location == 64:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 64
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.Station_1_location = 65
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 61
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 64
			elif location == 65:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 65
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1)
						target_state.Station_1_location = 62
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 65
			elif location == 66:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 66
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = 3
						target_state.msg_type = 2
						target_state.msg_ring = state.ring_1
						target_state.Station_1_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 66
			elif location == 67:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 74
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 73
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 72
				elif transition == 4:
					if branch == 0:
						target_state.Station_1_location = 68
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 67
			elif location == 68:
				if transition == 0:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (state.rcvTokenFrom_retries_1_errmode_1_1 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1_1) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1_1\".")
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 71
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 68
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1 = True
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 70
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_1 = True
						target_state.Station_1_location = 69
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 68
			elif location == 69:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 69
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 68
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 69
			elif location == 70:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 70
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (state.rcvTokenFrom_retries_1_errmode_1_1 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1_1) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1_1\".")
						target_state.Station_1_location = 71
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 70
			elif location == 71:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_1 = 0
						target_state.Station_1_location = 57
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 71
			elif location == 72:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 72
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 69
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt_1 = min((state.cRcvInt_1 + 1), 3)
						target_state.Station_1_location = 72
			elif location == 73:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 73
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_1 = False
						target_state.Station_1_location = 74
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 70
				elif transition == 3:
					if branch == 0:
						target_state.Station_1_location = 73
			elif location == 74:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 74
				elif transition == 1:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_1 = (state.rcvTokenFrom_retries_1_errmode_1_1 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1_1 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1_1) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1_1\".")
						target_state.Station_1_location = 71
				elif transition == 2:
					if branch == 0:
						target_state.Station_1_location = 74
			elif location == 75:
				if transition == 0:
					if branch == 0:
						target_state.failed = True
						target_state.stationClock_retries_1 = 0
						target_state.Station_1_location = 25
				elif transition == 1:
					if branch == 0:
						target_state.Station_1_location = 75
			elif location == 76:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 76
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 2
						target_state.msg_receiver = 2
						target_state.msg_type = 5
						target_state.msg_ring = state.ring_1
						target_state.ring_1 = 1
						target_state.Station_1_location = 77
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 76
			elif location == 77:
				if transition == 0:
					if branch == 0:
						target_state.Station_1_location = 77
				elif transition == 1:
					if branch == 0:
						target_state.ring_1 = 2
						target_state.safe = False
						target_state.Station_1_location = 51
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_1 = min((state.stationClock_retries_1 + 1), 13)
						target_state.Station_1_location = 77

# Automaton: Station_2
class Station_2Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 3, 3, 3, 3, 2, 3, 6, 5, 3, 3, 2, 3, 10, 3, 10, 3, 3, 3, 10, 3, 3, 2, 2, 3, 4, 3, 3, 4, 4, 3, 3, 6, 5, 3, 3, 2, 4, 4, 3, 3, 10, 3, 10, 3, 3, 3, 10, 3, 3, 2, 3, 3, 3, 3, 2, 3, 6, 5, 3, 3, 2, 4, 4, 3, 3, 6, 5, 3, 3, 2, 4, 4, 3, 2, 3, 3]
		self.transition_labels = [[0, 1], [0, 1], [0, 1, 35], [1, 2, 35], [1, 3, 35], [1, 4, 35], [0, 1], [0, 1, 2], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 4, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [1, 2, 35], [1, 3, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 1], [0, 1], [0, 1], [0, 1, 35], [0, 1, 5, 35], [1, 2, 35], [1, 3, 35], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 2, 35], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 4, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [1, 2, 35], [1, 3, 35], [0, 0, 0, 1, 5, 5, 5, 5, 5, 35], [1, 6, 35], [0, 0, 1], [0, 1], [0, 1, 35], [1, 2, 35], [1, 3, 35], [1, 4, 35], [0, 1], [0, 1, 2], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [1, 2, 35], [0, 1, 5, 5, 3, 35], [0, 1, 5, 5, 35], [1, 6, 35], [1, 6, 35], [0, 1], [1, 6, 3, 35], [1, 6, 3, 35], [1, 3, 35], [0, 1], [1, 2, 35], [1, 3, 35]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Station_2_location = 0
		state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
		state.rcvTokenFrom_retries_1_errmode_1_2 = 0
		state.receives_currentlySending_2 = False
		state.stationClock_retries_2 = 0
		state.errmode_rcvTokenFrom_1_2 = 0
		state.cRcvInt_2 = 0
		state.ring_2 = 1
		state.safe_1 = True
		state.itd_1 = 9
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Station_2_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Station_2_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Station_2_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Station_2_location
		if location == 0:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 1:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (state.cRcvInt_2 < 0)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_2 < 0)
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return (state.stationClock_retries_2 >= 1)
			elif transition == 2:
				return (state.stationClock_retries_2 < 1)
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return (state.stationClock_retries_2 < 1)
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (state.stationClock_retries_2 == 1)
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_2 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (((state.msg_sender == 1) and (state.msg_ring == state.ring_2)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 1) or (state.msg_ring != state.ring_2))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt_2 < 2)
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_2 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (((state.msg_sender == 1) and (state.msg_ring == state.ring_2)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 1) or (state.msg_ring != state.ring_2))
			elif transition == 4:
				return (state.cRcvInt_2 < 2)
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries_2 < 0)
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1) and (state.rcvTokenFrom_retries_1_errmode_1_2 != 2)) and state.safe_1)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and ((state.rcvTokenFrom_retries_1_errmode_1_2 == 2) or (not state.safe_1)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)) and (state.rcvTokenFrom_retries_1_errmode_1_2 != 2)) and state.safe_1)
			elif transition == 3:
				return (not state.receives_currentlySending_2)
			elif transition == 4:
				return (((state.msg_ring == state.ring_2) and (state.msg_receiver == 3)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_receiver == 3)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_2) and (((state.msg_receiver != 3) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_2) and (state.msg_ring != 0)) and (state.msg_ring != 1))
			elif transition == 9:
				return (state.stationClock_retries_2 < state.itd_1)
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 16:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1) and (state.rcvTokenFrom_retries_1_errmode_1_2 != 2)) and state.safe_1)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and ((state.rcvTokenFrom_retries_1_errmode_1_2 == 2) or (not state.safe_1)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)) and (state.rcvTokenFrom_retries_1_errmode_1_2 != 2)) and state.safe_1)
			elif transition == 3:
				return (not state.receives_currentlySending_2)
			elif transition == 4:
				return (((state.msg_ring == state.ring_2) and (state.msg_receiver == 3)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_receiver == 3)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_2) and (((state.msg_receiver != 3) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_2) and (state.msg_ring != 0)) and (state.msg_ring != 1))
			elif transition == 9:
				return (state.stationClock_retries_2 < state.itd_1)
			else:
				raise IndexError
		elif location == 17:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 18:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_2 < 0)
			else:
				raise IndexError
		elif location == 19:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 20:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1) and (state.rcvTokenFrom_retries_1_errmode_1_2 != 2)) and state.safe_1)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and ((state.rcvTokenFrom_retries_1_errmode_1_2 == 2) or (not state.safe_1)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)) and (state.rcvTokenFrom_retries_1_errmode_1_2 != 2)) and state.safe_1)
			elif transition == 3:
				return (not state.receives_currentlySending_2)
			elif transition == 4:
				return (((state.msg_ring == state.ring_2) and (state.msg_receiver == 3)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_receiver == 3)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_2) and (((state.msg_receiver != 3) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_2) and (state.msg_ring != 0)) and (state.msg_ring != 1))
			elif transition == 9:
				return (state.stationClock_retries_2 < state.itd_1)
			else:
				raise IndexError
		elif location == 21:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 22:
			if transition == 0:
				return ((state.rcvTokenFrom_retries_1_errmode_1_2 == 2) or (not state.safe_1))
			elif transition == 1:
				return ((state.rcvTokenFrom_retries_1_errmode_1_2 != 2) and state.safe_1)
			elif transition == 2:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 23:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 24:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 25:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (state.stationClock_retries_2 < 0)
			else:
				raise IndexError
		elif location == 26:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition >= 2:
				return True
			else:
				raise IndexError
		elif location == 27:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries_2 < 0)
			else:
				raise IndexError
		elif location == 28:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 29:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 30:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 31:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 32:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_2 < 0)
			else:
				raise IndexError
		elif location == 33:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_2 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 3)) and (state.msg_ring == state.ring_2))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 3)) or (state.msg_ring != state.ring_2))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt_2 < 2)
			else:
				raise IndexError
		elif location == 34:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_2 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 3)) and (state.msg_ring == state.ring_2))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 3)) or (state.msg_ring != state.ring_2))
			elif transition == 4:
				return (state.cRcvInt_2 < 2)
			else:
				raise IndexError
		elif location == 35:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 36:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 37:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 38:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 39:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 40:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 41:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries_2 < 0)
			else:
				raise IndexError
		elif location == 42:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1) and (state.errmode_rcvTokenFrom_1_2 != 2)) and state.safe_1)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and ((state.errmode_rcvTokenFrom_1_2 == 2) or (not state.safe_1)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)) and (state.errmode_rcvTokenFrom_1_2 != 2)) and state.safe_1)
			elif transition == 3:
				return (not state.receives_currentlySending_2)
			elif transition == 4:
				return (((state.msg_ring == state.ring_2) and (state.msg_receiver == 3)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_receiver == 3)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_2) and (((state.msg_receiver != 3) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_2) and (state.msg_ring != 0)) and (state.msg_ring != 1))
			elif transition == 9:
				return (state.stationClock_retries_2 < state.itd_1)
			else:
				raise IndexError
		elif location == 43:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 44:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1) and (state.errmode_rcvTokenFrom_1_2 != 2)) and state.safe_1)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and ((state.errmode_rcvTokenFrom_1_2 == 2) or (not state.safe_1)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)) and (state.errmode_rcvTokenFrom_1_2 != 2)) and state.safe_1)
			elif transition == 3:
				return (not state.receives_currentlySending_2)
			elif transition == 4:
				return (((state.msg_ring == state.ring_2) and (state.msg_receiver == 3)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_receiver == 3)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_2) and (((state.msg_receiver != 3) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_2) and (state.msg_ring != 0)) and (state.msg_ring != 1))
			elif transition == 9:
				return (state.stationClock_retries_2 < state.itd_1)
			else:
				raise IndexError
		elif location == 45:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 46:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_2 < 0)
			else:
				raise IndexError
		elif location == 47:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 48:
			if transition == 0:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1) and (state.errmode_rcvTokenFrom_1_2 != 2)) and state.safe_1)
			elif transition == 1:
				return (((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and ((state.errmode_rcvTokenFrom_1_2 == 2) or (not state.safe_1)))
			elif transition == 2:
				return (((((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.stationClock_retries_2 >= state.itd_1)) and (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)) and (state.errmode_rcvTokenFrom_1_2 != 2)) and state.safe_1)
			elif transition == 3:
				return (not state.receives_currentlySending_2)
			elif transition == 4:
				return (((state.msg_ring == state.ring_2) and (state.msg_receiver == 3)) and (state.msg_type == 3))
			elif transition == 5:
				return ((((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_receiver == 3)) and (state.msg_type == 2))
			elif transition == 6:
				return ((state.msg_ring == state.ring_2) and (((state.msg_receiver != 3) and (state.msg_type != 5)) or (state.msg_type == 4)))
			elif transition == 7:
				return (((state.msg_ring == state.ring_2) or (state.msg_ring == 1)) and (state.msg_type == 5))
			elif transition == 8:
				return (((state.msg_ring != state.ring_2) and (state.msg_ring != 0)) and (state.msg_ring != 1))
			elif transition == 9:
				return (state.stationClock_retries_2 < state.itd_1)
			else:
				raise IndexError
		elif location == 49:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 50:
			if transition == 0:
				return ((state.errmode_rcvTokenFrom_1_2 == 2) or (not state.safe_1))
			elif transition == 1:
				return ((state.errmode_rcvTokenFrom_1_2 != 2) and state.safe_1)
			elif transition == 2:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 51:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 52:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (state.cRcvInt_2 < 0)
			else:
				raise IndexError
		elif location == 53:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_2 < 0)
			else:
				raise IndexError
		elif location == 54:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 55:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return (state.stationClock_retries_2 >= 1)
			elif transition == 2:
				return (state.stationClock_retries_2 < 1)
			else:
				raise IndexError
		elif location == 56:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 57:
			if transition == 0:
				return (state.rcvTokenFrom_retries_1_errmode_1_2 < 1)
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (state.rcvTokenFrom_retries_1_errmode_1_2 == 1)
			else:
				raise IndexError
		elif location == 58:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_2 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (((state.msg_sender == 1) and (state.msg_ring == state.ring_2)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 1) or (state.msg_ring != state.ring_2))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt_2 < 2)
			else:
				raise IndexError
		elif location == 59:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_2 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (((state.msg_sender == 1) and (state.msg_ring == state.ring_2)) and (state.msg_type != 5))
			elif transition == 3:
				return ((state.msg_sender != 1) or (state.msg_ring != state.ring_2))
			elif transition == 4:
				return (state.cRcvInt_2 < 2)
			else:
				raise IndexError
		elif location == 60:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 61:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 62:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 63:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 64:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 65:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 66:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.cRcvInt_2 < 0)
			else:
				raise IndexError
		elif location == 67:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_2 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 3)) and (state.msg_ring == state.ring_2))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 3)) or (state.msg_ring != state.ring_2))
			elif transition == 4:
				return True
			elif transition == 5:
				return (state.cRcvInt_2 < 2)
			else:
				raise IndexError
		elif location == 68:
			if transition == 0:
				return ((((state.deliverClock <= 0) or (state.deliverClock >= 2)) or (state.msg_type == 0)) and (state.cRcvInt_2 == 2))
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			elif transition == 2:
				return (((state.msg_type == 1) and (state.msg_receiver == 3)) and (state.msg_ring == state.ring_2))
			elif transition == 3:
				return (((state.msg_type != 1) or (state.msg_receiver != 3)) or (state.msg_ring != state.ring_2))
			elif transition == 4:
				return (state.cRcvInt_2 < 2)
			else:
				raise IndexError
		elif location == 69:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 70:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 71:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 72:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 73:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 74:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		elif location == 75:
			if transition == 0:
				return True
			elif transition == 1:
				return (not state.receives_currentlySending_2)
			else:
				raise IndexError
		elif location == 76:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition == 1:
				return True
			elif transition == 2:
				return (state.stationClock_retries_2 < 0)
			else:
				raise IndexError
		elif location == 77:
			if transition == 0:
				return (not state.receives_currentlySending_2)
			elif transition >= 1:
				return True
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Station_2_location
		if location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 8:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		elif location == 11:
			return None
		elif location == 12:
			return None
		elif location == 13:
			return None
		elif location == 14:
			return None
		elif location == 15:
			return None
		elif location == 16:
			return None
		elif location == 17:
			return None
		elif location == 18:
			return None
		elif location == 19:
			return None
		elif location == 20:
			return None
		elif location == 21:
			return None
		elif location == 22:
			return None
		elif location == 23:
			return None
		elif location == 24:
			return None
		elif location == 25:
			return None
		elif location == 26:
			return None
		elif location == 27:
			return None
		elif location == 28:
			return None
		elif location == 29:
			return None
		elif location == 30:
			return None
		elif location == 31:
			return None
		elif location == 32:
			return None
		elif location == 33:
			return None
		elif location == 34:
			return None
		elif location == 35:
			return None
		elif location == 36:
			return None
		elif location == 37:
			return None
		elif location == 38:
			return None
		elif location == 39:
			return None
		elif location == 40:
			return None
		elif location == 41:
			return None
		elif location == 42:
			return None
		elif location == 43:
			return None
		elif location == 44:
			return None
		elif location == 45:
			return None
		elif location == 46:
			return None
		elif location == 47:
			return None
		elif location == 48:
			return None
		elif location == 49:
			return None
		elif location == 50:
			return None
		elif location == 51:
			return None
		elif location == 52:
			return None
		elif location == 53:
			return None
		elif location == 54:
			return None
		elif location == 55:
			return None
		elif location == 56:
			return None
		elif location == 57:
			return None
		elif location == 58:
			return None
		elif location == 59:
			return None
		elif location == 60:
			return None
		elif location == 61:
			return None
		elif location == 62:
			return None
		elif location == 63:
			return None
		elif location == 64:
			return None
		elif location == 65:
			return None
		elif location == 66:
			return None
		elif location == 67:
			return None
		elif location == 68:
			return None
		elif location == 69:
			return None
		elif location == 70:
			return None
		elif location == 71:
			return None
		elif location == 72:
			return None
		elif location == 73:
			return None
		elif location == 74:
			return None
		elif location == 75:
			return None
		elif location == 76:
			return None
		elif location == 77:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Station_2_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Station_2_location
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
			elif transition == 2:
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
			else:
				raise IndexError
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 8:
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
		elif location == 9:
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
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 14:
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
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 16:
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
			else:
				raise IndexError
		elif location == 17:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 18:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 19:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 20:
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
			else:
				raise IndexError
		elif location == 21:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 22:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 23:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 24:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 25:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 26:
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
		elif location == 27:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 28:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 29:
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
		elif location == 30:
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
		elif location == 31:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 32:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 33:
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
		elif location == 34:
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
		elif location == 35:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 36:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 37:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 38:
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
		elif location == 39:
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
		elif location == 40:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 41:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 42:
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
			else:
				raise IndexError
		elif location == 43:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 44:
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
			else:
				raise IndexError
		elif location == 45:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 46:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 47:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 48:
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
			else:
				raise IndexError
		elif location == 49:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 50:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 51:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 52:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 53:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 54:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 55:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 56:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 57:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 58:
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
		elif location == 59:
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
		elif location == 60:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 61:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 62:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 63:
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
		elif location == 64:
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
		elif location == 65:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 66:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 67:
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
		elif location == 68:
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
		elif location == 69:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 70:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 71:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 72:
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
		elif location == 73:
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
		elif location == 74:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 75:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 76:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 77:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		else:
			raise IndexError
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Station_2_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.safe_1 = (state.safe_1 or (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1))
						target_state.Station_2_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.safe_1 = (state.safe_1 or (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1))
						target_state.Station_2_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = 2
						target_state.msg_type = 4
						target_state.msg_ring = state.ring_2
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 5
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 6
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 32
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = 1
						target_state.msg_type = 3
						target_state.msg_ring = state.ring_2
						target_state.stationClock_retries_2 = 0
						target_state.Station_2_location = 8
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 31
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 30
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 29
				elif transition == 4:
					if branch == 0:
						target_state.Station_2_location = 9
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 12
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 11
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 10
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 11
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 12
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 11
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.safe_1 = (state.safe_1 or (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1))
						target_state.Station_2_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 12
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (2 if state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 else 0)
						target_state.Station_2_location = 14
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 13
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.stationClock_retries_2 = 0
						target_state.ring_2 = 1
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 14
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1_2 = state.msg_sender
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.Station_2_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_sender
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.Station_2_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 15
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 16
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 15
			elif location == 16:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.stationClock_retries_2 = 0
						target_state.ring_2 = 1
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 16
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1_2 = state.msg_sender
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.Station_2_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_sender
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.Station_2_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 16
			elif location == 17:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 17
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 18
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 17
			elif location == 18:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 18
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = state.errmode_rcvTokenFrom_1_2
						target_state.msg_type = 1
						target_state.msg_ring = state.ring_2
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 19
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 18
			elif location == 19:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 19
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = True
						target_state.Station_2_location = 20
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 19
			elif location == 20:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 23
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.stationClock_retries_2 = 0
						target_state.ring_2 = 1
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 24
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 27
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 20
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 21
				elif transition == 5:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1_2 = state.msg_sender
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.Station_2_location = 15
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_sender
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (min(1, state.rcvTokenFrom_retries_1_errmode_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.rcvTokenFrom_retries_1_errmode_1_2)
						target_state.Station_2_location = 15
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 15
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 20
			elif location == 21:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 21
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 22
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 21
			elif location == 22:
				if transition == 0:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.ring_2 = 1
						target_state.safe_1 = False
						target_state.Station_2_location = 24
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.Station_2_location = 23
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 22
			elif location == 23:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.itd_1 = 7
						target_state.Station_2_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 23
			elif location == 24:
				if transition == 0:
					if branch == 0:
						target_state.failed = True
						target_state.stationClock_retries_2 = 0
						target_state.Station_2_location = 25
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 24
			elif location == 25:
				if transition == 0:
					if branch == 0:
						target_state.is_offline_3 = True
						target_state.stationClock_retries_2 = 0
						target_state.Station_2_location = 26
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 25
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 25
			elif location == 26:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 26
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 26
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 26
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 26
			elif location == 27:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 27
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = 3
						target_state.msg_type = 5
						target_state.msg_ring = state.ring_2
						target_state.ring_2 = 1
						target_state.Station_2_location = 28
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 27
			elif location == 28:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 28
				elif transition == 1:
					if branch == 0:
						target_state.ring_2 = 3
						target_state.safe_1 = False
						target_state.Station_2_location = 23
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 28
			elif location == 29:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 29
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 8
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 10
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 29
			elif location == 30:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 30
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = True
						target_state.Station_2_location = 31
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 11
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 30
			elif location == 31:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 31
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)
						target_state.Station_2_location = 12
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 31
			elif location == 32:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 32
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = 1
						target_state.msg_type = 2
						target_state.msg_ring = state.ring_2
						target_state.Station_2_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 32
			elif location == 33:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 40
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = True
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 39
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 38
				elif transition == 4:
					if branch == 0:
						target_state.Station_2_location = 34
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 33
			elif location == 34:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = (state.stationClock_retries_2 + 1)
						if target_state.stationClock_retries_2 > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries_2) + " is greater than the upper bound of 13 for variable \"stationClock_retries_2\".")
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 37
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 34
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = True
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 36
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 35
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 34
			elif location == 35:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 35
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 34
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 35
			elif location == 36:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 36
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.stationClock_retries_2 = (state.stationClock_retries_2 + 1)
						if target_state.stationClock_retries_2 > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries_2) + " is greater than the upper bound of 13 for variable \"stationClock_retries_2\".")
						target_state.Station_2_location = 37
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 36
			elif location == 37:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 37
			elif location == 38:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 38
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 35
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 38
			elif location == 39:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 39
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 40
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 36
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 39
			elif location == 40:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 40
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries_2 = (state.stationClock_retries_2 + 1)
						if target_state.stationClock_retries_2 > 13:
							raise OverflowError("Assigned value of " + str(target_state.stationClock_retries_2) + " is greater than the upper bound of 13 for variable \"stationClock_retries_2\".")
						target_state.Station_2_location = 37
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 40
			elif location == 41:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.errmode_rcvTokenFrom_1_2 = (2 if state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 else 0)
						target_state.Station_2_location = 42
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 41
			elif location == 42:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.ring_2 = 1
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 42
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = state.msg_sender
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.Station_2_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_sender
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.Station_2_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 42
			elif location == 43:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 43
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 44
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 43
			elif location == 44:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.ring_2 = 1
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 44
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = state.msg_sender
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.Station_2_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_sender
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.Station_2_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 44
			elif location == 45:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 45
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 46
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 45
			elif location == 46:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 46
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = state.rcvTokenFrom_retries_1_errmode_1_2
						target_state.msg_type = 1
						target_state.msg_ring = state.ring_2
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 47
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 46
			elif location == 47:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 47
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = True
						target_state.Station_2_location = 48
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 47
			elif location == 48:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 51
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.ring_2 = 1
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 75
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.safe_1 = False
						target_state.itd_1 = 0
						target_state.Station_2_location = 76
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 48
				elif transition == 4:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.itd_1 = 0
						target_state.Station_2_location = 49
				elif transition == 5:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = state.msg_sender
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 45
				elif transition == 6:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_ring
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.Station_2_location = 43
				elif transition == 7:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.ring_2 = state.msg_sender
						if target_state.ring_2 < 1:
							raise OverflowError("Assigned value of " + str(target_state.ring_2) + " is less than the lower bound of 1 for variable \"ring_2\".")
						target_state.errmode_rcvTokenFrom_1_2 = (min(1, state.errmode_rcvTokenFrom_1_2) if ((state.msg_ring == 1) or (state.msg_ring == state.ring_2)) else state.errmode_rcvTokenFrom_1_2)
						target_state.Station_2_location = 43
				elif transition == 8:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 43
				elif transition == 9:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 48
			elif location == 49:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 49
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 50
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 49
			elif location == 50:
				if transition == 0:
					if branch == 0:
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.ring_2 = 1
						target_state.safe_1 = False
						target_state.Station_2_location = 75
				elif transition == 1:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.errmode_rcvTokenFrom_1_2 = 0
						target_state.Station_2_location = 51
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 50
			elif location == 51:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.itd_1 = 7
						target_state.Station_2_location = 52
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 51
			elif location == 52:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 53
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 52
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 52
			elif location == 53:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 53
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = 2
						target_state.msg_type = 4
						target_state.msg_ring = state.ring_2
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 54
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 53
			elif location == 54:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 54
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 55
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 54
			elif location == 55:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 55
				elif transition == 1:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.stationClock_retries_2 = 0
						target_state.Station_2_location = 56
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 55
			elif location == 56:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 57
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 56
			elif location == 57:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 66
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 57
				elif transition == 2:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = 1
						target_state.msg_type = 3
						target_state.msg_ring = state.ring_2
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = 0
						target_state.Station_2_location = 58
			elif location == 58:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 65
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 58
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 64
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 63
				elif transition == 4:
					if branch == 0:
						target_state.Station_2_location = 59
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 58
			elif location == 59:
				if transition == 0:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 62
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 59
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 61
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 60
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 59
			elif location == 60:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 60
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 59
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 60
			elif location == 61:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 61
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = False
						target_state.Station_2_location = 62
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 61
			elif location == 62:
				if transition == 0:
					if branch == 0:
						target_state.stationClock_retries_2 = 0
						target_state.safe_1 = (state.safe_1 or (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1))
						target_state.Station_2_location = 41
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 62
			elif location == 63:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 63
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 58
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 60
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 63
			elif location == 64:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 64
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = True
						target_state.Station_2_location = 65
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 61
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 64
			elif location == 65:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 65
				elif transition == 1:
					if branch == 0:
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = (not state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1)
						target_state.Station_2_location = 62
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 65
			elif location == 66:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 66
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = 1
						target_state.msg_type = 2
						target_state.msg_ring = state.ring_2
						target_state.Station_2_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 66
			elif location == 67:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 74
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = True
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 73
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 72
				elif transition == 4:
					if branch == 0:
						target_state.Station_2_location = 68
				elif transition == 5:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 67
			elif location == 68:
				if transition == 0:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (state.rcvTokenFrom_retries_1_errmode_1_2 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1_2) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1_2\".")
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 71
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 68
				elif transition == 2:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1_1 = True
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 70
				elif transition == 3:
					if branch == 0:
						target_state.receives_currentlySending_2 = True
						target_state.Station_2_location = 69
				elif transition == 4:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 68
			elif location == 69:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 69
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 68
				elif transition == 2:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 69
			elif location == 70:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 70
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (state.rcvTokenFrom_retries_1_errmode_1_2 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1_2) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1_2\".")
						target_state.Station_2_location = 71
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 70
			elif location == 71:
				if transition == 0:
					if branch == 0:
						target_state.cRcvInt_2 = 0
						target_state.Station_2_location = 57
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 71
			elif location == 72:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 72
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 67
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 69
				elif transition == 3:
					if branch == 0:
						target_state.cRcvInt_2 = min((state.cRcvInt_2 + 1), 3)
						target_state.Station_2_location = 72
			elif location == 73:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 73
				elif transition == 1:
					if branch == 0:
						target_state.receives_currentlySending_2 = False
						target_state.Station_2_location = 74
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 70
				elif transition == 3:
					if branch == 0:
						target_state.Station_2_location = 73
			elif location == 74:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 74
				elif transition == 1:
					if branch == 0:
						target_state.rcvTokenFrom_retries_1_errmode_1_2 = (state.rcvTokenFrom_retries_1_errmode_1_2 + 1)
						if target_state.rcvTokenFrom_retries_1_errmode_1_2 > 3:
							raise OverflowError("Assigned value of " + str(target_state.rcvTokenFrom_retries_1_errmode_1_2) + " is greater than the upper bound of 3 for variable \"rcvTokenFrom_retries_1_errmode_1_2\".")
						target_state.Station_2_location = 71
				elif transition == 2:
					if branch == 0:
						target_state.Station_2_location = 74
			elif location == 75:
				if transition == 0:
					if branch == 0:
						target_state.failed = True
						target_state.stationClock_retries_2 = 0
						target_state.Station_2_location = 25
				elif transition == 1:
					if branch == 0:
						target_state.Station_2_location = 75
			elif location == 76:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 76
				elif transition == 1:
					if branch == 0:
						target_state.msg_sender = 3
						target_state.msg_receiver = 3
						target_state.msg_type = 5
						target_state.msg_ring = state.ring_2
						target_state.ring_2 = 1
						target_state.Station_2_location = 77
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 76
			elif location == 77:
				if transition == 0:
					if branch == 0:
						target_state.Station_2_location = 77
				elif transition == 1:
					if branch == 0:
						target_state.ring_2 = 3
						target_state.safe_1 = False
						target_state.Station_2_location = 51
				elif transition == 2:
					if branch == 0:
						target_state.stationClock_retries_2 = min((state.stationClock_retries_2 + 1), 13)
						target_state.Station_2_location = 77

# Automaton: Uplinks3
class Uplinks3Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [4, 2, 3, 3, 3, 2, 4, 2, 3, 3, 3, 2, 2, 3, 3, 3, 2]
		self.transition_labels = [[7, 8, 9, 35], [10, 35], [11, 0, 35], [12, 0, 35], [13, 0, 35], [14, 35], [7, 8, 9, 35], [15, 35], [16, 0, 35], [17, 0, 35], [18, 0, 35], [14, 35], [19, 35], [20, 0, 35], [21, 0, 35], [22, 0, 35], [14, 35]]
		self.branch_counts = [[1, 1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Uplinks3_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Uplinks3_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Uplinks3_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Uplinks3_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Uplinks3_location
		if location == 0:
			return True
		elif location == 1:
			if transition == 0:
				return (state.deliverClock == 1)
			elif transition == 1:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 2:
			if transition == 0:
				return (state.msg_sender != 1)
			elif transition == 1:
				return (state.msg_sender == 1)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return (state.msg_sender != 2)
			elif transition == 1:
				return (state.msg_sender == 2)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				return (state.msg_sender != 3)
			elif transition == 1:
				return (state.msg_sender == 3)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 6:
			return True
		elif location == 7:
			if transition == 0:
				return (state.deliverClock == 1)
			elif transition == 1:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return (state.msg_sender != 1)
			elif transition == 1:
				return (state.msg_sender == 1)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return (state.msg_sender != 2)
			elif transition == 1:
				return (state.msg_sender == 2)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return (state.msg_sender != 3)
			elif transition == 1:
				return (state.msg_sender == 3)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return (state.deliverClock == 1)
			elif transition == 1:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return (state.msg_sender != 1)
			elif transition == 1:
				return (state.msg_sender == 1)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return (state.msg_sender != 2)
			elif transition == 1:
				return (state.msg_sender == 2)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return (state.msg_sender != 3)
			elif transition == 1:
				return (state.msg_sender == 3)
			elif transition == 2:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		elif location == 16:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.deliverClock < 1)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Uplinks3_location
		if location == 0:
			return None
		elif location == 1:
			return None
		elif location == 2:
			return None
		elif location == 3:
			return None
		elif location == 4:
			return None
		elif location == 5:
			return None
		elif location == 6:
			return None
		elif location == 7:
			return None
		elif location == 8:
			return None
		elif location == 9:
			return None
		elif location == 10:
			return None
		elif location == 11:
			return None
		elif location == 12:
			return None
		elif location == 13:
			return None
		elif location == 14:
			return None
		elif location == 15:
			return None
		elif location == 16:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Uplinks3_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Uplinks3_location
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
			elif transition == 2:
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
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 14:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 15:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			else:
				raise IndexError
		elif location == 16:
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
			location = state.Uplinks3_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.deliverClock = 0
						target_state.Uplinks3_location = 12
				elif transition == 1:
					if branch == 0:
						target_state.deliverClock = 0
						target_state.Uplinks3_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.deliverClock = 0
						target_state.Uplinks3_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.Uplinks3_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 3
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 5
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.msg_sender = 0
						target_state.msg_receiver = 0
						target_state.msg_type = 0
						target_state.msg_ring = 0
						target_state.Uplinks3_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.deliverClock = 0
						target_state.Uplinks3_location = 12
				elif transition == 1:
					if branch == 0:
						target_state.deliverClock = 0
						target_state.Uplinks3_location = 7
				elif transition == 2:
					if branch == 0:
						target_state.deliverClock = 0
						target_state.Uplinks3_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.Uplinks3_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 9
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 9
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 10
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 10
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 11
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 11
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.msg_sender = 0
						target_state.msg_receiver = 0
						target_state.msg_type = 0
						target_state.msg_ring = 0
						target_state.Uplinks3_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 11
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 12
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 14
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 14
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 13
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 15
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 15
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 14
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.Uplinks3_location = 16
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 16
				elif transition == 2:
					if branch == 0:
						target_state.Uplinks3_location = 15
			elif location == 16:
				if transition == 0:
					if branch == 0:
						target_state.msg_sender = 0
						target_state.msg_receiver = 0
						target_state.msg_type = 0
						target_state.msg_ring = 0
						target_state.Uplinks3_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.Uplinks3_location = 16

# Automaton: Channels3
class Channels3Automaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [8, 8, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
		self.transition_labels = [[21, 16, 22, 11, 18, 12, 14, 35], [21, 16, 22, 11, 18, 12, 14, 35], [0], [23, 35], [0], [24, 35], [0], [25, 35], [0], [26, 35], [0], [27, 35], [0], [28, 35]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [2], [1, 1], [2], [1, 1], [2], [1, 1], [2], [1, 1], [2], [1, 1], [2], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Channels3_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Channels3_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Channels3_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Channels3_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Channels3_location
		if location == 2 or location == 4 or location == 6 or location == 8 or location == 10 or location == 12:
			return True
		elif location == 0:
			return True
		elif location == 1:
			return True
		elif location == 3:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.c < 0)
			else:
				raise IndexError
		elif location == 5:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.c < 0)
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.c < 0)
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.c < 0)
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.c < 0)
			else:
				raise IndexError
		elif location == 13:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.c < 0)
			else:
				raise IndexError
		else:
			raise IndexError
	
	def get_rate_value(self, state: State, transition: int) -> Optional[float]:
		location = state.Channels3_location
		if location == 2 or location == 4 or location == 6 or location == 8 or location == 10 or location == 12:
			return None
		elif location == 0:
			return None
		elif location == 1:
			return None
		elif location == 3:
			return None
		elif location == 5:
			return None
		elif location == 7:
			return None
		elif location == 9:
			return None
		elif location == 11:
			return None
		elif location == 13:
			return None
		else:
			raise IndexError
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Channels3_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Channels3_location
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
		elif location == 2:
			if transition == 0:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			else:
				raise IndexError
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 4:
			if transition == 0:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
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
			if transition == 0:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			else:
				raise IndexError
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 8:
			if transition == 0:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			else:
				raise IndexError
		elif location == 9:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 10:
			if transition == 0:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			else:
				raise IndexError
		elif location == 11:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			else:
				raise IndexError
		elif location == 12:
			if transition == 0:
				if branch == 0:
					return (9 / 10)
				elif branch == 1:
					return (1 / 10)
			else:
				raise IndexError
		elif location == 13:
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
			location = state.Channels3_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 12
				elif transition == 1:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 10
				elif transition == 2:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 8
				elif transition == 3:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 6
				elif transition == 4:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 4
				elif transition == 5:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 2
				elif transition == 6:
					if branch == 0:
						target_state.Channels3_location = 1
				elif transition == 7:
					if branch == 0:
						target_state.Channels3_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 12
				elif transition == 1:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 10
				elif transition == 2:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 8
				elif transition == 3:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 6
				elif transition == 4:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 4
				elif transition == 5:
					if branch == 0:
						target_state.c = 0
						target_state.Channels3_location = 2
				elif transition == 6:
					if branch == 0:
						target_state.Channels3_location = 1
				elif transition == 7:
					if branch == 0:
						target_state.Channels3_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 3
					elif branch == 1:
						target_state.Channels3_location = 1
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Channels3_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 5
					elif branch == 1:
						target_state.Channels3_location = 1
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Channels3_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 7
					elif branch == 1:
						target_state.Channels3_location = 1
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Channels3_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 9
					elif branch == 1:
						target_state.Channels3_location = 1
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Channels3_location = 9
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 11
					elif branch == 1:
						target_state.Channels3_location = 1
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Channels3_location = 11
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 13
					elif branch == 1:
						target_state.Channels3_location = 1
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.Channels3_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Channels3_location = 13

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[35]]
		self.branch_counts = [[1]]
	
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
			return True
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
						target_state.deliverClock = min((state.deliverClock + 1), 3)
						target_state.c = min((state.c + 1), 1)

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1, -1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "model_type", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Station", "_aut_Station_1", "_aut_Station_2", "_aut_Uplinks3", "_aut_Channels3", "_aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.model_type = "mdp"
		self.transition_labels = { 0: "τ", 1: "msg_arrives_N", 2: "send", 3: "send_done", 4: "reseto", 5: "receive", 6: "msg_arrives_Y", 7: "send1", 8: "send2", 9: "send3", 10: "send_done3", 11: "c3t1", 12: "c3t2", 13: "c3t3", 14: "msg_arrives", 15: "send_done2", 16: "c2t1", 17: "c2t2", 18: "c2t3", 19: "send_done1", 20: "c1t1", 21: "c1t2", 22: "c1t3", 23: "receive2b", 24: "receive3b", 25: "receive1b", 26: "receive3a", 27: "receive1a", 28: "receive2a", 29: "reseto1", 30: "reseto2", 31: "reseto3", 32: "receive1", 33: "receive2", 34: "receive3", 35: "tick" }
		self.sync_vectors = [[0, -1, -1, -1, -1, -1, 0], [-1, 0, -1, -1, -1, -1, 0], [-1, -1, 0, -1, -1, -1, 0], [-1, -1, -1, 0, -1, -1, 0], [-1, -1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, -1, 0, 0], [4, -1, -1, -1, -1, -1, 29], [-1, 4, -1, -1, -1, -1, 30], [-1, -1, 4, -1, -1, -1, 31], [-1, -1, -1, 13, -1, -1, 13], [-1, -1, -1, 17, -1, -1, 17], [-1, -1, -1, 20, -1, -1, 20], [2, -1, -1, 7, -1, -1, 7], [3, -1, -1, 19, -1, -1, 19], [-1, 2, -1, 8, -1, -1, 8], [-1, 3, -1, 15, -1, -1, 15], [-1, -1, 2, 9, -1, -1, 9], [-1, -1, 3, 10, -1, -1, 10], [1, 1, 1, 14, 14, -1, 14], [1, 1, 6, 14, 14, -1, 14], [1, 6, 1, 14, 14, -1, 14], [1, 6, 6, 14, 14, -1, 14], [6, 1, 1, 14, 14, -1, 14], [6, 1, 6, 14, 14, -1, 14], [6, 6, 1, 14, 14, -1, 14], [6, 6, 6, 14, 14, -1, 14], [5, -1, -1, -1, 25, -1, 32], [5, -1, -1, -1, 27, -1, 32], [-1, 5, -1, -1, 23, -1, 33], [-1, 5, -1, -1, 28, -1, 33], [-1, -1, 5, -1, 24, -1, 34], [-1, -1, 5, -1, 26, -1, 34], [-1, -1, -1, 21, 21, -1, 21], [-1, -1, -1, 22, 22, -1, 22], [-1, -1, -1, 16, 16, -1, 16], [-1, -1, -1, 18, 18, -1, 18], [-1, -1, -1, 11, 11, -1, 11], [-1, -1, -1, 12, 12, -1, 12], [35, 35, 35, 35, 35, 35, 35]]
		self.properties = [
			Property("MinFailed", PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])])),
			Property("MinOffline1", PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [1])])])),
			Property("MaxOffline1", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [1])])])),
			Property("MinOffline2", PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [2])])])),
			Property("MaxOffline2", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [2])])])),
			Property("MinOffline3", PropertyExpression("p_min", [PropertyExpression("eventually", [PropertyExpression("ap", [3])])])),
			Property("MaxOffline3", PropertyExpression("p_max", [PropertyExpression("eventually", [PropertyExpression("ap", [3])])]))
		]
		self.variables = [
			VariableInfo("msg_sender", None, "int", 0, 3),
			VariableInfo("msg_receiver", None, "int", 0, 3),
			VariableInfo("msg_type", None, "int", 0, 6),
			VariableInfo("msg_ring", None, "int", 0, 3),
			VariableInfo("deliverClock", None, "int", 0, 3),
			VariableInfo("failed", None, "bool"),
			VariableInfo("is_offline_1", None, "bool"),
			VariableInfo("is_offline_2", None, "bool"),
			VariableInfo("is_offline_3", None, "bool"),
			VariableInfo("iter", None, "int", 0, 3),
			VariableInfo("c", None, "int", 0, 1),
			VariableInfo("Station_location", 0, "int", 0, 77),
			VariableInfo("is_offline_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1", 0, "bool"),
			VariableInfo("rcvTokenFrom_retries_1_errmode_1", 0, "int", 0, 3),
			VariableInfo("receives_currentlySending", 0, "bool"),
			VariableInfo("stationClock_retries", 0, "int", 0, 13),
			VariableInfo("safe_initToken", 0, "bool"),
			VariableInfo("errmode_rcvTokenFrom_1", 0, "int", 0, 3),
			VariableInfo("cRcvInt", 0, "int", 0, 3),
			VariableInfo("ring", 0, "int", 1, 3),
			VariableInfo("Station_1_location", 1, "int", 0, 77),
			VariableInfo("initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1", 1, "bool"),
			VariableInfo("rcvTokenFrom_retries_1_errmode_1", 1, "int", 0, 3),
			VariableInfo("receives_currentlySending", 1, "bool"),
			VariableInfo("stationClock_retries", 1, "int", 0, 13),
			VariableInfo("errmode_rcvTokenFrom_1", 1, "int", 0, 3),
			VariableInfo("cRcvInt", 1, "int", 0, 3),
			VariableInfo("ring", 1, "int", 1, 3),
			VariableInfo("safe", 1, "bool"),
			VariableInfo("itd", 1, "int", 0, 12),
			VariableInfo("Station_2_location", 2, "int", 0, 77),
			VariableInfo("initToken_txError_receivedIntToken_rcvAck_rcvAck_1_txError_1_receivedIntToken_1", 2, "bool"),
			VariableInfo("rcvTokenFrom_retries_1_errmode_1", 2, "int", 0, 3),
			VariableInfo("receives_currentlySending", 2, "bool"),
			VariableInfo("stationClock_retries", 2, "int", 0, 13),
			VariableInfo("errmode_rcvTokenFrom_1", 2, "int", 0, 3),
			VariableInfo("cRcvInt", 2, "int", 0, 3),
			VariableInfo("ring", 2, "int", 1, 3),
			VariableInfo("safe", 2, "bool"),
			VariableInfo("itd", 2, "int", 0, 12),
			VariableInfo("Uplinks3_location", 3, "int", 0, 16),
			VariableInfo("Channels3_location", 4, "int", 0, 13)
		]
		self._aut_Station = StationAutomaton(self)
		self._aut_Station_1 = Station_1Automaton(self)
		self._aut_Station_2 = Station_2Automaton(self)
		self._aut_Uplinks3 = Uplinks3Automaton(self)
		self._aut_Channels3 = Channels3Automaton(self)
		self._aut_GlobalSync = GlobalSyncAutomaton(self)
		self.components = [self._aut_Station, self._aut_Station_1, self._aut_Station_2, self._aut_Uplinks3, self._aut_Channels3, self._aut_GlobalSync]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.msg_sender = 0
		state.msg_receiver = 0
		state.msg_type = 0
		state.msg_ring = 0
		state.deliverClock = 0
		state.failed = False
		state.is_offline_1 = False
		state.is_offline_2 = False
		state.is_offline_3 = False
		state.iter = 0
		state.c = 0
		self._aut_Station.set_initial_values(state)
		self._aut_Station_1.set_initial_values(state)
		self._aut_Station_2.set_initial_values(state)
		self._aut_Uplinks3.set_initial_values(state)
		self._aut_Channels3.set_initial_values(state)
		self._aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_Station.set_initial_transient_values(transient)
		self._aut_Station_1.set_initial_transient_values(transient)
		self._aut_Station_2.set_initial_transient_values(transient)
		self._aut_Uplinks3.set_initial_transient_values(transient)
		self._aut_Channels3.set_initial_transient_values(transient)
		self._aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return (state.failed and (state.iter <= 2))
		elif expression == 1:
			return (((state.is_offline_1 and (not state.is_offline_2)) and (not state.is_offline_3)) and (state.iter <= 2))
		elif expression == 2:
			return ((((not state.is_offline_1) and state.is_offline_2) and (not state.is_offline_3)) and (state.iter <= 2))
		elif expression == 3:
			return ((((not state.is_offline_1) and (not state.is_offline_2)) and state.is_offline_3) and (state.iter <= 2))
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return (state.failed and (state.iter <= 2))
		elif expression == 1:
			return (((state.is_offline_1 and (not state.is_offline_2)) and (not state.is_offline_3)) and (state.iter <= 2))
		elif expression == 2:
			return ((((not state.is_offline_1) and state.is_offline_2) and (not state.is_offline_3)) and (state.iter <= 2))
		elif expression == 3:
			return ((((not state.is_offline_1) and (not state.is_offline_2)) and state.is_offline_3) and (state.iter <= 2))
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Station.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Station_1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Station_2.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Uplinks3.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Channels3.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_GlobalSync.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_Station = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Station.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Station.get_guard_value(state, i):
				trans_Station[self._aut_Station.get_transition_label(state, i)].append(i)
		trans_Station_1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Station_1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Station_1.get_guard_value(state, i):
				trans_Station_1[self._aut_Station_1.get_transition_label(state, i)].append(i)
		trans_Station_2 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Station_2.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Station_2.get_guard_value(state, i):
				trans_Station_2[self._aut_Station_2.get_transition_label(state, i)].append(i)
		trans_Uplinks3 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Uplinks3.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Uplinks3.get_guard_value(state, i):
				trans_Uplinks3[self._aut_Uplinks3.get_transition_label(state, i)].append(i)
		trans_Channels3 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Channels3.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Channels3.get_guard_value(state, i):
				trans_Channels3[self._aut_Channels3.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self._aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1, -1, -1]]
			# Station
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Station[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Station[sv[0]][0]
						for i in range(1, len(trans_Station[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Station[sv[0]][i]
			# Station_1
			if synced is not None:
				if sv[1] != -1:
					if len(trans_Station_1[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_Station_1[sv[1]][0]
						for i in range(1, len(trans_Station_1[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_Station_1[sv[1]][i]
			# Station_2
			if synced is not None:
				if sv[2] != -1:
					if len(trans_Station_2[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_Station_2[sv[2]][0]
						for i in range(1, len(trans_Station_2[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_Station_2[sv[2]][i]
			# Uplinks3
			if synced is not None:
				if sv[3] != -1:
					if len(trans_Uplinks3[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_Uplinks3[sv[3]][0]
						for i in range(1, len(trans_Uplinks3[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_Uplinks3[sv[3]][i]
			# Channels3
			if synced is not None:
				if sv[4] != -1:
					if len(trans_Channels3[sv[4]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][4] = trans_Channels3[sv[4]][0]
						for i in range(1, len(trans_Channels3[sv[4]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][4] = trans_Channels3[sv[4]][i]
			# GlobalSync
			if synced is not None:
				if sv[5] != -1:
					if len(trans_GlobalSync[sv[5]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][5] = trans_GlobalSync[sv[5]][0]
						for i in range(1, len(trans_GlobalSync[sv[5]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][5] = trans_GlobalSync[sv[5]][i]
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
		combs = [[-1, -1, -1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_Station.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Station.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Station.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_Station_1.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_Station_1.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Station_1.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_Station_2.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_Station_2.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Station_2.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_Uplinks3.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_Uplinks3.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Uplinks3.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		if transition.transitions[4] != -1:
			existing = len(combs)
			branch_count = self._aut_Channels3.get_branch_count(state, transition.transitions[4])
			for i in range(1, branch_count):
				probability = self._aut_Channels3.get_probability_value(state, transition.transitions[4], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][4] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Channels3.get_probability_value(state, transition.transitions[4], 0)
			for i in range(existing):
				combs[i][4] = 0
				probs[i] *= probability
		if transition.transitions[5] != -1:
			existing = len(combs)
			branch_count = self._aut_GlobalSync.get_branch_count(state, transition.transitions[5])
			for i in range(1, branch_count):
				probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[5], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][5] = i
					probs.append(probs[j] * probability)
			probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[5], 0)
			for i in range(existing):
				combs[i][5] = 0
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
				self._aut_Station.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_Station_1.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_Station_2.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_Uplinks3.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			if transition.transitions[4] != -1:
				self._aut_Channels3.jump(state, transient, transition.transitions[4], branch.branches[4], i, target_state, target_transient)
			if transition.transitions[5] != -1:
				self._aut_GlobalSync.jump(state, transient, transition.transitions[5], branch.branches[5], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
