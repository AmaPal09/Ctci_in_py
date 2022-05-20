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
		return length

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
