# -*- coding: utf-8 -*-

"""
@Created: 2020/10/13 13:50
@AUTH: MeLeQ
@Used: pass
"""

from tools import gene_random_list


def insert_sort(random_list: list) -> list:
    """
    插入排序 保证前面的队列是一个有序的  每次从后面找一个插入到有序的里面去  当后面的数比前面小才需要进行插入  否则跳过当前数
    :param random_list:
    :return:
    """
    length = len(random_list)
    if length <= 1:
        return random_list
    for i in range(1, length):
        for j in range(i,0,-1):
            if random_list[j-1] > random_list[j]:
                random_list[j-1], random_list[j] = random_list[j], random_list[j-1]
            else:
                break
    return random_list


if __name__ == '__main__':
    r = insert_sort(gene_random_list())
    print(r)