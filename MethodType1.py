class Solution(object):
    pass


def set_age(self, age):
    self.age = age


s = Solution()
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(10)
print(s.age)
