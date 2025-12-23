class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float('inf')
        profit =0 
        for i in range(len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]
            else:
                profit = max(profit, prices[i]- min_prices)

        return profit    
