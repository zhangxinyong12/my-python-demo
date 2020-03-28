# 面向对象
class Phone:
    brand = '小米'
    price = 4999
    type = "mate 8 pro"

    def __init__(self):  # 构造方法
        print('开始初始化Phone')

    def call(self):
        # self指的是实例
        print(self)
        print(self.type)
        print('正在打电话')
        # print(self.type2)  # 不一定保证有这个属性和方法


myPhone = Phone()

# print(myPhone.brand)
# myPhone.brand = '红米'
# print(myPhone.brand)
# myPhone.call()
#
# myPhone2 = Phone()
#
# myPhone2.call()
# myPhone2.type2 = '33333333333'
# print(myPhone2.type2)
