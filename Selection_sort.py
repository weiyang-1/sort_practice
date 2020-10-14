# -*- coding: utf-8 -*-

"""
@Created: 2020/10/13 14:20
@AUTH: MeLeQ
@Used: pass
"""

from tools import *


def select_sort(random_list: list) -> list:
    """
    选择排序 每次从未排序的队列里面找一个最小的  放到已排序的队列末端
    :param random_list:
    :return:
    """
    length = len(random_list)
    if length <= 1:
        return random_list
    for i in range(length):
        min_data_index = i
        for j in range(i, length):
            if random_list[j] < random_list[min_data_index]:
                min_data_index = j
        random_list[i], random_list[min_data_index] = random_list[min_data_index], random_list[i]
    return random_list


if __name__ == '__main__':
    r = select_sort(gene_random_list())
    print(r)