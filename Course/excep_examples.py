"""
This is the script for using try and except. It also doubles as solution for
exercise 41. Everything in here was discussed during the afternoon on the
23.02.2022.
"""
# Since I want to work in a while loop for this example I have to define my
# loop variable i first
i = 0
# Since I want to do a Division I have to define the number I want to divide
# next, in our case we take the simple 10.
Base = 10
# Now I initiate my while loop with the loop variable i
while i < 5:
    # In my loop I create my try statements. Each try has to be accompied be at
    # least one except. The except can be empty (use pass) but it has to be
    # present
    try:
        # First we get an input from the user and cast it to an integer. This
        # can raise an ValueError if we hand over a String to our int() method.
        Number = int(input("Type in a number "))
        # Now we calculate our Division. Of course this part of the code is only
        # run if we didn't encounter an error during the line above. The
        # Division can return a ZeroDivisionError if our input number was 0.
        Divi = Base / Number
    # Now we can set up our exceptions. First we create an exception for the
    # ValueError that could occur during our casting of the input.
    except ValueError:
        # The code below is only executed if we encountered an ValueError. So
        # if we encounter any other kind of error this code is ignored by the
        # program
        print("Please type in a number")
    # Now we can set up additional exceptions for other specific errors or
    # all remaining errors. The exception below is run if the user typed in a
    # 0 at the input in line 19.
    except ZeroDivisionError:
        # As soon as the program encounters an ZeroDivisionError this code is
        # executed.
        print("Division by Zero is not possible")
    # Last but not least I include an empty except at the end. This is not very
    # elegant and normally you would let the errors occure and use each except
    # with a specific error. But for our purposes these empty excepts are fine.
    except:
        print("What a mess. We encountered some unknown Error.")
    # If we didn't encounter an error, we can use else to add some additional
    # code that is executed afterwards. Since this part of the program is only
    # executed if everything went well during our try we can use the things we
    # did beforehand just fine.
    else:
        # The two lines below are only executed after we encountered no errors.
        # So we can access the two variables we tried to define during our try
        # without an problems
        print("Your input was:", Number)
        print("10 divided by your number equals:", Divi)
    # Last but not least we have to update our inning index, to circumvent
    # running an infinite loop as we saw in an example today.
    i += 1
