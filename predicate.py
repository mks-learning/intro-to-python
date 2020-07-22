def square(number):
    # this is a value retuning function
    return number * number


def isVowel(letter):
    vow = ('aeiou')
    if letter in vow:
        return True
    else:
        return False


def numVowles(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if isVowel(string[i]):
            count += 1
            # count = count + 1 is shortend to +=
    return count


# print("Enter a number to square: ")
# num = int(input())
# numsquared = square(num)
# print(numsquared)
#
# the program for this entire file is below There
#
print("Please enter a word and I will count the vowels:")
word = input()
wordvow = numVowles(word)
print('There are ' + str(wordvow) + ' vowels in ' + word + '.')
