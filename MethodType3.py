class Solution(object):
    pass


def set_age(self, age):
    self.age = age


Solution.set_age = set_age
s = Solution()
s.set_age(10)
print(s.age)
