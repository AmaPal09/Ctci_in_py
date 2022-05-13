#
# URLify
# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you aare given the "true" length of the string. (Note: if implementing in java please use a character array so that you can perform this operation in place.)
#

import unittest

def urlifySol1(inStr):
	return "%20".join(inStr.split(" "))

def urlifySol2(inStr):
	return inStr.strip().replace(" ","%20")

class Test(unittest.TestCase):
	def test_urlifySol1(self):
		self.assertEqual("Mr%20John%20Smith",urlifySol1("Mr John Smith"))

	def test_urlifySol2(self):
		self.assertEqual("Mr%20John%20Smith",urlifySol2("Mr John Smith   "))


unittest.main()