"""
This is the script of the second Day of our python Course.
We worked on Inputs, mathematical operations like "+", "//" and so, as well as
tried our hands on some if statements and played around with logical operators
"and", "or" as well as "not"
"""
print("~" * 25)  # prints 25 ~symbols in a line
print("Using inputs")  # a small headline
print("")  # prints an empty line
# We want ot get the Name and age of the user, all inputs ar strings
# The \n means the entry is in the next line
FirstName = input("What is your first Name: \n")
LastName = input("What is your last Name: ")
# with the help of (in) we can change the type of the variable Age
# from string to int()
Age = int(input("How old are you: "))
# Now we print out the given inputs in one string
print("")
# printing a combination of all three variables
print(FirstName + " " + LastName + " is " + str(Age) + "-years old")
# printing the type of Age to see if casting was successful
print("Age has the type " + str(type(Age)))
# end of the input part

print("~" * 25)
print("Working with mathematical operations")
print("")
# We will define some variables at first
nr1 = 24
nr2 = 2
nr3 = 3
# You can use the mathematical operations on variables like this
sum = nr1 + nr2  # Adding up two numbers with "+"
print("The sum of " + str(nr1) + " and " + str(nr2) + " is " + str(sum))
subtrac = nr1 - nr2  # subtracting two numbers
print(str(nr1) + " minus " + str(nr2) + " equals " + str(subtrac))
# you can use all operations also with random numbers. For dividing it woould
# look like this for example
quotient = 27 / 3
print("27 divided by 3 equals " + str(quotient))
# multiplicate 4 by 5
print("4 multiplicated by 5 equals " + str(4 * 5))
# Using integer division // returns a variable of the type integers
# everything after the "." of the floating number is cut off
print("24 divided by 5 results in an integer value of " + str(24 // 5))
# With the help of power we can compute squres and roots
# for square we have to use **2 and for the square root we can use **0.5
# you can use this to calculate bigger roots by using things like **(1/4) for
# the fourth root for example.
print("3 to the power of 3 equals " + str(3 ** 3))
print("The square root of nine is " + str(9 ** 0.5))
print("The third root of 27 is " + str(27 ** (1 / 3)))
# Divide by 28 by 5 and print out the remainder ( called "Rest" in german)
print("28 divided by 5 leaves a remainder of " + str(28 % 5))

# We can always use shortcuts for mathematical operations
print("Variable nr1 has the value " + str(nr1))
nr1 += 5  # now we add 5 to our variable nr1 (has a value of 24)
print("Variable nr1 has the value " + str(nr1))
nr1 -= 8  # now we subtract 8 from variable nr1 (has currently a value of 29)
print("Variable nr1 has the value " + str(nr1))
# We can use these shortcuts for multiplication and division as well
print("Variable nr2 has the value " + str(nr2))
nr2 *= 5  # we multiplicate our variable nr2 (has a value of 2) by 5
print("Variable nr2 has the value " + str(nr2))
nr2 /= 2  # we divide our variable nr2 (has a value of 10) by 2
print("Variable nr2 has the value " + str(nr2))
print("~" * 25)

print("Results for Exercise 4")
print("")
# First we ask the user for an input
UserName = input("What is your Name? ")
if UserName == "Christoph Knorr":  # We check if the names match
    print("That is a nice Name")
# We check if maybe another nice Name was given
# This check wil only be done if the first one after the if was false
elif UserName == "John Cleese":
    print("I like Monty Python")
# We check if maybe another nice Name was given
# This check wil only be done if the first one after the if was false and
# the second one after the elif was also false
elif UserName == "":
    print("I like Monty Python as well")
else:  # if all three checks above were false we do this
    print("You have a nice Name")
print("")
print("~" * 25)

print("Results for Exercise 5")
# First we ask for two inputs again, but be carefule you have to change the
# type of the variable into a number first by using int()
Nr1 = int(input("Give me a number: "))
Nr2 = int(input("Give me a number: "))
# Now we calculate the sum of our inputs
sum = Nr1 + Nr2
# Next we check if our sum is bigger than 100
if sum > 100:
    print("This is a big number")
# Then we check if our is between 10 and 100, remember this check is only done
# if the first one was false
elif sum > 10:
    print("This is a mediocre number")
# Now comes the third check for numbers between 5 and 10
elif sum > 5:
    print("This is a small number")
# Last but not least comes the print out if the sum is smaller than 5
else:
    print("This is a very small number")
print("")
print("~" * 25)

print("Results of Exercise 6")
print("")
# First we want to get the four inputs from the User
# Remember that you have to change the type of the string input
Nr1 = int(input("Choose your first Number: "))
Nr2 = int(input("Choose your second Number: "))
Nr3 = int(input("Choose your third Number: "))
Nr4 = int(input("Choose your fourth Number: "))
# We check for the first condition input1=input2 and input3=input4
if Nr1 == Nr2 and Nr3 == Nr4:
    print("You fullfilled the first condition")
# We check for the second condition input1=input3 and input2=input4
elif Nr1 == Nr3 and Nr2 == Nr4:
    print("You fullfilled the second condition")
# We check for the third condition input1=input4 or input2=input3
elif Nr1 == Nr4 or Nr2 == Nr3:
    print("You fullfilled the third condition")
# if no conoditions were satisfied do this
else:
    print("You didn't fullfill any condition")
