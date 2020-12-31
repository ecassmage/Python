numbers = []
day1 = open('input.txt')
for line in day1.readlines():
    numbers.append(int(line.replace('\n', '')))

[print("The Answer to Part 2 is: %d" % (numbers[i] * numbers[j] * numbers[m]))
 for i in range(0, len(numbers)-2) for j in range(i+1, len(numbers)-1)
 for m in range(j+1, len(numbers)) if numbers[i] + numbers[j] + numbers[m] == 2020]
