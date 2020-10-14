# -*- coding: utf-8 -*-

"""
@Created: 2020/10/13 11:35
@AUTH: MeLeQ
@Used: pass
"""


import random


def gene_random_list() -> list:
    """
    生成随机乱序列表
    :return:
    """
    return [random.randint(1, 100) for _ in range(100)]


if __name__ == '__main__':
    l = gene_random_list()
    print(l)