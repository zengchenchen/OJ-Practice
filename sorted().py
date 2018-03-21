x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)
y = [4, 6, 2, 1, 7, 9]
y[:] = [0, 0, 0, 0, 0, 0]
print(y)
z = [4, 6, 2, 1, 7, 9]
z[:].sort()
print(z)

a = [('2', '3', '10'), ('1', '7', '7'), ('5', '6', '7'),
     ('2', '5', '10'), ('2', '4', '10')]
b1 = sorted(a, key=lambda x: (int(x[2]), int(x[1])), reverse=False)
b2 = sorted(a, key=lambda x: int(x[2]), reverse=False)
b3 = sorted(a, key=lambda x: x[2], reverse=False)
print(b1)
print(b2)
print(b3)

s = "Sorting1234"
c1 = sorted(s, key=lambda x: x.isdigit())
c2 = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0))
c3 = sorted(s, key=lambda x: (x.isdigit(), x.isdigit()
                              and int(x) % 2 == 0, x.isupper()))
c4 = sorted(s, key=lambda x: (x.isdigit(), x.isdigit()
                              and int(x) % 2 == 0, x.isupper(), x))
print(c1)
print(c2)
print(c3)
print(c4)
