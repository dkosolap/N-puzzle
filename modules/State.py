

class State():
	def __init__(self, matrix, count=0):
		self._matrix = matrix
		self._g = 0
		self._h = 0
		self._f = 0
		self._parent
		
	def getF():
		return self._h + self._g
	def getH():
		return self._h
	def getG():
		return self._g
	def setG(g):
		self._g = g
	def setH(h):
		self._h = h
	def getParent():
		return self._parent
	def setParent(parent):
		self._parent = parent
	def equals(exc):
		pass


	# Rules
	def getNeighbors(currState):
		# stateList
		pass
	def getDistance(aState, bState):
		# int
		pass
	def getHRules(state):
		# int
		pass
	def isTerminate(state):
		# boolean
		pass