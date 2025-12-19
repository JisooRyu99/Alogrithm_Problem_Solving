# 1
# O(n²) 복잡도
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        for i in range(len(numbers)):
            r = len(numbers)-1    
            while i < r:
                if numbers[i] + numbers[r] == target:
                    return [i+1, r+1]
                
                r-=1


# 2
# 복잡도: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l<r:
            s = numbers[l] + numbers[r]
            if s== target:
                return [l+1, r+1]
            
            elif s < target:
                l += 1
            else: 
                r-=1
        
            
            
