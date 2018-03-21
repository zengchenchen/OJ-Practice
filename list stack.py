class MinStack(object):

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def getMin(self):
        return min(self.items)


obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
a = obj.getMin()
print(a)
