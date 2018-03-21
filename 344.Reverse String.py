class Solution(object):
    def reverseString(self, s):
        list_s = list(s)
        list_s.reverse()
        rev_s = ''.join([i for i in list_s])
        return rev_s


a = Solution()
print(a.reverseString('hello'))
