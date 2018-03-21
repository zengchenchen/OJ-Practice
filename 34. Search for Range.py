import bisect


class Solution():
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):  # 二分法查找
        left = 0
        right = len(A) - 1

        result = [-1, -1]

        while left <= right:
            mid = (left + right) / 2

            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                result[0] = mid
                result[1] = mid

                i = mid - 1
                while i >= 0 and A[i] == target:
                    result[0] = i
                    i -= 1

                i = mid + 1
                while i < len(A) and A[i] == target:
                    result[1] = i
                    i += 1

                break

        return result

    def searchRange1(self, nums, target):  # 运用库bisect,该库接受有序的序列，内部实现就是二分法
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect_right(nums, target) - 1] if target in nums[lo:lo + 1] else [-1, -1]


a = Solution()
print(a.searchRange1([1, 1, 1, 2], 1))
