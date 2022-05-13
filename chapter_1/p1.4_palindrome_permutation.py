#
# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or a phrase that is the same
# forwards and backwards. The palindrome does not need to be limited
# to just dictionary words. You can ignore casing and non-letter
# characters.
#

import unittest

charSet = {'a', 'b', 'c', 'd',
		   'e', 'f', 'g', 'h',
		   'i', 'j', 'k', 'l',
		   'm', 'n', 'o', 'p',
		   'q', 'r', 's', 't',
		   'u', 'v', 'w', 'x',
		   'y', 'z'}


def checkPalindromeSol1(inStr):
	if not inStr or len(inStr) < 1:
		return False

	if len(inStr) == 1:
		return True

	charCountDict = {}

	for char in inStr:
		if char.lower() in charSet:
			charCountDict[char.lower()] = charCountDict.get(char.lower(),0)+1

	countOdds = False
	for char, count in charCountDict.items():
		if count%2 == 1:
			if countOdds:
				return False
			else:
				countOdds = True

	return True


class Test(unittest.TestCase):
	def test_checkPalindromeSol1(self):
		self.assertEqual(True, checkPalindromeSol1("Tact Coa"))
		self.assertEqual(False, checkPalindromeSol1("Tact boa"))
		self.assertEqual(True, checkPalindromeSol1("a1231a"))
		self.assertEqual(False, checkPalindromeSol1("a1b"))

unittest.main()