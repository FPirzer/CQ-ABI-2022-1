"""
This is the script for the first Day of our Python course.
We declare some variables adjust them and change their types.
Furthermore we run a simple example for if-statements
"""
# Declaring some simple variables by using "="
Name = "Christoph"  # The Name of the programmer
Age = 34  # The age of the programmer
Income = 1.524  # The income of the programmer

# print out the variables as test
# print can take any kind of variable as argument.
print(Age)  # prints just out a "34"
# We can combine several strings by using a simple "+"
print("Name is " + Name)  # prints out the String "Name is Christoph"
# We need the str(Age) to change the type of integer Variable Age into a
# String variable to print it out like this because we can't use the "+"
# on these variables because they have different types
print("Age is " + str(Age))
# as with integers we need the str(Income) in this case for floats as well
print("Income is " + str(Income))

# Some test operations to declare new variables by using
# old variables as starting point
NewAge = Age + 2  # The variable NewAge contains the value 36
FullName = Name + " Knorr"  # The variable FullName contains "Christoph Knorr"
print("NewAge is " + str(NewAge))
print(FullName)

# Adjust value of a specific variables
# This can be daone by using operations like "+=" for Addition
# or "-=" for Subtraction
# Holds also true for Multiplication using "*=" and Division using "/="
Age += 1  # Adding 1 to Age so Age contains the value 35
print("Age is " + str(Age))
print("Age is " + str(Age + 1))
Name += " Knorr"  # Elongating the String with " Knorr"
print("Name is " + Name)

# We can change the type of a int by using division
print(type(Age))
Age /= 2  # Divide Age by 2
print(Age)
# we have to use str() here as well since the output of type()
# is not a string
print("Age has the type " + str(type(Age)) + " after division")

# We want to convert a string into an integer
Agestring = "35"
print(type(Agestring))
# The command int() converts the string to an integer value
Agestring = int(Agestring)
print(type(Agestring))

# Simple Example for if-statements
if NewAge == 37:  # check if the variable NewAge contains the value 37
    print("You're 37")
    print(NewAge)
elif Age < 35:  # check if the variable Age contains a value smaller than 35
    print("Your're younger than 35")
else:  # if both checks were false beforehand we do something else
    print("You're between 34 and 37 or older than 37")
