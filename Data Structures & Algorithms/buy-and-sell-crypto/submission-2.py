class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        abc = True
        for num in range(1, len(prices)):
            if(prices[num] > prices[num - 1]):
                abc = False
            
        if (abc):
                return 0
        hh = 0
        hdif = 0
        for i in range(len(prices)):

            for num2 in range(i, len(prices)):
                if (prices[num2] > prices[i]):
                    hh = prices[num2] - prices[i]
                    if (hh > hdif):
                        hdif = hh
        return hdif
        