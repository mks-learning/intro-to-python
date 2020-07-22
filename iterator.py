# # # numbers = [1, 2, 3]
# # # it = iter(numbers)
# # # print(next(it))
# # # print(next(it))
# # # print(next(it))#
# # fileit = open('grade.dat', 'r')
# # print(next(fileit), end='')
#
# grades = {'c': '9', 'b': '8', 'a': '11'}
# # for key in grades.keys():
# #     print(key, grades[key])
# it = iter(grades)
# #  print(next(it))
# # print(next(it))
# for key in grades:
# #     print(key, grades[key])
#
# numbers = range (1, 10)
# it = iter(numbers)
# print(next(it))
import os
files = os.popen('ls *.py')
fileit = iter(files)
for file in files:
    print(file, end='')
