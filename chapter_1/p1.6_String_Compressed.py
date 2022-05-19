#
# String Compression
# Implement a method to perform basic string compression using the counts of
# repeated characters. For example, the string aabcccccaaa would become
# a2b1c5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the origunal string. You can
# assume the string has only uppercase and lowercase letters(a-z)
#

#
# Examples
# 1) "aabcccccaaa" -> a2b1c5a3
# 2) "abcd" -> abcd
# 3) "aabbc" -> a2b2c
# 4) "" -> ""
# 5) "aaAAAbCCcccaaAAA" -> a2A3b1C2c3a2A3
#

def string_compressor(inStr):
	if not inStr:
		return inStr

	if len(inStr) <= 1:
		return inStr

	i = 0
	prevChar = inStr[i]
	prevCharCtr = 1
	compressedArray = []
	i += 1

	while i < len(inStr):
		if prevChar != inStr[i]:
			compressedArray.append(prevChar)
			compressedArray.append(str(prevCharCtr))
			prevChar = inStr[i]
			prevCharCtr = 1
		else:
			prevCharCtr += 1
		i += 1

	compressedArray.append(prevChar)
	compressedArray.append(str(prevCharCtr))

	if len(compressedArray) > len(inStr):
		return inStr
	else:
		return "".join(compressedArray)

import unittest

class Test(unittest.TestCase):

	test_cases = [
		("aabcccccaaa", "a2b1c5a3"),
		("abcd", "abcd"),
		("aabbc", "aabbc"),
		("", ""),
		("aaAAAbCCcccaaAAA", "a2A3b1C2c3a2A3")
	]

	test_functions = [
		string_compressor,
	]

	def test_string_compressor(self):
		for f in self.test_functions:
			for test_string, expected in self.test_cases:
				assert f(test_string) == expected



if __name__ == "__main__":
	import sys

	if len(sys.argv) > 1:
		print(string_compressor(sys.argv[-1]))
	else:
		unittest.main()
