#
# Return Kth to Last
# Implement an algorithm to find the kth to last element of a singly linked list.
#

#
# Explaination:
# Sol1
# 	use 2 ptr.
# 	ptr1 points to the head of the list
# 	ptr2 at the kth element of the list
# 	Now check if ptr2.next == null, then ptr2 is last element.
# 	Hence ptr1 is kth to last element.
# 	else jump both ptrs to their next ptrs.
# Sol2
#

#
# Questions:
# 1) What to return if LL length is 3 and 4th to last element is asked for?
# 2) What is its an empty LL
# 3) What to return: the node or the val?
# 4)
#

#
# Assumption:
# 1) Node is expect as return
# 2) Function is passed with the head of the LL
#

# /*
# Example:
# 1) '' => ''
# 2) 'a'->'e'->'c'->'d'->'c'->'a', 4 => 'c'->'d'->'c'->'a'
# */