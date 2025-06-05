"""
Author : Marinda Keller
Purpose: W 04 Word Game, milestone and final
"""
# creativity[select a random word from a list of words]

print ("Welcome to the Word Game!")
print()

# variables
secret_word = ""
secret_word = "shelf"
guess = ""
count = 0
index = 0
sw_len = -1
guess_len = -1
sw_len = int(len(secret_word))

# start outer loop
while guess != secret_word:
    if count == 0:
        print("Your hint is: ")
    else:
        print ()
        print ("try again again")
    
# for i in secret_word: # HINT
    for index, letter in enumerate(secret_word):
        #print(f"The letter {letter} is at index {i}")
        print("_ ", end="")
    print()
    #print ("**PASSED 2&4**")
    guess = input("What is your guess? ").lower()
    count = count + 1
    guess_len = int(len(guess))
    #print (guess_len)
    if guess_len != sw_len:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        #print ("**PASSED 3**")
    else:
        #print ("**PASSED 5**")
        print("Your hint is: ", end="")
        for index, letter in enumerate(guess):
            #if letter[index] == letter[]:
                #print(letter.upper(), end=" ")
            if letter in secret_word:
                print(letter.lower(), end=" ")
            else:
                print("_", end=" ")
if guess == secret_word:
    print(f"You guessed it in {count}!")
else:
    print ("Something went wrong.")


"""for letter in guess:

for letter in secret_word: 
    if letter == :
        print("_", end="")
    else:
        print((letter), end="")    
print()"""




"""

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