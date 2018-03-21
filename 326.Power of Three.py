class Solution(object):
    def isPowerOfThree1(self, n):
        if n % 3 != 0:
            return False
        if n / 3 == 1.0:
            return True
        return self.isPowerOfThree1(n / 3)

    def isPowerOfThree2(self, n):
        return n > 0 and 1162261467 % n == 0


a = Solution()
print(a.isPowerOfThree1(27))
print(a.isPowerOfThree2(27))
