class Solution(object):
    def moveZeroes1(self, nums):
        move_nums = []
        num = 0
        for i in nums:
            if i == 0:
                num = num + 1
            else:
                move_nums.append(i)
        for i in range(num):
            move_nums.append(0)
        return move_nums

    def moveZeroes2(self, nums):
        num = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                num = num + 1
                i = i - 1
            i = i + 1
        for i in range(num):
            nums.append(0)
        return nums


a = Solution()
print(a.moveZeroes2([0, 0, 1]))
