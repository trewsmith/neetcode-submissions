class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = prices[0]
        prof = 0
        for i in range(1, len(prices)):
            
                
            if prices[i] <= prices[i - 1]:
                high = prices[i - 1]
                prof += high - low
                low = prices[i]
        
        if prices[len(prices) - 1] > prices[len(prices) - 2]:
            high = prices[len(prices) - 1]
            prof += high - low

        return prof