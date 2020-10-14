# -*- coding: utf-8 -*-

"""
@Created: 2020/10/13 14:41
@AUTH: MeLeQ
@Used: pass
"""

from tools import *


def quick_sort_simple(random_list: list) -> list:
    """
    一行代码搞定快速排序
    :param random_list:
    :return:
    """
    return random_list if len(random_list) <= 1 else quick_sort_simple([i for i in random_list[1:] if i < random_list[0]]) + [random_list[0]] + quick_sort_simple([i for i in random_list[1:] if i >= random_list[0]])


def quick_sort(random_list: list) -> list:
    """
    快速排序 使用二分的方法快速的把列表的数据进行排序
    :param random_list:
    :return:
    """
    if len(random_list) <=1:
        return random_list
    else:
        left_list = []
        right_list = []
        for i in random_list[1:]:
            if i < random_list[0]:
                left_list.append(i)
            else:
                right_list.append(i)
        return quick_sort(left_list) + [random_list[0]] + quick_sort(right_list)


if __name__ == '__main__':
    r = quick_sort(gene_random_list())
    print(r)