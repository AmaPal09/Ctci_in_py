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


	prevChar = ""
	prevCharCtr = 0
	compressedArray = []
	i = 0


