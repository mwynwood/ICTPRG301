# Ask the user a question and store the response as a string
name = input("What is your name? ")
print("Hello", name)

# Ask the user a question and store the response as a string.
# Convert the response to a integer and print it.
age = input("What is your age? ")
age = int(age)
print("You are", age, "years old")
# What happens if we try and convert a letter to a integer?

# To avoid this, we can use a try-except block to deal 
# with the error rather than crashing the whole program.
# Surround the code that could produce an error in the try block,
# and if it does produce an error, deal with it in the except block.
# This code will display the error message and set the age to 0.
age = input("What is your age? ")
try:
    age = int(age)
except Exception as e:
    print(e)
    age = 0
print("You are", age, "years old")