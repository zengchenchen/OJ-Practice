class Solution(object):
    def maxArea(self, height):
        i, j, S = 0, len(height) - 1, 0
        while j > i:
            s = (j - i) * min(height[i], height[j])
            S = max(S, s)
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return S


a = Solution()
print(a.maxArea([3, 2, 4, 7, 5, 2, 6, 1]))
