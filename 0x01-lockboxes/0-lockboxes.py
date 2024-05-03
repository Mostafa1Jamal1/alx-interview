#!/usr/bin/python3
''' Lockboxes interview question '''


def canUnlockAll(boxes):
    ''' determines if all the boxes can be opened. '''
    keys = {0}
    opened = set()
    while (len(keys) > len(opened)):
        for key in (keys - opened):
            opened.add(key)
            keys.update(boxes[key])

        for key in keys:
            if (key > len(boxes)):
                keys.remove(key)

        if (len(opened) == len(boxes)):
            return True

    return False
