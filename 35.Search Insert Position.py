class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(0, len(nums) - 1):
            if nums[i] < target <= nums[i + 1]:
                return i + 1
            elif target <= nums[i]:
                return i
            else:
                i = i + 1
        return i + 1


temp = Solution()
print(temp.searchInsert([1, 3, 5, 7], 6))
