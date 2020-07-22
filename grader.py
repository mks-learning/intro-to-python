print("What was the score?")
grade = int(input())
if grade >= 90:
    grade = "A"
elif grade >= 80:
    grade = "B"
elif grade >= 70:
    grade = "C"
elif grade >= 60:
    grade = "D"
elif grade <= 59:
    grade = "F"
else:
   print("Did not recognize input.")    

print("")
print("The students grade: " + grade)
print("")
