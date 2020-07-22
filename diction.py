sentence = 'The quick brown fox jumps over the lazy dog'
sentence += ' Sphinx of black quartz judge my vow'
words = sentence.split(' ')
words = sorted(words)
print('Sentence in sorted order:\n')
print(words)
# (list), [tuple], {dictionary}
numWords = {}
for i in range(0, len(words)):
    # this is a dictionary of words, keys is the word, vaule is the count
    if words[i] in numWords:
        numWords[words[i]] += 1
    else:
        numWords[words[i]] = 1

print('Words list and count: \n')
for key in numWords.keys():
    print(key, numWords[key])
