class Solution(object):
    def firstUniqChar(self, s):
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return s.index(key)
        return -1

    def firstUniqChar1(self, s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1


a = Solution()
print(a.firstUniqChar('lleetcode'))
print(a.firstUniqChar1('lleetcode'))
