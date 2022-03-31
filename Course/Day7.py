"""
This is the Python script of our seventh day of Python. We started the day
with talking about nested loops again. The results for the first two parts of
exercise 25 are in the script Day6.py since I wrote them yesterday. Afterwards
we discussed functions in Python.
"""
import random
# First we want ot finish Exercise 25. Do be able to do this we have to
# create two new random matrices, just like we did yesterday
testmatrix1 = [list(random.sample(range(10, 100),5)),
list(random.sample(range(10, 100),5)),
list(random.sample(range(10, 100),5))]
print("Our random matrix1 looks like this:\n",testmatrix1)
testmatrix2 = [list(random.sample(range(10, 100),5)),
list(random.sample(range(10, 100),5)),
list(random.sample(range(10, 100),5))]
print("Our random matrix2 looks like this:\n",testmatrix2)
print("")
# Next we have to set up a result matrix, which do down below. The matrix
# consists of three lists that contain only Zeros, just ot make sure the
# dimensions are correct
resultmatrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# Now we can initiate our nested loops just as we did beforehand, first over
# the outer list
for i in range(3):
    # second of the elements of the inner lists
    for j in range(5):
        # Now we can Multiply the elements
        resultmatrix[i][j] = testmatrix1[i][j] * testmatrix2[i][j]
#Now we print out our result
print("The resultmatrix looks like this:\n",resultmatrix)
print("")

# In the afternoon we began to work with functions. To illustrate this I will
# use the first function that is needed for exercise 28, so I won't define it
# again later.
# To illustrate the principle of global and local variables we will use the
# variable addition as an example. We declare it before the definition of our
# function as shown below:
addition = 8
print("addition before function:",addition)
# Now we define our function sumup, that calculates the addition of two
# integers. First we have to create the signature of the function with the help
# of the def statement. After the def statement you have the name of the
# function (sumup in our case) and the parameters (a and b in our case). The
# signature is closed with a :
def sumup(a,b):
    # Now we can add whatever code we want to run once the function is called
    # back later on. So first we add up our two parameters and store the result
    # in the local variable addition
    addition = a+b
    # Than we print out the local variable addition to illustrate the principle
    # of global and local variables.
    print("addition in function:",addition)
    # A function ends as soon as a return is encountered or the indented block
    # of source code ends. In our course we will use only functions that return
    # values, so you always have to include a return
    return addition
# To illustrate the principle of global and local variables we print out the
# global variable addition again
print("addtion after the function:",addition)
#Now we can call back our function and store the returned value in another
# global variable called CalcSum
CalcSum = sumup(6,7)
# Now we can print out hte result of our call back
print("Result of call back of sumup for 6 and 7:",CalcSum)

# For exercise 28 you have to define three additional functions as shown below
# The first one calculates the subtraction of one integer from another
def Subtraction(a,b):
    subtract = a-b
    return subtract
# The second one calculates the product of two variables
def Multiplication(a,b):
    product = a*b
    return product
# The third one calculates the division of two parameters
def Division(a,b):
    quotient = a/b
    return quotient
# Now we can call back our functions as follows
CalcSub = Subtraction(13,5)
CalcMulti = Multiplication(3,6)
CalcDiv = Division(105,6)
# Now we print out our results
print("Result of call back of Subtraction for 13 and 5:",CalcSub)
print("Result of call back of Multiplication for 3 and 6:",CalcMulti)
print("Result of call back of Division for 105 and 6:",CalcDiv)
print("")
# Of course you can use your functions multiple times. That is the main reason
# for creating them
CalcSum2 = sumup(5,8)
CalcSub2 = Subtraction(678689,126356)
# You can even use floats instead of integers and your functions still run
CalcMulti2 = Multiplication(8.5,6.3)
CalcDiv2 = Division(13,3)
print("Result of 2. call back of sumup for 5 and 8:",CalcSum2)
print("Result of 2. call back of Subtraction for 678689 and 126356:",CalcSub2)
print("Result of 2. call back of Multiplication for 8.5 and 6.3:",CalcMulti2)
print("Result of 2. call back of Division for 13 and 3:",CalcDiv2)
print("")

