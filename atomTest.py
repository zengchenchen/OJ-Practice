def quick_sort(num, l, r):
    print(l, r, num)
    if l > r:
        return
    flag = l
    for i in range(l + 1, r + 1):
        if num[flag] > num[i]:
            num[flag + 1], num[i] = num[i], num[flag + 1]
            num[flag], num[flag + 1] = num[flag + 1], num[flag]
            flag = flag + 1
    quick_sort(num, l, flag - 1)
    quick_sort(num, flag + 1, r)
    return num


num1 = [2, -2, 4, 7, 1, 6, 0]
print(quick_sort(num1, 0, 6))
