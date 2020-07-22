# #fpr known sets of data
# # # grades = [71, 81, 77, 84]
# # # # for i in range(len(grades)):
# # # #     grades[i] = grades[i] + 5
# # # print(grades)
# # # grades = [grade + 5 for grade in grades]
# # # print(grades)
# # words = ['NOW', 'HELLO', 'IS', 'HOW']
# # print(words)
# # words = [word.lower() for word in words]
# # print(words)
# #
# # list cmp for files
# # #
# # file = open('grade.dat')
# # grades = file.readlines()
# # print(grades)
# # for i in range(len(grades)):
# #      grades[i] = grades[i].rstrip()
# grades = [grade.rstrip() for grade in open('grade.dat')]
# print(grades)


# N = range(1,101)
# EN = [x for x in N if x % 2 == 0]
# print(EN)

sent = "here is a sentence of lots of words that are in a single sentence."
words = sent.split(' ')
wlen = [(word, len(word)) for word in words]
for i in wlen:
    print(i)
