class Solution(object):
    def strStr(self, haystack, needle):
        if needle == '':
            return -1
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for j in range(1, len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                    if j == len(needle) - 1:
                        return i
        return -1


temp = Solution()
print(temp.strStr('hellow', 'lll'))
