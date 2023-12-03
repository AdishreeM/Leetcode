# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
# 1662. Check If Two String Arrays are Equivalent
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         return ''.join(word1) == ''.join(word2)

# Above solution requires potentially huge blocks of contiguous memory which can be solved
# by storing the individual chars in a list instead of a string

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        chars_in_word1 = [ ch for word in word1 for ch in list(word) ]
        chars_in_word2 = [ ch for word in word2 for ch in list(word) ]
        return chars_in_word1 == chars_in_word2
