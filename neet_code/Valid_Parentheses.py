class Solution:
    def isValid(self, s: str) -> bool:
        chars_dict = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for i in range(len(s)):
            if s[i] in chars_dict:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                ch = stack.pop()
                if chars_dict[ch] != s[i]:
                    return False
        return not stack
