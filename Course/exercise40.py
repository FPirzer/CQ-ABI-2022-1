"""
This is the program that I wrote for exercise 40.
This program takes a positional argument and three optional arguments for
argparse and works with them.
"""
# First we import the module argparse so that we can set up our arguments later
# on
import argparse

# Now we define our parser, so thath python knows it has to read the command
# line. This allows us to hand over things to the program directly on the start
# of your script. The String you put after description is the help message that
# is displayed if you use the option -h later on. This kind of help is
# generated automatically
parser = argparse.ArgumentParser(
    description="This little script takes some strings and puts them together. You can change the outcome by either adding spaces to the output or to reverse the output."
)
# First we declare our positional arguments. These arguments have to be handed
# over to the program on the start or otherwise you get an error. The error
# message is again generated automatically woth the help of the parse_args()
# method seen later after our arguments. The argument used here takes some
# strings, thats why we use type=str, the nargs="+" tells the parser that he
# has to add the given arguments to a list.
parser.add_argument(
    "strings", metavar="S", type=str, nargs="+", help="the strings to concanate"
)
# Now we can add some Boolean arguments. As soon as we add the argument to our
# parser it starts to exist. If we use the action store_true like seen below,
# the default value of args.space becomes False. This changes if the user
# hands over either -s or --space to the program on the start. With the help
# of arguments like this you can change the behavior of your script. It follows
# the same rules as we saw for linux commands. For example ls alone just works
# but you can change its behavior if you use ls -l or ls -a. The argument down
# below allows us to add white spaces between our words later on.
parser.add_argument(
    "-s", "--space", action="store_true", help="add spaces to the strings",
)
# Now we can add a second Boolean argument. Again this argument is False per
# default and can be set to True if the user uses the option -r or --reverse on
# the start of the program. With the help of this option the order of the parsed
# Strings can be reversed later on.
parser.add_argument(
    "-r",
    "--reverse",
    action="store_true",
    help="reverse the order of the input strings",
)
# Now I add an argument that is True on default and can be changed to False if
# the user chooses it. Here we allow the user to skip the print out of the
# resulting concanated string if he wants to.
parser.add_argument(
    "-p", "--print", action="store_false", help="suppress the print out of the result",
)
# Now I ant to add an option that takes further arguments. To make this possible
# we have to add the nargs = "?" so that maximal one additional argument can be
# handed over to the program. if you want to use multiple nargs you would have
# to use nargs="+" like we saw for our positional argument. If you want to be
# on the safe side use "*" because, now the program runs even if no additional
# arguments are given after the -a or --addition
parser.add_argument(
    "-a",
    "--addition",
    type=str,
    nargs="?",
    help="optional character that can be added between the words. Takes zero or one additional argument",
)
# After we added all arguments to our parser we have to make sure that the
# program can read them in and put the resulting values in a variable called
# args in this case. You can access all arguments of args by using them with
# help of a dot, just like you saw for os.system() for example. So by using
# args.space for example we could access our Boolean variable to see if we have
# to add spaces to our result.
args = parser.parse_args()
# From here on our main program starts. So everything beyond this point is done
# as long as you hand over at least one string to your program on the start.
# What the program  than does depends on how the user set his options. The if
# statement below checks if the user wants to use a reversed order of his input.
# You can use if statements in a simplified version as seen below as long as the
# variable after the if is boolean (True or False). So the example below would
# be True if the user added -r or --reverse to the call of our program.
if args.reverse:
    # We can now reverse the order of our strings by using the reversed method
    # we already saw earlier than we were talking about loops. The variable
    # args.strings is a list that contains all our positional strings we added
    # to the call of our program.
    args.strings = reversed(args.strings)
# Now we start with the creation of our concanated string. We have to define
# an empty string variable first. In our case the variable is called Bigword and
# by assigning only "" to it, Python recognizes the variable as String that
# contains nothing
Bigword = ""
# Now we can loop over our strings we got from the user. Since args.strings is
# a simple list, we can use a for loop as seen below to iterate through it
for word in args.strings:
    # In a first step we add the current entry of out string list to our result
    # string. We can do this by simply using the += command, since in Python
    # the addition of strings leeds to a concanating of these strings.
    Bigword += word
    # Now we check if the user wants a separate addition to its string. So this
    # check is only true if the user added -a or --addition to the start of our
    # program
    if args.addition:
        # Now we can again loop through the possible additional characters the
        # user wants to add to his string. If he didn't specify any additional
        # characters, this loop is empty and nothing happens
        for add in args.addition:
            # So again we add the additional text to our big string
            Bigword += add
    # Now we check if the user wants to add white spaces to its big string. As
    # we saw earlier we can do this with the help of a simple if statement
    if args.space:
        # To add white spaces, we just add them to our big string with the +=
        # shown below
        Bigword += " "
# Now we check if the program should print out the result or not. Remember that
# the args.print is True by default so the statement below is only False if the
# user used the -p or --print option on the start of the program.
if args.print:
    # No we print out our result.
    print(Bigword)
