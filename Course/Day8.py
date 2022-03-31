"""
This is the Python script of our eighth day of Python. We started the day
with talking about functions again, including funtions that return multiple
values to the main program. Afterwards we used the keywords break, continue
and pass. Last but not least we talked about importing other modules to python.
We talked about os and math.
"""
import random, os

os.system("clear")
# First we want ot finish Exercise 25. Do be able to do this we have to
# create two new random matrices, just like we did yesterday
testmatrix1 = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
print("Our random matrix1 looks like this:\n", testmatrix1)
testmatrix2 = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
print("Our random matrix2 looks like this:\n", testmatrix2)
print("")

# Now we can set up our function. First we generate the signature
def MatrixMulti(InputMatrix1, InputMatrix2):
    # Next we have to set up a result matrix, which do down below.
    resultmatrix = []
    # Now we can initiate our nested loops just as we did beforehand, first
    # over the outer list
    for i in range(len(InputMatrix1)):
        # First we append an empty list to our result matrix
        resultmatrix.append([])
        # second of the elements of the inner lists
        for j in range(len(InputMatrix1[i])):
            # Now we can Multiply the elements
            product = testmatrix1[i][j] * testmatrix2[i][j]
            # now we append the result to our result matrix
            resultmatrix[i].append(product)
    # Now we return the result
    return resultmatrix


# Now we can call back our functionj with the help of our test matrices
MultiMatrix = MatrixMulti(testmatrix1, testmatrix2)
# Now we print out our result
print("The resultmatrix looks like this:\n", MultiMatrix)
print("")

# Now we are working with functions that return multiple values to the main
# program. We start with a simple example that calculates an addition and a
# subtraction of two values. We create our signature in the simple way shown
# below:
def sum_sub(Int1, Int2):
    # Now we include our two calculations
    sumup = Int1 + Int2
    subup = Int1 - Int2
    # Now we can return our tow results, but keep in mind that the order you
    # hand over your results to the main program is defined by the order in
    # your return command. On call back later on you can't change this order
    return sumup, subup


# Now we can call back our function with the help of two new variables
SumEx, SubEx = sum_sub(15, 25)
print("The results of our Example function are:")
print("Addition of 15 and 25:", SumEx)
print("Subtraction of 15 and 25:", SubEx)
print("")

# Now for Exercise 31 we have to create another function like this
def Operations(Int1, Int2):
    # Now we include our four calculations
    sumup = Int1 + Int2
    subup = Int1 - Int2
    multup = Int1 * Int2
    divup = Int1 / Int2
    # Now we can return our four results to the main program
    return sumup, subup, multup, divup


# Now we call back our function like this
SumEx, SubEx, MultEx, DivEx = Operations(12, 21.3)
print("The results of our Example function are:")
print("Addition of 12 and 21.3:", SumEx)
print("Subtraction of 12 and 21.3:", SubEx)
print("Multiplication of 12 and 21.3:", MultEx)
print("Division of 12 and 21.3:", DivEx)
print("")

# Now we want to tackle exercise 32. We have to define our function like This
def listoperations(Inputlist):
    # First we define our return values, an empty list and a sum that is
    # currently 0
    resultlist = []
    sumup = 0
    # Now we create our loop, we have to use len() since we don't know the size
    # of our input and with reversed we can access the elements in our input
    # from the back to the front
    for i in reversed(range(len(Inputlist))):
        # First we add up the elements
        sumup += Inputlist[i]
        # Now append our empty reutrn list with the elements of our input
        resultlist.append(Inputlist[i])
    # Last but not least we return our two values
    return resultlist, sumup


# For the call back we first create a random list
randomlist1 = list(random.sample(range(10, 100), random.randint(5, 26)))
print("Our randomlist1 looks like this:\n", randomlist1)
# Now we call back our function with two new variables
reverselist1, sum1 = listoperations(randomlist1)
# Now we can print out our results to check them
print("Our reverselist1 looks like this:\n", reverselist1)
print("The sum of our randomlist1 equals ", sum1)
print("")

# Now we want to work with the keywords pass, break and continue. These can be
# used to adjust how a loop iterates. We will do that by using Exercise 64 as
# an example. First we generate a randomlist again
randomlist2 = list(random.sample(range(35, 76), random.randint(5, 26)))
print("Our randomlist2 looks like this:\n", randomlist2)
# Than we define our variable that contains the sum over the list
sum2 = 0
# Now we construct our loop
for i in range(len(randomlist2)):
    # Now we add up our elements
    sum2 += randomlist2[i]
    # Now we add our if statement that can't be True
    if sum2 < 0:
        # Now we add a pass so that we don't run into any errors
        pass
    # Now we add an if statement that breaks the loop if our sum is too big
    if sum2 > 250:
        break
    # Last but not least we add an if statement that uses continue to skip over
    # some print commands
    if 45 < randomlist2[i] < 65:
        continue
    # These print outs can only take place if the loop is still running, that
    # means the sum is smaller than 250 at this point, and if the current entry
    # in our list is smaller than 45 or bigger than 65
    print("We are at iteration", i)
    print("The entry in the list at index", i, "is", randomlist2[i])

