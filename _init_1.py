class Solution(object):
    def __init__(self, name):
        self.mynName = name
        print(self.mynName)
        self.myAge = self.getAge(18)
        print(self.myAge)
        return

    def getAge(self, age):
        self.myAgehaha = age
        return self.myAgehaha


temp = Solution('zcc')
