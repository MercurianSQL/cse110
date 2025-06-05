"""
Author : Marinda Keller
Purpose: W 04 Word Game, milestone and final
"""
# creativity[select a random word from a list of words]

print ("Welcome to the Word Game!")
secret_word = ""
secret_word = "maren"
guess = ""
sw_len = -1
guess_len = -1
count = 0
sw_len = int(len(secret_word))
print(sw_len)
if guess != secret_word:
    print("Your hint is:", end="")
    for i in secret_word:
        print("_ ", end= "")
        print()
guess = input("What is your guess? ").lower()
count = count + 1
if guess == secret_word:
    print(f"You guessed it in {count}!")
elif guess!= secret_word:
    guess_len = int(len(guess))
    print(guess_len)
    if sw_len == guess_len:
        print("Your hint is:", end="")
    for i in secret_word:
        print("_ ", end="")
else:
    print("Sorry, the guess must have the same number of letters as the secret word.")


"""
        for i,letter in enumerate(secret_word): 
            print("_ ", end="")
Steps:
Additional requirements:
1-Use a loop to generate the initial hint. done
2a-Add a check to verify that the length of the guess is the same as the length of the secret word. If it is not, display a message. done
2b-If they are the same, then proceed to give the hint. -stuck
Add the hints according to the rules above.
Make sure to account for the following in your hints:
Letters that are not present at all in the secret word (underscore _).
Letters that are present in the secret word, but in a different spot (lowercase).
Letters that are present in the secret word at that exact spot spot (uppercase).
Additionally, be sure to add a space after every character in the hint as in the examples above.
1- Pull the word (first use a set word and print to test)
2ish) Index the word 
3) Print the hint
4) to be deleted - print their word to test
5) loop look for matching letters
6) loop look for matching index
7) reprint hint (this would be a loop)
"""
"""for letter in guess:
for letter in secret_word: 
    if letter == :
        print("_", end="")
    else:
        print((letter), end="")    
print()
"""

"""
milestone requirements:
Have a secret word stored in the program.
Prompt the user for a guess.
Continue looping as long as that guess is not correct.
Calculate the number of guesses and display it at the end.
You do not need to have any hints at this point.



# important repeatable code
end game:
    print ("You guessed it!")
    print (f"It took you {count} guesses")
    again = input("Would you like to play again? yes/no    ").lower()
print ("Thank you for playing. Goodbye.")

list words:
color = ""
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(f"{color}") # no f and {} needed here. 
print()

# Looping through strings
letter = ""
favorite = ""
word = "commitment"
favorite = input("What is your favorite letter? ").lower()
# for letter in (word): no () in example
for letter in word: 
    if letter == favorite:
        print("_", end="")
    else:
        print((letter), end="")    
print()
"""
