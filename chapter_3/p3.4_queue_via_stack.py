#
# Queue via Stacks
# Implement a MyQueue class which implements a queue using two stacks.
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
# 1)
#

from stack import Stack

class MyQueue():
	def __init__(self):
		self.newStack = Stack()
		self.oldStack = Stack()

	def push(self, val):
		self.newStack.push(val)

	def loadOldStack(self):
		while (not self.newStack.isEmpty()):
			self.oldStack.push(self.newStack.pop())

	def peek(self):
		if self.oldStack.isEmpty():
			self.loadOldStack()
		return self.oldStack.peek()

	def pop(self):
		if self.oldStack.isEmpty():
			self.loadOldStack()
		return self.oldStack.pop()

mQ1 = MyQueue()
for i in range(5):
	mQ1.push(i)
print(mQ1.newStack._stack)
print(mQ1.peek())
print(mQ1.pop())
print(mQ1.push(7))
print(mQ1.newStack._stack)
print(mQ1.peek())
print(mQ1.pop())
print(mQ1.pop())
print(mQ1.pop())
print(mQ1.newStack._stack)