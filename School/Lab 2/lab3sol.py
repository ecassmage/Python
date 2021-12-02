str1 = '51//4'  # assigning string to str1
print(f"str1 is: {str1}")  # printing str1

print(f"First occurrence of / is at index: {str1.find('/')}")  # finding first occurrence of / and printing it.

num1 = eval(str1)  # evaluating str1
print(f"The Evaluated form of str1 is: {num1}")  # printed the evaluated str1

str2 = str1[0:3]  # splicing str1 for the first 3 characters
print(f"the first three characters of {str1} are {str2}")  # printing the first 3 characters

name = input("Please input your name here: ")  # assigning the inputted name to name
print(f"Your name is {len(name)} characters long")  # printing the given name

upperName = name.upper()  # converting name using the method upper
print(f"Your name in all uppercase letters is: {upperName}")  # printing upperName

last = upperName[-1]  # assigning the string of the last letter of upperName to last
print(f"{last} appears in {upperName} {upperName.count(last)} time", end='')  # printing the number of occurrences the last letter is found in the upperName, the end='' is just so I can choose to add an s to the end or not
print("s") if upperName.count(last) > 1 else print()  # if else to determine whether to print an s or not. needs the blank print() so as to add a \n character or else the next line will be on the same line as this one.


str3 = str1 + name  # concatenating str1 with name, no space between them
print(f"{str1} concatenated with {name} is {str3}")  # printing the concatenated str3
