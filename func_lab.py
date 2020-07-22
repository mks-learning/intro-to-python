# define a function that countrs the number of letters in a given string
def countLetters(words):
    if len(words) < 1:
        return 0
    else:
        return len(words[0]) + countLetters(words[1:])


def first(word):
    return word[0]


def acro(word):
    acro = ''
    acro = acro.join(list(map(first, sentence))).upper()
    return acro


sentence = ['All', 'good', 'and', 'bad', 'things', 'come', 'to', 'an', 'end']
# firstlet = list(map(first, sentence))
# acro = acro.upper()
print(sentence)
# print(firstlet)
acro = acro(sentence)
print(acro)
# print(ACRO)
