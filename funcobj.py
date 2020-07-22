#
#
# num = 10
# sqnum = square(num)
# sqnumber = square
# sqnum = sqnumber(2)
# print(sqnum)
#
# #map - higher-oder function, it calls anoyher function to work

# square = lambda x: x * x
# print(square(2))

# numbers = [1, 2, 3, 4]
# numberssq = list(map(lambda x: x * x, numbers))

def square(number):
    return number * number


def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def sum(x,y):
    return x+ y


# numbers = [1, 2, 3, 4]
# numberssq = list(map(square, numbers))
# print(numberssq)
# evens = list(filter(even, numbers))
# print(numbers)
# print(evens)


import functools
numbers = list(range(1,11))
sum = functools.reduce(sum, numbers)
print(numbers)
print(sum)
