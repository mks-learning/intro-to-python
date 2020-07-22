# create a function to calculate factorials
def fact(number):
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product


print('Please enter a number you would like the factorial of?')
factnum = int(input())
print('The factorial of ' + str(factnum) + ' is ' + str(fact(factnum)) + '.')
