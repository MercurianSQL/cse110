"""
Author: Marinda Keller
Purpose: Guess my number codealong activity
"""
import random
"""
again = "yes"
while again == "yes":
    count = 0
    guess = 0
    number = 0
    number = random.randint(1, 10)
    #print (number) for testing
    print("Guess my number")
    while guess != number:
        guess = int(input("What is your guess?    "))
        count = count + 1
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
    print ("You guessed it!")
    print (f"It took you {count} guesses")
    again = input("Would you like to play again? yes/no    ").lower()
print ("Thank you for playing. Goodbye.") #18 lines of code, 25-7
"""
#Notes on Instructor code:

# strategy = break it into smaller bits of code.
# define variable


again = "y"
while again == "y":
    count = 0
    guess = 0
    number = 0
    number = random.randint(1, 10)
    #print (number) use for testing
    print("Guess my number")
    while guess != number:
        guess = int(input("What is your guess?    "))
        count = count + 1
        if guess < number:
            print("Higher") 
        elif guess > number:
            print("Lower")
        else:
            print("You guessed it!")
            print(f"It took you {count} guesses.")
    again=input("Would you like to play again? Y or N?    ").lower()
print("Thank you for playing. Goodbye.") #19 lines of code, 52-33