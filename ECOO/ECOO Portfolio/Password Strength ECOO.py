import re

input_folder = 'E:\\ECOO\\Password\\Input\\DATA21.txt'
output_folder = 'E:\\ECOO\\Password\\Output\\DATA22.txt'
passwords = []
# string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
# special_char = ['!', '@', '#', '$', '%', '^', '&', '*',
#                 '(', ')', '-', '_', '=', '+', '[', '{',
#                 ']', '}', "\%", '|', ';', ':', "'",
#                 '''"''', ',', '<', '.', '>', '/', '?', '`', '~']

with open('%s' % input_folder, 'r') as txt, open('%s' % output_folder, 'w') as txt2:
    txt.readline()
    for line in txt:
        line = line.replace('\n', '')
        passwords.append(line)
    for pw in passwords:

        need = ''
        pw2 = ''
        requirements = 0
        upper = False
        lower = False
        digits = False
        symbols = False
        length = True
        count_upper = 0
        count_lower = 0
        count_digit = 0
        count_invalid = 0
        upper_c = 0
        lower_c = 0
        digit_c = 0
        score = 0
        perma_cd = 0
        perma_cl = 0
        count_seqd = 0
        count_seql = 0
    # requirements
        if len(pw) < 8:
            length = False
        if any(c.isupper() for c in pw):
            requirements = requirements + 1
            upper = True
        if any(c.islower() for c in pw):
            requirements = requirements + 1
            lower = True
        if any(c.isdigit() for c in pw):
            requirements = requirements + 1
            digits = True
        if not all(c.isalnum() for c in pw):
            requirements = requirements + 1
            symbols = True
        if length is True:
            if requirements < 3:
                if upper is False:
                    need = need + 'upper\n'
                if lower is False:
                    need = need + 'lower\n'
                if digits is False:
                    need = need + 'digits\n'
                if symbols is False:
                    need = need + 'symbols\n'
            else:
                score = score + 10
                pass
        # print('First Score:', score)
        # score = 0
    # consecutive penalties
        for u in pw:
            if u.isupper():
                if lower_c >= 1:
                    score = score - (2 * (lower_c - 1))
                    lower_c = 0
                if digit_c >= 1:
                    score = score - (2 * (digit_c - 1))
                    digit_c = 0
                count_upper = count_upper + 1
                upper_c = upper_c + 1
            elif u.islower():
                if digit_c >= 1:
                    score = score - (2 * (digit_c - 1))
                    digit_c = 0
                if upper_c >= 1:
                    score = score - (2 * (upper_c - 1))
                    upper_c = 0
                count_lower = count_lower + 1
                lower_c = lower_c + 1
            elif u.isdigit():
                if lower_c >= 1:
                    score = score - (2 * (lower_c - 1))
                    lower_c = 0
                if upper_c >= 1:
                    score = score - (2 * (upper_c - 1))
                    upper_c = 0
                count_digit = count_digit + 1
                digit_c = digit_c + 1
            else:
                if lower_c >= 1:
                    score = score - (2 * (lower_c - 1))
                    lower_c = 0
                if upper_c >= 1:
                    score = score - (2 * (upper_c - 1))
                    upper_c = 0
                if digit_c >= 1:
                    score = score - (2 * (digit_c - 1))
                    digit_c = 0
        if lower_c >= 1:
            score = score - (2 * (lower_c - 1))
            lower_c = 0
        if upper_c >= 1:
            score = score - (2 * (upper_c - 1))
            upper_c = 0
        if digit_c >= 1:
            score = score - (2 * (digit_c - 1))
            digit_c = 0
        count_symbol = len(pw) - count_upper - count_lower - count_digit
        # print('Second Score:', score)
        # score = 0
    # Upper and Lower Case Amount
        if count_upper > 0:
            score = score + (len(pw) - count_upper) * 2
        if count_lower > 0:
            score = score + (len(pw) - count_lower) * 2
        # print('Third Score:', score)
        # score = 0
    # Digits and Symbols and Length
        score = score + (6 * count_symbol) + (len(pw) * 4)
        if pw.isdigit():
            pass
        else:
            score = score + (4 * count_digit)
        # print('Fourth Score:', score)
        # score = 0
        print('password: %s\n'
              'uppercase: %s\n'
              'lowercase: %s\n'
              'digits: %s\n'
              'symbols: %s\n' %
              (pw, count_upper, count_lower, count_digit, (len(pw) - count_upper - count_lower - count_digit)))
        # Middle Digits
        for x in range(1, len(pw) - 1):
            pw2 = pw2 + pw[x]
        for u in pw2:
            if u.isupper() or u.islower():
                count_invalid = count_invalid + 1
        score = score + (2 * (len(pw2) - count_invalid))
        # print('Fifth Score:', score)
        # score = 0
    # Only Digits / Letters
        if pw.isdigit():
            score = score - len(pw)
        if pw.isalpha():
            score = score - len(pw)
        # print('Sixth Score:', score)
        # score = 0
    # Sequential Digits
        for u in pw:
            if u.isalpha():
                if count_seql <= 0:
                    prev_ord = ord(u)
                    count_seql = 1
                    if count_seqd >= 1:
                        if count_seqd <= 2:
                            count_seqd = 0
                        else:
                            if perma_cd < count_seqd:
                                perma_cd = count_seqd
                            count_seqd = 0

                elif count_seql == 1:
                    if (ord(u) - prev_ord) == -1:
                        count_seql = count_seql + 1
                        p = False
                        prev_ord = ord(u)
                    elif (ord(u) - prev_ord) == 1:
                        count_seql = count_seql + 1
                        p = True
                        prev_ord = ord(u)
                    else:
                        prev_ord = ord(u)
                        if perma_cl < count_seql:
                            perma_cl = count_seql
                        count_seql = 1
                else:
                    if p is True:
                        if (ord(u) - prev_ord) == 1:
                            count_seql = count_seql + 1
                            p = True
                            prev_ord = ord(u)
                        else:
                            if perma_cl < count_seql:
                                perma_cl = count_seql
                                prev_ord = ord(u)
                                count_seql = 1
                    if p is False:
                        if (ord(u) - prev_ord) == -1:
                            count_seql = count_seql + 1
                            p = False
                            prev_ord = ord(u)
                        else:
                            if perma_cl < count_seql:
                                perma_cl = count_seql
                                prev_ord = ord(u)
                                count_seql = 1
            elif u.isdigit():
                if count_seqd <= 0:
                    prev_ord = ord(u)
                    count_seqd = 1
                    if count_seql >= 1:
                        if count_seql <= 2:
                            count_seql = 0
                        else:
                            if perma_cl < count_seql:
                                perma_cl = count_seql
                            count_seql = 0

                elif count_seqd == 1:
                    if (ord(u) - prev_ord) == -1:
                        count_seqd = count_seqd + 1
                        p = False
                        prev_ord = ord(u)
                    elif (ord(u) - prev_ord) == 1:
                        count_seqd = count_seqd + 1
                        p = True
                        prev_ord = ord(u)
                    else:
                        prev_ord = ord(u)
                        if perma_cd < count_seqd:
                            perma_cd = count_seqd
                        count_seqd = 1
                else:
                    if p is True:
                        if (ord(u) - prev_ord) == 1:
                            count_seqd = count_seqd + 1
                            p = True
                            prev_ord = ord(u)
                        else:
                            if perma_cd < count_seqd:
                                perma_cd = count_seqd
                                prev_ord = ord(u)
                                count_seqd = 1
                    if p is False:
                        if (ord(u) - prev_ord) == -1:
                            count_seqd = count_seqd + 1
                            p = False
                            prev_ord = ord(u)
                        else:
                            if perma_cd < count_seqd:
                                perma_cd = count_seqd
                                prev_ord = ord(u)
                                count_seqd = 1
        if perma_cl < count_seql:
            perma_cl = count_seql
        if perma_cd < count_seqd:
            perma_cd = count_seqd
        # print("\nPerma_cl: ", perma_cl)
        # print("Perma_cd: ", perma_cd)
        if perma_cl > 2:
            score = score - (3 * (perma_cl - 2))
        if perma_cd > 2:
            score = score - (3 * (perma_cd - 2))
        print(score)

        if score < 0:
            txt2.write('password: (%s), Very Weak (score = 0)\n' % pw)
        elif 0 <= score <= 20:
            txt2.write('password: (%s), Very Weak (score = %s)\n' % (pw, score))
        elif 21 <= score <= 40:
            txt2.write('password: (%s), Weak (score = %s)\n' % (pw, score))
        elif 41 <= score <= 60:
            txt2.write('password: (%s), Good (score = %s)\n' % (pw, score))
        elif 61 <= score <= 80:
            txt2.write('password: (%s), Strong (score = %s)\n' % (pw, score))
        elif 81 <= score <= 100:
            txt2.write('password: (%s), Very Strong (score = %s)\n' % (pw, score))
        elif score > 100:
            txt2.write('password: (%s), Very Strong (score = 100)\n' % pw)

txt.close(), txt2.close()