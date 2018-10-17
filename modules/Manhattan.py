from modules.State import State

class Manhattan:
	def __init__(self, result):
		self.result = result
		self.len = result.len()
		self.len = (self.len * self.len)
	def getH(self, state):
		res = 0
		for i in range(self.len):
			x1, y1 = (self.getIndex(self.result, i))
			x2, y2 = (self.getIndex(state, i))
			res += abs(x1 - x2) + abs(y1 - y2)
		return res
	def getIndex(self, exc, num):
		for i, row in enumerate(exc.matrix):
			for j, col in enumerate(row):
				if col is num:
					return i, j