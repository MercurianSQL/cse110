"""
Author : Marinda Keller
Purpose: W 04 Word Game, milestone and final
"""
# creativity[select a random word from a list of words]

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

"""for letter in guess:

for letter in secret_word: 
    if letter == :
        print("_", end="")
    else:
        print((letter), end="")    
print()"""




"""
milestone requirements:
Have a secret word stored in the program.
Prompt the user for a guess.
Continue looping as long as that guess is not correct.
Calculate the number of guesses and display it at the end.
You do not need to have any hints at this point.

Additional requirements:

Use a loop to generate the initial hint.
Add a check to verify that the length of the guess is the same as the length of the secret word. If it is not, display a message. If they are the same, then proceed to give the hint.
Add the hints according to the rules above.
Make sure to account for the following in your hints:
Letters that are not present at all in the secret word (underscore _).
Letters that are present in the secret word, but in a different spot (lowercase).
Letters that are present in the secret word at that exact spot spot (uppercase).
Additionally, be sure to add a space after every character in the hint as in the examples above.

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