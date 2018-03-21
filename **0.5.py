class Solution(object):
    def mySqrt(self, x):
        i = x
        while i * i - x > 0.001:
            i = (i + x / i) / 2
        return int(i)


temp = Solution()
print(temp.mySqrt(4))
