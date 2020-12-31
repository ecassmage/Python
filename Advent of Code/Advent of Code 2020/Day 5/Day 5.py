import math
ID = 0
ID_list = []
ID_missing = []
with open("E:\\Advent\\Day 5.txt", 'r') as Day5:
    Day5.readline()
    for i in Day5:
        i = i.replace('\n', '')
        x = list(i)
        rows_t = 127
        rows_b = 0
        rows = 0
        columns = 0
        columns_l = 7
        columns_r = 0
        for j in i:
            if j == 'F':
                rows_t = math.floor(rows_t - (rows_t - rows_b) / 2)
            elif j == 'B':
                rows_b = math.ceil(rows_t - (rows_t - rows_b) / 2)
            elif j == 'L':
                columns_l = math.floor(columns_l - (columns_l - columns_r) / 2)
            elif j == 'R':
                columns_r = math.ceil(columns_l - (columns_l - columns_r) / 2)
            if rows_t == rows_b:
                rows = rows_t
            if columns_r == columns_l:
                columns = columns_l
        # print(rows)
        # print(columns)
        ID_list.append((rows * 8) + columns)
        if (rows * 8) + columns > ID:
            ID = (rows * 8) + columns
    #     print("ID: %s" % ID)
    # print(ID_list)
    c = 0
    for i in range(0, len(ID_list)):
        for j in range(0, len(ID_list) - i - 1):
            if ID_list[j] > ID_list[j+1]:
                hold = ID_list[j]
                ID_list[j] = ID_list[j+1]
                ID_list[j+1] = hold
    # print("print: %s" % ID_list)

    for i in range(0, 1024):
        if i in ID_list:
            pass
        else:
            ID_missing.append(i)
            c = c + 1
    for i in ID_missing:

        pass
    # print(ID_missing)
    # print(c)
    print("ID: %s" % ID)
    for i in range(1, len(ID_missing) - 1):
        if ID_missing[i - 1] - ID_missing[i] != -1 or ID_missing[i + 1] - ID_missing[i] != 1:
            print("This one works: %s" % ID_missing[i])

            # while True:
            #     if i == 'F':
            #         rows_t = math.ceil(rows_t/2)
            #     else:
            #         rows_b = math.ceil(rows_t/2)
            #     if rows_t == rows_b:
            #         rows = rows_t
            #         break
        # print(x)