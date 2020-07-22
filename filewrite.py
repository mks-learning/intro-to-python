# outfile = open('text.dat', 'w')
# outfile.write('this is line1 \n')
# outfile.write('this is line2 \n')
# outfile.close()
outfile = open('grade.dat', 'w')
grade = 0
count = 0
while grade != 'q':
    print("Enter a grade ('q' to quit):")
    grade = input()
    if grade == 'q':
        break
    outfile.write(grade + '\n')
    count = count + 1
outfile.close()
print("You added "+str(count)+" grades to the file.")
