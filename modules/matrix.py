
from modules.Color import *
import numpy as np


class Matrix:

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