class Solution(object):
    def spiralOrder(self, matrix):
        s = []
        while matrix:
            if len(matrix[0]) == 0:
                return s
            if len(matrix[0]) == 1:
                for i in matrix:
                    s = s + i
                return s
            s = s + matrix.pop(0)
            if matrix:
                for i in matrix:
                    s.append(i.pop())
            if matrix:
                s = s + matrix.pop()[::-1]
            if matrix:
                for j in matrix[::-1]:
                    s.append(j.pop(0))
        return s

    def spiralOrder2(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])


a = Solution()
print(a.spiralOrder([[1, 11], [2, 12], [3, 13], [4, 14]]))
# 特殊情况应该考虑：matrix=[],matrix=[[]],matrix=[[1],[2],[3]]，从一开始就确定大致分几类;
# pop()函数使用应熟练，避免empty list 出错；
# 基础知识应重视，matrix=[](false),matrix=[[]](true).
