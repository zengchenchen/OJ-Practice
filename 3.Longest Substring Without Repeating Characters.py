class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s = list(s)
        maxlenList = []
        substringlist = []
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        for i in range(len(s) - 1):
            substringlist.append(s[i])
            while s[i + 1] not in substringlist:
                substringlist.append(s[i + 1])
                i = i + 1
                if i == len(s) - 1:
                    break
            maxlenList.append(len(substringlist))
            substringlist = []
        return max(maxlenList)

    def lengthOfLongestSubstring1(self, s):
        start, maxLength = 0, 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


a = Solution()
print(a.lengthOfLongestSubstring(''))
print(a.lengthOfLongestSubstring1(''))
