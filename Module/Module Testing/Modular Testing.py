# def num_to_eng(n):
#     words = {
#         0: ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine '],
#         1: ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ',
#             'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen '],
#         2: ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety '],
#         3: ['hundred '],
#         4: {2: 'thousand ', 3: 'million ', 4: 'billion ', 5: 'trillion ', 6: 'quadrillion '}}
#     a = list(str(n))
#     number_word = ''
#     pleb = []
#     levels = []
#     for i in reversed(a):
#         pleb.insert(0, i)
#         if len(pleb) == 3:
#             levels.insert(0, pleb)
#             pleb = []
#     if len(pleb) > 0:
#         levels.insert(0, pleb)
#     for position, bigger in enumerate(levels):
#         added_to, flip = False, 0
#         for num, i in enumerate(bigger):
#             i = int(i)
#             num_x = len(bigger) - num
#             if num_x == 3:
#                 if i == 0:
#                     continue
#                 else:
#                     number_word += words[0][i] + words[3][0]
#                     added_to = True
#             elif num_x == 2:
#                 if i == 1:
#                     flip = 1
#                 elif i > 1:
#                     number_word += words[2][i]
#                     added_to = True
#             elif num_x == 1 and flip + i > 0:
#                 number_word += words[0 + flip][i]
#                 flip = 0
#                 added_to = True
#         if position + 1 < len(levels) and added_to:
#             number_word += words[4][len(levels) - position]
#     if str(n).isdigit() and len(number_word) == 0:
#         return 'zero'
#     return number_word[:-1]
#
#
# print(repr(num_to_eng(1000)))
from Module.Modules import custom
# from logic import *
# import Tree
print(custom.fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(123))


def fibonacci(x, lis={}):
    if x in lis:
        return lis[x]
    if x <= 1:
        return 1
    xy = fibonacci(x-1) + fibonacci(x-2)
    lis.update({x: xy})
    return xy


fibonacci(10)
exit()
a = 50
b = 45
c = 50
d = 'a'
e = 0
f = 0
g = 1
# print(number_to_word(100020140342134))
# if xor(a == c, a == c):
#     print("Hello")
# else:
#     print("Not Hello")
# print(a == c, a == c)
# if nor(e == g, e == g):
#     print("Hi Man")
# else:
#     print('Hi Girl')
