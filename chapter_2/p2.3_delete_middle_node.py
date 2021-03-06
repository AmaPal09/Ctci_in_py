#
# Delete Middle Node
# Implement an algorith to delete a node in the middle (ie., any node
# but the first and the last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node
#

#
# Explaination:
#

#
# Questions:
# 1) What to return if LL length is 3 and 4th to last element is asked for?
# 2) What if its an empty LL
# 3) What to return: the node or the val?
#

#
# Assumption:
# 1) Function is passed with just the middle node that is to be deleted
# 2) Nothing is returned
#

#
# Example:
# 1) '' => ''
# 2) (1->2->3->4->5->6) Input(node 6) => (1->2->3->4->5->6)
# 3) ('a'->'e'->'c'->'d') Input(node c) => ('a'->'e'->'c'->'d')
#

from linked_list import LinkedList
from linked_list import ListNode
import unittest

def del_middle_node(node):
	if (node and node.next):
		node.value = node.next.value
		node.next = node.next.next



class Test(unittest.TestCase):
	test_cases = [
		([1,2,3], 4, [5,6,7], [1,2,3,5,6,7]),
		([1,2,3], 4, [], [1,2,3,4])
	]

	test_functions = [del_middle_node]

	def test_del_middle_node(self):
		for f in self.test_functions:
			for p1, m, p2, expected in self.test_cases:
				ll = LinkedList()
				ll.add_multiple(p1)
				middle_node = ll.add(m)
				ll.add_multiple(p2)
				del_middle_node(middle_node)
				print(ll.values())
				print(expected)
				assert ll.values() == expected


if __name__ == "__main__":
	unittest.main()