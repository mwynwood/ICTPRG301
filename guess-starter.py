# Guess the Number
# This is a starting point for the Guess the Number game.
#
# Name: 
# Last Updated: 21/9/2019 
#
# The source code file name should be "guess-YOURNAME" with the appropriate extension
# The game explains the rules
# The game randomly selects a secret number (an integer), between 1 and 100 inclusive (you may need to import a library to use the random method)
# Players have 7 guesses to pick the number
# The player has the opportunity to enter their guess in the form in an integer
# Players are told after each guess whether their guess is too low, too high,, or correct, and how many guesses they have left
# If players gets their guess right, they get a special winning message, and the game ends
# If players runs out of guesses, then the game ends
# Your code must adhere to the "PEP 8 -- Style Guide for Python Code". If you are using another language, consult with your teacher for the appropriate style guide.
# Your code must contain comments explaining clearly how your code works

secret = 42 #random?
guess = 0
guess_count = 0
guess_total = 7

print("GUESS THE NUMBER")
print("Guess the number between 1 and 100.")

while True:
    print("")
    print("Guesses remaining: ")
    guess = int(input('Your guess: '))
    guess_count = guess_count + 1
    
    print("Too high")
    
    print("Too low")
    
    print("You win! You got it in " + str(guess_count) + " guesses!")