# teams = {'Boston', 'NY_Yankees', 'Texas', 'Detroit', 'St_Louis', 'Toronto',
#          'Cincinnati', 'Colorado', 'Arizona', 'Kansas_City'}
terms = ['gp', 'ab', 'r', 'ht', '2bh', '3bh', 'hr']
teams = {}
dataList = []
with open("E:\\Scripting\\Python\\ecoo\\data_2012_11.txt", "r") as theFile:

    # You can just take the first line of a file like this
    first_line = theFile.readline()
    print(first_line)

    # This for loop will go through an entire file.
    for line in theFile:
        dataList.append(line)
        words = line.split()
        teams[words[0]] = {terms[0]: words[2], terms[1]: words[2], terms[2]: words[3],
                           terms[3]: words[4], terms[4]: words[5],
                           terms[5]: words[6], terms[6]: words[7]}

        # name = line.split()
        # del(name[1:8])
        # print(name)
        # del(words[0])
        # print(words)
        # iter(words)
        # for x in range(0, 10):
        #     n = name[x]
        #     n = dict(zip(terms, words))
        # del(k['name'])
        # print(name)
    for item in dataList:
        # print(item)
        print(teams)
