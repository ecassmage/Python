import re
import math
import copy
bus = ''
time = 0
with open("E:\\Advent\\Day 13.txt", 'r') as Day13:
    day13 = Day13.readlines()
    departure, num = day13[0], re.findall(r'[0-9]{1,4}', day13[1])
    full_list = re.findall(r'(x|[0-9]{1,4})', day13[1])
    # print(full_list)
    # print(num)
    # print(departure)
    departure = int(departure)
    difference = departure
for i in range(0, len(num)):
    finish = math.ceil(int(departure) / int(num[i]))
    if ((finish * int(num[i])) - int(departure)) <= difference:
        difference = (finish * int(num[i])) - int(departure)
        time = finish * int(num[i])
        bus = num[i]
# print("We got time of: %d\nDeparture time at: %d\nand bus of: %s" % (difference, time, bus))
t, c = 0, 0
line_up = True
b = []
N = []
x = []
complete = []
multiple = 1
completion = 0
copy_list = copy.copy(num)
copy_list[0] = 0
# print(copy_list)
# for i in range(1, len(num)):
#     t1 = int(num[0])
#     c = 1
#     t2 = t1
#     print(int(full_list.index(copy_list[i])))
#     while True:
#         if t1 % int(copy_list[i]) == int(full_list.index(copy_list[i])):
#             copy_list[i] = c
#             break
#         else:
#             t1 = t1 + t2
#             c = c + 1
# print(copy_list)
# num.pop(0)
for i in range(0, len(num)):
    multiple = multiple * int(num[i])
for i in range(0, len(num)):
    # b.append(int(copy_list[i]))
    b.append(int(full_list.index(num[i])))
    N.append(multiple / int(num[i]))
    x1 = N[i] % int(num[i])
    # print(x1)
    c = 1
    x2 = x1
    while True:
        if x1 % int(num[i]) == 1:
            x.append(c)
            break
        else:
            x1 = x1 + x2
            c = c + 1
    complete.append(float(b[i] * N[i] * x[i]))
# print(b)
# print(N)
# print(num)
# print(x)
# print(complete)
# print(multiple)
for i in range(len(complete)):
    completion = completion + float(complete[i])
# print(completion)
print("The Answer to Part 2 is: %d" % (int(multiple) - (int(completion) % int(multiple))))
