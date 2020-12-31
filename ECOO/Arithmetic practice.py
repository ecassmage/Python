input_folder = 'E:\\ECOO\\Arithmetic\\Input\\DATA31.txt'

with open('%s' % input_folder, 'r') as txt:
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
                    # skips = 1
                    equation = equation + l
                    # cut_out = i[c + 2:]
                    # print('cut out: ', cut_out)
                    # for x in cut_out:
                    #     if skips == 0:
                    #         print(cut_out.index(x))
                    #         break
                    #     print('x: ', x)
                    #     if x == '(':
                    #         skips = skips + 1
                    #     elif x == ')':
                    #         skips = skips - 1
                    #
                    #     print('skips: ', skips)
                    # print('Problem: ', l)
                    # print('Skip number: ', x)
                    # print(i[cut_out.index(x) + c])
            elif '+' in l:
                if i[c + 1] != '(':
                    equation = equation + \
                               i.replace('+', 'a')[c + 1] + \
                               i.replace('+', 'a')[c] + \
                               i.replace('+', 'a')[c + 2]
                    c = c + 2
                else:
                    print('Problem: ', l)
                    equation = equation + l
            elif '-' in l:
                if i[c + 1] != '(':
                    equation = equation + \
                               i.replace('-', 's')[c + 1] + \
                               i.replace('-', 's')[c] + \
                               i.replace('-', 's')[c + 2]
                    c = c + 2
                else:
                    print('Problem: ', l)
                    equation = equation + l
            elif '/' in l:
                if i[c + 1] != '(':
                    equation = equation + \
                               i.replace('/', 'q')[c + 1] + \
                               i.replace('/', 'q')[c] + \
                               i.replace('/', 'q')[c + 2]
                    c = c + 2
                else:
                    print('Problem: ', l)
                    equation = equation + l
            elif '%' in l:
                if i[c + 1] != '(':
                    equation = equation + \
                               i.replace('%', 'r')[c + 1] + \
                               i.replace('%', 'r')[c] + \
                               i.replace('%', 'r')[c + 2]
                    c = c + 2
                else:
                    print('Problem: ', l)
                    equation = equation + l
            else:
                equation = equation + l
            print(equation)
            c = c + 1
        cut_out = ''

        while True:
            equation2 = ''
            loop = False
            index = 0
            # if '*' in equation:
            equation_find = equation.find('*')

            # print('Found You', equation_find)
            skips = 0
            cut_out = equation[0:]
            location = equation.find('*')
            print('These are Cut Out: ', cut_out)
            for letter in cut_out:
                # print('This is the Letter: ', letter, skips)
                if letter == '*':
                    if loop is True:
                        equation2 = equation2 + letter
                    loop = True
                    continue
                elif letter == '+':
                    if loop is True:
                        equation2 = equation2 + letter
                        continue
                    loop = True
                if loop is True:

                    if letter == '(':
                        skips = skips + 1
                        print('skips', skips, letter, cut_out.index(letter))
                        index = index + 1
                        equation2 = equation2 + letter
                    elif letter == ')':
                        skips = skips - 1
                        print('skips', skips, letter, cut_out.index(letter))
                        index = index + 1
                        equation2 = equation2 + letter
                    else:
                        index = index + 1
                        equation2 = equation2 + letter
                    if skips == 0:
                        print('Cut Out Number: ', index)
                        equation2 = equation2 + 'm'
                        loop = False
                        # equation = equation.replace('*', 'm')
                else:
                    equation2 = equation2 + letter

                equation = equation2

            # if '+' in equation:
            #     equation_find = equation.find('*')
            #
            #     # print('Found You', equation_find)
            #     skips = 0
            #     cut_out = equation[0:]
            #     location = equation.find('*')
            #     print('These are Cut Out: ', cut_out)
            #     for letter in cut_out:
            #         # print('This is the Letter: ', letter, skips)
            #         if letter == '*':
            #             if loop is True:
            #                 equation2 = equation2 + letter
            #             loop = True
            #             continue
            #         elif letter == '+':
            #             if loop is True:
            #                 equation2 = equation2 + letter
            #             loop = True
            #         if loop is True:
            #
            #             if letter == '(':
            #                 skips = skips + 1
            #                 print('skips', skips, letter, cut_out.index(letter))
            #                 index = index + 1
            #                 equation2 = equation2 + letter
            #             elif letter == ')':
            #                 skips = skips - 1
            #                 print('skips', skips, letter, cut_out.index(letter))
            #                 index = index + 1
            #                 equation2 = equation2 + letter
            #             else:
            #                 index = index + 1
            #                 equation2 = equation2 + letter
            #             if skips == 0:
            #                 print('Cut Out Number: ', index)
            #                 equation2 = equation2 + 'm'
            #                 loop = False
            #                 # equation = equation.replace('*', 'm')

                print('This is Equation2: ', equation2)
            if '*' not in equation2:
                break
            if ('*' or '+' or '-' or '/' or '%') not in equation:
                break

        print(equation)
        # if '*' in loop:
        #     skips = 1
        #     cut_out = equation[2:]
        #     print('cut out: ', cut_out)
        #     for x in cut_out:
        #         if skips == 0:
        #             print('Cut Out Number: ', cut_out.index(x))
        #             break
        #         print('x: ', x)
        #         if x == '(':
        #             skips = skips + 1
        #         elif x == ')':
        #             skips = skips - 1
