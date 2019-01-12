
# python3.6 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

import sys
import re

from modules.Astar import *
from modules.Manhattan import *
import random

def generate_martix(desired):
	cp = State(copy.deepcopy(desired))
	for x in range(10, 100):
		i = random.randint(1, 100)
		if (i % 4 == 0):
			cp.moveLeft()
		if (i % 4 == 1):
			cp.moveTop()
		if (i % 4 == 2):
			cp.moveRight()
		if (i % 4 == 3):
			cp.moveBottom()
	return cp.matrix

def check_unique_all(all_int_array, total):
	correct_array = []
	for x in range(0, total * total):
		correct_array.append(x)
	if (correct_array != sorted(all_int_array, key=int)):
		print("Invalid puzzle - duplicating values")
		exit()
		return False
	return True


def check_els(one_int_array, total):
	all_int_array = []
	for el in one_int_array:
		el = int(el)
		if (el < 0):
			print("Invalid puzzle - one of the values is too small")
			exit()
		elif (el > total * total - 1):
			print("Invalid puzzle - one of the values is too big")
			exit()
		else:
			all_int_array.append(el)

	if (check_unique_all(all_int_array, total)):
		return True

def count_inversions(final_state, current_state):
	inversions = 0
	i = 0
	while (final_state != current_state):
		for i, cur_val in enumerate(current_state):
			if i != final_state.index(cur_val):
				current_state.insert(final_state.index(cur_val) + 1, cur_val)
				current_state.pop(i)
				inversions = inversions + abs(i - final_state.index(cur_val))
				break

	# print ("inversions: ", inversions)
	return inversions


def is_blank_odd(current_state):

	index = current_state.index(0)
	if index in range(0, 3) or index in range(8, 11):
		return 0
	else:
		return 1

def is_solvable(total, current_state):

	if (total == 3):
		current_state.remove(0)
		final_state = [1, 2, 3, 8, 4, 7, 6, 5]
		if (count_inversions(final_state, current_state) % 2) == 0:
			return True
		else:
			return False
	elif (total == 4):
		final_state = [1, 2, 3, 4, 12, 13, 14, 5, 11, 15, 6, 10, 9, 8, 7]
		odd = is_blank_odd(current_state)
		current_state.remove(0)
		inversions = count_inversions(final_state, current_state)


		# According to the formulas
		#
		# if ( inversions % 2) == 0 and odd == 1:
		# 	print ("Solvable")
		# elif (inversions % 2) == 1 and odd == 0:
		# 	print ("Solvable")
		# elif inversions == 0:
		# 	print ("Solvable")
		# else:
		# 	print ("Unsolvable")
		#
		# According to Oborysen:
		if ( inversions % 2) == 0 and odd == 0:
			return True
		elif (inversions % 2) == 1 and odd == 1:
			return True
		elif inversions == 0:
			return True
		else:
			return False
	elif (total == 5):
		current_state.remove(0)
		final_state = [1, 2, 3, 4, 5, 16, 17, 18, 19, 6, 15, 24, 20, 7, 14, 23, 22, 21, 8, 13, 12, 11, 10, 9]
		if (count_inversions(final_state, current_state) % 2) == 0:
			return True
		else:
			return False



	

def validation():

	num_lines = 0
	total = -1
	flag = "-m"
	step = False

	if len(sys.argv) >= 2 and len(sys.argv) <= 4:
		if len(sys.argv) == 3:
			if (sys.argv[2] == "-s"):
				 step = True
			else:
				flag = sys.argv[2]
				if (sys.argv[2] != "-m") and (sys.argv[2] != "-lc") and (sys.argv[2] != "-ct"):
					print ("Error: Wrong flag.")
					exit()
		elif (len(sys.argv) == 4):
			step = True
			if (sys.argv[2] == "-s"):
				 flag = sys.argv[3]
			else:
				flag = sys.argv[2]
			if (flag != "-m") and (flag != "-lc") and (flag != "-ct"):
				print ("Error: Wrong flag.")
				exit()
		input_array = []
		try:
			with open(sys.argv[1], "r") as f:
				lines = f.readlines()
				for line in lines:
					input_array.append(line)
		except IOError:
			print ("Error: File does not appear to exist.")
			exit()

		for i,line in enumerate(input_array):
			if (line[0] != '#'):
				totals_index = i
				break
		if ' ' in line.strip():
			print ("Invalid puzzle - no width specified")
			exit()
		elif not line.strip().isdigit():
			print ("Invalid puzzle - wrong dimension format")
			exit()
		else:
			total = int(line.strip())
			if (total < 3 or total > 5):
				print ("Invalid total")
				exit()
			if (total == 3):
				desired = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
			elif (total == 4):
				desired =  [[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]]
			elif (total == 5):
				desired =  [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 0, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]

		final_array = []
		for line in input_array[totals_index + 1:]:
			if (line[0] != '#') and line != '\n':
				final_array.append(line.split("#", 1)[0])

		int_array = []
		int_line = []
		i = 0
		for line in final_array:
			line = re.sub( "\s+", ' ', line).strip()
			if line.strip().count(' ') != total - 1:
				print("Invalid puzzle - wrong width")
				exit()
			else:
				line = line.strip().split(' ')
				int_array.append(line)
				for el in line:
					try: 
						el = int(el)
					except ValueError:
						print("Invalid puzzle - elements must be positive integers")
						exit()
				i = i + 1

		if (i != total):
			print("Invalid puzzle - dimension doesn't correspond to the number of lines")
			exit()
		one_int_array = []
		for line in int_array:
			for el in line:
				one_int_array.append(int(el))

		final_int_array = []
		if (check_els(one_int_array, total)):
			for line in int_array:
				final_int_array.append(list(map(int, line)))
			# if is_solvable(total, one_int_array):
			return(desired, final_int_array, flag, step)
			# else:
				# print("Unsolvable puzzle")
				# exit()
	elif len(sys.argv) == 1:
		print (bcolors.FAIL + "Please provide a file. Will generate a random one.")
		print (bcolors.WARNING + "python3 main.py <map> -m | -lc | -ct")
		print (bcolors.OKBLUE + " -m   Manhattan distance")
		print (" -lc  Linear conflict")
		print (" -ct  Corner tiles" + bcolors.ENDC)
		desired = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]]
		final_int_array = generate_martix(desired)
		return(desired, final_int_array, flag, step)
	else:
		print ("Error. Too many args.")
		exit()
		return False

def sravnenie(exc, res):
	if (exc == res).all():
		print("True")
	else:
		print("False")