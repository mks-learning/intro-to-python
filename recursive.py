# def fact(number):
#     if number <= 1:
#         return 1
#     else:
#         return number * fact(number - 1)
#
#
# print("Please enter a number you would like to know the factorial")
# factnum = int(input())
# print(str(fact(10)) + "is the factorial of " + str(factnum) + '.')


def explode(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])


def removeDups(word):
    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])


# print(explode("hello"))
word = 'aabbccddeeff'
print(word)
print(removeDups(word))
