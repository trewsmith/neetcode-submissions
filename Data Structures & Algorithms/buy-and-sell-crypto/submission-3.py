class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 9999999999999
        profit = 0
        
        for num in range(len(prices)):
            if(prices[num] < lowest):
                lowest = prices[num]
            if(prices[num] - lowest > profit):
                profit = prices[num] - lowest
        return profit