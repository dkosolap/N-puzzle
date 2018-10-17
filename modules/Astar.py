
from modules.State import *

class Astar:
	def __init__(self, rules):
		self.rules = rules

	def search(self, startState):
		self.closeList = list()
		self.openList = list()
		self.openList.append(startState)
		startState.setG(0)
		startState.setH(self.rules.getH(startState))

		while (len(open)):
			state = self.getStateWithMinF(openList)
			if (self.rules.isFinish(state)):
				closeStateLen = len(closeList)
				return self.completeSolution(state)
			openList.remove(state)
			closeList.append(state)
			neighbors = self.rules.getNeighbors()
			for x in neighbors:
				if (closeList.count(x) != -1):
					continue
				g = state.getG() + self.rules.getDistance(state, x)
				isGBetter = False
				if (openList.count(x) != -1):
					x.setH(self.rules.getG(x))
					openList.append(x)
					isGBetter = True
				else:
					isGBetter = g < x.getG() 
				if isGBetter:
					x.setParent(state)
					x.setG(g)
		return False
	def getStateWithMinF(self, states):
		res = False
		val = -1
		for x in states:
			if x.getF() < val:
				val = x.getF()
				res = x
		return res

	def completeSolution(self, state):
		return state


		