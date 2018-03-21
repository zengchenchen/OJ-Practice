class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        end = len(A)
        read = 1
        write = 1
        while read < end:
            if A[read] != A[read - 1]:
                A[write] = A[read]
                write += 1
            read += 1
        return write


p = Solution([1, 2, 2, 3])
print(p)
