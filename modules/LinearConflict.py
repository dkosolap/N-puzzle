from modules.State import State

class LinearConflict:
	def __init__(self, result):
		self.result = result
		self.lenRow = len(result.matrix)
		self.len = (self.lenRow * self.lenRow)
	def getH(self, state):
		res = 0
		for i in range(self.len):
			x1, y1 = (self.getIndex(self.result, i))
			x2, y2 = (self.getIndex(state, i))
			res += abs(x1 - x2) + abs(y1 - y2)
		return res + self.getlinConf(state);
	def getlinConf(self, state):
		res = 0
		delta = 2
		# horizontal
		for i, y in enumerate(state.matrix):
			for k, x in enumerate(y):
				j = k + 1
				while (j < self.lenRow):
					x1, y1 = (self.getIndex(self.result, y[k]))
					x2, y2 = (self.getIndex(self.result, y[j]))
					if y1 == y2 and x1 > x2:
						res += delta
					j += 1
		# vertical
		i = 0
		matrix = state.matrix
		while (i < self.lenRow):
			j = 0
			while j < self.lenRow:
				k = j + 1
				while k < self.lenRow:
					x1, y1 = (self.getIndex(self.result, matrix[j][i]))
					x2, y2 = (self.getIndex(self.result, matrix[k][i]))
					if x1 == x2 and y1 > y2:
						res += delta
					k += 1
				j += 1
			i += 1
		return res
	def getIndex(self, exc, num):
		for i, row in enumerate(exc.matrix):
			for j, col in enumerate(row):
				if col is num:
					return i, j