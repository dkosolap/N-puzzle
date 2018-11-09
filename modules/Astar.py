
from modules.State import *
from modules.Manhattan import *

class Astar:
	def __init__(self, res):
		self.hevristik = Manhattan(res)
		self.totalSize = 0
		self.maxSize = 0
		self.res = res
		pass

	def search(self, startState):
		self.closeList = list()
		self.openList = list()
		startState.setG( 0 )
		startState.setH(self.hevristik.getH(startState))
		self.openList.append(startState)
		# print(startState)

		while (len(self.openList)):
			current = self.getStateWithMinF(self.openList)
			# print(len(self.openList), len(self.closeList))
			if (self.res == current):
				# closeStateLen = len(closeList)
				return self.completeSolution(current.getParent())
			self.openList.remove(current)
			self.closeList.append(current)
			neighbors = current.getNeighbors()
			for x in neighbors:
				if (self.closeList.count(x)):
					continue
				g = current.getG() + current.getDistance()
				isGBetter = False 
				tmp = self.openList.count(x)
				# print(tmp)
				if (tmp != -1):
					x.setH( self.hevristik.getH(x) )
					self.openList.append(x)
					self.totalSize += 1
					count = len(self.openList)
					if (count > self.maxSize):
						self.maxSize = count
					isGBetter = True
				else:
					isGBetter = g < x.getG() 
			# return
				if isGBetter:
					x.setParent(current)
					x.setG(g)
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
		resList = list()
		while(state.getParent()):
			resList.append(state)
			state = state.getParent()
		return resList


		