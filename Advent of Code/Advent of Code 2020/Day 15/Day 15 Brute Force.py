import re
nums = []
called = []
c = 1
called_str, called_num = '', 0


def numbers(x, y, z):
    difference = 0
    # print("Hello: %d: %d: %s: %s" % (difference, x, y, z))
    if z in y:
        last = int(y[y.index(str(z)) + 1])
        difference = x - last
    return difference


with open('E:\\Advent\\Day 15.txt', 'r') as Day15:
    current = ''
    day15 = Day15.readlines()
    for i in day15:
        nums = re.findall(r'[0-9]{1,3}', i)
    for i in range(len(nums) - 1):
        called.append(str(nums[i]))
        called.append(c)
        print(called)
        current = nums[i + 1]
        c += 1

while c <= 30000000:
    called_str = current

    called_num = c
    returned = numbers(c, called, current)
    current = str(returned)
    if str(called_str) not in called:
        called.append(str(called_str))
        called.append(called_num)
    else:
        called[called.index(called_str) + 1] = called_num
    c += 1
    if c % 30000 == 0:
        print(c)
print(called)
print(called_num)
print(called_str)