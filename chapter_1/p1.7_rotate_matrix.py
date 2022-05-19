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
# 123       741
# 456  -->  852
# 789       963


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
