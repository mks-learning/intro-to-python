def ftoc(temp):
    return (temp - 32.0) * (5.0 / 9.0)

def ctof(temp):
    return temp * (9.0 / 5.0) + 32.0

def convert(temp, toScale):
    if toScale.lower() == 'c':
        return ftoc(temp)
    else:
        return ctof(temp)

print("Enter a temprature: ")
tempra = int(input())
print("Enter a scale to convert to (c or f): ")
scale = input()
convertedtemp = convert(tempra, scale)
print(tempra, convertedtemp, scale)
