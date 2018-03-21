class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res.append(
                list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))
            print(res[-1])
        return res[:numRows]


a = Solution()
print(a.generate(5))
