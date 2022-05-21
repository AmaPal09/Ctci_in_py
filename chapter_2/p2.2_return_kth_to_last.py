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
# 1) Node is expected as return
# 2) Function is passed with the LL
#

# /*
# Example:
# 1) '' => ''
# 2) 'a'->'e'->'c'->'d'->'c'->'a', 4 => 'c'->'d'->'c'->'a'
# */

from linked_list import LinkedList
import unittest

def return_kth_to_last(ll, k):
	if len(ll) < k:
		return None

	head = ll.head
	curr_node = head
	k_displace_node = curr_node

	for i in range(k):
		if k_displace_node == None:
			return None
		k_displace_node = k_displace_node.next

	while k_displace_node:
		curr_node = curr_node.next
		k_displace_node = k_displace_node.next

	return curr_node


class Test(unittest.TestCase):
	test_cases = [
		([10, 20, 30, 40, 50], 1, 50),
		([10, 20, 30, 40, 50], 3, 30),
		([10,20], 3, None),
		([], 0, None),
		([10, 20, 30, 40, 50], 5, 10)
	]

	test_functions = [
		return_kth_to_last,
	]


	def test_return_kth_to_last(self):
		for f in self.test_functions:
			for case, k, expected in self.test_cases:
				result_node = return_kth_to_last(LinkedList(case), k)
				if expected == None:
					assert result_node == expected
				else:
					assert result_node.value == expected

if __name__ == "__main__":
	unittest.main()