# readin = open('foo.dat', 'r')
# line = readin.readline()
# while (line):
#     print(line, end='')
#     line = readin.readline()
#
# for line in open('foo.dat'):
#     print(line, end='')

sum = 0
count = 0
for grade in open('grade.dat'):
    print(grade, end='')
    sum = sum + int(grade)
    count = count + 1
average = sum / count
print('Average: ' + str(average))
