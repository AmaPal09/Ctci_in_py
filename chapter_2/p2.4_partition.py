#
# Partition
# Write code to partition a linked list around a value x, such that
# all nodes less than x come before all nodes greater than or equal
# to x. (IMPORTANT: The partition element x can appera anywhere in
# the "right partition"; it does not need to appear between the left
# and right partitions. The additional spacing in the example below
# indicates the partition. Yes, the output below is one of many value
# outputs!)
#

#
# Explaination:
#

#
# Questions:
#

#
# Assumption:
#

#
# Example:
# 1) '3->5->8->5->10->2->1' [partition = 5] => '3->1->2 -> 10->5->5->8'
# 2) '1->6->4->3->2' [partition = 3]
# 3) '6->3->1' [partition = 3]

from linked_list import ListNode, LinkedList
import unittest

def partition_ll(head, pivot):

	if not head:
		return head


	curr = head
	left_head = None
	left_tail = None
	right_head = None
	right_tail = None

	leftLL = LinkedList()
	leftLL.head = left_head
	rightLL = LinkedList()
	rightLL.head = right_head


	while curr:
		if curr.value < pivot:
			if left_head == None:
				left_head = ListNode(curr.value)
				left_tail = left_head
			else:
				left_tail.next = ListNode(curr.value)
				left_tail = left_tail.next

		else:
			if right_head == None:
				right_head = ListNode(curr.value)
				right_tail = right_head
			else:
				right_tail.next = ListNode(curr.value)
				right_tail = right_tail.next

		curr = curr.next

	if left_tail:
		left_tail.next = right_head
		return left_head
	else:
		return right_head


# a1 = ListNode(3,ListNode(5, ListNode(8, ListNode(5, ListNode(10, ListNode(2, ListNode(1)))))))
# ll1 = LinkedList()
# ll1.head = a1
# print(ll1)
# a1 = partition_ll(a1,5)
# ll1.head = a1
# print(ll1)

# a2 = ListNode(1, ListNode(6, ListNode(4, ListNode(3, ListNode(2)))))
# ll2 = LinkedList()
# ll2.head = a2
# print(ll2)
# a2 = partition_ll(a2,3)
# ll2.head = a2
# print(ll2)

# a3 = ListNode(6, ListNode(3, ListNode(1)))
# ll3 = LinkedList()
# ll3.head = a3
# print(ll3)
# a3 = partition_ll(a3,2)
# ll3.head = a3
# print(ll3)

# a4 = ListNode(2, ListNode(4, ListNode(3)))
# ll4 = LinkedList()
# ll4.head = a4
# print(ll4)
# a4 = partition_ll(a4,1)
# ll4.head = a4
# print(ll4)

# a5 = ListNode(1, ListNode(3, ListNode(2)))
# ll5 = LinkedList()
# ll5.head = a5
# print(ll5)
# a5 = partition_ll(a5,1)
# ll5.head = a5
# print(ll5)


class Test(unittest.TestCase):

	test_cases = [
		([3,5,8,5,10,2,1], 5, [3,2,1,5,8,5,10]),
		([1,6,4,3,2], 3, [1,2,6,4,3]),
		([6,3,1], 2, [1,6,3]),
		([2,4,3], 1, [2,4,3]),
		([1,3,2], 4, [1,3,2])
	]

	test_functions = [
		partition_ll,
	]

	def test_partition_ll(self):
		for f in self.test_functions:
			for case, pivot, expected in self.test_cases:
				ll1 = LinkedList(case)
				ll1.head = f(ll1.head, pivot)
				assert ll1.values() == expected

if __name__ == "__main__":
	unittest.main()