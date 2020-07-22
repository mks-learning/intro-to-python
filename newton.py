# usefulness of nested functions and variables

import math


#
# def sqrt(number):
#     return sqrthelp(1.0, number)
#
#
# def sqrthelp(guess, number):
#     if(closeenough(guess, number)):
#         return guess
#     else:
#         return sqrthelp(improve(guess, number), number)
#
#
#
#
#
#
def average(x, y):
    return (x + y) / 2


def square(number):
    return number * number


def sqrt(number):
    def closeenough(guess, number):
        return (math.fabs((square(guess)) - number) < 0.001)

    def improve(guess):
        return average(guess, (number / guess))

    def sqrthelp(guess):
        if(closeenough(guess)):
            return guess
        else:
            return sqrthelp(improve(guess))

    return sqrthelp(1.0)
