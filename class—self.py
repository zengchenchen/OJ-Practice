class ListNote(object):
    def fun(self, x, y):
        self.name = x
        gender = y
        return gender

    def Try(self):
        return self.name


a = ListNote()
print(a.fun('zcc', 18))
print(a.name)
print(a.Try())
