# 1
class Solution:
    def negative_num(self, s):
        try:
            num_val = float(s.strip())
            return num_val < 0
        except:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t.isdigit() or self.negative_num(t):
                nums.append(int(t))
            else:
                n1 = nums.pop()
                n2 = nums.pop()
                if t == "+":
                    result = n1 + n2
                elif t == "-":
                    result = n2 - n1
                elif t == "*":
                    result = n1*n2
                elif t == "/":
                    result = int(n2 / n1)
                nums.append(result)

        return nums[0]







# 더 간단 버전
class Solution:
    def negative_num(self, s):
        try:
            num_val = float(s.strip())
            return num_val < 0
        except:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t not in "+-*/":
                nums.append(int(t))
            else:
                n1 = nums.pop()
                n2 = nums.pop()
                if t == "+":
                    result = n1 + n2
                elif t == "-":
                    result = n2 - n1
                elif t == "*":
                    result = n1*n2
                elif t == "/":
                    result = int(n2 / n1)
                nums.append(result)

        return nums[0]
