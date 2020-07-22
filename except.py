# try:
#     print("Enter a numerator: ")
#     numer = int(input())
#     print("Enter a denominator: ")
#     denom = int(input())
#     q = numer / denom
#     print(q)
# except ZeroDivision:
#     print('Cannot devide by zero')
#     print('Enter a new denominator:')
#     denom = int(input())
#     q = numer / denom
#     print(q)

print("filename?")
fname = input()
log = open(fname, 'r')
for line in log:
    print(line, end='')
#    file.close()
# except:
#     print('Cannot open file.')
#     print('Enter a new file name:')
#     fname = input()
#     file = open(fname, 'r')
#     for line in file:
#          print(line, end='')
#    file.close()
# finally:
#     file.close()
