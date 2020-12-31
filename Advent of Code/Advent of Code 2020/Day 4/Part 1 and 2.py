import re
input_folder = 'E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 4\\input.txt'

array, strong_array = [], []
valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
a = ''
c = 0
part_1, part_2 = 0, 0


def everything_is_registered(x, y):
    global part_1
    valid_passport = True
    for valid_work in valid:
        if valid_work not in y:
            valid_passport = False
            break
    if valid_passport:
        part_1 += 1
        if len(x) == len(y):
            check_passport(x, y)


def check_passport(x, y):
    global part_2
    if len(x) != 7:
        return
    for y_element in range(0, len(y)):
        if y[y_element] == 'byr':
            if 1920 <= int(x[y_element]) <= 2002:
                pass
            else:
                return
        if y[y_element] == 'iyr':
            if 2010 <= int(x[y_element]) <= 2020:
                pass
            else:
                return
        elif y[y_element] == 'eyr':
            if 2020 <= int(x[y_element]) <= 2030:
                pass
            else:
                return
        elif y[y_element] == 'hgt':
            if 150 <= int(x[y_element]) <= 193 or 59 <= int(x[y_element]) <= 76:
                pass
            else:
                return
        elif y[y_element] == 'hcl' or y[y_element] == 'ecl' or y[y_element] == 'pid':
            continue
    part_2 += 1


with open("%s" % input_folder, 'r') as file:
    for line in file.readlines():
        if line == '\n':
            everything_is_registered(strong_array, array)
            array, strong_array = [], []
        else:
            array1 = re.findall(r'(byr|iyr|eyr|hgt|hcl|ecl|pid)', line)
            array2 = re.findall(r'byr:(\d{4})|iyr:(\d{4})|eyr:(\d{4})|hgt:(\d{3})cm|hgt:(\d{2})in|hcl:#([0-9a-f]{6})'
                                r'|ecl:(amb|blu|brn|gry|grn|hzl|oth)|pid:([0-9]{9})', line)
            [strong_array.append(j) for i in array2 for j in i if j != '']
            [array.append(i) for i in array1]
    file.close()
strong_array = []
everything_is_registered(strong_array, array)

print("The Answer to Part 1 is: %d" % part_1)
print("The Answer to Part 2 is: %d" % part_2)
