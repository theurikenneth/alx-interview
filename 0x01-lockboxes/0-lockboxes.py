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
    from copy import Deepcopy

    # checks if boxes is a positive integer and a list
    if type(boxes) != list or len(boxes) < 1:
        return False

    # checking that all boxes have a valid key
    for x in boxes:
        if type(box) != list:
            return False

    # deepcopy allows creation of copies without altering originals
    duplicate_boxes = deepcopy(boxes)

    # creating a list of keys available
    available_keys = [0]
    #confirm that there are available using the while loop
    while len(available_keys) > 0:
        # setting the first key
        first_key = available_keys[0]
        # removing used keys since they are not valid
        available_keys = available_keys[1:]
        #confirms that the given first key is valid
        if type(first_key) is not int or first_key < 0:
            return False

        # indicate that the box is opened using the -1 flag
        duplicate_boxes[first_key].append(-1)
        # check through the opened boxes key and save that
        for current_key in duplicate_boxes[first_key]:
            # if its marked -1, it is not valid
            if current_key is -1:
                continue
            # check if it is within range
            if current_key >= len(duplicate_boxes):
                continue
            # continue if the box was already opened
            if -1 in duplicate_boxes[current_key] or current_key in available keys:
                continue
            # append and update the available keys
            available_keys.append(current_key)

    # confirming all boxes are opened (they have -1 flag)
    for x in duplicate_boxes:
        if -1 not in x:
            return False # shows it was not unlocked

    return True

