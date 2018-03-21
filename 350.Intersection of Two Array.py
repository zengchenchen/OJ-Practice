from collections import Counter


class Solution(object):
    def intersect1(self, nums1, nums2):
        dic1 = {}
        dic2 = {}
        li = []
        for i in nums1:
            dic1[i] = dic1.get(i, 0) + 1
            if i in nums2:
                dic2[i] = dic2.get(i, 0) + 1
                nums2.remove(i)
        print(dic1)
        print(dic2)
        for key, val in dic1.items():
            for i in range(min(val, dic2.get(key, 0))):
                li.append(key)
        return li

    def intersect2(self, nums1, nums2):
        c1, c2 = Counter(nums1), Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])


a = Solution()
print(a.intersect2([1, 1, 2, 2, 3, 4], [1, 3, 2, 1, 5]))
