class Solution(object):
    def isHappy(self, n):
        li = []
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in li:
                return False
            else:
                li.append(n)
        return True


a = Solution()
print(a.isHappy(1))
