class Solution:
    def maxArea(self, heights: List[int]) -> int:
        amount = 0
        l, r = 0, len(heights)-1

        while l<r:
            y = min(heights[l], heights[r])
            x = r-l
            if heights[l] < heights[r]:
                l +=1
            else:
                r-=1
            amount = max(amount, x*y)

 

        return amount
