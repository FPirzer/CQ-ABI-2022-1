"""
This is the Python script of our ninth day of Python. We continued with talking
about modules. We started with math and random.
"""
import random, os, math

os.system("clear")
# In the first part of the day we work with math. Here I show you the results
# for exercise 36. First we get our two inputs from the user.
# I use floats so that the user can put in any kind of number.
input1 = float(input("You're first number: "))
input2 = float(input("You're second number: "))
# Than we have to generate a User choice to get our constant
Const = input("Do you want to use Pi, Euler number or tau?: ")
# Now we print out the inputs
print("")
print("Input1 before adjustement:", input1)
print("Input2 before adjustement:", input2)
print("")
# Now we have to multiply our inputs with the constant depending on the user
# choice. First if he chooses Pi
if Const == "Pi":
    # We can use *= to simply multiply the current value with Pi and set so
    # a nwe value for ourt input variable
    print("Your chosen constant:", math.pi)
    input1 *= math.pi
    input2 *= math.pi
    print("For the following results the input numbers were multiplied by Pi")
# Second if he chooses euler number
elif Const == "Euler":
    # We can use *= to simply multiply the current value with e and set so
    # a nwe value for ourt input variable
    print("Your chosen constant:", math.e)
    input1 *= math.e
    input2 *= math.e
    print("For the following results the input numbers were multiplied by Euler number")
# Third if he chooses Tau
elif Const == "Tau":
    # We can use *= to simply multiply the current value with Tau and set so
    # a nwe value for ourt input variable
    print("Your chosen constant:", math.tau)
    input1 *= math.tau
    input2 *= math.tau
    print("For the following results the input numbers were multiplied by Tau")
# Last but not least, if the choice wasn't a known constant
else:
    print("You didn't choose an availabl constant.")
    print("We will use the original inputs")
# Now we print out the inputs after the adjustment
print("")
print("Input1 after adjustement:", input1)
print("Input2 after adjustement:", input2)
print("")
# Now we can use the different function sof math to calculate different
# things. To make it easier to understand I will always use a variable called
# out1, out2 and so on for each math function we have to call
# First we calculate the value of e^input1
out1 = math.exp(input1)
print("The result for math.exp of input1 is:", out1)
# Now we calculate the logartihm of input1 to the base e
# for all logarithmic functions the input can't be zero, so we have to create an
# if statement here. Remember != means not equal
if input1 != 0 and input2 != 0:
    out2 = math.log(input1)
    print("The result for math.log of input1 is:", out2)
    # Now we calculate the logarithm of input1 to the base of input2
    out3 = math.log(input1, input2)
    print("The result for math.log of input1 to the base of input2 is:", out3)
    # Now we calculate the logartihm of input1 to the base 2
    out4 = math.log2(input1)
    print("The result for math.log2 of input1 is:", out4)
    # Now we calculate the logartihm of input1 to the base 10
    out5 = math.log10(input1)
    print("The result for math.log10 of input1 is:", out5)
# Now we calculate input1 to the power of input2 (input1^înput2)
out6 = math.pow(input1, input2)
print("The result of math.pow of input1 to the power of input2:", out6)
# now we calculate the square root of input1
out7 = math.sqrt(input1)
print("The result for math.sqrt of input1 is:", out7)
# Now we calculate the trigonometric functions
out8 = math.cos(input1)
out9 = math.sin(input1)
out10 = math.tan(input1)
print("The result for math.cos of input1 is:", out8)
print("The result for math.sin of input1 is:", out9)
print("The result for math.tan of input1 is:", out10)
# for the arcus trigonometric functions you need values that are between -1 and
# 1, so I included a simple if statement to stop anything bad from happening
if -1 <= input1 <= 1:
    out11 = math.acos(input1)
    out12 = math.asin(input1)
    out13 = math.atan(input1)
    print("The result for math.acos of input1 is:", out11)
    print("The result for math.asin of input1 is:", out12)
    print("The result for math.atan of input1 is:", out13)
print("")

