class A:
    def test(self):
        print('AAAAAAAA')


class Person:
    def __init__(self, no, name, salary):
        self.no = no
        self.name = name
        self.salary = salary

    def eat(self):
        print('再吃')

    def __str__(self):
        msg = '工号：{}，姓名：{}，本月工资：{}'.format(self.no, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary


class Work(Person):
    def __init__(self, no, name, salary, hours, per_hour):
        super().__init__(no, name, salary)
        self.hours = hours
        self.per_hour = per_hour

    def getSalary(self):
        money = self.hours * self.per_hour
        self.salary += money
        return self.salary

    def eat(self, foot):
        super().eat()
        print('再吃{}'.format(foot))


class Salesman(Person):
    def __init__(self, no, name, salary, salemoney, percent):
        super().__init__(no, name, salary)
        self.salemoney = salemoney
        self.percent = percent


w = Work('001', 'lilei', 2000, 160, 2)
s = w.getSalary()
print(s)
w.eat('西瓜')


# p164

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
print(s.age)
