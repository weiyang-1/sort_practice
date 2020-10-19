# -*- coding: utf-8 -*-

"""
@Created: 2020/10/19 16:23
@AUTH: MeLeQ
@Used: pass
"""

from tools import *


def build_heap(p_list: list) -> None:
    """
    构建大顶堆
    :param l:
    :return:
    """
    l_len = len(p_list)
    for i in range((l_len - 2) // 2, -1, -1):
        re_heap(p_list, l_len, i)


def re_heap(r_list: list, size: int, root) -> None:
    """
    重构大顶堆
    :param h:
    :param size:
    :param root:
    :return:
    """
    larger = root
    left = root * 2 + 1
    right = left + 1
    if left < size and r_list[left] > r_list[larger]:
        larger = left
    if right < size and r_list[right] > r_list[larger]:
        larger = right
    if larger != root:
        r_list[larger], r_list[root] = r_list[root], r_list[larger]
        re_heap(r_list, size, larger)


def heapsort(random_list: list) -> list:
    """
    堆排序 大顶堆一直变化最大的数和最后一个数  经过多次变化可以实现全 数组的排序
    :param random_list:
    :return:
    """
    build_heap(random_list)

    l_len = len(random_list)
    for i in range(l_len - 1, -1, -1):
        random_list[0], random_list[i] = random_list[i], random_list[0]
        re_heap(random_list, i, 0)
        # show_tree(random_list)
    return random_list


if __name__ == '__main__':
    print(heapsort(gene_random_list()))
