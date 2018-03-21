class Solution(object):
    def __init__(self, name, age):
        self.myName = name
        self.myAge = age

    def getAge(self):
        return self.myName, self.myAge


temp = Solution('zcc', 18)
print(temp.getAge())
print(temp.myName)
temp.myAge = 17
print(temp.myAge)
