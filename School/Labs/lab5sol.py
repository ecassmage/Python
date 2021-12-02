str1 = input("Please input an alphanumeric string: ")
# feel like match would be good for this.

try:  # kind of cheaty to just go for the error and skip it
    num = int(str1)  # This will cause a ValueError Exception to signal python. Try will catch this and pass the program to the except section of the program. this will only trigger if str1 contains more then just digits.
    print(f"The Character {chr(num)} has {str1} as its ASCII value.") if 48 <= num <= 122 else print("You have entered a numeric string.")  # Prints should no valueError exception be caught. aka this is an int.

except ValueError:  # catches and ignores the ValueError Exception
    for char in str1:  # goes through the characters in str1
        if 48 <= ord(char) <= 57:  # if withing this ascii integer range
            break  # breaks at this point. Will skip the else and print the last line
    else:  # if the for loop is not forced to break the entire way through then this  will be run.
        # not sure if I can use regex :(
        if str1.find('abc') >= 0:  # if this string of characters if found then print this message
            print("“Your string contains ‘abc’.”")
        elif str1.find('ab') >= 0:  # else if this string of characters if found then print this message
            print("“Your string contains ‘ab’.”")
        else:  # else then print this message
            print("“You have entered an alphabetic string.”")
        exit()  # exit the program at this point as to not need a guard statement for the final print statement.
    print(f"The ASCII value of the first character in str1 is {ord(str1[0])}")
