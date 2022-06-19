"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        count = 0
        result = 0
        chars = set()
        while i < len(s):
            while s[i] in chars:
                chars.remove(s[count])
                count += 1
            chars.add(s[i])
            result = max(result, len(chars))
            i += 1

        return result
