
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


def tobool(value):
    bool_accepted = {'valid': [True, 'True', '1', 1], 'invalid': [False, 'False', '0', 0]}
    if value in bool_accepted['valid']:
        return True
    elif value in bool_accepted['invalid']:
        return False


def bubble_sort(value):
    for x in range(0, len(value)):
        for y in range(0, len(value) - x - 1):
            if value[y] > value[y + 1]:
                hold = value[y]
                value[y] = value[y + 1]
                value[y + 1] = hold
    return value


def issorted(value, ):
    for i in range(len(value) - 1):
        if value[i] > value[i + 1]:
            return False
    else:
        return True


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


words = {
        0: ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine '],
        1: ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ',
            'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen '],
        2: ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety '],
        3: ['hundred '],
        4: {2: 'thousand ', 3: 'million ', 4: 'billion ', 5: 'trillion ', 6: 'quadrillion '}}


def number_to_word(n):
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