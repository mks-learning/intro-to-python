print('This program calculates factorials. What number\'s \
factorial would you like to calculate?')
num = int(input())
fact = 1
if num < 100:
    for i in range(1, num + 1):
        fact = fact * i
    print(str(num) + '! is ' + str(fact) + '.')
else:
    print('I\'m a wee computer and can\'t process that high just yet. Bye')
