#
# Loop Detection
# Given a linked list which might contain a loop, implement an
# algorithm that returns the node at the beginning of the loop (if
# one exist)
#

#
# Explaination:
#

#
# Questions:
# 1) What about nodes with " "?
#

#
# Assumption:
# 1) Function is passed the head of the linked list.
# 2) Not a method on the LL class
#

#
# Example:
# 1) A -> B -> C -> D -> E -> C [same as the C earlier]
# 2) C
#

from linked_list import ListNode, LinkedList
import unittest

def is_a_loop(head):

	if not head:
		return False

	slow_ptr = head
	fast_ptr = head

	while fast_ptr and fast_ptr.next:
		slow_ptr = slow_ptr.next
		fast_ptr = fast_ptr.next.next

		if fast_ptr == slow_ptr:
			break


	if fast_ptr == None or fast_ptr.next == None:
		return None

	slow_ptr = head

	while slow_ptr != fast_ptr:
		slow_ptr = slow_ptr.next
		fast_ptr = fast_ptr.next

	return fast_ptr


class Test(unittest.TestCase):
	def test1_is_a_loop(self):
		A = ListNode("a")
		B = ListNode("b")
		C = ListNode("c")
		D = ListNode("d")
		E = ListNode("e")
		A.next = B
		B.next = C
		C.next = D
		D.next = E
		E.next = C

		assert is_a_loop(A) == C

	def test2_is_a_loop(self):
		A = ListNode("a")
		B = ListNode("b")
		C = ListNode("c")
		D = ListNode("d")
		E = ListNode("e")
		A.next = B
		B.next = C
		C.next = D
		D.next = E
		E.next = None

		assert is_a_loop(A) == None

if __name__ == "__main__":
	unittest.main()