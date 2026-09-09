class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                temp = prices[j] - prices[i]
                if temp > maxProfit:
                    maxProfit = temp
            j = i + 1

        return maxProfit