# Now we work on exercise 37 to learn more about random.
# Before the real program starts we can define an empty list, that we can
# use to collect our random numbers
RandList = []
# First we have to generate six inputs to be able to get our random integers
Int1 = int(input("Starting point of your first range: "))
Int2 = int(input("End point of your first range: "))
Int3 = int(input("Starting point of your second range: "))
Int4 = int(input("End point of your second range: "))
Int5 = int(input("Starting point of your third range: "))
Int6 = int(input("End point of your third range: "))
# Now we generate our random numbers, we have to add one to the end point to
# include the given number
RandNr1 = random.randint(Int1, Int2 + 1)
RandNr2 = random.randint(Int3, Int4 + 1)
RandNr3 = random.randint(Int5, Int6 + 1)
# Now we put our random integers in our big list. We can do this by using extend
# and a Pseudo list in the brackets
RandList.extend([RandNr1, RandNr2, RandNr3])
# Now we print out the results
print("Our random integers are:")
print("For the range of", Int1, "up to", Int2, "the random int is:", RandNr1)
print("For the range of", Int3, "up to", Int4, "the random int is:", RandNr2)
print("For the range of", Int5, "up to", Int6, "the random int is:", RandNr3)
print("")
# Now we want to know how many random floats the user wants to generate
Int7 = int(input("How many random floats do you want to create? "))
# Now we can create a loop to generate our random numbers
for i in range(Int7):
    # First we generate our random number
    RandNr4 = random.random()
    # Than we print out our random number
    print("The random float at iteration", i + 1, "is", RandNr4)
    # Last but not least we put our random float into our list
    RandList.append(RandNr4)
print("")
# Now we want our to generate two normal distribution values with the help
# of user inputs. This time we use floats instead of integers
Float1 = float(input("Your first mu for normal distributions: "))
Float2 = float(input("Your first tau for normal distributions: "))
Float3 = float(input("Your second mu for normal distributions: "))
Float4 = float(input("Your second tau for normal distributions: "))
print("")
# Now we can generate our random numbers with random.gauss()
RandNr5 = random.gauss(Float1, Float2)
RandNr6 = random.gauss(Float3, Float4)
# Now we print out our results
print(
    "The first normal distribution for mu=", Float1, "and tau=", Float2, "is", RandNr5
)
print(
    "The second normal distribution for mu=", Float3, "and tau=", Float4, "is", RandNr6
)
# Now we put our random numbers in the list again
RandList.extend([RandNr5, RandNr6])
# Now we want ot see what happens if we switch mu and tau
RandNr7 = random.gauss(Float2, Float1)
RandNr8 = random.gauss(Float4, Float3)
# Now we print out our results
print(
    "The first normal distribution for mu=", Float2, "and tau=", Float1, "is", RandNr7
)
print(
    "The second normal distribution for mu=", Float2, "and tau=", Float3, "is", RandNr8
)
print("")
# Now we put our random numbers in the list again
RandList.extend([RandNr7, RandNr8])
# Now we can print out the list of our random numbers
print("The list containing all random numbers looks like this:\n", RandList)
print("")
# Now we shuffle our list and print it out again
random.shuffle(RandList)
print("The list containing all rondom numbers looks like this after shuffle:")
print(RandList)
# If you want to round your numbers you can use the method round(). It takes
# two parameters, first the number you want ot round and second the number of
# numbers after the point you want to round to. I show it to you with an
# simple example of our normal distribution values
print("RandNr5 rounded to only two decimal places:", round(RandNr5, 2))

# In our second lesson on this day we talked about NumPy or numerical python.
# This module allows the user to use many different mathematical operations for
# working with arrays and matrices. At the center of this module is the numpy
# ndarray that can be created in several different ways. To work with NumPy
# you should use an import as shown below, since it follows international
# conventions for using an alias
import numpy as np

