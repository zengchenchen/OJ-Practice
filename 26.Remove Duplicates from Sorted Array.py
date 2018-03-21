def removeDuplicates(A):
    if len(A) == 0:
        return 0
    j = 0
    for i in range(0, len(A)):
        if A[i] != A[j]:
            A[i], A[j + 1] = A[j + 1], A[i]
            j = j + 1
    B = A
    return B[:j], A


print(removeDuplicates([1, 5, 5, 5, 6, 6, 3]))
