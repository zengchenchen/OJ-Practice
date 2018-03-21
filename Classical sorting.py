# 冒泡排序
class Solution(object):
    def mp(self, li):
        a, b = 0, 1
        for i in range(len(li) - 1):
            j, k = a, b
            while k < len(li) - i:
                if li[j] <= li[k]:
                    li[j], li[k] = li[k], li[j]
                j = j + 1
                k = k + 1
        return li


a = Solution()
print(a.mp([12, 35, 99, 18, 76]))

# 插入排序


class Solution(object):
    def cr(self, li):
        a, b = 0, 1
        L = [-float('inf'), li[0], float('inf')]
        for i in range(1, len(li)):
            j, k = a, b
            while k < len(L):
                if L[j] <= li[i] <= L[k]:
                    L.insert(j + 1, li[i])
                    print(L)
                    break
                j = j + 1
                k = k + 1
        return L[1:len(L) - 1]


a = Solution()
print(a.cr([12, 35, 99, 18, 76]))

# 快速排序


class Solution(object):
    def kp(self, li):
        if len(li) <= 1:
            return li
        i = 0
        for j in range(1, len(li)):
            if li[j] <= li[i]:
                li.insert(0, li.pop(j))
                i = i + 1
        li[:i] = self.kp(li[:i])
        li[i + 1:] = self.kp(li[i + 1:])
        return li


a = Solution()
print(a.kp([13, 27, 38, 49, 49, 65, 1]))
