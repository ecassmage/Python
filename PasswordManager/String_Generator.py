import math
import key
import copy


class HashZeroException(Exception):
    def __init__(self, key_value, desired_ext):
        self.key_value = key_value
        self.desired_ext = desired_ext

    def __str__(self):
        return f"An exception was raised when the key: {self.key_value} was passed through\n" \
               f"Keys >= 1 and an integer"


def beginning_encrypt(word, lis, length):
    string_temp = ""
    for digit in str(len(word)):
        if lis.index(digit) == 0:
            string_temp += lis[-1]
        else:
            string_temp += lis[lis.index(digit) - 1]
    string_temp += ' '
    for digit in str(length):
        if lis.index(digit) == len(lis) - 1:
            string_temp += lis[0]
        else:
            string_temp += lis[lis.index(digit) + 1]
    string_temp += ' e'
    return string_temp


def unlock_encrypt(word, lis):
    string_temp = ""
    list_of_important_stuff = []
    direction = 0
    word = list(word)
    while True:
        char = word[0]
        if char == 'e':
            break
        elif char == ' ':
            list_of_important_stuff.append(string_temp)
            direction += 1
            string_temp = ''
        else:
            if direction % 2 == 0:
                if lis.index(char) == len(lis) - 1:
                    string_temp += lis[0]
                else:
                    string_temp += lis[lis.index(char) + 1]
            else:
                if lis.index(char) == 0:
                    string_temp += lis[-1]
                else:
                    string_temp += lis[lis.index(char) - 1]
        word.pop(0)
    word.pop(0)
    return list_of_important_stuff, ''.join(word)


def EV_encryption(word, skey=None, length=1000, short=False, encrypt=True):
    if skey is None:
        skey = len(word)
    if skey <= 0:
        raise HashZeroException(0, 0)
    if short is False:
        hashList = key.hash_key(skey)
    else:
        hashList = key.hash_key_short(skey)
    c = 1
    hash_string = ""
    temp_string = ""
    n = skey
    if encrypt:
        temp_string = beginning_encrypt(word, hashList, length)
        string_length = length
    else:
        list_of_stuff, word = unlock_encrypt(word, hashList)
        string_length = int(list_of_stuff[0])
        length = int(list_of_stuff[1])
    new_hashList = copy.copy(hashList)
    while len(hash_string) < string_length:
        for letter in word:
            new_hashList = key.hash_key(n, new_hashList)
            new_hashList = key.caesarCypher(n, new_hashList)
            n = abs(math.ceil(((((c * 1.2) - 1) ** 2 + 5) * c) / ((skey / int((list(str(c)))[0])) + 4))) + length
            n = math.floor(math.sqrt(n ** 4.1635)) - length
            while n >= len(hashList):
                big_divide = len(hashList)
                while big_divide < n:
                    big_divide *= 10
                if big_divide > n:
                    big_divide /= 10
                big_divide = math.floor(big_divide)
                if n > big_divide:
                    n -= big_divide
                else:
                    n -= len(hashList)
            if encrypt:
                hash_string += new_hashList[hashList.index(letter)]
                c += hashList.index(letter) + 1
            else:
                hash_string += hashList[new_hashList.index(letter)]
                c += hashList.index(hash_string[-1]) + 1
                if len(hash_string) >= string_length:
                    break
    if encrypt:
        return temp_string + hash_string
    else:
        return hash_string


#


"""
n = math.floor(math.sqrt((abs(math.ceil(((((c * 1.2) - 1) ** 2 + 5) * c) / ((hash_key / int((list(str(c)))[0])) + 4))) + length) ** 4.1635)) - length

"""