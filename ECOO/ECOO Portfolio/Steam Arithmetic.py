input_folder = 'E:\\ECOO\\Arithmetic\\Input\\DATA31.txt'
output_folder = 'E:\\ECOO\\Arithmetic\\Output\\DATA32.txt'


def cleaning(symbol, equation, place_holder):
    while True:
        equation2 = ''
        loop = False
        index = 0
        # print('Found You', equation_find)
        skips = 0
        cut_out = equation[0:]
        location = equation.find('*')
        # print('These are Cut Out: ', cut_out)
        for letter in cut_out:
            # print('This is the Letter: ', letter, skips)
            if letter == symbol:
                if loop is True:
                    equation2 = equation2 + letter
                loop = True
                continue
            if loop is True:

                if letter == '(':
                    skips = skips + 1
                    # print('skips', skips, letter, cut_out.index(letter))
                    index = index + 1
                    equation2 = equation2 + letter
                elif letter == ')':
                    skips = skips - 1
                    # print('skips', skips, letter, cut_out.index(letter))
                    index = index + 1
                    equation2 = equation2 + letter
                else:
                    index = index + 1
                    equation2 = equation2 + letter
                if skips == 0:
                    # print('Cut Out Number: ', index)
                    equation2 = equation2 + place_holder
                    loop = False
            else:
                equation2 = equation2 + letter
        # print('This is Equation2 : ', equation2)
        equation = equation2
        if '*' or '+' or '-' or '/' or '%' not in equation:
            break
    return equation


with open('%s' % input_folder, 'r') as txt, open('%s' % output_folder, 'w') as txt2:
    txt.readline()

    for i in txt:
        equation = ''
        c = 0
        ln = 0
        plus = 0
        i = i.replace('\n', '')
        i = i.replace(' ', '')
        i = i.replace('q', '/')
        i = i.replace('r', '%')
        # print(i)
        while True:
            try:
                l = i[c]
            except IndexError:
                break

            if '*' in l:
                plus = c
                if i[c + 1] != '(':

                    equation = equation + \
                               i.replace('*', 'm')[c + 1] + \
                               i.replace('*', 'm')[c] + \
                               i.replace('*', 'm')[c + 2]
                    c = c + 2
                else:
                    equation = equation + l
            elif '+' in l:
                if i[c + 1] != '(':
                    equation = equation + \
                               i.replace('+', 'a')[c + 1] + \
                               i.replace('+', 'a')[c] + \
                               i.replace('+', 'a')[c + 2]
                    c = c + 2
                else:
                    # print('Problem: ', l)
                    equation = equation + l
            elif '-' in l:
                if i[c + 1] != '(':
                    equation = equation + \
                               i.replace('-', 's')[c + 1] + \
                               i.replace('-', 's')[c] + \
                               i.replace('-', 's')[c + 2]
                    c = c + 2
                else:
                    # print('Problem: ', l)
                    equation = equation + l
            elif '/' in l:
                if i[c + 1] != '(':
                    equation = equation + \
                               i.replace('/', 'q')[c + 1] + \
                               i.replace('/', 'q')[c] + \
                               i.replace('/', 'q')[c + 2]
                    c = c + 2
                else:
                    # print('Problem: ', l)
                    equation = equation + l
            elif '%' in l:
                if i[c + 1] != '(':
                    equation = equation + \
                               i.replace('%', 'r')[c + 1] + \
                               i.replace('%', 'r')[c] + \
                               i.replace('%', 'r')[c + 2]
                    c = c + 2
                else:
                    # print('Problem: ', l)
                    equation = equation + l
            else:
                equation = equation + l
            # print(equation)
            c = c + 1
        cut_out = ''
        while True:
            if '+' in equation:
                equation = cleaning('+', equation, 'a')
            elif '*' in equation:
                equation = cleaning('*', equation, 'm')
            elif '-' in equation:
                equation = cleaning('-', equation, 's')
            elif '/' in equation:
                equation = cleaning('/', equation, 'q')
            elif '%' in equation:
                equation = cleaning('%', equation, 'r')
            else:
                break
            # print('Before: ', equation)

        equation = equation.replace('m', '*')
        equation = equation.replace('a', '+')
        equation = equation.replace('s', '-')
        equation = equation.replace('q', '//')
        equation = equation.replace('r', '%')
        equation = equation.replace("'", '')


        # print('After: ', equation)
        # float(equation)
        print(eval(equation))
        txt2.write('%s\n' % eval(equation))
