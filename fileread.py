# infile = open('grade.dat', 'r')
# line = infile.readline()
# print (line)

count = 0
total = 0
infile = open('grade.dat', 'r')
grade = infile.readline()
while (grade):
    print(grade)
    count = count + 1
    total = total + int(grade)
    grade = infile.readline()
average = total / count
print("Average: " + str(average))
