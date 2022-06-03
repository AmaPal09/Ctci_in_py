#
# Three in one
# Describe how you could use a single array to implement three stacks
#

#
# Explaination:
# [
# 	top
# 	middletop
# 	middlebottom
# 	bottom
# ]
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

import unittest

class Three_in_stack():
	def __init__(self):
		self.container = []
		self.middle_top = 0
		self.middle_bottom = 0

	def push_top(self, value):
		self.container.insert(0,value)
		self.middle_top += 1
		self.middle_bottom += 1

	def push_middle(self,value):
		self.container.insert(self.middle_top,value)
		self.middle_bottom += 1

	def push_bottom(self, value):
		self.container.insert(self.middle_bottom, value)


	def is_top_empty(self):
		if self.middle_top == 0:
			return True
		else:
			return False

	def is_middle_empty(self):
		if self.middle_top == self.middle_bottom:
			return True
		else:
			return False

	def is_bottom_empty(self):
		if self.middle_bottom == len(self.container):
			return True
		else:
			return False

	def pop_top(self):
		if not self.is_top_empty():
			pop = self.container.pop(0)
			self.middle_top -= 1
			self.middle_bottom -= 1
			return pop
		else:
			return None

	def pop_middle(self):
		if not self.is_middle_empty():
			pop = self.container.pop(self.middle_top)
			self.middle_bottom -= 1
			return pop
		else:
			return None

	def pop_bottom(self):
		if not self.is_bottom_empty():
			pop = self.container.pop(self.middle_bottom)
			return pop
		else:
			return None


	def peek_top(self):
		if not self.is_top_empty():
			peek = self.container[0]
			return peek
		else:
			return None

	def peek_middle(self):
		if not self.is_middle_empty():
			peek = self.container[self.middle_top]
			return peek
		else:
			return None

	def peek_bottom(self):
		if not self.is_bottom_empty():
			peek = self.container[self.middle_bottom]
			return peek
		else:
			return None


class Test(unittest.TestCase):
	a3to1 = Three_in_stack()
	a3to1.push_top(3)
	assert a3to1.container == [3]
	a3to1.push_top(2)
	a3to1.push_top(1)
	assert a3to1.container == [1,2,3]
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 3

	assert a3to1.peek_top() == 1
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 3

	assert a3to1.pop_top() == 1
	assert a3to1.middle_top == 2
	assert a3to1.middle_bottom == 2
	assert a3to1.is_top_empty() == False
	a3to1.pop_top()
	a3to1.pop_top()
	assert a3to1.middle_top == 0
	assert a3to1.middle_bottom == 0
	assert a3to1.pop_top() == None
	assert a3to1.middle_top == 0
	assert a3to1.middle_bottom == 0
	assert a3to1.peek_top() == None
	assert a3to1.is_top_empty() == True

	a3to1.push_top(3)
	a3to1.push_top(2)
	a3to1.push_top(1)

	a3to1.push_middle(6)
	assert a3to1.container == [1,2,3,6]
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 4
	a3to1.push_middle(5)
	a3to1.push_middle(4)
	assert a3to1.container == [1,2,3,4,5,6]
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 6

	assert a3to1.peek_middle() == 4
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 6

	assert a3to1.pop_middle() == 4
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 5
	assert a3to1.is_middle_empty() == False

	assert a3to1.pop_middle() == 5
	assert a3to1.pop_middle() == 6
	assert a3to1.pop_middle() == None
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 3


	a3to1.push_middle(6)
	a3to1.push_middle(5)
	a3to1.push_middle(4)

	a3to1.push_bottom(9)
	assert a3to1.container == [1,2,3,4,5,6,9]
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 6
	a3to1.push_bottom(8)
	a3to1.push_bottom(7)
	assert a3to1.container == [1,2,3,4,5,6,7,8,9]
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 6

	assert a3to1.peek_bottom() == 7
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 6

	assert a3to1.pop_bottom() == 7
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 6
	assert a3to1.is_bottom_empty() == False

	assert a3to1.pop_bottom() == 8
	assert a3to1.pop_bottom() == 9
	assert a3to1.pop_bottom() == None
	assert a3to1.middle_top == 3
	assert a3to1.middle_bottom == 6

	assert a3to1.peek_bottom() == None
	assert a3to1.is_bottom_empty() == True


if __name__ == "__main__":
	unittest.main()
