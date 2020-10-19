# -*- coding: utf-8 -*-

"""
@Created: 2020/10/19 16:23
@AUTH: MeLeQ
@Used: pass
"""

from tools import *


def build_heap(l):
    """
    构建大顶堆
    :param l:
    :return:
    """
    l_len = len(l)
    for i in range((l_len - 2) // 2, -1, -1):
        re_heap(l, l_len, i)


def re_heap(h, size, root):
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
    if left < size and h[left] > h[larger]:
        larger = left
    if right < size and h[right] > h[larger]:
        larger = right
    if larger != root:
        h[larger], h[root] = h[root], h[larger]
        re_heap(h, size, larger)


def heapsort(random_list: list) ->list:
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
