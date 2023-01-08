#!/usr/bin/python3
"""
    This function returns a list
    with a pascal triangle list
    """


def pascal_triangle(n: int):
    ''' returns a list of pascal triangle '''
    pascal = []
    if n <= 0:
        return []
    for line in range(n):  # number of raws
        arr = [0 for i in range(line + 1)]  # new array for each
        for i in range(n):  # to add elements to the individual array
            if i > line:
                # break if it reaches the limit
                break
            if i == 0 or i == line:
                # add one if it is at the beggining or at the ending
                arr[i] = 1
            else:
                # add compute from perivous and add to the current list
                arr[i] = (pascal[line - 1][i - 1] +
                          pascal[line - 1][i])
        pascal.append(arr)
    return pascal
