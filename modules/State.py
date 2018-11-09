from modules.Color import *
import numpy as np
import copy
import hashlib


class State():
	def __init__(self, matrix, count=0):
		self.matrix = matrix
		self.y, self.x = self.getCoordinate()
		self.size = len(matrix)
		self._parent = False
		self._g = 0
		self._h = 0
		self._f = 0
		self.hash = self.hashMatrix()
		# self._parent
		
	def getF(self):
		return self._h + self._g
	def getH(self):
		return self._h
	def getG(self):
		return self._g
	def setG(self, g):
		self._g = g
	def setH(self, h):
		self._h = h
	def getParent(self):
		return self._parent
	def setParent(self, parent):
		self._parent = parent
	def equals(self, exc):
		pass
	def __eq__(self, exc):
		return np.array_equal(self.matrix, exc.matrix)


	def getNeighbors(currState):
		res = list()
		cp = State(copy.deepcopy(currState.matrix))
		cp.moveLeft()
		if (currState != cp):
			res.append(cp)
		cp = State(copy.deepcopy(currState.matrix))
		cp.moveTop()
		if (currState != cp):
			res.append(cp)
		cp = State(copy.deepcopy(currState.matrix))
		cp.moveRight()
		if (currState != cp):
			res.append(cp)
		cp = State(copy.deepcopy(currState.matrix))
		cp.moveBottom()
		if (currState != cp):
			res.append(cp)
		return res
	def getDistance(self):
		return 1


	def __str__(self):
		res = ("F:" + str(self.getF()) + " H:" + str(self._h) + " G:" + str(self._g) + "\n")
		for x in self.matrix:
			for y in x:
				if y < 10:
					if y == 0:
						res += " " + bcolors.OKGREEN + str(y) + bcolors.ENDC + " "
					else:
						res += " " + str(y) + " "
				else:
					res += str(y) + " "
			res += "\n"
		return res

# 	=================================
	def 	hashMatrix( self ):
		res = str(self.size)
		for x in self.matrix:
			for y in x:
				res += str(y)
		return res
# 	=================================
	def getCoordinate(self):
		for i, x in enumerate(self.matrix):
			for j, y in enumerate(x):
				if (y == 0):
					return i, j
	def moveTop(self):
		if (self.y != 0):
			tmp = self.matrix[self.y][self.x]
			self.matrix[self.y][self.x] = self.matrix[self.y - 1][self.x]
			self.matrix[self.y - 1][self.x] = tmp
			self.y -= 1
			self.hash = self.hashMatrix()
			
			# self._g += 1
	def moveBottom(self):
		if (self.y != self.size - 1):
			tmp = self.matrix[self.y][self.x]
			self.matrix[self.y][self.x] = self.matrix[self.y + 1][self.x]
			self.matrix[self.y + 1][self.x] = tmp
			self.y += 1
			self.hash = self.hashMatrix()
			
			# self._g += 1
	def moveLeft(self):
		if (self.x != 0):
			tmp = self.matrix[self.y][self.x]
			self.matrix[self.y][self.x] = self.matrix[self.y][self.x - 1]
			self.matrix[self.y][self.x - 1] = tmp
			self.x -= 1
			self.hash = self.hashMatrix()
			
			# self._g += 1
	def moveRight(self):
		if (self.x != self.size - 1):
			tmp = self.matrix[self.y][self.x]
			self.matrix[self.y][self.x] = self.matrix[self.y][self.x + 1]
			self.matrix[self.y][self.x + 1] = tmp
			self.x += 1
			self.hash = self.hashMatrix()
			
			# self._g += 1