def triangles(num):
    li = [1]
    for i in range(1, num + 1):
        yield li
        li = list(map(lambda x, y: x + y, li + [0], [0] + li))


f = triangles(5)
for i in f:
    print(i)
