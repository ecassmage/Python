if __name__ == '__main__':  # guard
    L = ["vanadium", "erbium", "argon", "tantalum", "iodine", "rhenium", "bismuth"]  # List of L
    print(f"The Starting list is: {L}")  # Prints out the list L
    num = int(input("Please input a valid integer between 0 and 6 inclusive: "))  # Takes input type int. Assumes inputted correctly as question said to.
    e = L[num]  # Takes the num element in L and passes its reference to e
    print(f"The Value Collected at index {num} is: {e}")  # prints the num index and the e element

    if e[-3:] == "ium":  # If the element ends with ium, go here
        print(f"The Number of characters in {e} is: {len(e)}")  # print the element e and the length of the element e.

    elif e[0] in "aeiou":  # else if the element does not end with ium, go here
        L.pop(L.index(e))  # pops (removes) the element at index L.index(e) which will search through list until it finds the element e in question and then return index postion
        print(f"The New List is: {L}")  # Prints the new list avec element e absent.
