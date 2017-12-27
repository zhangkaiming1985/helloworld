import os

# if os.path.exists('sketch'):
try:
    date = open('sketch')
    for line in date:
        try:
            (role, line_spoken) = line.split(":", 1)
            # 可选参数，用于限定定界符的个数。
            print(role, "said:", line_spoken)
        except ValueError:
            pass
    date.close()
except IOError:
    print("The date file is missing.")



'''
print(date.readline(), end='')
print(date.readline(), end='')

date.seek(0)
# seek返回起始位置
for line in date:
    print(line)

date.seek(0)
(role, line_spoken) = date.readline().split(":")
print(role, line_spoken)

for line in date.readline().split(":"):
    print(line)

for line in date:
    if not line.find(":") == -1:
        (role, line_spoken) = line.split(":", 1)
        # 可选参数，用于限定定界符的个数。
        print(role, "said:", line_spoken)
'''