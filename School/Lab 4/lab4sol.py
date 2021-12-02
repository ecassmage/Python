import copy


def oneA():  # for organization but mainly for recursion in oneD
    list1 = [[55, 32.01, -14.2, 6.74], 0, 119.954, -17, 0, ['Mercury', 'Venus']]  # List 1
    """This is weird, in my time of using python I never realised you could actually use semi colons for separation of lines"""
    'a.'; print(f"This is list1: {list1}")  # -- The Answer for one A
    return list1  # Returns the Generated List


def oneB(list1):  # for organization but mainly for recursion in oneD
    num = 0.0  # float initialized variable
    for ele in list1:  # For loop
        if type(ele) == int or type(ele) == float:  # if else to add up the sum of the list
            num += ele  # adds the sum up

    'b.'; print(f"The Sum of all applicable objects is: {num}")  # -- The Answer for one B


def oneC(list1):  # for organization but mainly for recursion in oneD
    list1[0][list1[0].index(max(list1[0]))] = "max"  # pass by reference will allow changes to stay after the function closes
    'c'; print(f"The New List is: {list1}")  # -- The Answer for one C


def oneD(list1, last=True):  # for organization but mainly for recursion in oneD
    num = 0  # nums initialized to int 0
    for i in list1:  # for loop iterates through elements in list passed
        if type(i) == list:  # checks if type is a list
            num += oneD(i, False)  # if so goes and calls oneD again to go through this nested list
        elif i == 0:  # else if element is a 0 then
            num += 1  # adds 1 more to the count
    if last:  # this is for enclosure of the function. checks if this is the first recursion depth
        'd.'; print(f"There are a total of {num} 0's in the list including for nested lists")  # -- The Answer for one D
    else:
        return num  # if not first level of recursion then goes back a level carrying the number of 0's back with it.


def oneE(list1):  # for organization but mainly for recursion in oneD
    list1.insert(2, [1, 2])  # inserts the list [1, 2] into index position 2
    list1.append(8)  # appends 8 to the end of the list
    print(f"list1 is now: {list1}")  # -- The Answer for one E


def oneF(list1):  # for organization but mainly for recursion in oneD
    list2 = copy.deepcopy(list1)  # you can not make a new copy of a list without using copy.deepcopy if there are nested lists inside them. This is because lists use pass by reference so the pointer is the only thing being copied as new.
    # list1.copy() can be used if there are no nested lists since if there are, the same problem will occur in that the nested list will be modifiable from both copies instead of just 1. deepcopy uses recursion probably to go deep into the list.
    list2.extend(['alpha', 'beta'])  # extends to the end of the list all the elements in the list given
    print(f"The new List2 is: {list2}")  # -- The Answer for one F


if __name__ == '__main__':  # A habit you get into when working with modules and Multiprocessing
    list1 = oneA()  # runs question 1 A
    oneB(list1)  # runs question 1 B
    oneC(list1)  # runs question 1 C
    oneD(list1)  # runs question 1 D
    oneE(list1)  # runs question 1 E
    oneF(list1)  # runs question 1 F
