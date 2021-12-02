if __name__ == '__main__':
    cards = [[8, 'hearts'], [6, 'clubs'], [3, 'spades'], [5, 'clubs'], [10, 'diamonds'], [4, 'spades'], [2, 'hearts'], [7, 'spades']]  # List of Cards

    print(f"This is the list of cards pre sort: {cards}")  # Prints the list pre sort
    for i in range(len(cards)):  # First for loop keeps track of how many iterations bubble sort has gone through so far
        for j in range(0, len(cards) - i - 1):  # ptr for where currently at in the list
            if cards[j][0] > cards[j+1][0]:  # checks if card[j] > next card and if so will initiate swap protocols
                temp = cards[j]  # temporarily holds the reference for cards[j] so that it won't be lost to garbage collection on next line
                cards[j] = cards[j+1]  # sets cards[j] to point to cards[j+1]
                cards[j+1] = temp  # sets cards[j+1] to point to temp which is storing the old value of cards[j]
    print(f"This is the list of cards post sort: {cards}")  # Prints the list post sort

    suit = input("Input clubs, diamond, spades, or hearts please to claim a number: ")  # takes input of clubs, diamond, spades and hearts. Doesn't account for wrong input since lab said didn't matter.
    comma = False  # for formatting whether a comma should be printed or not
    print("The number(s) of that suit we could find are: ", end='')  # Just some flavor text for the outputted number
    for integer, word in cards:  # takes each list inside the cards list and splits it between integer: element[0] and word: element[1]
        if word == suit:  # if the suit (word: suit) equals the inputted suit then do what is in here.
            if comma:  # formatting for nice commas
                print(", ", end='')  # prints out a comma end='' removes the '\n' outputted in print so next print will be on same line
            else:
                comma = True  # sets comma to True, this is so that no comma will appear after the last number.
            print(integer, end='')  # prints the integer for the suit
    if not comma:  # if comma is still False then that means the inputted suit wasn't found and therefore this will tell you that a typo probably occurred during the input phase.
        print(f"N/A, {suit} is not recognized")  # Text to state that the inputted suit is not recognized.
    else:
        print()  # this will print a '\n' at the end of the process so as to make up for the missing '\n' in program
