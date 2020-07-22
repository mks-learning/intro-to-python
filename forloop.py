# for i in [1,2,3,4,5]:
#     print(i)
#

# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for x in numbers:
#     sum = sum + x
# print(sum)

# For listing out a letter in a word

# word = "hello"
# for letter in word:
#     print(letter)

sentence = "now is the time for all good people to come to the aid"
count = 0
for letter in sentence:
    vowels = "aeiou"
    if letter in vowels:
        count = count + 1
print("The number of vowels in the sentence is " + str(count))
