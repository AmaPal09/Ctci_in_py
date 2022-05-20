#
# Remove Dups
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# how will you solve this problem if a temp buffer is not allowed
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

import unittest

class ListNode:
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next = next_node

	def __str__(self):
		return str(self.value)


class LinkedList:
	def __init__(self, values=None):
		self.head = None
		self.tail = None
		if values is not None:
			self.add_multiple(values)

	def __iter__(self):
		curr_node = self.head
		while curr_node:
			yield curr_node
			curr_node = curr_node.next

	def __len__(self):
		length = 0
		curr_node = self.head
		while curr_node:
			length += 1
			curr_node = curr_node.next

	def __str__(self):
		ll_array = [str(val) for val in self]
		return "->".join(ll_array)

	def add(self, value):
		if self.head is None:
			self.head = ListNode(value)
			self.tail = self.head
		else:
			self.tail.next = ListNode(value)
			self.tail = self.tail.next

	def add_multiple(self, values):
		for val in values:
			self.add(val)

	def values(self):
		return [v.value for v in self]




def remove_dups(head):
	curr_node = head
	prev_node = None
	node_set = set()

	while curr_node:
		if curr_node.value in node_set:
			prev_node.next = curr_node.next
			curr_node = curr_node.next
		else:
			node_set.add(curr_node.value)
			prev_node = curr_node
			curr_node = curr_node.next

	return head


def remove_dups_2(head):
	curr_node = head

	while curr_node:
		runner_node = curr_node

		while runner_node.next:
			if runner_node.next.value == curr_node.value:
				runner_node.next = runner_node.next.next
			else:
				runner_node = runner_node.next

		curr_node = curr_node.next


class Test(unittest.TestCase):
	test_cases = [
		([1,1], [1]),
		([], []),
		([1,2,3,4,3,2,5], [1,2,3,4,5]),
		([1,2,3], [1,2,3]),
		([1,1,1,1], [1]),
	]

	test_functions = [
		remove_dups,
		remove_dups_2
	]

	def test_removing_of_dups(self):
		for f in self.test_functions:
			for case, expected in self.test_cases:
				test_ll = LinkedList(case)
				f(test_ll.head)
				assert test_ll.values() == expected



if __name__ == "__main__":
	unittest.main()