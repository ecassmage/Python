c = 0
preamble = []
amble = []
with open("E:\\Advent\\Day 9.txt", 'r') as Day9:
    Day9.readline()
    for i in Day9:
        i = i.replace(' ', '')
        i = i.replace('\n', '')
        if c < 5:
            preamble.append(int(i))
        amble.append(int(i))
        c = c + 1
amp = False
print(amble)
jj = 0
mm = 0
i_carry = 0
i_amble_carry = 0
for i in range(25, len(amble)):
    for j in range(i - 25, i - 1):
        jj = amble[j]
        for m in range(i - 24, i):
            mm = amble[m]
            if amble[i] == amble[j] + amble[m]:
                amp = True
                break
        if amp:
            break
    if amp is False:
        print("The Answer to Part 1 is: %d" % amble[i])
        i_carry = i
        i_amble_carry = amble[i]
        break
    else:
        amp = False
carry = 0
carry_list = []
good = False
for i in range(0, i_carry):
    carry = 0
    carry_list = []
    for j in range(i, i_carry):
        carry = carry + amble[j]
        carry_list.append(amble[j])
        if carry == i_amble_carry:
            good = True
            break
        elif carry > i_amble_carry:
            break
    if good is True:
        break
addition = 0
for i in range(0, len(carry_list)):
    addition = addition + carry_list[i]
# print(addition)
large = 0
small = carry_list[0]
for i in range(0, len(carry_list)):
    if carry_list[i] > large:
        large = carry_list[i]
    elif carry_list[i] < small:
        small = carry_list[i]
# print("Large: %d\nSmall: %d\nTogether: %d" % (large, small, large + small))
print("The Answer to Part 2 is: %d" % (int(large) + int(small)))