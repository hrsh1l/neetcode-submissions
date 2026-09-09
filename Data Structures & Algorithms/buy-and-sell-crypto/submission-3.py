class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        initial = prices[0] 
        maxProfit = 0

        for i in range(1, len(prices)):
            diff = prices[i] - initial

            maxProfit = max(diff, maxProfit)

            if diff <=0:
                initial = prices[i]

        
        return maxProfit


