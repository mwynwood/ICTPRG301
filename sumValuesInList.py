# This code adds up all the numbers in a list

numbers = [42, 105, 234, 142, 49, 25, 69]
total = 0

# Iterate through each value of our list
for number in numbers:
	total = total + number

print("The total is", total)

# Here is another way to iterate through our list.
# This way uses the RANGE() and LEN() functions to 
# go through the list with "i" representing the 
# position of the value in the list.
for i in range(len(numbers)):
	print("Position: ", i, " Value: ", numbers[i])