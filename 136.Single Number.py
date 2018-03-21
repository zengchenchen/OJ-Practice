class Solution():
    def Single_Number(self, li):
        for i in range(0, len(li)):
            signal = True
            for j in range(0, i):
                if li[i] == li[j]:
                    signal = False
                    break
            if signal == True:
                for k in range(i + 1, len(li)):
                    if li[i] == li[k]:
                        signal = False
                        break

            if signal == True:
                return li[i]

    def quick_sort(self, li, l, r):
        if l - 1 >= r:
            return
        flag = l - 1
        for i in range(l, r + 1):
            if li[flag] > li[i]:
                temp = li[i]
                del li[i]
                li.insert(flag, temp)
                flag = flag + 1
        self.quick_sort(li, l, flag - 1)
        self.quick_sort(li, flag + 2, r)
        if li[0] != li[1]:
            return li[0]
        elif li[len(li) - 1] != li[len(li) - 2]:
            return li[len(li) - 1]
        else:
            for i in range(1, len(li) - 1):
                while li[i] != li[i - 1] and li[i] != li[i + 1]:
                    return li[i]


a = Solution()
print(a.Single_Number([1, 2, 2]))
li1 = [2, 2, 4, 7, 4, 3, 3]
print(a.quick_sort(li1, 1, 6))
