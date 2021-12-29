#!/usr/bin/python3
"""
determines if a given dataset represents a
valid UTF-8 encoding
"""


def validUTF8(data):
    if type(data) is not list:
        return False
    for dataset in data:
        if type(dataset) is not int:
            return False
    retuen True
