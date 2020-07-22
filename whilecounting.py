# sum = 0
# number = 1
# print("What plustorial do you want to calculate?")
# lastnum = int(input())
# while number <= lastnum:
#     sum = sum + number
#     number = number + 1
# print("The plustorial of " + str(lastnum) + " is " + str(sum) + ". All done.")

#Calculating Interest on an account
print("What is the begining balance?")
initbalance = int(input())
balance = initbalance
print("What is the interest rate?")
rate = int(input())/100 + 1
year = 1
while year <= 10:
    balance = balance * rate
    print("for year " + str(year) + ": " + str(balance) + " is your balance.")
    year = year + 1
intearned = balance - initbalance
print ("The inital balance of "+ str(initbalance) + "  grows to " + str(balance) + " at a rate of "+ str(rate)+ "over 10 years. That is "+str(intearned)+" in interest alone.")
