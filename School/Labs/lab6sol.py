nums = []  # empty list
while True:  # Infinite Loop
    num = input("Please give me a positive integer or -1 to Quit: ")  # takes an input no guard as to what will be inputted.
    try:  # a try except section for quick attempting to change num to a float. this will check if this is a number or not.
        float(num)
    except ValueError:  # this will trigger if you didn't follow the instructions.
        print(f"{num} is NOT a Number")
        continue
    if int(float(num)) == float(num):
        if int(num) == -1:  # will exit the while True loop.
            break
        elif int(num) > 0:  # this will append the new num to the list of acceptable numbers.
            nums.append(int(num))
        else:
            print(f"{num} is not a valid Integer")  # This is an invalid integer, ie. less then 0 so while it is an integer, it is not a valid integer
    else:
        print(f"{num} is not a valid Number")  # This is not a valid number, ie it is not an integer.
print("We Done Here\n")  # This states that you have successfully exited the while loop
print(f"The Numbers you followed the rules for are: {nums}")  # This is the list of correct numbers

if len(nums) > 0:  # if list is empty this won't be done
    print(f"The average value of all items is: {round(sum(nums) / len(nums), 2)}")  # Will give the average value of all the items in the list
    print(f"The Smallest integer entered is: {min(nums)}")  # will return the smallest integer in the list.
