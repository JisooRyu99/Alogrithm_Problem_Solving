class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


"""
찾는 문자열을 찾으면 index return
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
"""
