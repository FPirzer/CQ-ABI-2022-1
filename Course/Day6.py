"""
This is the Python script I wrote during our sixthday of Python.
We worked only on loops today. We started out with simple for loops, before
working with loops over iterables like lists, sets, tuples or dictionaries in
our second lesson of the day. In the afternoon we talked about while loops and
last but not least we tried our hands on nested loops in the last part. I
included the solutions for all exercises in this script for your documents, so
that you can try to repeat things if needed.
"""
# We need this import command, so that python can access the methods that are
# associated with the module random. We will talk about using modules later,
# since there is a wide variety of them. So for now just use the import command
# as shown below.
import random
# In our first small example we just want to calculate the Faculty for numbers
# from 1 up to 10
#We have to define our result variable at first
faculty = 1
# Now we initiate the loop. In the example below i will run through the numbers
# 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10
for i in range(1,11):
    # Each of the commands below is now done for each iteration of the loop
    # as soon as we have code that isn't indented any more, it would not be
    # seen as part the loop any more
    print("The running index i =",i)
    # Here we calculate the multiplication
    faculty = faculty * i
    print("The Faculty equals ",faculty)

# In our second example we want to work only with the even numbers 2, 4, 6 and
# so on until we reach 22
for i in range(0,23,2):
    # For this example we are doing just a small printout
    print("Hello " + str(i))
print("") # This isn't part of the loop any more

# Now for Exercise 23 we have three different loops. I show the results here
# with just the basic needed number of iterations
print("Results for Exercise 23")
# For the first loop of this exercise you have to define a variable called
# sum first
sum1 = 0
# Now we initiate our loop, to run from 0 to 21 we have to define a range of 22
for i in range(22):
    # To calculate the sum we just add the running index i to the variable sum
    # we defined beforehand
    sum1 += i
# Now we print out our result
print("The result of the first loop is: ", sum)
# For the second loop we have to define a new variable beforehand again
sum2 = 0
# Now we have to initiate the loop with the help of range in the form shown
# below beacause we want to use only even numbers
for i in range(0,23,2):
    # To calculate this other sum we again just add our running index i to the
    # predefined variable. Remember i is increased by two for each iteration
    sum2 += i
# Now we print out or second result
print("The result of the second loop is: ", sum2)
# The third loop is a bit tricky. There are multiple ways to tackle an exercise
# like this with the help of loops. I will show you some ways.
# The first way would be by using an empty list and the known number of
# repetiitions
resultlist1 = [] # We first define an empty list
# Now we initiate our loop
for i in range(22):
    # since we know our biggest number we can append our empty list like this
    resultlist1.append(21-i) # This adds the reverse numbers to our list
print("The list for the first way of doing the third loop:\n",resultlist1)
# Another way would be to create a list with range beforehand
resultlist2 = list(range(22))
# Now we use the same loop initiation
for i in range(22):
    # Now we can overwrite the entries in our resultlist
    resultlist2[i] = 21 - i # With this we would get the reverse list as well
print("The list for the second way of doing the third loop:\n",resultlist2)
print("")
# Last but not least you could use the version Shoko showed us, by using reverse
# and adding up the lists
# First we create an empty list again
resultlist3 = []
# Now we loop over the reversed range. The reversed command gives us a range
# that starts at 21 and ends at 0
for i in reversed(range(22)):
    # The command below lets us just add a small list containing only the
    # running index to our resultlist3
    resultlist3 += [i]
print("The list for the third way of doing the third loop:\n",resultlist3)
print("")

# Now we want to talk about how to loop over the elements contained in an
# iterable object (list, tuple, set or dictionary). For To make this clear I
# defined a list, a tuple, a set and a dictionary below. I varied the order
# of the elements to illustrate which loop runs over which iterable
list1 = [2,5,1,9, "Hello"]
tuple1 = (2,5, "Hello",1,9)
set1 = {2,9, "Hello",5,1}
dict1 = {"C":89, "A":67, "B":34}
# So now we can loop over the elements of our iterables. We start with the list
print("The elements of list1 are:")
# So we initiate our loop but this time we don't use a range but the list and
# our running index isn't an integer but the different entries of our list
for elem in list1:
    print(elem)
