# -*- coding: utf-8 -*-

"""
@Created: 2020/10/14 10:39
@AUTH: MeLeQ
@Used: pass
"""

from tools import *


def shell_sort(random_list: list) -> list:
    """
    希尔排序 插入排序的优化  按照步长进行多次插入排序  每次把步长缩短一半  直到步长为1
    :param random_list:
    :return:
    """
    length = len(random_list)
    if length <= 1:
        return random_list
    gap = length//2
    while gap > 0:
        for i in range(gap, length):
            for j in range(i, 0, -gap):
                if random_list[j-gap] > random_list[j]:
                    random_list[j], random_list[j-gap] = random_list[j-gap], random_list[j]
        if gap == 1:
            break
        gap = gap//2
    return random_list


if __name__ == '__main__':
    r = shell_sort(gene_random_list())
    print(r)