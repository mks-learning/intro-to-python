class Person:
    # defining the attribures of the class person - name, sex, age
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.sex

    def changeName(self, name):
        # allows for future naeme changes
        self.name = name

    def changeAge(self):
        # accounts for aging of the Person
        self.age = self.age + 1


person1 = Person('Jane Doe', 23, 'F')
person2 = Person('Vikram Patel', 24, 'M')
print('Person1: ' + str(person1))
person1.changeAge()
print('Person1: ' + str(person1))
person1.changeName('Happy Eats')
print('Person1: ' + str(person1))
print('Person2: ' + str(person2))
