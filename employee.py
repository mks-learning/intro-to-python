class Employee:
    def __init__(self, name, payRate):
        self.name = name
        self.payRate = payRate

    def __str__(self):
        return self.name + ', ' + str(self.payRate)

    def pay(self, hoursWorked):
        return self.payRate * hoursWorked


class Manager(Employee):
    def __init__(self, name, payRate, isSalaried):
        Employee.__init__(self, name, payRate)
        self.salaried = isSalaried

    def __str__(self):
        retStr = Employee.__str__(self)
        retStr+= " salaried: " + str(self.salaried)
        return retStr

    def pay(self, hoursWorked):
        if self.salaried:
            return self.payRate
        else:
            return self.payRate * hoursWorked

    def overTimePay(self, hoursWorked):
        return (self.hoursWorked - 40) * 1.5 * self.payRate


emp1 = Employee('Jane Doe', 25.00)
print(emp1)
print('Gross Pay: ' + str(emp1.pay(40)))
m1 = Manager('Sue Smith', 2400, True)
m2 = Manager('Chad Hangen', 18.00, False)
print(m1)
print('Gross Pay: ' + str(m1.pay(50)))
print(m2)
print('Gross Pay: ' + str(m2.pay(35)))
