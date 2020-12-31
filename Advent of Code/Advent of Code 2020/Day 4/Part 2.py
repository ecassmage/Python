input_folder = 'E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 4\\input.txt'

array = []
a = ''
c = 0


def check_passport(x):
    global a
    global c
    element = 0
    cid = False
    ecl = False
    pid = False
    eyr = False
    hcl = False
    byr = False
    iyr = False
    hgt = False
    x.append(a)
    a = ''
    # print(array)
    for t in x:
        element = element + 1
        if t == 'cid':
            cid = True
        elif t == 'ecl':
            if x[element] == 'amb' or \
                    x[element] == 'blu' or \
                    x[element] == 'brn' or \
                    x[element] == 'gry' or \
                    x[element] == 'grn' or \
                    x[element] == 'hzl' or \
                    x[element] == 'oth':
                ecl = True
        elif t == 'pid':
            if len(x[element]) == 9 and x[element].isnumeric() is True:
                pid = True
        elif t == 'eyr':
            try:
                if 2020 <= int(x[element]) <= 2030:
                    eyr = True
            except ValueError:
                continue
        elif t == 'hcl':
            hc = list(x[element])
            hair_count = 0
            # print(hc)
            fail = False
            hash_tag = False
            alp_count = 0
            num_count = 0
            for hair in range(0, 7):
                if hc[0] == '#':
                    pass
                elif 0 <= int(hair) <= 9:
                    num_count = num_count + 1
                    if num_count > 3:
                        fail = True
                elif hair == 'a' or hair == 'b' or hair == 'c' or hair == 'd' or hair == 'e' or hair == 'f':
                    alp_count = alp_count + 1
                    if alp_count > 3:
                        fail = True
                        break
                else:
                    fail = True
                    break
                hair_count = hair_count + 1
            if hair_count == 7 and fail is False:
                hcl = True
            else:
                hcl = False

        elif t == 'byr':
            try:
                if 1920 <= int(x[element]) <= 2002:
                    byr = True
            except ValueError:
                continue
        elif t == 'iyr':
            try:
                if 2010 <= int(x[element]) <= 2020:
                    iyr = True
            except ValueError:
                continue

        elif t == 'hgt':
            height = []
            measure = []
            h = ''
            m = ''
            tt = list(x[element])
            for g in tt:
                if g.isnumeric() is True:
                    h = h + str(g)
                else:
                    m = m + str(g)
            height.append(h)
            measure.append(m)
            if measure[0] == 'cm':
                if 150 <= int(height[0]) <= 193:
                    hgt = True
            elif measure[0] == 'in':
                if 59 <= int(height[0]) <= 76:
                    hgt = True

    if ecl is True and pid is True and eyr is True and hcl is True and byr is True and iyr is True \
            and hgt is True:
        c = c + 1
    else:
        pass


with open("%s" % input_folder) as file:
    for i in file.readlines():
        x = i.strip(':')
        y = list(x)
        for j in y:
            if i == '\n':
                check_passport(array)
                array = []
            if j == ':' or j == ' ' or j == '\n':
                array.append(a)
                a = ''
            else:
                a = a + j
check_passport(array)

print("The Answer to Part 2 is: %d" % c)
