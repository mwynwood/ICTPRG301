# List Examples

# Make an empty list
my_list = []

# Make a list of integers
my_list = [42, 105, 234, 142, 49, 25, 69]

# Print the list
print(my_list)

# Sort the list
my_list.sort()

# Add an item to the list
my_list.append("We are the Borg")

# Add multiple items in one go
my_list.extend(["Resistance", "is", "futile"])

# Print the list
print(my_list)

# Count the length of a list
print("List Length:", len(my_list))

# Print the item at position 1
print(my_list[1])

# Change the item in position 0
my_list[0] = 42

# Print the list
print(my_list)

# Remove the item in position 2
my_list.pop(2)

# Print the list
print(my_list)

# Remove an item by value
my_list.remove(42)

# Print the list
print(my_list)
