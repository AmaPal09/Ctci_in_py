class Stack:
	def __init__(self):
		self._stack = []

	def isEmpty(self):
		return len(self._stack) == 0

	def peek(self):
		if self.isEmpty():
			return None
		else:
			return self._stack[-1]

	def size(self):
		return len(self._stack)

	def push(self, val):
		self._stack.append(val)

	def pop(self):
		if self.isEmpty():
			return None
		else:
			return self._stack.pop()
