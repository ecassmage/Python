"""This is My custom Module which is just a centralized module for any function I decide to make at any point and think
it might be useful in the future."""

"""This will check if the float is a float or not.
float is defined by the programmer as 1.5 or 1.0, anything with a single . and at least
a non float is defined by the programmer as anything else
ie. 1, '1', """


def isfloat(value):
    try:
        if float(value) and str(value).find('.') == 1:
            return True
        else:
            return False
    except ValueError:
        return False


"""isbool is a function for checking whether a value can be boolean or not"""


def isbool(value):
    bool_accepted = [True, False, 'True', 'False', '1', '0', 1, 0]
    if value in bool_accepted:
        return True
    else:
        return False


"""tobool will change certain inputs to boolean counterparts, common things recognised as boolean values"""


def tobool(value):
    bool_accepted = {'valid': [True, 'True', 'true', '1', 1, 'T', 't'],
                     'invalid': [False, 'False', 'false', '0', 0, 'F', 'f']}
    if value in bool_accepted['valid']:
        return True
    elif value in bool_accepted['invalid']:
        return False


"""Bubble Sort to sort like a bubble or something. If You don't know bubble sort you shouldn't be using it."""


def bubble_sort(value):
    for x in range(0, len(value)):
        for y in range(0, len(value) - x - 1):
            if value[y] > value[y + 1]:
                hold = value[y]
                value[y] = value[y + 1]
                value[y + 1] = hold
    return value


"""to check if it is sorted smallest to largest."""


def issorted(value, ):
    for i in range(len(value) - 1):
        if value[i] > value[i + 1]:
            return False
    else:
        return True


"""Famous interview question make all numbers divisible by three as Fizz and any number divisible by 5 as Buzz
if both have both words count and if none then just have the number."""


def fizzbuzz(value):
    for i in range(value + 1):
        if i % 3 == 0:
            print('fizz', end='')
        if i % 5 == 0:
            print('buzz', end='')
        if i % 3 != 0 and i % 5 != 0:
            print(i, end='')
        print('')
    return


"""Josephus question of killing to the right of you how do you be the last one standing."""


def josephus(value):
    x = 0
    while True:
        if 2 ** x > value:
            x = 2 ** (x - 1)
            break
        else:
            x += 1
    z = 1
    for _ in range(value - x):
        z += 2
    return z


def fibonacci(x, lis={}):
    if x in lis:
        return lis[x]
    if x <= 1:
        return 1
    xy = fibonacci(x-1) + fibonacci(x-2)
    lis.update({x: xy})
    return xy


"""This is a number to word generator that will convert any 
number given to it between 0 and 1 less then a quintillion
This can be increased simply by adding more levels to the 
4th level of the words dictionary and it will immediately take
effect to increase the limit. This can pull in both strings 
and integers but not decimals so floats are not okay.
Largest Current Number 999,999,999,999,999,999"""
words = {
        0: ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine '],
        1: ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ',
            'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen '],
        2: ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety '],
        3: ['hundred '],
        4: {2: 'thousand ', 3: 'million ', 4: 'billion ', 5: 'trillion ', 6: 'quadrillion '}}


def number_to_word(n, other=False):
    try:
        a = list(str(n))
        number_word = ''
        pleb = []
        levels = []
        for i in reversed(a):
            pleb.insert(0, i)
            if len(pleb) == 3:
                levels.insert(0, pleb)
                pleb = []
        if len(pleb) > 0:
            levels.insert(0, pleb)
            pleb = []
        for position, bigger in enumerate(levels):
            added_to, flip = False, 0
            for num, i in enumerate(bigger):
                i = int(i)
                num_x = len(bigger) - num
                if num_x == 3:
                    if i == 0:
                        continue
                    else:
                        number_word += words[0][i] + words[3][0]
                        added_to = True
                elif num_x == 2:
                    if i == 1:
                        flip = 1
                    elif i > 1:
                        number_word += words[2][i]
                        added_to = True
                elif num_x == 1 and flip + i > 0:
                    number_word += words[0 + flip][i]
                    flip = 0
                    added_to = True
            if position + 1 < len(levels) and added_to:
                number_word += words[4][len(levels) - position]
        if str(n).isdigit() and len(number_word) == 0:
            return 'zero'
        return number_word[:-1]
    except ValueError:
        if other:
            return False
        else:
            raise ValueError(f"{type(n)} is not a proper data type to input, input needs to be (int) or (str)")
    except KeyError:
        if other:
            return False
        else:
            raise KeyError(f"{n} is too large and is therefore not capable of being converted.")


def inputf(x, y=None, special=False):
    def failure():
        print(f"{type(z)} is not the desired data type {y}")

    true = ['True', 'true', '1', 't', 'T', True]
    false = ['False', 'false', '0', 'f', 'F', False]
    while True:
        z = input(x)
        if y is None:
            return z
        elif y == int:
            try:
                z = int(z)
            except ValueError:
                failure()
                continue
            return z
        elif y is bool and (z in true or z in false):
            if special:
                if z in true:
                    return True
                else:
                    return False
            return z
        elif y == str:
            if special:
                try:
                    int(z)
                    failure()
                except ValueError:
                    return z
            else:
                return z
        else:
            failure()











