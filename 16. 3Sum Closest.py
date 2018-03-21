class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        a = []
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                T = nums[i] + nums[l] + nums[r]
                a.append(T)
                if T < target:
                    l = l + 1
                elif T > target:
                    r = r - 1
                else:
                    return T
        a.sort()
        if len(a) == 1 or target < a[0]:
            return a[0]
        if target > a[len(a) - 1]:
            return a[len(a) - 1]
        for j in range(len(a)):
            if a[j] > target:
                break
            j = j + 1
        if a[j] - target > target - a[j - 1]:
            return a[j - 1]
        else:
            return a[j]


a = Solution()
print(a.threeSumClosest([1, 1, 1, 1], 4))
