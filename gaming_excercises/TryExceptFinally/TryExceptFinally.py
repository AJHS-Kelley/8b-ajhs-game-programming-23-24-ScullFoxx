# This is a method for testing code and preventing crashes.
# try -- except -- else -- finally

try: # The code in this block is ALWAYS executed.
    myVariable = 1
    print(myVariabl)
except NameError: # This specific except line of code will ONLY run if there is a NameError
    print("There is an incorrect variable name in your code.")
except: # This code will always run IF there is an error (exception) raised.
    print("Something has gone wrong!")
else: # This code runs if there are NO ERRORS
    print("Code executed correctly with no exceptions.\n")
finally: # THIS CODE ALWAYS RUNS, IT'S LIKE THE TERMINATOR.
    print("I'll be back.\n")