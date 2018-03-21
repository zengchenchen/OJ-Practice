class Solution(object):
    def maxProfit(self, p):
        mp = 0
        for i in range(0, len(p) - 1):
            if max(p[i + 1:]) - p[i] > mp:
                mp = max(p[i + 1:]) - p[i]
        return mp


a = Solution()
b = a.maxProfit([1, 2, 8, 4, 3])
print(b)
