def hover(a,b):
    isBetweenX = a[0] >= b[0] and a[0] <= b[0]+b[2]
    isBetweenY = a[1] >= b[1] and a[1] <= b[1]+b[3]
    if (isBetweenY and isBetweenX):
        return True
    return False

def locationAnchor(anchor):
    if anchor == 'NONE':
        return [0, 0]
    elif anchor == 'BOTTOM_RIGHT':
        return [1000, 680]
