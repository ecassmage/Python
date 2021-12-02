if __name__ == "__main__":  # guard statement

    lowerString = input("Please enter and alphabetic string: ").lower()  # receives a string in lowercase or uppercase (converts to lowercase) and stores this variable in lowerString.
    print(f"Your string in lowercase is: {lowerString}")  # prints the lowerString variable

    # Kind of wish I had Python 3.10, match would have been useful for this but I mainly wanted to try it out. (match is pythons new switch, so switches are now here, yay)
    if lowerString < "green":  # Checks if less then green. Do This
        print("Your string precedes 'green'")  # prints this message is lowerString is less then green
    elif lowerString < "red":  # Checks if less then red. Do This
        print("Your string precedes 'red'")  # prints this message is lowerString is less then red
    elif lowerString < "yellow":  # Checks if less then yellow. Do This
        print("Your string precedes 'yellow'")  # prints this message is lowerString is less then yellow
    else:  # else repeat the word 3 times
        print(f"Your string in lowercase repeated three times is {3*lowerString}")  # prints a message containing the string 3 times.
