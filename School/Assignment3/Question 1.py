# did this a while ago, didn't want to write comments.


if __name__ == '__main__':  # guard.
    nums = [92.2, -13, 541, 0, -35.755, 4]  # nums list.

    print(f"This is the nums list: {nums}")  # prints nums w/ suitable message.
    nums.sort()  # sorts the nums list with the sort method.
    print(f"This is the nums list sorted: {nums}")  # prints nums w/ suitable message.
    num = input("Please enter a valid input: ")  # takes input from user. Assumes input is number, checks for if integer or float. Probably easier way but can't remember what that would be.
    try:  # tries to convert to int, if fails then does except.
        num = int(num)  # converts num to int. Should fail on . of num.
    except ValueError:  # excepts that input is a float.
        num = float(num)  # converts to float. If this fails then user didn't follow rules.
    for indexPos, numberInList in enumerate(nums):  # operates a for loop where each iterated element has its value + the index position in the enumeration. ie 92.2 would have (0, 92.2) where it is split to be indexPos=0, numberInList=92.2.
        if num < numberInList:  # sorts by bubble sort, except this is O(n) since the list is already sorted and only needs single for loop.
            nums.insert(indexPos, num)  # inserts at position where num is less then current index holder.
            break  # will break the for loop, therefore skipping the for else.
    else:  # this will trigger if no insert position was found.
        nums.append(num)  # if num is bigger then last number this will be triggered.
    print(f"The New List of nums is {nums}")  # This will print the new list out.
