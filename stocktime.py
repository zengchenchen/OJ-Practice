class Solution(object):
    def maxProfit(self, prices):
        low = float('inf')
        profit = 0
        for i in prices:
            profit = max(profit, i - low)
            low = min(low, i)
        return profit


a = Solution()
b = a.maxProfit([1, 2, 8, 4, 3])
print(b)
