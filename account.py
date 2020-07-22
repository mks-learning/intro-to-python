class Account:
    def __init__(self, acctNumber, balance):
        self.acctNumber = acctNumber
        self.balance = balance

    def __str__(self):
        retStr = "For account: " + str(self.acctNumber) + '\n'
        retStr += "the balance is " + str(self.balance)
        return retStr


class Checking(Account):
    def __init__(self, acctNumber, balance, fee):
        # remember when extending a class view inheritance
        # you need to define the init as the original attributes
        # so they are availalbe to the chile (inherited) class
        Account.__init__(self, acctNumber, balance)
        self.fee = fee

    def __str__(self):
        retStr = "Account type: Checking\n"
        retStr += Account.__str__(self)
        return retStr

    def getFee(self):
        return self.fee

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds in account.')
        else:
            self.balance = self.balance - amount - self.fee


acct1 = Account('2342342', 1083.00)
print(acct1)
dda = Checking('0973', 13933.00, .95)
print(dda)
dda.withdraw(100)
print(dda)
dda.deposit(100.95)
print(dda)
