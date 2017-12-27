name = 'hello,world.'

if name.startswith('hel'):
    print('Yes, the String stat with "hel"')
if 'o' in name:
    print('Yes, the String contains "o".')
if name.find('or') != -1:
    print('Yes, the String contains "or"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India']
delimiter.join(mylist)
print(mylist)
print(delimiter.join(mylist))
