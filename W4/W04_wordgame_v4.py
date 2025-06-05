"""
Author : Marinda Keller
Purpose: W 04 Word Game, milestone and final
"""
# creativity[select a random word from a list of words]

print ("Welcome to the Word Game!")
print()

# variables
secret_word = ""
secret_word = "fives"
guess = ""
guess_len = -1
sw_len = -1
count = 0
index = 0
sw_len = int(len(secret_word))

print ("Welcome to the Word Game!")
print()
print("Your hint is:", end="")
for index, letter in enumerate(secret_word):
    print("_ ", end="")

# start outer loop
while guess != secret_word:
    print()
    guess = input("What is your guess? ").lower()
    count = count + 1
    guess_len = int(len(guess))
    if guess == secret_word:
        print(f"Congratulations! You guessed it in {count}!")
    elif guess_len != sw_len:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print ("try again")
    else:
        print ("try again")
        print("Your hint is: ", end="")

# start outer loop
        for index, letter in enumerate(guess):
            if letter == secret_word[index]:
                print(letter.upper() + " ", end="")
            elif letter in secret_word:
                print(letter.lower() + " ", end="")
            else:
                print("_ ", end="")


"""
multiple loops - one big loop that keeps going until 
they guessed the word correctly, and one smaller loop inside 
of the bigger one. 
The small loop will look at each letter in the user's guess and 
see if it is correct or not and 
print out different things based on the current letter.

To generate a hint, 
inside of your outer while loop you need to loop across 
the users guess (using a loop that has an index). 
After you made that loop, then inside the loop, do the following:

IF
Make an "if" to check to see if the current letter matches. 
If so, then print out the current letter as a capital letter. 
You will end up having to use indexing to do this (something like 
    *** if letter == secret_word[index]: ***
ELIF
Make an "elif" to check to see if the letter is in the secret word. 
If so, then print out the current letter as a lower case letter. 
You can use "in" to determine if a letter is in a string. 
ELSE
covers the scenario where it doesn't match (print out a _)


"""