print("Our list has", len(randomlist2), "entries")
print("We ran", i, "iterations to calculate a sum")
print("The resulting sum is", sum2)

# Now we talk about using modules to be able to use a greater functionality
# in Python. we will start with the example calendar from the presentation
# To import a whole module you can simply use the import command, as we already
# saw for random
import calendar

# Now you can access all methods of calendar by using calendar.method(). In the
# example below we want to use the prcal() function of the module calendar
Year1 = calendar.prcal(2022)
print(Year1)

# If we want to use only specific functions or methods of a module we can
# import only parts of the module. In the example below we import only the
# method prcal() from the module calendar()
from calendar import prcal

# Now we can use the function prcal() in a simpler way than before, but keep
# in mind that different modules can have methods with the same name, that
# produce different results. So sometimes it is better to import the whole
# module instead of only using one function
Year2 = prcal(2020)
print(Year2)

# After we tackled the basics, we can now go on with exercise 33. We need the
# module random, which we already used multiple times. The import is already
# done at the beginning of this script (line 8), so we don't have to repeat
# this here. The method we need for generating a random number is randint().
# This method takes two arguments, the start and the end of a range in which the
# random number should lie. As always the end number is excluded from the range,
# so for a number between 0 and 99 we need the following declaration:
randomnumber = random.randint(0, 100)
# Now we daclare a Boolean variable found that is false to use for our while
# loop
found = False
# Next we define our variable to count the needed iterations
count = 0
# After all needed variables are defined, we can now initiate our loop
while found == False:
    # First we get the input from the user
    Guess = int(input("Take a guess: "))
    # Second we add up our count
    count += 1
    # Third we combine our Guess with the random number with the help of if
    # and elif. First we check if the guess is bigger than the random number
    if Guess > randomnumber:
        print("Your guess was too big")
    # Our second check is too see if the guess was too small
    elif Guess < randomnumber:
        print("Your guess was too small")
    # The third check is true if the user guessed right
    elif Guess == randomnumber:
        # First we print out a congratulation
        print("You are right")
        # Now we print out the amount of guesses the user needed
        print("You needed", count, "guesses.")
        # Last but not least we set our boolean variable to true, so that we
        # can exit the loop. You could use break instead.
        found = True
    # I created a simple break out of the loop after 50 iterations, so that the
    # user can't let the program run forever
    if count == 50:
        print("You were too slow")
        break

# Now we want to work with the module os. I alredy imported it at the beginning
# of the script in line 8
# With os.system() you can hand over commands directly to your commandline. In
# the example below you list the contents of the current directory
os.system("ls")
print("")
# With the help of os.mkdir() you can create directories, but only if the don't
# already exist
os.mkdir("Test_os2")
# If you want to create child directories you can use os.makedirs() with a path
# All directories in the path are created along the way. With the help of the
# exist_ok=True parameter you can even create the directories even if they
# already exist.
os.makedirs("Test_os/Hello/World", exist_ok=True)
# os.chdir() allows you to change your current working directory analogous to cd
os.chdir("Test_os")
# With the help of os.getcwd() you can access your current working directory,
# bu tkeep in mind that this only works with the brackets at the end
print(os.getcwd())
# Ypu can use os.system() like shown below to create Files with the help of
# touch or other commands
os.system("touch Hello.txt")
os.system("ls")

# Now I want to show you how you could do exercise 34
# First you create your parent directory
os.mkdir("Exercise34")
# Than you change into this new directory
os.chdir("Exercise34")
# Now you can create the child directories. To simplify this task you can use
# a list of strings and loop over them
Dirs = ["Dir1", "Dir2", "Dir3", "Dir4", "Dir5"]
# You could now use a loop to handle the rest of the exercise as follows:
# first you loop over your list
for Dir in Dirs:
    # now we create our directories
    os.mkdir(Dir)
    # than we go into our directories
    os.chdir(Dir)
    # Now we create our Files. We can put together strings with a simple +
    os.system("touch " + Dir + ".txt")
    # last but not least we have to move one directory up again
    os.chdir("..")

# In the last part of the day we work with math. To show you how math works
# I will use the exercise 35. First you have to import the module
import math

# Now we get our two inputs from the user. I use floats so that the user can
# put in any kind of number
input1 = float(input("You're first number: "))
input2 = float(input("You're second number: "))
# Now we can use the different function sof math to calculate different
# things. To make it easier to understand I will always use a variable called
# out1, out2 and so on for each math function we have to call
# First we calculate the value of e^input1
out1 = math.exp(input1)
print("The result for math.exp of input1 is:", out1)
# Now we calculate the logartihm of input1 to the base e
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
if -1 < input1 < 1:
    out11 = math.acos(input1)
    out12 = math.asin(input1)
    out13 = math.atan(input1)
    print("The result for math.acos of input1 is:", out11)
    print("The result for math.asin of input1 is:", out12)
    print("The result for math.atan of input1 is:", out13)
