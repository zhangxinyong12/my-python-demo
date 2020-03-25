# #
# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n  # yield = return + 暂停
#
#
# # g = func()
# # print(g)
# # print(g.__next__())
# # print(next(g))
#
#
# def fid(length):
#     a, b = 0, 1
#     n = 0
#     while n < length:
#         yield b
#         a, b = b, a + b
#         n += 1
#     return '结束'
#
#
# g = fid(8)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen():
#     i = 0
#     while i < 5:
#         temp = yield i
#         print('temp=', temp)
#         i += 1
#     return '没有更多'
#
#
# g = gen()
# g.send(None)
# n1 = g.send('abc')
# print(n1)
# n2 = g.send('erdf')
# print(n2)
#  进程 > 线程 >  协程
#
# def task1(n):
#     for i in range(n):
#         print('正在搬第{}块砖'.format(i))
#         yield
#
#
# def task2(n):
#     for i in range(n):
#         print('这么着听第{}首有音乐'.format(i))
#         yield
#
#
# g1 = task1(10)
# g2 = task2(5)
#
# while True:
#     try:
#         next(g1)
#         next(g2)
#     except:
#         break
# 可迭代的对象
# 生成器
# 元组
# 列表
# 集合
# 字典
# 字符串
from collections.abc import Iterable

list1 = [1, 2, 3, 4]
print('list1', isinstance(list1, Iterable))

str1 = '1111'
print('str1', isinstance(str1, Iterable))

g = (x for x in range(10))
print('g', isinstance(g, Iterable))
# 迭代器
''''
迭代器

'''
list1 = iter(list1)
print(next(list1))

# p 142
