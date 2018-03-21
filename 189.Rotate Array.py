class Solution(object):
    def rotate(self, nums, k):
        if len(nums) == 0:
            return nums
        for i in range(k):
            n = nums.pop()
            nums.insert(0, n)
        return nums


a = Solution()
print(a.rotate([1], 10))
