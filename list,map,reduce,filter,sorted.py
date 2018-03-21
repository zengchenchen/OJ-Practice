a = ['a', 'b', 'c']
# a.insert(0,'A')
# a.remove('a')
# a[0]='a1'
# print(a[-1])

from functools import reduce
a = list(map(lambda x: x + 1, [1, 2, 3]))
a1 = list(map(str, [1, 2, 3]))

b = reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9])

c = list(filter(lambda x: x > 0, [-1, -2, 0, 1, 2]))
c1 = list(filter(lambda x: x and x.strip(), ['a', ' ', '', 'b', 'c', None]))

d = sorted([4, 3, 2, 1])
dict_ = {'a': 1, 'b': 2, 'c': 3}
# print(list(dict_.keys()))
# print(list(dict_.values()))
# print(list(dict_.items()))
d1 = sorted(dict_.keys())
d2 = sorted(dict_.values())
d3 = sorted([-1, -2, -3, -4], key=abs, reverse=True)

import re
e = re.match(r'[\+\-]+', '+-')
print(e)

f = ''
print(f.join(['z', 'c', 'c']))

g = 'abc'
print(g[::-1])  # 反向切片翻转字符串
print(g[0].isalnum())  # 判断字符串是否是由字母或数字组成的
print(g.islower())  # 判断字符串是否由小写字母组成
print(g.istitle())  # 字符串中所有的单词拼写首字母是否为大写，且其他字母为小写

h = [('one', 1), ('two', 2), ('three', 3)]
print(dict(h))  # dict()函数,将list转化为dict
