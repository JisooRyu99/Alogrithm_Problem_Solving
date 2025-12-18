# 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s if c.isalpha() or c.isdigit()]
        forward = "".join(s).lower()
        backward = "".join(reversed(forward)).lower()

        return forward == backward


## reverse는 시간복잡도가 좋지 않아서


# 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c.lower() for c in s if c.isdigit() or c.isalpha()]
        left, right = 0, len(new_s) - 1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left +=1
            right -=1
        return True
