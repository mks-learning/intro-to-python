import newton


def square(number):
    print("not from newton module")
    return number * number


number = 12
print("Square from newton.py: ")
print(newton.square(number))
print("Square from program: ")
print(square(number))
