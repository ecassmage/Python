import re
splitted = []
for line in open("Score.txt", 'r').readlines():
    for string in line.split("</tr>"):
        splitted.append(string)

for i in range(len(splitted)):
    splitted[i] = splitted[i].replace("\n", "")


file = open("Score.txt", "w")
for line in splitted:
    if len(line) > 0:
        file.write(line + "\n")
file.close()
listOfScores = []
for line in open("Score.txt", 'r').readlines():
    splitted = re.findall("[0-9]+", line)
    if line.find("Exception in thread \"main\"") >= 0:
        splitted = [splitted[0], splitted[1], "ERROR"]
    if len(splitted) > 0 and splitted[2] != "ERROR":
        for num in range(len(splitted)):
            splitted[num] = int(splitted[num])
        listOfScores.append(splitted)


print(listOfScores)

listOfDifferences = {}
for time in listOfScores:
    if time[1] not in listOfDifferences:
        bah = time
        listOfDifferences.update({time[1]: [time]})
    else:
        pah = listOfDifferences[time[1]].append(time)


listOfDifferencesSorted = {}
for Key in sorted(list(listOfDifferences.keys())):
    lis = listOfDifferences[Key]
    sortedList = sorted(lis, key=lambda x: x[2])
    listOfDifferencesSorted.update({Key: sortedList})

print("\nSorted Rankings")
for Key in list(listOfDifferencesSorted.keys()):
    print(f"DataSizes: {Key}")
    for row in range(len(listOfDifferencesSorted[Key])):
        print(f"{row}:  \tSubmission: {listOfDifferencesSorted[Key][row][0]}   \tTime: {listOfDifferencesSorted[Key][row][2]}")
    print("\n")

print(listOfDifferences)
