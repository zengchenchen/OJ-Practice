# -*- coding: utf-8 -*-
def removeDuplication(li):
    a = li[:]
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                li.remove(a[j])
    return li


li = [1, 1, 1, 2]
print(removeDuplication(li))
