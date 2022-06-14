#
# Sort Stack
# Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek and isEmpty.
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
#

#
# Example:
# 1)
#

from stack import Stack

def sortStack(inStack):
	tempStack = Stack()
	tmpvar = None

	while (not inStack.isEmpty()):
		tmpvar = inStack.pop()

		while (not tempStack.isEmpty() and tempStack.peek() > tmpvar):
			inStack.push(tempStack.pop())

		tempStack.push(tmpvar)

	while not tempStack.isEmpty():
		inStack.push(tempStack.pop())


t1 = Stack()
t1.push(5)
t1.push(7)
t1.push(3)
t1.push(9)
t1.push(10)
print(t1._stack)
sortStack(t1)
print(t1._stack)