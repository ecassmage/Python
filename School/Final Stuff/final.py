__ID__ = 110043572  # global, for some reason.


if __name__ == '__main__':  # guard against other processes triggering this code
    mynum = int(str(__ID__)[-3:])  # just some funny stuff.
    print(f"The last three numbers in my fancy ID: {mynum}")  # print message. outputs mynum.
    summation = 0  # this is sum. Sorry, didn't want to name it sum as this will overwrite built in function and it isn't really a good idea to overwrite the built ins since you will no longer be able to use it.
    list1 = [5, 278, 982, 150, 300, 789]  # list of nums
    print(f"This is list1: {list1}")  # print message. outputs list
    # really wanted to use match instead of if elif else, but don't know if marker is using 3.10
    for element in list1:  # for loop
        if element < mynum:  # if less then
            print(f"element {element} is less then mynum {mynum}.")  # print message. outputs element and mynum if element is less then mynum
            summation += element  # summation addition
    print(f"The final summation is {summation}.")  # print message. outputs summed up number
