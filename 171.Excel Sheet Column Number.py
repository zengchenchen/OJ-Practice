class Solution(object):
    def titleToNumber(self, s):
        l = len(s)
        su = 0
        for i in s:
            su = su + (ord(i) - 64) * (26**(l - 1))
            l = l - 1
        return su


a = Solution()
print(a.titleToNumber('ABA'))
