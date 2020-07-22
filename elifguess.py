message = "Based on the temprature, the recommened activity for you is "
print("What\'s the temprature today?")
temprature = int(input())
if temprature >= 80:
    message = message + "swmimming."
elif temprature >= 65:
    message = message + "tennis."
elif temprature >= 32:
    message = message + "golf."
else:
    message = message + "reading a book by the fire."
print("")
print(message)
print("")
