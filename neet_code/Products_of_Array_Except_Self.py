# 첫번째 코드
from functools import reduce
class Solution:
    def cal(self, x, y):
        return x*y
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [reduce(self.cal, nums[1:])]
        for i in range(1, len(nums)-1):
            
            cal1 = reduce(self.cal, nums[:i])
            cal2 = reduce(self.cal, nums[i+1:])
            result.append(cal1*cal2)
     
        result.append(reduce(self.cal, nums[:-1]))
        
        return result

#reduce는 시각 복잡도가 올라가기 때문에 다른 시도

# 두번째 코드
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            result[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= right
            right *= nums[i]

        return result
