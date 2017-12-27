"""

这是nester.py模块，提供了一个名为print_lol的函数用来打印列表，
其中包含或不包含嵌套列表。
增加一个名为print_file的函数，用来将内容输入到文件中，并保持print_lol的特性。

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


def print_file(the_list, the_file, indent = True, the_separator = ''):
    """

    :param the_list:位置参数，所提供的列表将递归输入到文件中，各占一行。
    :param the_file:写入文件名。
    :param indent:是否分割，True代表默认分割。
    :param the_separator:分隔符，默认为空。
    :return: NONE

    """
    try:
        with open(the_file, 'w') as date:
            for each_item in the_list:
                try:
                    print(each_item, file=date, end='')
                    if indent:
                        print(the_separator, file=date)
                except ValueError as err:
                    print("value error:" + str(err))
    except IOError as err:
        print("file error:" + str(err))