# Now we go on with exercise 29. Here you have to define two functions, that
# use source code you already wrote during our loop exercises.
# First we want a function that calculates the sum of a list, so we set up our
# signature as follows
def Sumlist(InputList):
    # Now we have to define our return value
    Result = 0
    # In the next step we have to iterate over the list that was handed over
    # Since we don't know the length of the list we have to use len()
    for i in range(len(InputList)):
        # Now we can sum up the elements
        Result += InputList[i]
    # Last but not least we return the calculated sum
    return Result
# The second function we want to define returns a reversed list from our handed
# over list. So we again set up the signature in a simple way
def Reverselist(InputList):
    # Now we have to define an empty list First
    ResultList = []
    # In the next step we iterate over the list that was handed over. We have
    # use len() again since we don't know the length of our parameter. With the
    # help of the reversed() command we generate a range that starts with the
    # biggest index and ends with oru smallest index (0)
    for i in reversed(range(len(InputList))):
        # Now we append the result list with the reversed values from our
        # parameter. Since we start witht he last index of our parameter and
        # end with the first one we can use a simple append like this
        ResultList.append(InputList[i])
    # Last but not least we have to return the reversed list
    return ResultList
# To call the functions above we have to generate a randomlist first, so that
# we have a parameter we can hand over to them
randomlist1 = list(random.sample(range(10, 100),random.randint(1,20)))
# Now we call back the Sumlist function with our randomlist1
SumRandom = Sumlist(randomlist1)
# And print out the result
print("The sum of our randomlist:",SumRandom)
# To call back the Reverselist function with our randomlist1 we use it in a
# similiar way
reverserandom1 = Reverselist(randomlist1)
# Now we print out the two lists
print("Our two lists look like this:")
print("Original:",randomlist1)
print("Reverse :",reverserandom1)
print("")

# Last but not least we talked about functions with nested loops inside of
# them. We saw this in form of exercise 30. First we have to generate our
# rnadom amtrix again.
testmatrix1 = [list(random.sample(range(10, 100),5)),
list(random.sample(range(10, 100),5)),
list(random.sample(range(10, 100),5))]
print("Our random matrix looks like this:\n",testmatrix1)
print("")
# Now we have to set up our first function to calculate the sum over all
# elements of the matrix
# So we set up our signature like below:
def SumMatrix(InputMatrix):
    # To sum up all value in this matrix we first have to create return value
    result = 0
    # Now we have to create our nested lists. The first list runs through our
    # outer list so the initiation looks like below. Remebrer to use len()
    for i in range(len(InputMatrix)):
        # Now we have to initiate our second loop, which runs through our inner
        # lists, so we have a different range that loops over all elements of
        # the inner list we are accessing currently
        for j in range(len(InputMatrix[i])):
            # Now we can add the element of the inner list to our sum
            # So you have to access the testmatrix with the help of the indices
            # the first index i represents one of the three lists and the
            # index j represents one of the entries in the corresponding inner
            # list
            result += InputMatrix[i][j]
    # Now we can return the sum
    return result
#Now we can call back our function as shown below
sumrandom2 = SumMatrix(testmatrix1)
print("The sum of our testmatrix is:",sumrandom2)
# Our second function should find the maximum value of a matrix
def MaxMatrix(InputMatrix):
    maxmatrix = 0
    # Now we can initiate our nested loops just as we did beforehand, first over
    # the outer list
    for i in range(len(InputMatrix)):
        # second of the elements of the inner lists
        for j in range(len(InputMatrix[i])):
            # Now we have to include an if-statement to see if the current entry
            # is bigger than the set maximum
            if InputMatrix[i][j] > maxmatrix:
                # Now we set our variable maxmatrix to the new found maximal value
                maxmatrix = InputMatrix[i][j]
    # After the loop is finished we can return the found maximum value
    return maxmatrix
# Now we can call back our function
maxrandom1 = MaxMatrix(testmatrix1)
# At last we print out our found result
print("The maximum of our testmatrix is:",maxrandom1)
