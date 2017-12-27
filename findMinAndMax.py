# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0], L[0])
    else:
        min_num = L[0]
        max_num = L[0]
        for i in L:
            if i < min_num:
                min_num = i
            elif i > max_num:
                max_num = i
        return (min_num, max_num)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