print("")
# Now we do the same for the tuple
print("The elements of tuple1 are:")
# You can use the same running index as long as you already finished the loops
# beforehand. But keep in mind that elem is still defined
for elem in tuple1:
    print(elem)
print("")
# Our third loop now runs over the set
print("The elements of set1 are:")
for elem in set1:
    print(elem)
print("")
# If we are working with a dictionary the default behavior is to iterate over
# the keys of the dictionary, so a loop like the one below prints out the keys
print("The keys of dict1 are:")
for elem in dict1:
    print(elem)
print("")
# If you want to use the values and not the keys of the dictionary you would
# have to adjust your print command like shown below
print("The values of dict1 are:")
for elem in dict1:
    print(dict1[elem])
print("")
# To access the values of a dictionary in a alphabetically sorted order you
# would need to create a list with the keys first
keys1 = list(dict1.keys())
# Now you have to sort your list
keys1.sort()
# And now you can loop over your dictionary in an alphabetical order
print("Alphabetical order of values in dict1:")
for elem in keys1:
    print(dict1[elem])
print("")

# Now for exercise 63, I will show you the results with a list that was
# generated at random just like, Fabian showed in the chat. I will include
# a comment that contains a list that is typed in by me as well. So you can
# interchange them by commenting either one of the two out.
print("Results for Exercise 63")
# First we create our list
# randomlist1 = [5,94,18,2,63,55,78,23,15,9,43,38,81,18,6,45,96,26,47,37]
randomlist1 = [random.randrange(1, 100, 1) for i in range(20)]
# In our first loop we want to sum up all elements of this random list. So we
# have to define a sum variable beforehand
sumrandom1 = 0
# Now we loop over our random list and sum up the elements
for elem in randomlist1:
    sumrandom1 += elem
print("The sum of the random list is: ",sumrandom1)
print("")
# For the second part we need a user input first. Don't forget to cast it to an
# integer
guess = int(input("Please type in a number: "))
print("")
print("Checking the numbers lead to the following results:")
# Now we can again loop over our random list
for elem in randomlist1:
    # First we have to check if the number in the list is bigger than guess
    if elem > guess:
        # we print out the answer
        print("The current element of the list is bigger than " + str(guess))
    # Than we create an elif statement to see if the number in the list is
    # smaller than the guess
    elif elem < guess:
        # Again we print out the answer
        print("The current element of the list is smaller than " + str(guess))
    # last but not least the numbers could be equal
    else:
        # We print out a corresponding answer
        print("The current number equals " + str(guess))
print("")

# Now we want to work with while loops. These loops are used if you don't know
# how many repititions you need to fulfill a specific task. I will first show
# you a simple example in this code and than I will give you the solutions to
# exercise 24
# For the example as well as for exercise 24 we will use a random list. We will
# again work with a list that was generated at random just like, Fabian showed
# in the chat but I combined it with a random number at the end.
# So the code "random.randint(2,25)" generates a random integer in the range
# from 5 to 25 so that we don't know how long our finished list is
randomlist2 = random.sample(range(10, 100), random.randint(5,25))
print("Our randomized list looks like this: \n",randomlist2)
# # Now we want to create our first simple while loop. We have to define a
# # running index i first
# i = 0
# # Now we can initiate our while loop. We have to use the len() because we don't
# # know how many entries our list has.
# while i < len(randomlist2):
#     # Now we add a simple print command to see what the loop does
#     print(randomlist2[i])
#     # You have to update your running index manually, otherwise the loop would
#     # go on forever without stopping. Tis is always done at the end of the loop
#     i += 1
print("")

