# -*- coding: utf-8 -*-

"""
@Created: 2020/10/14 11:48
@AUTH: MeLeQ
@Used: pass
"""

from tools import gene_random_list


def merge_list(left_list: list, right_list: list) -> list:
    """
    合并两个数组的值 将其按照大小顺序放到新的数组中
    :param left_list: 有序数组
    :param right_list: 有序数组
    :return: 有序数组
    """

    tmp_list = []
    l_index = r_index = 0
    if len(left_list) == 0 and len(right_list) == 0:
        return tmp_list
    while l_index < len(left_list) and r_index < len(right_list):
        if left_list[l_index] <= right_list[r_index]:
            tmp_list.append(left_list[l_index])
            l_index += 1
        else:
            tmp_list.append(right_list[r_index])
            r_index += 1
    if l_index == len(left_list):
        for i in right_list[r_index:]:
            tmp_list.append(i)
    else:
        for j in left_list[l_index:]:
            tmp_list.append(j)

    return tmp_list


def merge_sort(random_list: list) -> list:
    """
    归并排序 把数组分出无数个小数组  每个小数组排序之后合并到一起
    :param random_list:
    :return:
    """
    if len(random_list) <= 1:
        return random_list
    else:
        left = merge_sort(random_list[:(len(random_list)//2)])
        right = merge_sort(random_list[(len(random_list)//2):])
        return merge_list(left, right)


if __name__ == '__main__':
    r = merge_sort(gene_random_list())
    print(r)