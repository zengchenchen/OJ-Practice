class Solution(object):
    def isAnagram(self, s, t):
        li_s = list(s)
        li_t = list(t)
        li_s.sort()
        li_t.sort()
        if li_s == li_t:
            return True
        else:
            return False


a = Solution()
print(a.isAnagram('abce', 'cba'))
