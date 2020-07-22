class Account:
    def __init__(self, acctNumber, balance):
        self.acctNumber = acctNumber
        self.balance = balance

    def __str__(self):
        retStr = "For account: " + str(self.acctNumber) + '\n'
        retStr += "the balance is " + str(self.balance)
        return retStr

    def deposit(self, amount):
        self.balance += amount


class Savings(Account):
    def __init__(self, acctNumber, balance):
        # remember when extending a class view inheritance
        # you need to define the init as the original attributes
        # so they are availalbe to the chile (inherited) class
        Account.__init__(self, acctNumber, balance)

    def __str__(self):
        retStr = "Account type: Savings\n"
        retStr += Account.__str__(self)
        return retStr

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds in account.')
        else:
            self.balance = self.balance - amount


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

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds in account.')
        else:
            self.balance = self.balance - amount - self.fee


# acct1 = Account('2342342', 1083.00)
# print(acct1)
dda = Checking('0973', 13933.00, .95)
sda = Savings('45096', 1000012.23)
# print(sda)
# dda.withdraw(100)
# print(sda)
# dda.deposit(500)
# print(sda)
accounts = [dda, sda]
print('Display information for: \n')
for i in range(0, len(accounts)):
    print(accounts[i])
