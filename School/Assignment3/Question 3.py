if __name__ == '__main__':  # guard
    strList = ['the', 'quick', 'brown', 'python', 'jumps', 'over', 'the', 'lazy', 'dog']  # list of strList.
    print(f"This is strList: {strList}")  # prints strList w/ suitable message.
    char = ""  # sets char to empty string
    while not 'a' <= char.lower() <= 'z' or len(char) != 1:  # while loop for char. if input does not follow rules then this won't break. Rules being needs to be an english alphabetical character and needs to be a single character
        if char != "":  # this will guard against being berated before you even have a chance to input anything.
            print(f"Please follow the Rules, {char} is not valid")  # prints a you didn't follow rules message.

        char = input("Please enter a single character only, letters aloud: ")  # takes a str input. (not char input)
    char = char.lower()  # char is converted to lowercase. I convert officially out here as assignment said once valid input convert to lowercase however if output is bad then it wasn't valid. My logic is dumb but I stick by it.
    numOfAppearances = 0  # number of appearances set to int 0.
    numOfAppearancesWMultiple = 0  # number of appearances set to int 0.
    for word in strList:  # goes through the words in strList.
        # I forgot what this next line does. Took me a minute to figure it out again.
        if -1 != word.find(char) == word.rfind(char):  # first checks if char is found in word from left side, then checks if looking from right side you reach the same location. If yes then it only appears once in word as question asks for.
            print(f"{char} appears in '{word}' at index {word.index(char)}")  # prints out the character, the word located in and the index position w/ suitable message
            numOfAppearances += 1  # num of appearances of single character found words

        elif -1 != word.find(char):
            print(f"{char} appears in '{word}' at index {word.index(char)} but also appears in other locations as well")  # prints out the character, the word located in and the index position w/ suitable message
            numOfAppearancesWMultiple += 1  # num of appearances of multiple characters found words
    print(f"{char} appears in {numOfAppearances} words in strList") if numOfAppearances != 1 else print(f"{char} appears in {numOfAppearances} word in strList")  # for singular / plural grammar.

    # This is extra for duplicate characters.
    if numOfAppearancesWMultiple > 0:  # if no duplicates were found, then don't print this.
        print(f"{char} appears in {numOfAppearancesWMultiple + numOfAppearances} word(s) where characters has 1 or more occurrences")  # prints out a message
