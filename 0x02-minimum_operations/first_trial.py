#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method
that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """ find the min operations needed to achive the required H number """
    if n < 2 or not isinstance(n, int):
        return 0
    letter = 1
    copy = 1
    op = 1
    factors = []

    # find all the dividors
    for factor in range(2, (n // 2) + 1):
        if n % factor == 0:
            factors.append(factor)

    nim = min(factors)  # find the min divider to use latter

    # count the operation
    while letter <= n:
        if letter == n:
            return op
        # paste until reaching the least factor
        if letter < nim:
            op += 1
            letter += copy
        # paste
        if letter in factors:
            op += 1
            copy = letter
            op += 1
            letter += copy
            # print(f"copy-paste:  paste letter: {letter} copy: {copy}")
        else:
            op += 1
            letter += copy
    return 0
