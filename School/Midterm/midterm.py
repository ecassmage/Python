"""

Developer: Evan Morrison
Version: 1.0.0
Since: 1.0.0

First things first, I got a little confused here as part a) says: Initialize a variable name1 with your last name in uppercase letters. Print name1 with a suitable message.
However there is a NOTE at the bottom which states NOTE: In step a) you MUST initialize name with your actual first name. The output of your code will be different from other students in the class.
I am confused with the fact it says use your last name in part a then in the note it says use first name.
my first name is EVAN if that needs to be changed, Not sure. I added a line in comments which has the line should the NOTE be wanted instead.
"""


if __name__ == "__main__":  # Just a guard statement against modules and multiprocessing, don't want to break the habit of using it.

    name1 = "MORRISON"  # This is my last name in all uppercase.
    # if I was mistaken and I needed to use my first name then the next line is what I would have put
    # name1 = "EVAN"

    print(f"This is my last name: {name1}")  # This will print out a statement plus my last name stored in name1

    mynum = ord(name1[0])  # this will store the ascii value of the first letter of my last name in mynum

    print(mynum, end="")  # this is just to print out the number so whoever is marking can see that the number is odd / even.
    # the end="" means that print will at the end of printing to the buffer write "" instead of "\n" which end is defaulted to. this is so that the next print statement will be on the same line
    # this is done so that this only has to be written once.

    print(f" is even, so the result is even") if mynum % 2 == 0 else print(f" if odd, so the result is odd")  # if else statement conjoined into one to save space. Love languages which have something like this.
    # first print statement will trigger if (mynum % 2 == 0) results to True and the second print statement will trigger if False.
