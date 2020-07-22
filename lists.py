def take(num, lyst):
    tlist = []
    for i in range(0, num, -1):
        print(i)
        tlist.append(lyst[i])
    return tlist


def drop(num, lyst):
    dlist = []
    for i in range(num, len(lyst), -1):
        print(i)
        dlist.append(lyst[i])
    return dlist


names = ['Ray', 'Martin','Lewis', 'LaBron', 'James']
print(names)
somenames = take(-3, names)
print(somenames)
dnames = drop(3, names)
print(dnames)
