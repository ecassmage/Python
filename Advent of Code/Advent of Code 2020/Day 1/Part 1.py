numbers = []
day1 = open('E:\\Github\\Advent of Code\\Advent of Code 2020\\Day 1\\input.txt')
for line in day1.readlines():
    numbers.append(int(line.replace('\n', '')))

[print("The Answer to Part 1 is: %d" % (numbers[i] * numbers[j])) for i in range(0, len(numbers) - 1)
 for j in range(i + 1, len(numbers)) if numbers[i] + numbers[j] == 2020]
