"""
Author: Marinda Keller
Purpose: Practice while loops
"""

print ("Welcome to the Word Game!")
print()
secret_word = ""
secret_word = "shelf"
guess = ""
position = 0
count = 0
position = 0
sw_len = -1
guess_len = -1
sw_len = int(len(secret_word))
while guess != secret_word:
    print("Your hint is:", end="")
    #HERE 
    for index, letter in enumerate(secret_word):
        #print(f"The letter {letter} is at position {i}")
        print("_ ", end="")

    print(count)
    guess = input("What is your guess? ").lower()
    count = count + 1

    if guess == secret_word:
        print("CONGRATULATIONS!")
    else:
        print("Your hint is: ", end=" ")
        print()
        while position < len(secret_word) and position < len(guess):
            if guess[position] == secret_word[position]:
                print(guess[position].upper() + " ", end="")
            elif guess[position] in secret_word:
                print(guess[position].lower() + " ", end="") 
            else:
                print(("_ "), end="")
            position = position + 1
            print()
print ("test run")
print()

"""
problems not in order
-hints and letters are not appearing on the same line
--solution: look at where the end="" are
-hints do not continue if the guess word is shorter than the secret word
--solution: look at a <>= solution
-hints do not continue after the first round
--issue with a loop

-min requirements:
Have a secret word stored in the program. done
Prompt the user for a guess. done
Continue looping as long as that guess is not correct. STUCK
Calculate the number of guesses and display it at the end. start troubleshooting here
You do not need to have any hints at this point.

Code: 
print ("Welcome to the Word Game!")
secret_word = ""
secret_word = "fives"
guess = ""
count = 0
while guess != secret_word:
    guess = input("What is your guess? ").lower()
    count = count + 1
if guess == secret_word:
    print(f"You guessed it in {count}!")

"""
