#!/usr/bin/env python3

import sys
import re

from modules.Astar import *
from modules.Manhattan import *
from modules.Validation import *
from modules.State import *
import random

def main():
	res, mat, flag, step = validation()
	start = State(mat)
	res = State(res)
	astar = Astar(res, flag)

	if (start == res):
		resList = list()
	else:
		resList = astar.search(start)

	if ( not resList):
		print(bcolors.FAIL + "Unsolvable puzzle!" + bcolors.ENDC)
		exit()
		
	
	print("Complexity in time: ", astar.totalSize)
	print("Complexity in size: ", astar.maxSize)
	print("Number of moves from initial state to solution: ", len(resList) + 1)
	print("Start state\n", start)

	resList.reverse()
	if (step):
		for x in resList:
			print(x)
	print("Result state\n", res)

if __name__ == "__main__":
    main()
