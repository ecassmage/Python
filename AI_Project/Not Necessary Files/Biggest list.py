import re
list_of_nums = open('Not Necessary Files/input')
list_keep = []
for i in list_of_nums:
    line = re.findall(r'assert\(choose\((\d+), (\d+)\) == (\d+)\);', i)
    list_keep.append(line)

largest_num = 0
largest_n, largest_m = 0, 0
for lis in list_keep:
    # print(f"({lis[0][0]}, {lis[0][1]}) == {lis[0][2]}")
    if int(lis[0][2]) > int(largest_num):
        largest_num = int(lis[0][2])
        largest_n = int(lis[0][0])
        largest_m = int(lis[0][1])
c = 0
for i in range(41):
    c += i
print(c)
max_n = 40
all_combos = []
for n in range(max_n):
    lis = [i for i in range(n)]
    for m in range(n + 1):
        all_combos.append(tuple((lis, m)))
print(len(all_combos))
print(f"Largest n value is: {largest_n}\nLargest m value is: {largest_m}\nLargest List is: {largest_num}")

singy = {}
for i in list_keep:
    if int(i[0][0]) not in singy:
        singy.update({int(i[0][0]): [int(i[0][1])]})
    else:
        temp = singy[int(i[0][0])]
        temp.append(int(i[0][1]))
for i in singy:
    singy[i] = sorted(singy[i])
# singy = sorted(dict(singy))
for i in range(len(singy)):
    print(f"Number: {i} has: {singy[i]} Totalling: {len(singy[i])}")
