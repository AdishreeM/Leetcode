# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
# 1160. Find Words That Can Be Formed by Characters
# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.



class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        given_freq = Counter(chars)
        for word in words:
            word_freq = Counter(word)
            is_good = reduce(mul, [1 if word_freq[chr(ord('a')+i)] <= given_freq[chr(ord('a')+i)] else 0 for i in range(26)],1)
            ans += len(word) if is_good else 0
        return ans


# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         ans = 0
#         for word in words:
#             for i in range(26):
#                 if chars.count(chr(ord('a')+i)) < word.count(chr(ord('a')+i)):
#                     break
#             else:
#                 ans += len(word)
#         return ans