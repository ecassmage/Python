from math import ceil, sqrt

public_key, table = [], {}


def loop_size(x):
    c = 0
    while True:
        y = pow(7, c) % 20201227
        if y == x:
            return y
        c += 1


for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 25\\input.txt').readlines():
    public_key.append(int(line.replace('\n', '')))
print(public_key)
# loop_size_key = loop_size(i)
# print(loop_size_key)
m = ceil(sqrt(20201227))
for j in range(m):
    table.update({pow(7, j, 20201227): j})
inv = pow(7, (20201227 - 2) * m, 20201227)
give_back = 0
print(public_key[0], m, table, inv, give_back)
for j in range(m):
    y = (public_key[0] * pow(inv, j, 20201227)) % 20201227
    if y in table:
        give_back = j * m + table[y]
        break
print(give_back)
part_1 = pow(public_key[1], give_back, 20201227)
print("The Answer to Part 1 is: %d" % part_1)