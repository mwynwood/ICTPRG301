# HANGMAN
# This is a starting point for the Hangman game.
#
# Name: 
# Last Updated: 9 Nov 2019
#
# The source code file name should be "hangman-YOURNAME" with the appropriate extension
# The game explains the rules
# The current best score is read from a file called "hangman-score.txt" and printed to the screen. If this file does not exist, your program should set the best score to 0.
# The game randomly selects a secret word from an external dictionary file which has been read into an array or a list. The dictionary file will be provided to you. If the dictionary file cannot be accessed, your program must tell the user and then revert to a hard-coded set of five words.
# Players are allow 10 incorrect guesses before they are hanged"
# Players shown the secret word with guessed letters displayed, and others blanked out
# The player is given the opportunity to guess a letter
# Players are told how many incorrect guesses they have left before they are hanged
# If a player guesses right, a letter is revealed
# If a player guesses wrong, they lose a point
# The current state of the secret word is displayed
# If players runs out of guesses, they lose and the game ends
# If a player completes the secret word, they win and the game ends
# A players score is based on how many guesses they have remaining
# If the player beats the best score, their score is saved to a file called "hangman-score.txt", overwriting any previous score.
# Your code must adhere to the "PEP 8 -- Style Guide for Python Code". If you are using another language, consult with your teacher for the appropriate style guide.
# Your code must contain comments explaining clearly how your code works

print ("Hangman")

print("TODO: read file into a list, or use a preset list of words")
secret_word = "telecaster"
#print(secret_word)

print("TODO: read value form file, if the file is not there set an initial score")
best_score = 0
print("The score to beat is: ", best_score)

# Declare and initialise game variables
guess = ''
guesses = ''
turns = 7

# Play the game while you still have turns left
while turns > 0:
    # Print out the secret word, with some letters hidden
    blanks = 0 
    for letter in secret_word:
        if letter in guesses:
            print("?", end='')
        else:
            print("?", end='')
            blanks = blanks + 1
    print("")

    # If there are no more blanks, you win!
    if blanks == 0:
        print ("You won!")
        print("TODO: If they beat the Best Score, Write their score to the file")
    # If there are still blanks, ask the user to guess a letter
    else:
        guess = input("Guess: ")
        guesses = guesses + guess # add new guess to guessed letters

        # If the guess is not in the secret word, lose a life!
        if guess not in secret_word:
            turns = turns - 1
            print("TODO: what happens when they get it wrong?")
            if turns == 0:
                print ("You Loose")