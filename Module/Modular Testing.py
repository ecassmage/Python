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
import custom

print(custom.number_to_word(100020140342134))