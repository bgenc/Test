__author__ = 'bgenc'

def cumsum(l):
    length = len(l)
    newlist = range(0, length)
    for index in range(length):
        val = int(l[index])
        if index == 0:
            newlist[index] = val
        else:
            newlist[index] = newlist[index - 1] + val
    return newlist

myList = [4,3,6]
print cumsum(myList)