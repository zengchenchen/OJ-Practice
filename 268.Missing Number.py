class Solution(object):
    def missingNumber(self, nums):
        num = max(nums)
        for i in range(num + 1):
            if i not in nums:
                return i
        return num + 1

    def missingNumber1(self, nums):
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)


a = Solution()
print(a.missingNumber([0]))
