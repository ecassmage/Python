import re
import copy
from itertools import product
mask = []
mem = []
day_14 = []
full_binary = []
saved_mem = {}
with open("E:\\Advent\\Day 14.txt", 'r') as Day14:
    day14 = Day14.readlines()
    for d14 in day14:
        d14 = d14.replace('\n', '')
        day_14.append(d14)
for i in range(0, len(day_14)):
    if re.findall(r'mask', day_14[i]):
        cunt = list(day_14[i].replace('mask = ', ''))
        mask.append(list(day_14[i].replace('mask = ', '')))
    if re.findall(r'mem', day_14[i]):
        mem.append(day_14[i].replace('] =', '').replace('mem[', '').split(' '))
        try:
            if re.findall(r'mask', day_14[i + 1]):
                # print(mask)
                # print(mem)
                full_binary.append(mask)
                full_binary.append(mem)
                mask, mem = [], []
        except IndexError:
            # print(mask)
            # print(mem)
            full_binary.append(mask)
            full_binary.append(mem)
            mask, mem = [], []
for i in range(0, len(full_binary), 2):
    full_binary[i] = full_binary[i][0]
# print(saved_mem)
for i in range(1, len(full_binary), 2):
    for m in range(0, len(full_binary[i])):
        mask_binary = copy.deepcopy(full_binary[i-1])
        c = 0
        for j in full_binary[i - 1]:
            if j == 'X':
                c += 1
        combos = list(product(range(2), repeat=c))
        # combos.pop(-1)
        # combos.pop(0)
        # print(combos)
        # print(combos[0][1])
        mem_binary = list('{0:036b}'.format(int(full_binary[i][m][0])))
        # print(mem_binary)
        # print(mask_binary)
        result_binary = []
        for bit in range(0, len(mem_binary)):
            if mask_binary[bit] == '0':
                result_binary.append(mem_binary[bit])
            elif mask_binary[bit] == '1':
                result_binary.append(mask_binary[bit])
            elif mask_binary[bit] == 'X':
                result_binary.append('X')
        x_binary = []
        result_binary_save = copy.copy(result_binary)
        for reps in range(0, 2 ** c):
            position = 0
            stringed_binary = ''
            # print(result_binary)
            for bit in range(0, len(result_binary)):
                if result_binary[bit] == 'X':
                    result_binary[bit] = combos[reps][position]
                    stringed_binary = stringed_binary + str(combos[reps][position])
                    position += 1
                else:
                    stringed_binary = stringed_binary + result_binary[bit]
            # print(stringed_binary)
            x_binary.append(stringed_binary)
            result_binary = copy.copy(result_binary_save)
        for binaries in range(0, len(x_binary)):
            x_decimal = int(x_binary[binaries], 2)
            # print(x_decimal)
            # print(x_binary[binaries])
            # print(x_decimal)
            # print(x_decimal, full_binary[i][0][1])
            if x_decimal not in saved_mem:
                saved_mem.update({x_decimal: int(full_binary[i][m][1])})
            else:
                saved_mem.update({x_decimal: int(full_binary[i][m][1])})
        # print(saved_mem)
Part_2_answer = 0
for i in saved_mem:
    Part_2_answer += saved_mem[i]

print("The answer to part 2 is: %d" % Part_2_answer)
# print(full_binary)