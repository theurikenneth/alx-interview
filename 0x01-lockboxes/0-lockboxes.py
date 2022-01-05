#!/usr/bin/python3
""" A method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """
    boxes: list_of_list that represents both keys and boxes
    n number of boxes, which makes the length n-1
    a key with the same number as box open each other
    all keys are positive integers
    boxes start at index 0 and boxes[0] is unlocked
    return true, else false
    """
    box_number = len(boxes)
    keys_list = boxes[0]
    locked_box = [False] + [True] * (box_number - 1)
    for key in keys_list:
        if ((key < box_number) and (locked_box[key] is True)):
            locked_box[key] = False
            keys_list.extend(boxes[key])
    return not any(locked_box)
