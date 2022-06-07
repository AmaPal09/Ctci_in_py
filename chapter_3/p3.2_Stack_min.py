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
		super.__init__()
		self.minStack = Stack()
		self.minVal = None

	def push(self, val):
		super.push(val)
		if self.minVal < val or self.minVal == None:
			self.minStack.push(val)
			self.minVal = val

	def pop(self):
		popped = super.pop()
		if popped == self.minVal:
			self.minStack.pop()
			self.minVal = self.minStack.peek()

	def minimum(self):
		return self.minVal
