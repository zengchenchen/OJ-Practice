class animal(object):
    def run(self):
        print('animal is running,,,')


class dog(animal):
    pass


class cat(animal):
    def run(self):
        print('cat is running,,,')
        return


temp1 = dog()
temp1.run()
temp2 = cat()
temp2.run()
