class Students(object):
    def set_score(self, value):
        if not isinstance(value, int):
            return print('value must be int')
        if value < 0 or value > 100:
            return print('value must between 0~100')
        self.score = value


s = Students()
s.set_score(160)
