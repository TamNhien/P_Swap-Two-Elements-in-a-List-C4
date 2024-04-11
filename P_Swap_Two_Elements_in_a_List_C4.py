def swapPosition(lst, pos1, pos2):
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp
    return lst

lst = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPosition(lst, pos1-1, pos2-1))
