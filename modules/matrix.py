
from modules.Color import *
import numpy as np


class Matrix:
	def __init__(self, matrix):
		self.matrix = matrix
		self.y, self.x = self.getCoordinate()
		self.size = len(matrix)
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
	def moveBottom(self):
		if (self.y != self.size - 1):
			tmp = self.matrix[self.y][self.x]
			self.matrix[self.y][self.x] = self.matrix[self.y + 1][self.x]
			self.matrix[self.y + 1][self.x] = tmp
			self.y += 1
	def moveLeft(self):
		if (self.x != 0):
			tmp = self.matrix[self.y][self.x]
			self.matrix[self.y][self.x] = self.matrix[self.y][self.x - 1]
			self.matrix[self.y][self.x - 1] = tmp
			self.x -= 1
	def moveRight(self):
		if (self.x != self.size - 1):
			tmp = self.matrix[self.y][self.x]
			self.matrix[self.y][self.x] = self.matrix[self.y][self.x + 1]
			self.matrix[self.y][self.x + 1] = tmp
			self.x += 1
	def len(self):
		return len(self.matrix)
	def __eq__(self, exc):
		return np.array_equal(self.matrix, exc.matrix)
	def __str__(self):
		res = ""
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