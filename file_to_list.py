# Read each line from a file into an item in a list.
# If the file can't be read, use a pre-set list.
#
# The splitlines() function does all the work, automatically
# creating a list form the contents of the file with items
# distinguished by line breaks.

try:
    with open("myfile.txt","r") as f:
        my_list = f.read().splitlines()
        f.close()
except:
    print("Error reading file. Populating list with other things")
    my_list = ["apple", "banana", "pear", "orange", "grape"]
