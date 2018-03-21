class Solution(object):
    def sortColors(self, nums):
        a, b, c = 0, 0, 0
        for i in nums:
            if i == 0:
                a = a + 1
            elif i == 1:
                b = b + 1
            else:
                c = c + 1
        nums[:a] = [0 for j in range(a)]  # 切片是在原list上做改变
        nums[a:a + b] = [1 for j in range(b)]
        nums[a + b:] = [2 for j in range(c)]
        return nums

        # 使用字典做统计
        # items = ["cc","cc","ct","ct","ac"]
        # count = {}
        # for item in items:
        #     count[item] = count.get(item, 0) + 1


a = Solution()
print(a.sortColors([0]))
