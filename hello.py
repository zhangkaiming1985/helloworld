# -- coding: utf-8 --
# print()是一个函数。
print("hello world")

age = 10
name = 'xiaoming'

print('{0} is {1} this year.'.format(name, age))
print('{0:_^11}'.format('hello'), end=' ')
print('{0:.4f}'.format(1.0/3))

import sys


print(sys.path)
