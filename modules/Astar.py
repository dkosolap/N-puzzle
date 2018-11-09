






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
		self.closeSet = dict()
		self.openList = list()
		startState.setG( 0 )
		startState.setH(self.hevristik.getH(startState))
		self.openList.append(startState)
		while (len(self.openList)):
			current = self.getStateWithMinF(self.openList)
			if (self.res == current):
				return self.completeSolution(current.getParent())
			self.openList.remove(current)
			self.closeSet[current.hash] = current
			neighbors = current.getNeighbors()
			for neighbor in neighbors:
				if(self.closeSet.get(neighbor.hash)):
					continue
				g = current.getG() + current.getDistance()
				isGBetter = False 
				if (self.openList.count(neighbor) != -1):
					# print("1here")
					neighbor.setH( self.hevristik.getH(neighbor) )
					self.openList.append(neighbor)
					self.totalSize += 1
					count = len(self.openList)
					if (count > self.maxSize):
						self.maxSize = count
					isGBetter = True
				else:
					print("here")
					isGBetter = g <= neighbor.getG() 
				if isGBetter:
					# print("2here")
					neighbor.setParent(current)
					neighbor.setG(g)
		return False

	def getStateWithMinF(self, states):
		res = False
		val = 100500
		for x in states:
			if x.getF() <= val:
				val = x.getF()
				res = x
		return res

	def completeSolution(self, state):
		resList = list()
		while(state.getParent()):
			resList.append(state)
			state = state.getParent()
		return resList


	def 	find( self, state, listState ):
		for x in listState:
			if ( x  == state ):
				return ( True )
		return ( False )