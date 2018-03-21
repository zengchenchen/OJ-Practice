class Solution(object):
    def setZeroes(self, matrix):
        c = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    c.append([i, j])
        if c:
            for k in c:
                matrix[k[0]] = [0 for x in range(len(matrix[0]))]
                for l in range(len(matrix)):
                    matrix[l][k[1]] = 0
        return matrix


a = Solution()
print(a.setZeroes([[0]]))
