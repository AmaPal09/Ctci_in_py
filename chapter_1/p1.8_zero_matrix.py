#
# Zero Matrix
# Write an algorithm such that if an element in an MxN jmatrix is 0,
# its entire row and column are set to 0;
#

#
# Assumption
# All elements in the matrix are numeric
#

#
# Example:
# 1) [] -> []
# 2) [[]] -> []
# 3) [[1], [2,3]] -> [[1], [2,3]]
# 4) [
# 	[1 , 2 , 3 , 4 , 5 ],
# 	[6 , 7 , 8 , 9 , 10],
# 	[11, 12, 0 , 14, 15]
# ]  -> [
# 	[1 , 2 , 0 , 4 , 5 ],
# 	[6 , 7 , 0 , 9 , 10],
# 	[0 , 0 , 0 , 0 , 0 ]
# ]
#

def make_zero_matrix(in_mat):
	if len(in_mat) == 0:
		return in_mat

	if len(in_mat) == 1 and len(in_mat[0]) == 0:
		return in_mat

	for i in range(len(in_mat)):
		if len(in_mat[0]) != len(in_mat[i]):
			return in_mat

	row_indices_with_zero = [False]*len(in_mat)
	col_indices_with_zero = [False]*len(in_mat[0])

	for r in range(len(in_mat)):
		for c in range(len(in_mat[0])):
			if in_mat[r][c] == 0:
				row_indices_with_zero[r] = True
				col_indices_with_zero[c] = True

	# Make rows with 0, all 0
	for r in range(len(in_mat)):
		if row_indices_with_zero[r]:
			for c in range(len(in_mat[0])):
				in_mat[r][c] = 0

	# Make cols with 0, all 0
	for c in range(len(in_mat[0])):
		if col_indices_with_zero[c]:
			for r in range(len(in_mat)):
				in_mat[r][c] = 0

	return in_mat