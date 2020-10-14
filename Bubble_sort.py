# -*- coding: utf-8 -*-

"""
@Created: 2020/10/13 10:39
@AUTH: MeLeQ
@Used: pass
"""

from tools import gene_random_list


def bubble_sort_excue(random_list: list) -> list:
    """
    冒泡排序 按照从小到大依次排列 每次对比相邻的两个数 判断是否需要交换位置
    :param random_list: 乱序列表
    :return: 顺序列表
    """
    lenght = len(random_list)
    if lenght <= 1:
        return random_list
    for i in range(lenght-1):
        need_sort = False
        for j in range(lenght-i-1):
            if random_list[j] > random_list[j+1]:
                random_list[j], random_list[j+1] = random_list[j+1], random_list[j]
                need_sort = True
        if not need_sort:
            return random_list
    return random_list


if __name__ == '__main__':
    r = bubble_sort_excue(gene_random_list())
    print(r)