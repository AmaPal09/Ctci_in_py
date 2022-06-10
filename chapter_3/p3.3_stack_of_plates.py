#
# Stack of plates
# Imagine a (literal) stack of plates. If the stack gets too high,
# it might topple, Therefore in real life, we would likely start a new
# stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed
# of several stacks and should create a new stack once the previous one
# exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
# behave identically to a single stack (that is, pop() should return the
# same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt (int index) which performs a pop operation
# on a specific sub-stack.
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

class Stack_of_Plates:
	def __init__(self, capacity):
		self._stack = []
		self._capacity = capacity


	def is_Empty(self):
		return len(self._stack) == 0

	def get_last_stack(self):
		if self.is_Empty():
			return None
		else:
			return self._stack[-1]

	def push(self, val):
		last_stack = self.get_last_stack()
		if last_stack == None or last_stack.size() == self._capacity:
			new_stack = Stack()
			new_stack.push(val)
			self._stack.append(new_stack)
		else:
			last_stack.push(val)

	def pop(self):
		last_stack = self.get_last_stack()
		if last_stack == None:
			return None
		else:
			val = last_stack.pop()
			if len(last_stack) == 0:
				self._stack.pop()
			return val

	def peek(self):
		last_stack = self.get_last_stack()
		if last_stack == None:
			return None
		else:
			last_stack.peek()

	def peek_at_index(self, index):
		val = self._stack[index].pop()
		if self._stack[index].size() == 0:
			self._stack.pop(index)
		return val