# Now we go on with exercise 24.
# In the first part we are searching for a specific number within our list. We
# don't know if the number we are searching for is really in our list so we
# have to run a loop like this
# First we define our search parameter
search = 25
# First we define our running index
i = 0
# Now we initiate the loop
while i < len(randomlist2):
    # Now we create an if statement
    if randomlist2[i] == search:
        # We create a statement that we found the number
        print(str(search)+" was found at index " + str(i))
        # To stop the loop we can use the break command
        break
    # We update our running index
    i += 1
# If we don't find our searched value we our running index would be as big as
# the length of our list. So we can generate a simple if statement like this
if i == len(randomlist2):
    print(str(search)+" was not found")
print("")
# For the second part we first have to define our product
product = 1
# Now we define again our running index
i = 0
# Now we start our loop
while i < len(randomlist2):
    # Now we multiply the entires of our list with each other
    product *= randomlist2[i]
    # We update our running index
    i += 1
# We print out our result
print("The mulitplication of all elements results in: ",product)
print("")
# For the last part we need to generate a list by ourselves
randomlist3 = ["World","Hello","Christoph","Fabian","Vera","Python","CQ"]
# The line above shuffles the values of our string list at random. This is done
# in place as we also saw for the list methods.
random.shuffle(randomlist3)
# Now we define our running index again
i = 0
# And we can construct our loop like this
while i < len(randomlist3):
    # So we print out the string
    print(randomlist3[i])
    # We update our running index
    i += 1
print("")

# Now we work with nested loops. We have to initiate the second loop inside the
# first loop to make this happen. So we first initiate a loop that runs from 0
# up to 6:
for i in range(7):
    # Now we generate a second loop that runs from 0 up to 4 for each value of
    # the first loop. So for each i = 0, 1, 2, 3, 4, 5, 6 we will run the second
    # loop
    for j in range(5):
        # We multiplicate the two running indices with each other
        val = i*j
        # We print out the multiplication result
        print(i,'*',j,'=',val)
print("")
# Now we work on exercise 25.
# We have to generate a multi-dimensional list called testmatrix with the help
# of the random module. For this exercise we want our outer list to contain
# three lists with 5 radnom numbers from 10 to 99
testmatrix = [list(random.sample(range(10, 100),5)),
list(random.sample(range(10, 100),5)),
list(random.sample(range(10, 100),5))]
print("Our random matrix looks like this:\n",testmatrix)
print("")
# To sum up all value in this matrix we first have to create a variable sum3
sum3 = 0
# Now we have to create our nested lists. The first list runs through our outer
# list so the initiation look slike this:
for i in range(3):
    # Now we have to initiate our second loop, which runs through our inner
    # lists, so we have a range of 5
    for j in range(5):
        # Now we can add the element of the inner list to our sum
        # So you have to access the testmatrix with the help of the indices
        # the first index i represents one of the three lists and the second
        # index j represents one of the 5 entries in the corresponding inner
        # list
        sum3 += testmatrix[i][j]
# We print out the result after the loops. because this line has no indent
# python knows that it's no part of the loop anymore
print("The sum over the matrix is:",sum3)
print("")
# The second part is to find the maximum of our matrix. For this task we have
# define a variable maxmatrix at first
maxmatrix = 0
# Than we have to define two help variables maxi and maxj, to collect the
# position of the maximum
maxi = 0
maxj = 0
# Now we can initiate our nested loops just as we did beforehand, first over
# the outer list
for i in range(3):
    # second of the elements of the inner lists
    for j in range(5):
        # Now we have to include an if-statement to see if the current entry
        # is bigger than the set maximum
        if testmatrix[i][j] > maxmatrix:
            # Now we set our variable maxmatrix to the new found maximal value
            maxmatrix = testmatrix[i][j]
            # Now we replace our help variables maxi and maxj with the new
            # indices
            maxi = i
            maxj = j
            # Now we know at which position our maximal value is
# At last we print out our found result
print("The maximum of",maxmatrix,"is in list",maxi,"at index",maxj)
