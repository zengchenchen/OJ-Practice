class Solution(object):
    def majorityElement(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        print(dic)
        for key, val in dic.items():
            if val >= len(nums) / 2:
                return key


a = Solution()
print(a.majorityElement([8, 8, 7, 7, 7]))
