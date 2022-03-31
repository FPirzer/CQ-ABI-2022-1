"""
This is the Python script of our tenth day of Python. We continued with talking
about argparse. Afterwards we started with working with files (writing and
reading files) with the standard Python package. Afterwards we worked on
raising exceptions and last but not least I show you some ways to shorten
your code.
"""
import os

os.system("clear")
# For exercise 40 I created a separate called exercise40, that I upload on the
# BSCW as well.

# # After we were finished with argparse we started working with files. First we
# # learned how to write things into files. To be able to do this you have to use
# # the open() method that takes always two arguments. First the name of the file
# # you want to work with and second an operator that tells Python what you want
# # to do with your file. "w" stands for writing, and if you use it the contents
# # of your file are overwritten. You can also use "a" to add things to the end
# # of your file. In the following code I will try to explain the writing in files
# # alongside the exercise 43.
# # The exercist states that we should write two lines in a new file. Remember
# # that if you are naming a file that doesn't exist it's created on the call of
# # the open() method. For the first part we use the "w" option.
# File = open("Writing_python.txt", "w")
# # Now we opened our file we can add text to it. We use this with the
# # File.write() method. write() takes only one argument so if you want to combine
# # strings in it you have to use a + and can't use a comma like we saw for the
# # print command. Furthermore only strings can be written in a file, so you have
# # to cast numbers to strings before writing them into a file. So now we write
# # our first line
# File.write("This is a test\n")
# # The "\n" at the end of our string signals Python that it should create a line
# # break after the written text. So that we can go on in the next line. Now we
# # can write our second line as asked by the exercise
# File.write("This is a second test\n")
# # Now we close our file (and save it at the same time).
# File.close()
# # The next part of the exercise asks us to open the file again and add three
# # more lines to the file. So we have to open it again, but this time we use the
# # "a" operator to add text to the end of the file
# File = open("Writing_python.txt", "a")
# # Now we can add three more lines to our file with the write()
# File.write("This is a third test\n")
# File.write("This is a fourth test\n")
# File.write("This is a fifth test\n")
# # Now we have to close the file again to remove it from our memory.
# File.close()
# # The third part of the exercise wants us to create a file with the help of the
# # with statement and a loop. The file should contain the numbers from 0 up to
# # 10 in a reverse order as a form of countdown. So we start this part of the
# # exercise by generating our with operator as shown below. We use the "w"
# # operator in this case because we don't want to add additional content to the
# # file should it already exist.
# with open("Countdown.txt", "w") as File_with:
#     # Now we can initiate a for loop with a reversed range like we already saw
#     # before.
#     for i in reversed(range(11)):
#         # To write the numbers into the file you have to cast them to string
#         # beforehand. Don't forget to add the line break.
#         File_with.write(str(i) + "\n")

# After we learned how to write files we now want to read in the files again.
# There are four different methods to do this. Th efirst one is shown below. You
# can use this method to read in the whole file into one variable. please take
# note that the contents of the file are seen as one large string. To use this
# you have to open the file again in a with statement, but this time we use the
# "r" operator for reading.
with open("Countdown.txt", "r") as read_file:
    # Now we can read in the whole file into our variable contents
    contents = read_file.read()
# Now we can access the variable contents as shown below. Please keep in mind
# that all line breaks Python encounters during the reading stay intact in the
# resulting string, thus if you use print like it's done below, these line
# breaks are done as well
print(contents)
# To see how the whole string looks like you can use repr(),because now the line
# breaks aren't handed over to the print command.
print(repr(contents))
# The second method to read in our file is by using the readlines() method in
# our with statement. now we create a list that contains each line of the file
# as a separate entry in our list. We have to use the "r" operator here as well.
with open("Countdown.txt", "r") as read_file:
    # The command below creates a list named contents2 that contains each line
    # of our file as one entry. Please keep in mind that the line breaks are
    # also carried over if you use readlines() like this
    contents2 = read_file.readlines()
# Now we can print out our list.
print(contents2)
# The two methods I showed to you above should only be used for small files,
# since you put your whole file into your Ram. To put only one line at a time
# into your Ram use the method shown below with the for loop inside the with
# statement. Since this is also part of exercise 44 I use this example to show
# you how you could solve this exercise. First define your sum
sum1 = 0
# Second we open our file using the with statement
with open("Countdown.txt", "r") as read_file:
    # Now we can loop over the lines as shown below.
    for line in read_file:
        # Now we can work with each line by simply using the loop variable line
        # Keep in mind that you read in strings, so you have to cast them to
        # integers to be able to calculate a sum.
        sum1 += int(line)
# Now we can print out the sum we calculated.
print(sum1)

# Now we want to tackle exercise 45, in which we copy one file that the user
# chooses. First we have to get the input user.
FileOriginal = input("Which File do you want to copy? ")
# Now we have to open the Oroginal File
with open(FileOriginal, "r") as read_file:
    # Then we open a new File called Copy_Original to write the contents of our
    # read in file in it.
    with open("Copy_" + FileOriginal, "w") as write_file:
        # Now we loop over our read in file so that we use only one line of the
        # file at a time
        for line in read_file:
            # Last but not least we can write the lines we read in from our
            # original file into the copy.
            write_file.write(line)
