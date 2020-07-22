answer = "Watson"
tries = 0
while tries <= 3:
    print("We\'re playing a guessing game. What was the name of the machine that won on Jeopardy?")
    guess = input()
    tries = tries + 1
    if (guess == "Watson"):
        print("That\'s right.")
        break
    elif tries == 3:
        print("Sorry. The answer was "+answer)
        break
    else:
        print("Sorry guess another name.")
print("End")

# if answer == guess:
#     print("You got it right!")
# else:
#     print("Sorry, that is not the right answer. You get two more guesses.")
#     guess = input()
#     if guess == answer:
#         print("You got it right!")
#     else:
#         print("Sorry, wrong again. This is your last guess.")
#         guess = input()
#         if guess == answer:
#             print("You got it right! Well done.")
#         else:
#             print("That's also wrong. The correct answer is " + answer + ". Next time.")
# print("")
