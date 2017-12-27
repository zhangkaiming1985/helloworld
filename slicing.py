shoplist = ['apple', 'mango', 'banana', 'carrot']
name = 'swaroop'

print('Item 0 is', shoplist[0])
print('Item -1 is', shoplist[-1])

print('Item 0 to 3 is', shoplist[0:3])
print('Item start to end is', shoplist[:])
print('1', shoplist)
print('2', shoplist[1:])  # 从第二个元素开始
print('3', shoplist[:-1])  # 去掉最后一个元素
print('4', shoplist[:-2])  # 去掉倒数两个元素
print('5', shoplist[::])  # 相当于1，2，3参数全都默认，即从头到尾，步长为1
print('6', shoplist[:2])
print(shoplist[::4])



