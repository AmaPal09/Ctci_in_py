#
# Check permutation
# Given two strings, write a method to decide if one of them is a permutation of
# the other.
#

import unittest

#Sol1
def checkPermSol1(inStr1, inStr2):
	if len(inStr1) != len(inStr2):
		return False

	if inStr1 == None or inStr2 == None:
		return False

	inStr1Sorted = sorted(inStr1)
	inStr2Sorted = sorted(inStr2)

	inStr1 = "".join(inStr1Sorted)
	inStr2 = "".join(inStr2Sorted)

	return inStr1 == inStr2


#Sol2
def checkPermSol2(inStr1, inStr2):
	if len(inStr1) != len(inStr2):
		return False

	if inStr1 == None or inStr2 == None:
		return False

	charArray = [0] * 128

	for char in inStr1:
		val = ord(char)
		charArray[val] += 1

	for char in inStr2:
		val = ord(char)
		--charArray[val]
		if charArray[val] < 0:
			return False

	return True


class Test(unittest.TestCase):
	def test_checkPermSol1(self):
		self.assertEqual(True,checkPermSol1("dog", "god"))
		self.assertEqual(False,checkPermSol1("dog", "god "))
	def test_checkPermSol2(self):
		self.assertEqual(True,checkPermSol2("dog", "god"))
		self.assertEqual(False,checkPermSol2("dog", "god "))

unittest.main()

