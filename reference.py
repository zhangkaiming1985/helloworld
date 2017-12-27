print('Simple Assignment')
shoplist = ['apple', 'carrot', 'penguin', 'elephant']

mylist = shoplist

print('mylist', mylist)
del shoplist[0]
print('mylsit:', mylist)
print('shoplist:', shoplist)

mylist = shoplist[:]
del mylist[0]
print('mylist:', mylist)
print('shoplist:', shoplist)
