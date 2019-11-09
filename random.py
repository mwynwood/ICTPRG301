# Computers can not create truly random numbers.
# Instead, they create pseudorandom numbers by using a complex 
# alrogithm to produce a series of numbers that appear to be random.
# For most cases pseudorandom numbers are adequate.

# Import the random number library
# Python uses a pseudorandom number generator called the "Mersenne Twister".
import random

# Generates a random floating point number between 0-1
value = random.random()
print(value)

# Roll the Dice!
# Generates a random integer between 1-6
dice = random.randint(1,6)
print(dice)

# Picking a random value form a list using "choice"
my_list = ["apple", "banana", "pear", "orange", "grape"]
l = random.choice(my_list)
print(l)
# Or you can do it yourself by generating a random number
# between 0 and the length of the list minus 1, and then
# use that as an index:
rand = random.randint(0,len(my_list)-1)
print(my_list[rand])

# The pseudorandom number generator needs a "seed" as a 
# starting point for it to generate random numbers.
# If you don't specify a seed value, Python uses the 
# system time in milliseconds. If you specify a seed 
# value, the same sequence of pseudorandom numbers
# will be generated each time. Try it out by running this 
# code a few times, the same seed value should always 
# generate the same random number.
random.seed(1)
r = random.randint(1,100)
print(r)