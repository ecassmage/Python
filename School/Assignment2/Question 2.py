if __name__ == '__main__':  # guard statement
    num = None  # makes num = None. This is so to initialize the ptr outside of the while loop while giving it a value that won't trigger some of the checks.
    print("This will loop until a valid input is given")  # Since this is a little different then what was asked, which didn't require a loop to continue until wanted to quit I have this message here to explain what is going on.
    # This nothing is different between this and the example for the quiz except, this one effectively restarts the process after every failed input.
    while len(str(num)) != 3 or num <= 0:  # Loops until the user has entered an integer which is exactly three digits and positive. Anything else will fail the while loop
        if num is not None:  # if this is not the first iteration and we are here then do this. None can't be inputted by user without hacking/debugging so this should  only trigger on iteration 2 and onwards.
            if num == "":  # will print this if input contains characters which are not digits.
                print("Non digit characters were found inside of the input!!!")  # Prints this for above if statement
            elif len(str(num)) < 3:  # else if the length is less then three print out this
                print("Not enough digits")  # Prints this for above elif statement
            else:  # else if the length is greater then three print out this
                print("Too many digits")  # Prints this for above elif statement
        try:  # try guard. will catch exception ValueError and ignore it passing responsibility for error over to except ValueError. Other Exceptions will not be caught and will subsequently trigger an error.
            num = int(input("Please enter only a non-negative three digit number: "))  # Takes input and immediately convert input to an integer will raise a ValueError Exception if not all characters are digits,
            # including floats as period is not recognised.
        except ValueError:  # Deals with any raised ValueErrors caught inside the try body.
            num = ""  # sets the num variable to an empty str variable so as to avoid having it be checked again num <= 0 as that would cause and exception.
    string = str(num)  # sets the num int variable to str. This could be done inside the loop, however it assignment seemed to indicate it wanted to be done after it was verified so I did it separately out here
    a, b, c = int(string[0]), int(string[1]), int(string[2])  # Sets the variables a, b, c to their respective digits in a nice clean single line way.
    print(f"a = {a}, b = {b}, c = {c}")  # Prints out all of the variables here, with a <letter> = <variable Value> format
    print(f"The result of the short-circuit evaluation is {a and b or c}")  # checks the logic of a and b or c and returns the value received. x != 0 indicates False while anything else indicates True.
    print(f"The Expression is {bool(a and b or c)}")  # Prints the True/False Value of the logic argument with same logic indicated above.  x != 0 indicates False while anything else indicates True.

