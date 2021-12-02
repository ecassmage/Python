# import antigravity  # Greatest Library Python has.

if __name__ == "__main__":  # guard
    L = [23.4, 118, "ROSALIA batesi beeTLES  ", -49, 37]  # List called L.
    print(f"This is L: {L}")  # prints L.
    x = L.pop(2)  # pops the element at index 2 and returns it to x.
    print(f"This is L now: {L}")  # prints L.
    space = False  # for space formatting
    temp = ""  # temp for easier stuff
    for word in x.split(" "):  # splits based on space. I like adding the character even if not necessary. In this case it is though
        if space:  # if on second or later word
            temp += " "  # adds a space between each word.
        else:  # if first word
            space = True  # space set to True
        temp += word.capitalize()  # stores new capitalized words together
    x = temp  # sets x to be the new string
    print(f"This is centered with space: {x.center(30, '*')}")  # prints x centered
    x = x.rstrip()  # strips character from r side. default I believe is space, probably. rsplit uses *args in its definition and I can't seem to track its source code to check. was reminded of the antigravity library though
    print(f"This is centered without space: {x.center(30, '*')}")  # prints x centered
    x = x.replace("es", "*")  # replaces all occurences of es with *. Greatest thing besides regex.
    print(f"This is x without es: {x}")  # prints x
    L.insert(3, -5.1)  # Inserts -5.1 at index 3
    print(f"L has new element: {L}")  # prints L
    L = list(reversed(L))  # darn iterators needing to be converted to lists.
    print(f"L is Reversed: {L}")  # prints L
