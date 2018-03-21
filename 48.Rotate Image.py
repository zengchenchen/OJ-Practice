class Solution:
    def rotate(self, A):  # 使用zip函数，list(zip(A))与list(zip(*A))
        # a[::-1]对list列表进行反向操作，a=[1,2,3],a[:-1]=[1,2],a[:]=[1,2,3];[3::-1]就是从第3个位置坐标开始 截取顺序相反
        A[:] = zip(*A[::-1])
        return A

    def rotate2(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]


a = Solution()
print(a.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
