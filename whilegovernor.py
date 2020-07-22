average = 0.0
total = 0
count = 0
print("Enter a grade (enter -1 to quit): ")
grade = int(input())
while True:
    total = total + grade
    count = count + 1
    print("Enter a grade (enter -1 to quit): ")
    grade = int(input())
    # if grade <= -2:
    #     # throws out negative grades
    #     continue
    # if grade > 100:
    #     #throws out unachieveable grades
    #     continue
    if grade == -1:
        break
average = total / count
print("Average grade for this list is " + str(average))
