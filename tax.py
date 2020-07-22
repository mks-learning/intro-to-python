# 0 - 240 -> 0%
# 241 - 480 -> 15%
# 481 -> 28%
def tax(amount):
    if amount > 480:
        return amount * .28
    elif amount < 241:
        return 0
    else:
        return amount * .15


def netpay(grosspay):
    return grosspay - tax(grosspay)


# print('What is the amount to be taxed? ')
# amt = int(input())
# print('The amount you entered was ' + str(amt) + ' and the tax on that will \
# be ' + str(tax(amt)) + '.')
print('Enter the gross pay for the period:')
gp = int(input())
print('The net pay for this period is ' + str(netpay(gp)) + '.')
