"""
This is the script for the fourth day of our Python course. We are working
with normal lists, mutlidimensional lists and
"""
# We can use a nice little operator called "in" to check whether a value is in
# a list or not. Therefore we need a list and two variables
mylist = list(range(9))
Check1 = 4
Check2 = 12
# We can use the simple if statement below to check, whether a value is in the
# list. This returns TRUE as soon as the value is in the list and FALSE if not
if Check1 in mylist:
    print("This value is in the list")
# We can also use the NOT operator with in. So now the statement below returns
# FALSE if the value is in the list and TRUE if the value is not in the list
if Check2 not in mylist:
    print("This value is not in the list")
# We can use the in with strings as well. In the example below we didn't even
# declared a variable beforehand, because the if statements work like this as
# well.
mylist2 = ["Hello", "World"]
if "Hello" in mylist2:
    print("Hello again")

# Now we want to insert new values in a list. We define a new list first
mylist3 = list(range(11))
print(mylist3)
# You can use the insert function as shown below. The first parameter is the
# index at which we want to insert the value and the second parameter is the
# value we want to insert. Inserting is done in place just like with the
# functions remove(), append() or extend(), so keep in mind that you change
# your list by using insert()
mylist3.insert(5, 100)
print(mylist3)
# You can also insert strings into a list of integers or floats and vice versa
# For lists the data type of its entries don't matter
mylist3.insert(4, "Hello")
print(mylist3)
# If you want to replace an entry you have to overwrite the value at the
# specific position like shown below. There the entry at index 9 is replaced
# with a 1000
mylist3[9] = 1000
print(mylist3)

# We now want to work with some other list functions. Therefore we create two
# new lists containg either strings or integers
mylist4 = [2, 45, 6, 49, 8, 19, 6]
mylist5 = ["Hello", "World", "Bye", "Good Night", "Back", "BYe"]
print("Our example lists look like this")
print(mylist4)
print(mylist5)
print("")
# First we want to sort the lists in place with the help of the sort function.
# The sorting is done in ascending order, but by using the parameter
# reverse=True we can change the sorting to a descending order
mylist4.sort(reverse=True)
# For Strings upper case letters are placed before lower case letters, that's
# why the sorted list starts with "BYe"
mylist5.sort()
print("The sorted lists look like this")
print(mylist4)
print(mylist5)
print("")
# The index function returns an integer value that give the first occurence of
# the specified value. In the Example below we get a 4 since the first 6 is
# at index 4 in the list
print(
    "The first occurence of 6 is at position " + str(mylist4.index(6)) + " in mylist4"
)
print("")
# The functions max and min give out the maximum or minimum value of a list
# and thus need a list as parameter. For strings the behavior is analogous to
# the sorting function
print("The maximum values of the lists are:")
print(max(mylist4))
print(max(mylist5))
print("The minimum values of the lists are:")
print(min(mylist4))
print(min(mylist5))
print("")
# Count returns how often the specified value occurs in the list. For strings
# this function is case-sensitive
# this returns 2
print("The number of occurences of 6 in mylist4 are: " + str(mylist4.count(6)))
# this returns 0 because of case-sensitivity
print("The number of occurences of bye in mylist5 are: " + str(mylist5.count("bye")))
# this returns 1
print("The number of occurences of Bye in mylist5 are: " + str(mylist5.count("Bye")))
print("")
# Reverse lets us reverse the order of a list
mylist4.reverse()
mylist5.reverse()
print("The reversed list look like this")
print(mylist4)
print(mylist5)
print("")
# With the help of copy we can create a new list that is an exact copy of the
# original list. But changes that are done to the copy don't apply to the
# original. So in the example below even though I delete the 45 from mylist6,
# mylist4 still contains the 45 afterwards
mylist6 = mylist4.copy()
mylist6.remove(45)
print("mylist4 after removing 45 from the copy mylist6")
print(mylist4)
print("mylist6 after removing 45 from the copy mylist6")
print(mylist6)
print("")
# Last but no tleast we can use clear to remove all entries from a list. The
# variable remains but it's now an empty list
mylist6.clear()
print("mylist6 after using clear")
print(mylist6)

