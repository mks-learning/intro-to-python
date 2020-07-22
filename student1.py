class Student:
    # fields - name, id, grades(list)
    grades = []

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def addGrade(self, grade):
        self.grades.append(grade)

    def showGrades(self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds

    def __str__(self):
        return "Name: " + self.name + '\n' + \
               "Id: " + self.id + '\n' + \
               "Grades: " + self.showGrades()

    def average(self):
        total = 0
        for grade in self.grades:
            total += grade
            # since grades is an array using Len is a short cut to
            # elimnating the need for a counter
        return (total / len(self.grades))


stu1 = Student('Jones', '123')
stu1.addGrade(91)
stu1.addGrade(88)
stu1.addGrade(73)
print(stu1)
print("Average: " + str(stu1.average()))
