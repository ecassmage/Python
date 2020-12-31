import re
nums = []
called = {}
c = 1
called_str, called_num = '', 0
call_to_add = {}


def numbers(x, y, z):
    difference = 0

    if z in y:
        last = int(y[z])
        difference = x - last
    # print("Hello: %d: %d: %s: %s" % (difference, x, y, z))
    return difference


with open('E:\\Advent\\Day 15.txt', 'r') as Day15:
    current = ''
    day15 = Day15.readlines()
    for i in day15:
        nums = re.findall(r'[0-9]{1,3}', i)
    for i in range(len(nums) - 1):
        called.update({str(nums[i]): c})
        # print(called)
        current = nums[i + 1]
        c += 1

while c <= 30000000:
    called_str = current

    called_num = c
    returned = numbers(c, called, current)
    current = str(returned)
    if str(called_str) not in called:
        called.update({str(called_str): called_num})
        # called.append(str(called_str))
        # called.append(called_num)
    else:
        called.update({called_str: called_num})
    c += 1
    if c % 5000000 == 0:
        print("We are still running just be patient...")
# print(called)
# print(called_num)
print("The Answer to Part 2 is: %s" % called_str)