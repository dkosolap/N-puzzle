
from modules.State import *
from modules.Manhattan import *

class Astar:
	def __init__(self, res):
		self.hevristik = Manhattan(res)
		pass

	def search(self, startState):
		self.closeList = list()
		self.openList = list()
		self.openList.append(startState)
		startState.setG(0)
		startState.setH(self.hevristik.getH(startState))
		# print(startState)

		while (len(self.openList)):
			current = self.getStateWithMinF(self.openList)
			# if (self.rules.isFinish(current)):
				# closeStateLen = len(closeList)
				# return self.completeSolution(current)
			self.openList.remove(current)
			self.closeList.append(current)
			neighbors = current.getNeighbors()
			for x in neighbors:
				if (self.closeList.count(x)):
					continue
			# 	g = state.getG() + self.rules.getDistance(state, x)
			# 	isGBetter = False
			# 	if (openList.count(x) != -1):
			# 		x.setH(self.rules.getG(x))
			# 		openList.append(x)
			# 		isGBetter = True
			# 	else:
			# 		isGBetter = g < x.getG() 
			# 	if isGBetter:
			# 		x.setParent(state)
			# 		x.setG(g)
			return
		return False

	def getStateWithMinF(self, states):
		res = False
		val = 100500
		for x in states:
			if x.getF() < val:
				val = x.getF()
				res = x
		return res

	def completeSolution(self, state):
		return state


		