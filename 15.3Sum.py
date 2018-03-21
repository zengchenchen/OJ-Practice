class Solution(object):
    def threeSum1(self, nums):  # 时间复杂度为n*n*n
        S = []
        s = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                c = -nums[i] - nums[j]
                if c in nums[j + 1:]:  # 时间复杂度为n
                    s.append(nums[i])
                    s.append(nums[j])
                    s.append(c)
                    s.sort()
                    if s not in S:
                        S.append(s)
                    s = []
        return S

    def threeSum2(self, nums):  # 时间复杂度为n*n
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


a = Solution()
print(a.threeSum2([-1, 0, 0, 0, 1, 2, 2, -1, -4]))
