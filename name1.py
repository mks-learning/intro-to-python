class Name:
    # constructor - instantionation = create an instance of a class
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last

# to-string methond
# this def is what is resturned when you call the class on its own
# i.e print(aNme)
    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last

# this def is what is resturned when you call the class on its own
# i.e print(aNme.functioName())
    def lastFirst(self):
        return self.last + ', ' + self.first + ' ' + self.middle

    def initials(self):
        return self.first[0] + self.middle[0] + self.last[0]


aName = Name('Mary', 'Elizabeth', 'Smith')
print(aName)
print(aName.lastFirst())
print(aName.initials())
print("The value of the Name class is " + str(aName))
