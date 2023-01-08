#!/usr/bin/python3
"""
unlock all the boxes
The first box is open
and every box has a key to another box
"""


def canUnlockAll(boxes):
    """ find every key to open all """
    size = len(boxes)
    keys = [0]
    for i in keys:
        for key in boxes[i]:
            if key not in keys and key < size:
                keys.append(key)
    if len(keys) == size:
        return True
    else:
        return False
