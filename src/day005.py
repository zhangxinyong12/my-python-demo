# 抛出异常 raise
def login():
    userName = input('输入用户名')
    if len(userName) < 6:
        print('userName不合法')

        raise Exception('用户长度必须大于6位')
    else:
        print('用户名：', userName)


try:
    pass
    # login()
except Exception as err:
    print('注册失败')
    print(err)
else:
    print('注册成功')

#  列表推导式
names = ['agd', 'sdfgdf', 'toms', 'f', 'juej']
list1 = [name.capitalize() for name in names if len(name) > 3]
print(list1)
list2 = [item for item in range(1, 101) if item % 5 == 0 and item % 3 == 1]
print(list2)

newList = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newList)

list3 = [[1, 3, 5], [2, 4, 6], [3, 6, 9]]
newList3 = [(x[-1]) for x in list3]
print(newList3)
dict1 = {'a': 'A', 'b': 'B', 'c': 'C'}
newDist1 = {value: key for key, value in dict1.items()}
print(newDist1)
print('*' * 20)
# 生成器
g = (x * 3 for x in range(20))
print(type(g))
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(next(g))
# print(next(g))
# print(next(g))
while True:
    try:
        item = next(g)
        print(item)
    except:
        print('没有更多元素')
        break
# p138
