# Is Unique
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structure.

import unittest

# Sol1 using object
def isUniqueSol1(inStr):
	if not inStr:
		return False

	seen = set();

	for c in inStr:
		if c in seen:
			return False
		else:
			seen.add(c)

	return True


def isUniqueSol2(inStr):
	if not inStr:
		return False

	if len(inStr) > 128:
		return False

	charArray = [None] * 128
	# print(len(charArray))

	for c in inStr:
		val = ord(c)
		if charArray[val]:
			return False
		else:
			charArray[val] = True

	return True


class Test(unittest.TestCase):
	def test_isUniqueSol1(self):
		self.assertEqual(False,isUniqueSol1("aabbd"))
		self.assertEqual(False,isUniqueSol1("abcdea"))
		self.assertEqual(True,isUniqueSol1("abcdefg"))

	def test_isUniqueSol2(self):
		self.assertEqual(False,isUniqueSol2("aabbd"))
		self.assertEqual(False,isUniqueSol2("abcdea"))
		self.assertEqual(True,isUniqueSol2("abcdefg"))

# print(isUniqueSol1("aabbd"))
# print(isUniqueSol1("abcdea"))
# print(isUniqueSol2("abcdefg"))


unittest.main()