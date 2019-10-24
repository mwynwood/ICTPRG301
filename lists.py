# List Examples

# Make an empty list
myList = []

# Make a list of integers
myList = [42, 105, 234, 142, 49, 25, 69]

# Print the list
print(myList)

# Sort the list
myList.sort()

# Add an item to the list
myList.append("We are the Borg")

# Add multiple items in one go
myList.extend(["Resistance", "is", "futile"])

# Print the list
print(myList)

# Count the length of a list
print("List Length:", len(myList))

# Print the item at position 1
print(myList[1])

# Change the item in position 0
myList[0] = 42

# Print the list
print(myList)

# Remove the item in position 2
myList.pop(2)

# Print the list
print(myList)

# Remove an item by value
myList.remove(42)

# Print the list
print(myList)
