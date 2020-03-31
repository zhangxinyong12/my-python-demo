'''

静态方法 @staticmethod
只能访问类的属性和方法
无参数
'''


class Person:
    __age = 18  # 私有属性

    def show(self):
        pass
        # print(self.age)

    @classmethod
    def addAge(cls):
        cls.__age = cls.__age + 1
        print(cls.__age)

    @staticmethod
    def getAge():
        print('静态方法', Person.__age)


zhang = Person()
zhang.show()
Person.addAge()
Person.getAge()
# zhang.addAge()
# zhang.addAge()

# P147