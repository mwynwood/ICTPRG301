# IF Examples
#
# The IF statements lets you make decisions
# To do this, it evaulates a condition to be True or False
#
# == is Equivalent To
# != is Not Equivalent  To
# >  is Greater Than
# <  is Less Than
# >= is Greater than or Equal To
# <= is Less Than or Equal To

a = 7
b = 42

if a == b:
    print("a is equivalent to b")

if a < b:
    print("a is less than b")

# You can optionally include an ELSE clause to run code if the CONDITION is False:
age = 17
if age >= 18:
    print("You can vote!")
else:
    print("You can't vote!")