# # x = 1
# alphabet = []
# with open('E:\\ECOO\Alpha.txt', 'w') as Alpha:
#     # for code in range(ord('A'), ord('Z') + 1):
#     #     print(chr(code))
#     #     if x < 10:
#     #         Alpha.write("'%s': '0%s', " % (chr(code), x))
#     #     else:
#     #         Alpha.write("'%s': '%s', " % (chr(code), x))
#         # x = x + 1
#     alphabet.append(' ')
#     for code in range(ord('A'), ord('Z') + 1):
#         alphabet.append(chr(code))
#     alphabet.append(',')
#     alphabet.append('.')
#     alphabet.append('!')
#     alphabet.append('?')
#     print(alphabet)
#     for x in range(0, len(alphabet)):
#         if x < 10:
#             Alpha.write("'0%s': '%s', " % (x, alphabet[x]))
#         else:
#             Alpha.write("'%s': '%s', " % (x, alphabet[x]))

input_folder = 'E:\\ECOO\\Arithmetic\\Input\\DATA31.txt'

with open('%s' % input_folder, 'r') as txt:
    txt.readline()

    for i in txt:
        equation = ''
        c = 0
        ln = 0
        plus = 0
        i = i.replace('\n', '')
        t = i.replace(' ', '')

        # print(i)
        while True:
            try:
                l = t[c]
            except IndexError:
                break

            if '*' in l:
                if t[c + 1] != '(':
                    equation = equation + t[c + 1] + t[c] + t[c + 2]
                    c = c + 3
                else:
                    c = c + 1
            elif '+' in l:
                if t[c + 1] != '(':
                    equation = equation + t[c + 1] + t[c] + t[c + 2]
                    c = c + 3
                else:
                    c = c + 1
            elif '-' in l:
                if t[c + 1] != '(':
                    equation = equation + t[c + 1] + t[c] + t[c + 2]
                    c = c + 3
                else:
                    c = c + 1
            else:
                equation = equation + l
                c = c + 1
            # print(i[plus])
            print(equation)
