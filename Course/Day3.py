"""
This is the script of our third day working with Python
We finished out lessons about if statements and than started working on
data structures like lists. We covered the creation of lists, the operators
len() and range(), how to slice lists and last but not least we worked on
multi-dimensional lists. Keep in mind that this is no real program but a
collection of commands with comments for your study afterwards.
"""
# We will create a simple list containing the week days
# weekdays = [
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday",
# ]
# # We can print out this list
# print(weekdays)
# # We can access specific entries in a list with [] and the index, remember in
# # Python the indexing starts with 0
# print("The second entry in the list weekdays is " + weekdays[2])
# # To access a position with the help of a user input you would have first
# # create a variable with the user input, called Pos here
# Pos = int(input("Which position: "))
# # Than you could access the entry in the list with a variable, but the variable
# # has to be of the type int
# print("The entry on position " + str(Pos) + " in the list weekdays is " + weekdays[Pos])
# # You can always create lists that combine values of different types
# Example = [1, 3, "Hello", "World", 1.56]
# print(Example)
# print("The list above contains on Positions 0, 2 and 4 the following data types")
# print(type(Example[0]))
# print(type(Example[2]))
# print(type(Example[4]))

# # We can use tange to generate lists that contain specific integer values,
# # but since range is a generator we have to cast it to a list
# # The first list Nrs1 contains values from 0 up til 15, so the last value
# # is excluded
# Nrs1 = list(range(16))
# print(Nrs1)
# # We can use range with two parameters to define a start value and an end value
# # The start value is included in the list but the end value is excluded from it
# # So Nrs2 contains values from 5 up til 25
# Nrs2 = list(range(5, 26))
# print(Nrs2)
# # If we use range with three parameters we can adjust the numbers that are
# # included in the list. So in the example below Nrs3 contains the values
# # 0, 3, 6 ,9 ,12, 15, 18 and 21, that means only each third value
# Nrs3 = list(range(0, 21, 2))
# print(Nrs3)

# # We can elongate lists witht he help of two commands called append and extend
# # Both operations are done in place, that means you change the value of the list
# # you elongate with these commands. So you have to keep in mind that the list
# # that is returned differs from the list you used for this operation
# # We start by generating three lists for this example
# list1 = list(range(4))
# list2 = list(range(4))
# list3 = list(range(4))
# print("The example lists list1, list2 and list3 look like this:")
# print(list1)
# print(list2)
# print(list3)
# # Now we append the third list to the first list and create a multi-dimensional
# # list. Append adds the list3 as a whole to list1 so that list3 is now on index
# # 4 of the first list
# list1.append(list3)
# print("list1 looks now like this:")
# print(list1)  # We print out the whole new list
# # We print out the length of the new list
# print("The lenght of list1 is " + str(len(list1)))
# print("The index 4 (fifth entry) of list1 looks like this:")
# print(list1[4])  # We print out the entry on index 4 of the new list
# # If you want to access a specific entry in the added list you have to use
# # two indices
# print("The third entry of the list contained in list1 looks like this:")
# print(list1[4][2])
# # Normally append is used with single values since it doesn't iterate of the
# # contents given to it
# list1.append(5)
# print(list1)
# # If we use extend, the entries of the list we want to add to our old list
# # are added to it element-wise. The operator extend iterates over the contents
# # of list2 in the example below and adds its values to the list3
# list3.extend(list2)
# print(list3)  # We print out the whole new list
# We print out the length of the new list
# print("The lenght of list3 is " + str(len(list3)))
# print(list3[4])  # We print out the entry on index 4 of the new list
# If we use extend with a string the list would be extended with each letter
# of the string as a new entry of the list
# list3.extend("Hello")
# print(list3)
# # We can also use the "+" to combine two lists, but this doesn't work in place
# # so you have to define a new variable list5 like in the example below. This can
# # be used if you don't want to change your previously defined lists
# list4 = list(range(6))
# # We print out our two lists
# print("Our test lists look like this")
# print(list2)
# print(list4)
# # Now we combine our lists and create the new list list5
# list5 = list2 + list4
# # Now we print out all three lists again
# print("The two example lists and the added list look like this:")
# print(list2)
# print(list4)
# print(list5)
# You can access the last entries of a list by using negative indices
# The first example below accesses the last element of list5
# print(list5[-1])
# In this example we access the second to last element of list1 (the added list)
# and than access the second element of this added list
# print(list1[-2][2])

# # We now want to work on slices of lists, therefore we generate a new, longer
# # list at first
# list6 = list(range(16))
# # Now we print out the whole list first
# print("list6 looks like this:")
# print(list6)
# # Now we print out only a part of the list by using a slice. The printed out
# # lists includes the value on index2 of list6 but excludes the value on index
# # 9 of list6
# print("Indices 2 until 8 of list6 look like this:")
# print(list6[2:9])
# # We can even use slices to hand over only parts of a list to a new variable
# # in this case the list7 contains the values of the indices 10, 11 ,12 and 13
# # because the value of index 14 was excluded
# list7 = list6[10:14]
# print("The new list containing Indices 10 to 13 of list6 looks like this:")
# print(list7)
#
# # We can use some kind of wildcards for slices by using ":"
# # With the list6 above we could use the example below to get all values from
# # the fourth entry until the end
# print("The entries of list6 starting at Index 3 look like this:")
# print(list6[3:])
# # To access all entries until the third one we could use a print like this:
# print("The first three entries of list6 look like this:")
# print(list6[:3])
# # If we use two ":" before a number in the slice only each third number would
# # be returned:
# print("Using :: we would get a list like this:")
# print(list6[::3])
# # Last but not least we can use ::-1 to reverse a list
# print("Reverse of list6:")
# print(list6[::-1])

# We now want to shorten lists by removing certain elements from them
# Please note that every time you remove something from a list the indices
# are adjusted accordingly. So if you remove the third entry,the entry on index
# 4 in the original list is now on index 3 in the adjusted list
# All operations below are done in place, that means you change the contents of
# your variable and don't create new ones
mylist = ["apple", "banana", "orange", "apple", "lemon", "melon", "peach"]
print(mylist)
# We can remove specific entries just by handing over the value we want to remove
mylist.remove("lemon")
print(mylist)
# We can also remove entries by using indices if we don't know the exact value
mylist.remove(mylist[2])
print(mylist)
# If we have duplicates in our list, remove() only removes the first occurence
# of this value and leaves the remaining intact
mylist.remove("apple")
print(mylist)
# With the help of slices and the del command we can remove several entries at
# once
del mylist[1:3]
print(mylist)
