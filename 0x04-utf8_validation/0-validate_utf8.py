#!/usr/bin/python3
"""
Validate UTF-8 Module
"""


def validUTF8(data):
    """validate data if it is utf-8"""
    state = 0
    for num in data:
        bit = 0b10000000
        if not state:
            while (bit & num):
                state += 1
                bit >>= 1
            if state > 4:
                return False
            if state:
                state -= 1
                if state == 0:
                    return False
        elif state > 0:
            if num >> 6 != 2:
                return False
            state -= 1
    return not state
