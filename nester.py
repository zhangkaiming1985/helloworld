"""

这是nester.py模块，提供了一个名为print_lol的函数用来打印列表，
其中包含或不包含嵌套列表。

"""


def print_lol(the_list, level=0):
    """
    :param the_list：位置参数，所提供列表中的数据项将递归打印到屏幕，各占一行。
    :param level: 制表符参数，默认值为0，用于显示嵌套列表前的制表符个数。
    :return: NONE

    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level + 1)
        else:
            for tab_step in range(level):
                print('\t', end='')
            print(each_item)
