count_group = []
current_group = []
summation = 0
addition = 0
person = 0
with open("E:\\Advent\\Day 6.txt", 'r') as Day6:
    Day6.readline()
    for i in Day6:
        if i == '\n':
            for compter in range(1, len(current_group), 2):
                if current_group[compter] == person:
                    addition = addition + 1
            count_group.append(addition)
            addition = 0
            # print("The Price of a mile: %s" % current_group)
            current_group = []
            person = 0
            continue
        elif i != '\n':
            i = i.replace('\n', '')
        person = person + 1
        x = list(i)
        for juice in x:
            if juice not in current_group:
                current_group.append(juice)
                current_group.append(1)
            else:
                current_group[current_group.index(juice) + 1] = current_group[current_group.index(juice) + 1] + 1
for num in count_group:
    summation = summation + num
print("Because num is: %s\nWe got: %d" % (count_group, summation))