# After we imported NumPy we can generate our Arrays. The first method is to
# cast a list to an arrayy with the np.array() method
Array1 = np.array([5, 6, 8, 1, 5])
# The second and third option is to create arrays that contain only 0 (zeros)
# or only 1 (ones). Any ohter methods aren't supported. We can hand over
# multiple dimensions to these two methods and we have to use the same number of
# brackets as the matrix dimensions should be. The order of these dimensions is
# from the back to the front: columns, rows, matrices
Array2 = np.ones(5)
Array3 = np.zeros((3, 6))
Array4 = np.ones(((5, 6, 7)))
# We can now print our four arrays
print("Our Arrays look like this:")
print(Array1)
print(Array2)
print(Array3)
print(Array4)
# Numpy also has a function np.arange() that creates an array in a similar
# fashion to the already known range() generator
Array5 = np.arange(15)
print(Array5)
# We can also reshape our arrays witht he reshape() method, but keep in mind
# that the dimensions you hand over to reshape have to match the number of
# entries in your Array
Array5 = Array5.reshape(3, 5)
print(Array5)
# Last but not least we can generate random entries for our arrays. The values
# are from a "standard normal" distribution
Array6 = np.random.randn(4, 6)
print(Array6)
print("")
# NumPy furthermore gives access to manx simple functions that can be used on
# its arrays. The most notable are sum(), max() and min() that calculate the
# sum, maximum value and minimum value of your array. In stark contrast to the
# normal sum, max and min methods these work on multi-dimensional arrays as
# good as on one-dimensional ones, wereas the standard methods only work on
# one-dimensional ones.
Sum1 = Array1.sum()
Max1 = Array1.max()
Min1 = Array1.min()
Sum2 = Array6.sum()
Max2 = Array6.max()
Min2 = Array6.min()
print("Sum of Array1", Sum1)
print("Maximum of Array1", Max1)
print("Minimum of Array1", Min1)
print("Sum of Array6", Sum2)
print("Maximum of Array6", Max2)
print("Minimum of Array6", Min2)
print("")
# We can use the shape method to get the shape method to look up the dimensions
# of our arrays
print("Dimensions of Array1:", Array1.shape)
print("Dimensions of Array4:", Array4.shape)
print("")
# A last function I want to present ot you is the transpose() method, that
# switches lines and columns in your Arrays.
Array7 = Array6.transpose()
print("The transposed Array6 looks like this:")
print(Array7)
# You can access specific values of your arrays with the help of indices just
# like you could with lists. The order is again from the back to the front:
# columns, rows, matrices ...
# Keep in mind that the indexing in python starts at 0
print("Value in row 2 and column 5 of Array6:", Array6[1][4])

# In the afternoon we started working with pandas. To use pandas we need to
# import the module again. Similar to numpy there is an international standard
# for importing pandas with an alias called pd
import pandas as pd

# In the center of pandas stands its data structure called DataFrame which can
# be generated as seen below. The DataFrame shown here can also be used for
# exercise 39
dataframe1 = pd.DataFrame(
    np.random.randn(4, 6),
    index=["Test1", "Test2", "Test3", "Test4"],
    columns=list("ABCDEF"),
)
print("our DataFrame looks like this:")
print(dataframe1)
print("")
# To access specific values in a DataFrame you can use either loc or iloc. The
# loc mehtod allows you to access your values with the help of your index and
# column names. The index or row name comes always first and than comes your
# column name
print("The entry in row Test1 at column C is:", dataframe1.loc["Test1", "C"])
# If you use iloc you have to use two separate square brackets. You can use
# this method to access your values via Index and columns numbers. Again the
# row comes first and than the column. Remember that indexing starts at 0. If
# you use integer values as index or column names pandas can be confused, so
# use strings only
print("The entry in row 0 at column 1 is:", dataframe1.iloc[0][1])
print("")
# You can add new rows (or columns) to your dataframe, by simply assigning
# values to entries that aren't part of the DataFrame yet. In the example
# below we add a fifth row called "Test5" and put the value of 2.46 in column
# "B" of this row. All other entries of the newly added row are empty
dataframe1.loc["Test5", "B"] = 2.46
print("Our DataFrame after adding a row looks like this")
print(dataframe1)
print("")
# Pandas offers a variety of different functions to work with its DataFrames.
# We will talk only about sum, index, columns and sort_values here.
# First we have df.sum(), which calculates the sum of each columns of the
# DataFrame it's used on
print("The Sums of the Columns are:\n", dataframe1.sum())
print("")
# By handing over the parameter axis=1 we can change the behavior of sum, so
# that now the sum is calculated over the rows instead of the columns. This is
# true for many pandas methods. The default behavior is always to work on
# columns instead of rows.
print("The Sums of the Rows are:\n", dataframe1.sum(axis=1))
print("")
# You can use the methods df.index and df.columns to generate iterable objects
# that contain the index and column names respectively. So that you could use
# them in a loop for example to iterate over all your columns
print("Our indices look like this:", dataframe1.index)
print("Our column names look like this:", dataframe1.columns)
print("")
# You can also sort your DataFrame with the df.sort_values() method. You have
# to hand over the name of the column for which you wnat to sort your values.
# These operations can be done in place so if you don't want to change your
# DataFrame hand over the sorted DataFrame to a new object as shown below.
dataframe2 = dataframe1.sort_values("A")
print("Our DataFrame sorted according to column A looks like this:")
print(dataframe2)
print("")
# Last but not least you have a describe function that calculates means,
# standard deviations, maxima, minima and percentiles for your columns
print("The description for dataframe1 looks like this:")
print(dataframe1.describe())
