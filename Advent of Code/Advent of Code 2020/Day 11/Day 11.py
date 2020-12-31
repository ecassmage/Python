import copy
seats, seats1, carry_seats = [], [], []
bad = []
with open("E:\\Advent\\Day 11.txt", 'r') as Day11:
    Day11.readline()
    for i in Day11:
        i = i.replace('L', '#')
        i = i.replace('\n', '')
        x = list(i)
        seats.append(x)
carry_seats = copy.deepcopy(seats)
seats1 = copy.deepcopy(seats)
# for i in range(0, len(seats)):
    # print(seats1[i])
# print('\n')


while True:
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            bad = []
            c, l, lu, u, ru, r, rd, d, ld = seats[i][j], '', '', '', '', '', '', '', ''
            if c == '.':
                continue
            if i >= 1:
                u = seats[i - 1][j]
                bad.append(u)
                if j >= 1:
                    lu = seats[i - 1][j - 1]
                    bad.append(lu)
                if j <= len(seats[i]) - 2:
                    ru = seats[i - 1][j + 1]
                    bad.append(ru)
            if j >= 1:
                l = seats[i][j - 1]
                bad.append(l)
            if j <= len(seats[i]) - 2:
                r = seats[i][j + 1]
                bad.append(r)
            if i <= len(seats) - 2:
                d = seats[i + 1][j]
                bad.append(d)
                if j >= 1:
                    ld = seats[i + 1][j - 1]
                    bad.append(ld)
                if j <= len(seats[i]) - 2:
                    rd = seats[i + 1][j + 1]
                    bad.append(rd)

            # print("%s" % bad)
            if c == '#':

                count = 0
                for hash in bad:
                    if hash == '#':
                        count = count + 1
                    if count >= 4:
                        seats1[i][j] = 'L'

                        break

            elif c == 'L':
                count = 0
                empty = True
                for hash in bad:
                    if hash == '#':
                        empty = False
                        break
                if empty is True:
                    seats1[i][j] = '#'

    if seats == seats1:
        # print("BITCH")
        break
    else:
        # print("\n")
        # for i in range(0, len(seats)):
        #     print(seats1[i])
        # print('\n')
        # print("Print 1: %s" % seats[1])
        # print("Print 2: %s" % seats1[1])
        seats = copy.deepcopy(seats1)
        # for i in range(len(seats)):
        #     print(seats[i])
        # print('\n')

answer = 0
for i in range(len(seats)):
    for j in range(len(seats[i])):
        if seats[i][j] == '#':
            answer = answer + 1
print("Part 1 Answer: %d" % answer)

# for i in carry_seats:
#     print(i)
# print('\n')
seats = copy.deepcopy(carry_seats)
seats1 = copy.deepcopy(carry_seats)
height = len(seats)
width = len(seats[0])
while True:
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            center = seats[i][j]
            if center == '.':
                continue
            ul_dr_u = ''
            ul_dr_d = ''
            ur_dl_u = ''
            ur_dl_d = ''
            u_d_u = ''
            u_d_d = ''
            l_r_l = ''
            l_r_r = ''
            bad = []

            for UL_DR in range(1, i + 1):
                try:
                    if (0 <= i - UL_DR < i) and (0 <= j - UL_DR < j):
                        if seats[i - UL_DR][j - UL_DR] == 'L' or seats[i - UL_DR][j - UL_DR] == '#':
                            ul_dr_u = seats[i - UL_DR][j - UL_DR]
                            # print("Printed1: %s" % UL_DR)
                            bad.append(ul_dr_u)
                            break
                except IndexError:
                    break
            for UL_DR in range(0, height - i):
                try:
                    if (i < i + UL_DR <= height) and (j < j + UL_DR <= width):
                        if seats[i + UL_DR][j + UL_DR] == 'L' or seats[i + UL_DR][j + UL_DR] == '#':
                            ul_dr_d = seats[i + UL_DR][j + UL_DR]
                            bad.append(ul_dr_d)
                            # print("Printed2: %s" % UL_DR)
                            break
                except IndexError:
                    break

            for UR_DL in range(1, i + 1):
                try:
                    if (0 <= i - UR_DL < i) and (j < j + UR_DL <= width):
                        if seats[i - UR_DL][j + UR_DL] == 'L' or seats[i - UR_DL][j + UR_DL] == '#':
                            ul_dr_u = seats[i - UR_DL][j + UR_DL]
                            # print("Printed3: %s" % UR_DL)
                            bad.append(ul_dr_u)
                            break
                except IndexError:
                    break
            for UR_DL in range(1, j + 1):
                try:
                    if (i < i + UR_DL <= height) and (0 <= j - UR_DL < j):
                        if seats[i + UR_DL][j - UR_DL] == 'L' or seats[i + UR_DL][j - UR_DL] == '#':
                            ul_dr_d = seats[i + UR_DL][j - UR_DL]
                            # print("Printed4: %s" % UR_DL)
                            bad.append(ul_dr_d)
                            break
                except IndexError:
                    # print("SHHIITIIT")
                    break

            for U_D in range(1, i + 1):
                if (0 <= i - U_D < i) and (j == j):
                    if seats[i - U_D][j] == 'L' or seats[i - U_D][j] == '#':
                        u_d_u = seats[i - U_D][j]
                        # print("Printed5: %s" % U_D)
                        bad.append(u_d_u)
                        break
            for U_D in range(1, height - i):
                if (i < i + U_D <= height) and (j == j):
                    if seats[i + U_D][j] == 'L' or seats[i + U_D][j] == '#':
                        u_d_d = seats[i + U_D][j]
                        # print("Printed6: %s" % U_D)
                        bad.append(u_d_d)
                        break

            for L_R in range(1, j + 1):
                if (i == i) and (0 <= j - L_R < j):
                    if seats[i][j - L_R] == 'L' or seats[i][j - L_R] == '#':
                        l_r_l = seats[i][j - L_R]
                        # print("Printed7: %s" % L_R)
                        bad.append(l_r_l)
                        break
            for L_R in range(1, width - j):
                if (i == i) and (j < j + L_R <= width):
                    if seats[i][j + L_R] == 'L' or seats[i][j + L_R] == '#':
                        l_r_r = seats[i][j + L_R]
                        # print("Printed8: %s" % L_R)
                        bad.append(l_r_r)
                        break
            # print("%s" % bad)
            if center == '#':
                count = 0
                for hash in bad:
                    if hash == '#':
                        count = count + 1
                    if count >= 5:
                        seats1[i][j] = 'L'

                        break

            elif center == 'L':
                count = 0
                empty = True
                for hash in bad:
                    if hash == '#':
                        empty = False
                        break
                if empty is True:
                    seats1[i][j] = '#'
    if seats == seats1:
        # print("BITCH")
        # for lss in seats1:
            # print(lss)
        break
    else:
        # print("\n")
        # for lss in seats1:
        #     print(lss)
        # print("\n")
        # for i in range(0, len(seats)):
        #     print(seats1[i])
        # print('\n')
        # print("Print 1: %s" % seats[1])
        # print("Print 2: %s" % seats1[1])
        seats = copy.deepcopy(seats1)
        # for i in range(len(seats)):
        #     print(seats[i])
        # print('\n')

answer = 0
for i in range(len(seats)):
    for j in range(len(seats[i])):
        if seats[i][j] == '#':
            answer = answer + 1
print("Part 2 Answer: %d" % answer)