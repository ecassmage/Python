import random


def fullSet():
    suits = ['clubs', 'diamonds', 'spades', 'hearts']  # All the Suits of a deck of cards
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # All the Numbers of a deck of cards not adding jack - ace since that is really annoying to code in
    lis = []  # Empty List for the cards
    for i in suits:  # Generates a Set of all numbered cards
        for j in nums:  # Generates a Set of all numbered cards
            lis.append([j, f"'{i}'"])  # Yes I wanted '' in the strings. Sue Me
    random.shuffle(lis)  # Shuffles for Disorganization
    return lis  # Returns the Built List


def mergeSort(lis):
    # Efficient Sorting Algorithm of nlogn, bubble sort has n^2 which is much worse
    if len(lis) == 1:
        return lis  # if only 1 element is in list then just returns lis
    elif len(lis) == 2:
        return [min(lis), max(lis)]  # sets the min to the first position and max to the second position.
    else:
        lis1 = mergeSort(lis[:int(len(lis)/2)])  # Recursively Calls mergeSort for first half of split list
        lis2 = mergeSort(lis[int(len(lis)/2):])  # Recursively Calls mergeSort for second half of split list
        lis1Ptr = 0  # pointer for index position of lis1 when recombining them
        lis2Ptr = 0  # pointer for index position of lis2 when recombining them
        lis = []  # Empty the lis list of all its elements since the references are no longer needed.
        for i in range(len(lis1) + len(lis2)):  # for loop between 0 and len(lis1) + len(lis2)
            if lis1Ptr >= len(lis1):        # if all elements from lis1 have been used just add all the elements from lis2 to the end
                lis.extend(lis2[lis2Ptr:])  # if all elements from lis1 have been used just add all the elements from lis2 to the end
                break
            elif lis2Ptr >= len(lis2):      # if all elements from lis2 have been used just add all the elements from lis1 to the end
                lis.extend(lis1[lis1Ptr:])  # if all elements from lis2 have been used just add all the elements from lis1 to the end
                break
            else:
                if lis1[lis1Ptr][0] <= lis2[lis2Ptr][0]:  # if next element in lis1 is smaller or equal then the next element of lis2
                    lis.append(lis1[lis1Ptr])  # append the element from lis1 to lis
                    lis1Ptr += 1
                else:  # else if next element in lis2 is smaller then the next element of lis1
                    lis.append(lis2[lis2Ptr])  # append the element from lis2 to lis
                    lis2Ptr += 1
        return lis  # Return the Sorted list


if __name__ == '__main__':
    cards = fullSet()
    print(cards)
    # cards2 = mergeSort(cards)
    cards2 = sorted(cards, key=lambda x: int(x[0]))
    cards3 = mergeSort(cards)
    cards4 = sorted(cards)
    print(cards2)
    print(cards3)
    print(cards4)
