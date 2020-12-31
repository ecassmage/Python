import re
input_folder = 'input.txt'
part2 = 0

with open("%s" % input_folder, "r") as file:
    for line in file.readlines():
        num1, num2 = False, False
        nums, letter, password = re.findall(r'\d{1,3}', line), re.findall(r'\b[a-z]\b', line), re.findall(r'[a-z]{2,20}', line)
        password = list(password[0])
        if letter[0] == password[int(nums[0]) - 1]:
            num1 = True
        if letter[0] == password[int(nums[1]) - 1]:
            num2 = True
        if (num1 or num2) is True and (num1 != num2):
            part2 += 1

print("The Answer to Part 2 is: %d" % part2)