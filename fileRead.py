# Read a line form a File
#
# This example opens a file, reads the first line,
# and stores it as an INT in a variable called "value",
# and then closes the file.
# If the file can not be found, it sets "value" to 0
#
# The code lives inside a TRY-EXCEPT block which
# allows us to deal with any errors, and carry on.

try:
    with open("myfile.txt", "r") as f:
        value = int(f.readline())
        f.close()
except:
    print("Error reading file! Setting value to 0")
    value = 0
    
print("The value form the file is: " + str(value))