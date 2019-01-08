from modules.State import State

class CornerTiles:
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
		return res + self.getCornerTiles(state)

	def getCornerTiles(self, state):
		res = 0
		delta = 2
		corner = self.lenRow - 1

		# Left Top
		if self.result.matrix[0][0] != state.matrix[0][0] and self.result.matrix[0][1] == state.matrix[0][1]:
			res += delta
		if self.result.matrix[0][0] != state.matrix[0][0] and self.result.matrix[1][0] == state.matrix[1][0]:
			res += delta
		# Right Top
		if self.result.matrix[0][corner] != state.matrix[0][corner] and self.result.matrix[0][corner - 1] == state.matrix[0][corner - 1]:
			res += delta
		if self.result.matrix[0][corner] != state.matrix[0][corner] and self.result.matrix[1][corner] == state.matrix[1][corner]:
			res += delta
		# Right Bottom
		# if self.result.matrix[corner][corner] != state.matrix[corner][corner] and self.result.matrix[corner][corner - 1] == state.matrix[corner][corner - 1]:
		# 	res += delta
		# if self.result.matrix[corner][corner] != state.matrix[corner][corner] and self.result.matrix[corner - 1][corner] == state.matrix[corner - 1][corner]:
		# 	res += delta
		# left Bottom
		if self.result.matrix[corner][0] != state.matrix[corner][0] and self.result.matrix[corner][1] == state.matrix[corner][1]:
			res += delta
		if self.result.matrix[corner][0] != state.matrix[corner][0] and self.result.matrix[corner - 1][0] == state.matrix[corner - 1][0]:
			res += delta
		return res

	def getIndex(self, exc, num):
		for i, row in enumerate(exc.matrix):
			for j, col in enumerate(row):
				if col is num:
					return i, j
