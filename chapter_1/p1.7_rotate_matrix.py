#
# Rotate Matrix
# Given an image represented by an N X N matrix, where each pixel on
# the image is represented by an integer, write a method to rotate
# the image by 90 degrees. Can you do this in place?
#

#
# Assumption:
# The outer array always contains atleast one array inside.
#

#
# Example:
# 1) [[1]] -> [[1]]
# 2) [[]] -> [[]]
# 3) [[ , ], [ , ]] -> [[ , ], [ , ]]
# 4) [[1,2,3], [4,5,6], [7,8,9]] -> [[7,4,1], [8,5,2], [9,6,3]]
# 5) [] -> []
# 6) [[1], [2,3]] -> [[1], [2,3]]
#
# 1  2  3  4         13 9  5  1      			       741   123
# 5  6  7  8   --> 	 14 10 6  2   				       852   456
# 9  10 11 12     	 15 11 7  3 			           963   789
# 13 14 15 16		 16 12 8  4

#
# Explaination:
# Easiest way of implementing the rotations is rotation in layers.
# Perform circular rotation.
# Move top -> temp var
# Move left -> top
# Move bottom -> left
# Move right -> bottom
# Move temp -> right
#


def rotate_matrix(in_Sq_matrix):
	if not in_Sq_matrix:
		return in_Sq_matrix

	if (len(in_Sq_matrix) == 0 or len(in_Sq_matrix[0]) == 0
		or len(in_Sq_matrix) != len(in_Sq_matrix[0])):
		return in_Sq_matrix

	arr_len = len(in_Sq_matrix)


	for layer in range(arr_len//2):
		first = layer
		last = arr_len - 1 - layer

		for i in range(first, last):
			offset = i - first

			# temp <- top
			temp = in_Sq_matrix[first][i]
			# top <- left
			in_Sq_matrix[first][i] = in_Sq_matrix[last-offset][first]

			# left <- bottom
			in_Sq_matrix[last-offset][first] = in_Sq_matrix[last][last-offset]

			# bottom <- right
			in_Sq_matrix[last][last-offset] = in_Sq_matrix[i][last]

			# right <- temp
			in_Sq_matrix[i][last] = temp

	return in_Sq_matrix


def rotate_matrix_2(in_Sq_matrix):
	n = len(in_Sq_matrix)

	for i in range(n):
		if len(in_Sq_matrix[i]) != n:
			return in_Sq_matrix

	for layer in range(n // 2):
		first, last = layer, n - layer - 1

		for i in range(first, last):
			# save top
			top = in_Sq_matrix[layer][i]

			# top <- left
			in_Sq_matrix[layer][i] = in_Sq_matrix[-i - 1][layer]

			# left <-bottom
			in_Sq_matrix[-i - 1][layer] = in_Sq_matrix[-layer - 1][-i - 1]

			#bottom <- right
			in_Sq_matrix[-layer - 1][-i - 1] = in_Sq_matrix[i][-layer - 1]

			in_Sq_matrix[i][-layer-1] = top

	return in_Sq_matrix



def rotate_matrix_3(in_Sq_matrix):
	n = len(in_Sq_matrix)

	for i in range(n):
		if len(in_Sq_matrix[i]) != n:
			return in_Sq_matrix

	result = [[0]*n for i in range(n)]

	for i, j in zip(range(n), range(n-1,-1,-1)):
		for k in range(n):
			result[k][i] = in_Sq_matrix[j][k]
	return result


def rotate_matrix_4(in_Sq_matrix):

	for i in range(n):
		if len(in_Sq_matrix[i]) != n:
			return in_Sq_matrix

	return [list(reversed(row)) for row in zip(*in_Sq_matrix)]

# def convert_inStr_to_List(inStr):
# 	if inStr[0] != '[' or inStr[-1] != ']':
# 		return in_list

# 	print(inStr)
# 	converted_list = []
# 	list_open = False
# 	list_close = False
# 	listStr = ""

# 	for i in range(1, len(inStr)-1):
# 		if inStr[i] == '[':
# 			list_open = True
# 			listStr += inStr[i]
# 		elif inStr[i] == ']':
# 			list_close = True
# 			listStr += inStr[i]
# 			if list_open and list_close:
# 				converted_list.append(convert_inStr_to_List(listStr))
# 			list_open = False
# 			list_close = False
# 			listStr = ""
# 		else:
# 			if list_open:
# 				listStr+= inStr[i]
# 			else:
# 				if inStr[i].isdigit():
# 					 converted_list.append(int(inStr[i]))
# 				else:
# 					if inStr[i] != ",":
# 						converted_list.append(inStr[i])

# 	return converted_list



# if __name__ == "__main__":
# 	import sys


# 	print(rotate_matrix(convert_inStr_to_List(sys.argv[-1])))

import unittest

class Test(unittest.TestCase):
	test_cases = [
		([[1]], [[1]]),
		([[]], [[]]),
		([[ ], [ ]], [[], []]),
		([], []),
		([[1], [2,3]], [[1], [2,3]]),
		([[1,2,3], [4,5,6], [7,8,9]], [[7,4,1], [8,5,2], [9,6,3]]),
		(	[
				[1 , 2 , 3 , 4 , 5 ],
				[6 , 7 , 8 , 9 , 10],
				[11, 12, 13, 14, 15],
				[16, 17, 18, 19, 20],
				[21, 22, 23, 24, 25]
			],
			[
				[21, 16, 11, 6 , 1 ],
				[22, 17, 12, 7 , 2 ],
				[23, 18, 13, 8 , 3 ],
				[24, 19, 14, 9 , 4 ],
				[25, 20, 15, 10, 5 ]
			]
		)
	]


	test_functions = [
		rotate_matrix,
		# rotate_matrix_2,
		rotate_matrix_3,
		rotate_matrix_4
	]


	def test_rotation(self):
		for f in self.test_functions:
			print(f)
			for case, expected in self.test_cases:
				print(case)
				self.assertEqual(expected, f(case))

unittest.main()