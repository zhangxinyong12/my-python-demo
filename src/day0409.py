print('2020-04-09')


class Person:
    name = '34'
    __age = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def getname():
        print(Person.name)

    def setAge(self, age):
        self.__age = age


Person.getname()
zhang = Person('张三')
print(zhang.name)
Person.getname()
 # p 156
