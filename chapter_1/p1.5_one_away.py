#
# One away
# There are three three types of edits that can be performed on
# strings: insert a character, remove a character, or replace a
# character. Given two strings, write a function to check if they
# are one edit (or zero edits) away.
#

#
# Examples
# 'pale' 'bale' -> true
# 'pale' 'pales'-> true
# 'pale' 'pal'-> true
# 'pale' 'bales'-> false
#

import unittest

def checkReplaceOne(str1, str2):
	s1 = 0
	s2 = 0
	oneDiff = False
	while s1 < len(str1) or s2 < len(str1):
		if str1[s1] != str2[s2]:
			if oneDiff:
				return False
			else:
				oneDiff = True
		s1 += 1
		s2 += 1
	return True



def checkInsertOne(biggerStr, smallerStr):
	s = 0
	b = 0
	oneInsert = False

	while s < len(smallerStr):
		if smallerStr[s] != biggerStr[b]:
			if oneInsert:
				return False
			else:
				oneInsert = True
				b += 1
		else:
			s += 1
			b += 1

	return True


def oneAwaySol1(inStr1, inStr2):
	if not inStr1 or not inStr2:
		return False

	if len(inStr1) == len(inStr2):
		return checkReplaceOne(inStr1, inStr2)
	elif len(inStr1) == len(inStr2) +1:
		return checkInsertOne(inStr1, inStr2)
	elif len(inStr1) + 1 == len(inStr2):
		return checkInsertOne(inStr2, inStr1)
	else:
		return False



def is_one_away_compact(string1, string2):
    """
    This solution is more compact and checks for all operation
        in single traversal of string.
    """
    if abs(len(string1) - len(string2)) > 1:
        return False
    i, j = 0, 0
    found_difference = False
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if found_difference:
                return False
            else:
                found_difference = True

            if len(string1) == len(string2):
                j = j + 1
        else:
            j = j + 1
        i = i + 1
    return True


class Test(unittest.TestCase):
	def test_oneAwaySol1_true(self):
		self.assertTrue(oneAwaySol1("pale", "bale"))
		self.assertTrue(oneAwaySol1("pale", "paale"))
		self.assertTrue(oneAwaySol1("pale", "ple"))

	def test_oneAwaySol1_false(self):
		self.assertFalse(oneAwaySol1("pale", "bales"))

	def test_checkReplaceOne(self):
		self.assertEqual(True, checkReplaceOne("pale", "bale"))

	def test_is_one_away_compact(self):
		self.assertTrue(is_one_away_compact("pale", "ple"))


if __name__ == "__main__":

	import sys

	if len(sys.argv) > 1:
		print(oneAwaySol1(sys.argv[-2], sys.argv[-1]))
	else:
		unittest.main()