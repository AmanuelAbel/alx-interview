#!/usr/bin/python3

"""
unlock all the boxes
The first box is open
and every box has a key to another box
"""
def openBoxes(unopenedBoxes, openedBoxes, boxes):
        if len(unopenedBoxes) == 0:
            if len(openedBoxes) == len(boxes):
                return True
            else:
                return False
        key = unopenedBoxes.pop()
        # for key in unopenedBoxes:
        # print('my key is: ', key)
        if key not in openedBoxes:
            for i in boxes[key]:
                # print ("opendedssss:", key)
                if i not in openedBoxes and i < len(boxes):
                    unopenedBoxes.add(i)
        openedBoxes.add(key)
        # print('opened: ', openedBoxes)
        # print('unopened: ', unopenedBoxes)
        # print('--------------------------------')
        return openBoxes(unopenedBoxes, openedBoxes, boxes)
def canUnlockAll(boxes):
    size = len(boxes)
    openedBoxes = set()
    unopenedBoxes = set()
    unopenedBoxes.add(0)
    # openedBoxes = [0] * (size)
    # openedBoxes[0] = 1
    # print (openedBoxes)
    # for key in boxes[0]:
    #     unopenedBoxes.add(key)
    #     print ("first keys: ", key)
    x = openBoxes(unopenedBoxes, openedBoxes, boxes)
    return x
    # for i in range(size):
    #     if openedBoxes[i] == 1:
    #         for key in boxes[i]:
    #             print ("opened", i)
    #             if key < size and key >= 0:
    #                 openedBoxes[key] = 1
    #                 i = 0
    # if 0 in boxes:
    #     return False
    # else:
    #     return True


    for box in boxes:
        for key in box:
            if key < size and key >= 0:
                openedBoxes[key] = 1
    if 0 in openedBoxes:
        return False
    else:
        return True
    
    
#!/usr/bin/python3
"""
unlock all the boxes
The first box is open
and every box has a key to another box
"""

def openBoxes(unopenedBoxes, openedBoxes, boxes):
    """
    use all the keys as much as you can using set
    """
    if len(unopenedBoxes) == 0:
        if len(openedBoxes) == len(boxes):
            return True
        else:
            return False
    box = unopenedBoxes.pop()
    if box not in openedBoxes:
        for key in boxes[box]:
            if key not in openedBoxes and key < len(boxes):
                unopenedBoxes.add(key)
    openedBoxes.add(box)
    return openBoxes(unopenedBoxes, openedBoxes, boxes)


def canUnlockAll(boxes):
    """ using set """
    openedBoxes = set()
    unopenedBoxes = set()
    unopenedBoxes.add(0)
    x = openBoxes(unopenedBoxes, openedBoxes, boxes)
    return x
