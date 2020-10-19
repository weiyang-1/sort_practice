# -*- coding: utf-8 -*-

"""
@Created: 2020/10/13 11:35
@AUTH: MeLeQ
@Used: pass
"""

import math
import random


def gene_random_list() -> list:
    """
    生成随机乱序列表
    :return:
    """
    return [random.randint(1, 100) for _ in range(100)]


def show_tree(array: list):
    """
    展示大根树的形状
    :param array:
    :return:
    """
    index = 1
    depth = math.ceil(math.log2(len(array)))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()


if __name__ == '__main__':
    l = gene_random_list()
    print(l)
    # orignal_list = [0, 74, 73, 59, 72, 64, 69, 43, 36, 70, 61, 40, 16, 47, 67, 17, 31, 19, 24, 14, 20, 48, 5, 7, 3, 78, 84, 92, 97, 98, 99]
    # show_tree(orignal_list)