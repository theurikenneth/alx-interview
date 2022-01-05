#!/usr/bin/python3
"""
determines if a given dataset represents a
valid UTF-8 encoding
"""


def validUTF8(data):
    """shows whether a dataset
    is a valid encoding"""
    size = 0

    set1 = 1 << 7
    set2 = 1 << 6

    for element in data:
        set = 1 << 7
        if size == 0:
            while set & element:
                size += 1
                set = set >> 1
            if size == 0:
                continue
            if size == 1 or size > 4:
                return False
        else:
            if not (element & set1 and not (element & set2)):
                return False
        size -= 1
    return size == 0
"""
if type(data) is not list:
        return False
    for dataset in data:
        if type(dataset) is not int:
            return False
    return True
"""
