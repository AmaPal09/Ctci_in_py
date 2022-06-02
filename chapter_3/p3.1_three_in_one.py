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


a3to1 = Three_in_stack()
a3to1.push_top(3)
a3to1.push_top(2)
a3to1.push_top(1)
a3to1.push_middle(6)
a3to1.push_middle(5)
a3to1.push_middle(4)
a3to1.push_bottom(9)
a3to1.push_bottom(8)
a3to1.push_bottom(7)
print(a3to1.container)
print(a3to1.peek_top())
print(a3to1.peek_middle())
print(a3to1.peek_bottom())

print(a3to1.pop_top())
print(a3to1.peek_top())

print(a3to1.pop_middle())
print(a3to1.peek_middle())

print(a3to1.pop_bottom())
print(a3to1.peek_bottom())