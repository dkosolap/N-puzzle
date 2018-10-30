
from modules.State import *
from modules.Manhattan import *

class Astar:
	def __init__(self, res):
		self.hevristik = Manhattan(res)
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

			# if (self.rules.isFinish(current)):
				# closeStateLen = len(closeList)
				# return self.completeSolution(current)
			self.openList.remove(current)
			self.closeList.append(current)
			neighbors = current.getNeighbors()
			for x in neighbors:
				if (self.closeList.count(x)):
					continue
				g = current.getG() + current.getDistance()
				# print("gGlobe", g, current.getG(), current.getDistance())
				isGBetter = False
				if (self.openList.count(x) != -1):
					x.setH( self.hevristik.getH(x) )
					print("Here", x)
					self.openList.append(x)
					isGBetter = True
			
			print(len(self.openList))
			return
				# else:
				# 	isGBetter = g < x.getG() 
			# 	if isGBetter:
			# 		x.setParent(state)
			# 		x.setG(g)
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


		