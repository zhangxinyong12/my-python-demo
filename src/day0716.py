class Student:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


s = Student(20)
s.age = 10
print(s.age)


# 单例模式
class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


n1 = Singleton()
n2 = Singleton()
print(n1, n2)
print(n1 == n2)

# 模块
# import calculate
#
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res=calculate.add(*list1)
# print(res)

from calculate import add

res = add(*list1)
print(res)
