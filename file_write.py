# Write to a File
#
# This example opens a file for writing, writes the value of 
# the variable "value" as a String, and then closes the file.
# If the file can not be found, the file will be created.
# If the file can not be written to, if will display an error.
#
# The code lives inside a TRY-EXCEPT block which
# allows us to deal with any errors, and carry on.

value = 42
try:
    f = open("myfile.txt", "w")
    f.write(str(value))
    f.close()
    print("File written to successfully.")
except:
    print("Error writing to the file.")