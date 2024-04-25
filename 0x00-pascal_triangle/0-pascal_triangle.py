#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n """
    lists = []

    for i in range(n):
        Alist = []

        for j in range(i + 1):
            if j == 0 or j == i:
                Alist.append(1)
            else:
                Alist.append(lists[i-1][j] + lists[i-1][j-1])

        lists.append(Alist)
    return lists
