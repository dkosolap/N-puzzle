from modules.State import State

class LinearConflict:
	def __init__(self, result):
		self.result = result
		self.len = len(result.matrix)
		self.len = (self.len * self.len)
	def getH(self, state):
		res = 0
		for i in range(self.len):
			x1, y1 = (self.getIndex(self.result, i))
			x2, y2 = (self.getIndex(state, i))
			res += abs(x1 - x2) + abs(y1 - y2)
		return res + self.getlinConf(state);
	def getlinConf(self, state):
		res = 0
		for j in range(len(self.result.matrix)):
			for i in range(len(self.result.matrix[j]) - 1):
				x1, y1 = (self.getIndex(state, i))
				x2, y2 = (self.getIndex(state, i + 1))
				if y1 == y2 and x1 > x2:
					res += 1
		# print(res);
		return res
	def getIndex(self, exc, num):
		for i, row in enumerate(exc.matrix):
			for j, col in enumerate(row):
				if col is num:
					return i, j