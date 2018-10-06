
from modules.Color import *

class Matrix:
	def __init__(self, map):
		self.map = map
		self.y, self.x = self.getCoordinate()
		self.size = len(map)
	def getCoordinate(self):
		for i, x in enumerate(self.map):
			for j, y in enumerate(x):
				if (y == 0):
					return i, j
	def moveTop(self):
		if (self.y != 0):
			tmp = self.map[self.y][self.x]
			self.map[self.y][self.x] = self.map[self.y - 1][self.x]
			self.map[self.y - 1][self.x] = tmp
			self.y -= 1
	def moveBottom(self):
		if (self.y != self.size - 1):
			tmp = self.map[self.y][self.x]
			self.map[self.y][self.x] = self.map[self.y + 1][self.x]
			self.map[self.y + 1][self.x] = tmp
			self.y += 1
	def moveLeft(self):
		if (self.x != 0):
			tmp = self.map[self.y][self.x]
			self.map[self.y][self.x] = self.map[self.y][self.x - 1]
			self.map[self.y][self.x - 1] = tmp
			self.x -= 1
	def moveRight(self):
		if (self.x != self.size - 1):
			tmp = self.map[self.y][self.x]
			self.map[self.y][self.x] = self.map[self.y][self.x + 1]
			self.map[self.y][self.x + 1] = tmp
			self.x += 1
	def __str__(self):
		res = ""
		for x in self.map:
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