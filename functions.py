def square(number):
# this is a value retuning function
    return number * number

def numVowles(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        vow = ('aeiou')
        if string[i] in vow:
            count += 1
            # count = count + 1 is shortend to +=
    return count

# print("Enter a number to square: ")
# num = int(input())
# numsquared = square(num)
# print(numsquared)

print("Please enter a word and I will count the vowels:")
word = input()
wordvow = numVowles(word)
print('There are ' + str(wordvow) + ' vowels in ' + word + '.')