# Now we work with multi-dimensional lists. For an easier understanding I will
# call them matrices in here. For comprehension we define rows as the sublists
# contained in the outer list and columns as the number of entries in the
# sublists
# You can create multi-dimensional lists in two ways. First you could use the
# range function as shown below:
matrix1 = [list(range(5))] * 5  # this matrix is quadratic
matrix2 = [list(range(4))] * 3  # this matrix has more columns than rows
matrix3 = [list(range(6))] * 8  # this matrix has more rows than columns
# You could also generate matrices by typing in the whole lists like this
matrix4 = [[0, 1, 2], [0, 1, 5], [0, 1, 2]]
# Now we print out our examples
print("Our example matrices look like this")
print(matrix1)
print(matrix2)
print(matrix3)
print(matrix4)
print("")
# If you want to access a specific sublist you have to use a single index:
print("The list at index 1 in matrix4 is:")
print(matrix4[1])
# If you want to access a specific entry of a specific sublist, you have to
# use two indices:
print("The entry at index 2 of the list at index 1 in matrix 4 is:")
print(matrix4[1][2])

matrix2[1].remove(matrix2[1][2])
print(matrix2)

# Now we want to work with dictionaries. Dictionaries are another kind of data
# structures that consist of keys and values. To initiate a dictionary we need
# curly brackets {}. You can hand over entries to your dictionary on the
# initiation by putting them inside the curly brackets. A pair of one key and
# one value are separated by a ":" and different pairs are seprarated by ","
Numbers = {"Marco": 345, "Vera": 879}
print("Our dictionary after th initiation:")
print(Numbers)
print("")
# We can than add entries to the dictionary by simply using square brackets with
# a new key and a new value, just like the examples below
Numbers["Christoph"] = 124  # adds the key "Christoph" with a value of 124
Numbers["Fabian"] = 456
Numbers["Jens"] = [934]  # adds the key "Jens" with a list containing 934 as value
Numbers["Ivana"] = ""
print("Our original complete dictionary looks like this:")
print(Numbers)
print("")
# If we use a key that is already in the dictionary and hand over a value to it
# the original value is replaced.
Numbers["Fabian"] = 109
# But we can work with lists that are in the dictionary like shown below. The
# original list [934] would be appended and looks like this now [934, 678]
Numbers["Jens"].append(678)
print("Our changed dictionary looks like this:")
print(Numbers)
print("")
# The method .keys() returns a list with all keys in the dictionary. This list
# is unsorted alphabetically, but sorted timewise. Just like range keys() is
# just a generator, so you have to cast it to a list
print("The keys of our dictionary are:")
print(list(Numbers.keys()))
# With the two lines below we can sort our keys alphabetically.
Keys = list(Numbers.keys())
Keys.sort()
print("If we sort our keys we get thsi list:")
print(Keys)
print("")
# To generate a list of all values in a dictionary we can use the values()
# method. Again this is just a generator so we have to cast it to a list
print("The values of our dictionary look like this:")
print(list(Numbers.values()))
print("")
# To access a specific value of a dictionary we always have to use its key. So
# if we want to print out the values for Jens we have to use the example below
print("The value for Jens looks like this:")
print(Numbers["Jens"])
print("")
# If you want to know whether a key already exists or not you can use an if
# statement as shown below. This statements returns True if the key "Marco"
# already exists and returns False if the key doesn't exist
if "Marco" in Numbers:
    print("Marco is known")
else:
    print("Marco is unknown")
print("")
# You can remove entries in a dictionary with the help of the del command. So
# in the example below you would delete the key "Ivana" and its value
del Numbers["Ivana"]
print("Our dictionary after the use of del:")
print(Numbers)
print("")
# You can also use the pop method to remove a specific key and its value. So
# in the example below you would remove the key "Vera" and its value
print("Our dictionary after the use of pop():")
Numbers.pop("Vera")
print(Numbers)
