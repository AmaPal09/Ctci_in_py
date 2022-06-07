#
# Stack Min
# How would you design a stack which, in addition to push and pop,
# has a function min which returns the minimum element? Push, pop
# and min should all operate in O(1) time.
#

#
# Explaination:
#

#
# Questions:
# 1)
#

#
# Assumption:
# 1)
# 2)
#

#
# Example:
#
#

import unittest


class Stack:
	def __init__(self):
		self.stack = []

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		return self.stack.pop()

	def size(self):
		return len(self.stack)

	def is_empty(self):
		return self.size() == 0

	def peek(self):
		if not self.is_empty():
			return self.stack[-1]
		else:
			return None


class MinStack(Stack):
	def __init__(self):
		super().__init__()
		self.minStack = Stack()
		self.minVal = None

	def push(self, val):
		super().push(val)
		if self.minVal == None or self.minVal >= val :
			self.minStack.push(val)
			self.minVal = val

	def pop(self):
		popped = super().pop()
		if popped == self.minVal:
			self.minStack.pop()
			self.minVal = self.minStack.peek()

	def minimum(self):
		return self.minVal


class Test(unittest.TestCase):
	def test_MinStack(self):
		test_Stack1 = MinStack()
		assert test_Stack1.minimum() == None
		print(test_Stack1.minStack.stack)

		test_Stack1.push(4)
		assert test_Stack1.minimum() == 4
		print(test_Stack1.minStack.stack)

		test_Stack1.push(6)
		print(test_Stack1.minStack.stack)
		print(test_Stack1.stack)
		assert test_Stack1.minimum() == 4

		test_Stack1.push(2)
		print(test_Stack1.minStack.stack)
		print(test_Stack1.stack)
		assert test_Stack1.minimum() == 2

		test_Stack1.push(8)
		print(test_Stack1.minStack.stack)
		print(test_Stack1.stack)
		assert test_Stack1.minimum() == 2

		test_Stack1.push(2)
		print(test_Stack1.minStack.stack)
		print(test_Stack1.stack)
		assert test_Stack1.minimum() == 2

		test_Stack1.pop()
		print(test_Stack1.minStack.stack)
		print(test_Stack1.stack)
		assert test_Stack1.minimum() == 2

		test_Stack1.pop()
		print(test_Stack1.minStack.stack)
		print(test_Stack1.stack)
		assert test_Stack1.minimum() == 2

		test_Stack1.pop()
		print(test_Stack1.minStack.stack)
		print(test_Stack1.stack)
		assert test_Stack1.minimum() == 4

		test_Stack1.pop()
		print(test_Stack1.minStack.stack)
		print(test_Stack1.stack)
		assert test_Stack1.minimum() == 4


if __name__ == "__main__":
	unittest.main()
