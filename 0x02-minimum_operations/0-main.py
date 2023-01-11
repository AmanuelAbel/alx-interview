#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
print("Min # of operations to reach {} char: {}".format(9, minOperations(9)))
print("Min # of operations to reach {} char: {}".format(21, minOperations(21)))
print("Min # of operations to reach {} char: {}".format(0, minOperations(0)))
print("Min # of operations to reach {} char: {}".format(1, minOperations(1)))
print("Min # of operations to reach {} char: {}".format(19170307, minOperations(19170307)))
print("Min # of operations to reach {} char: {}".format(100, minOperations(100)))
print("Min # of operations to reach {} char: {}".format(2147483640, minOperations(2147483640)))

# print("Min # of operations to reach {} char: {}".format(2147483640, minOperations(2147483640)))


