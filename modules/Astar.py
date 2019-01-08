

from modules.State import *
from modules.Manhattan import *
from modules.LinearConflict import *
from modules.CornerTiles import *


class Astar:
	def __init__(self, res, flag):
		if flag == "-ct":
			print("Corner tiles")
			self.hevristik = CornerTiles(res)
		elif flag == "-lc":
			print("Linear conflict")
			self.hevristik = LinearConflict(res)
		else:
			print("Manhattan distance")
			self.hevristik = Manhattan(res)
		self.totalSize = 0
		self.maxSize = 0
		self.res = res
		pass

	def search(self, startState):
		closeSet = dict()
		self.openList = dict()
		startState.setG( 0 )
		startState.setH(self.hevristik.getH(startState))
		self.openList[startState.hash] = startState
		while (len(self.openList)):
			current = self.getStateWithMinF(self.openList)
			if (self.res == current):
				return self.completeSolution(current.getParent())
			del self.openList[current.hash]
			closeSet[current.hash] = current
			neighbors = current.getNeighbors()
			for neighbor in neighbors:
				if neighbor.hash in closeSet:
					continue
				g = current.getG() + current.getDistance()
				isGBetter = False 
				if not neighbor.hash in self.openList:
					neighbor.setH( self.hevristik.getH(neighbor) )
					self.openList[neighbor.hash] = neighbor
					self.totalSize += 1
					count = len(self.openList)
					if (count > self.maxSize):
						self.maxSize = count
					isGBetter = True
				else:
					isGBetter = g <= neighbor.getG() 
				if isGBetter:
					neighbor.setParent(current)
					neighbor.setG(g)
		return False

	def getStateWithMinF(self, states):
		res = False
		val = 100500
		for x in states:
			if states[x].getF() <= val:
				val = states[x].getF()
				res = states[x]
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