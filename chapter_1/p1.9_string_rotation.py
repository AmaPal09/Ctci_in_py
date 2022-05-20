#
# String Rotation
# Assume you have a method isSubstring which checks if one word is a
# substring of another. Given two strings, s1 and s2, write code to
# check if s2 is a rotation of s1 using only one call to
# isSubstring(e.g., "waterbottle" is a rotation of "erbottlewat").
#

#
# Explaination:
# If s2 is a rotation of s1 then the question is at what point the
# rotation starts.
# Eg:
# s1 = xy = waterbottle (xy string parts created at the point where
# rotation starts )
# x = wat
# y = erbottle
# s2 = yx = erbottlewat
# Hence, check if a way to split s1 into x & y such that xy = s1 and yx = s2.
# But irrespective of the division, yx will always be the substring of xyxy.
# Therefore s2 will always be the substring on s1s1.
#

#
# Questions:
#

#
# Assumption:
#

#
# Example:
# 1) " ", "a" -> false
# 2) "aabb", "aab" -> false
# 3) "waterbottle", "erbottlewat" -> true
# 4) " ", " " -> true
#

import unittest

def is_substring(subStr, fullStr):
	return subStr in fullStr

def string_rotation(s1, s2):
	if len(s1) != len(s2):
		return False

	if len(s1) == 0:
		return True

	full_string = s1+s1

	return is_substring(s2, full_string)



class Test(unittest.TestCase):
	test_cases = [
		(" ", "a", False),
		("aabb", "aab", False),
		("waterbottle", "erbottlewat", True),
		(" ", " ", True)
	]

	test_functions = [
		string_rotation
	]

	def test_string_rotation(self):
		for f in self.test_functions:
			for s1, s2, expected in self.test_cases:
				assert f(s1,s2) == expected

if __name__ == "__main__":
	unittest.main()