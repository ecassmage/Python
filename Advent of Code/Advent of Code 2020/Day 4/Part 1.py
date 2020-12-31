import re
input_folder = 'E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 4\\input.txt'

array = []
valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
a = ''
c = 0
valid_passports = 0


def part_1(x):
    global valid_passports
    valid_passport = True
    for element in valid:
        if element not in x:
            valid_passport = False
            break
    if valid_passport:
        valid_passports += 1


with open("%s" % input_folder, 'r') as file:
    for line in file.readlines():
        if line == '\n':
            part_1(array)
            array = []
        else:
            array1 = re.findall(r'byr|iyr|eyr|hgt|hcl|ecl|pid', line)
            for i in array1:
                array.append(i)
part_1(array)
print("The Answer to Part 1 is: %d" % valid_passports)
