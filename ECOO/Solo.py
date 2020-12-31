# You can add to the DATA11.txt file with more teams
# if you want and the program will take the extra team
# into account next time it is run.
#
# This is why there are so many extra steps to this
# Program
team = {}
terms = ['gp', 'ab', 'r', 'ht', '2bh', '3bh', 'hr']
teams = {}
dataList = []
y = 0
with open("E:\\Scripting\\Python\\sluggers\\DATA11.txt", "r") as theFile:
    first_line = theFile.readline()
    for line in theFile:
        dataList.append(line)
        words = line.split()
        name = line.split()
        del name[1:8]
        team[y] = words[0]
        y = y + 1
        global s

        if len(words) == 8:     # Turning the two lists into a dictionary, also checking for sufficient information
            teams[words[0]] = {terms[0]: words[2], terms[1]: words[2], terms[2]: words[3],  # per team so as to not
                               terms[3]: words[4], terms[4]: words[5],  # cause any errors
                               terms[5]: words[6], terms[6]: words[7]}
        else:
            with open("E:\\Scripting\\Python\\sluggers\\DATA12.txt", 'w') as DATA12:    # adding onto any team that
                s = len(words)  # does not meet the appropriate amount of information
                if len(words) == 7:
                    print('You are missing %s statistic from '
                          '%s, please fix this.\n\n' % (8 - len(words), words[0]))
                    DATA12.write('You are missing %s statistic from %s, please fix this.'
                                 % (8 - len(words), words[0]))
                else:
                    print('You are missing %s statistics from '
                          '%s, please fix this.' % (8 - len(words), words[0]))
                    DATA12.write('You are missing %s statistics from %s, please fix this.\n\n'
                                 % (8 - len(words), words[0]))
                if len(words) <= 2:
                    for uu in range(0, 3 - s):
                        words.append('1')
                else:
                    pass
                s = len(words)
                for u in range(0, 8 - s):
                    words.append('0')
                teams[words[0]] = {terms[0]: words[2], terms[1]: words[2], terms[2]: words[3],
                                   terms[3]: words[4], terms[4]: words[5],
                                   terms[5]: words[6], terms[6]: words[7]}
                DATA12.close()
baa = 0
saa = 0
print('2011 Regular Season')
print('====================')
with open("E:\\Scripting\\Python\\sluggers\\DATA12.txt", 'a') as DATA12:    # The new file being created DATA12 /
    t = len(team)   # added too
    DATA12.write('2011 Regular Season\n')
    DATA12.write('====================\n')
    for x in range(0, t):

        a = team[x]  # The Dictionary being given variable names
        gp = (teams[a]['gp'])
        ab = (teams[a]['ab'])
        r = (teams[a]['r'])
        ht = (teams[a]['ht'])
        dbh = (teams[a]['2bh'])
        tbh = (teams[a]['3bh'])
        hr = (teams[a]['hr'])
        sbh = int(ht) - int(dbh) - int(tbh) - int(hr)   # The math behind the calculations
        ba = int(ht) / int(ab)
        baa = float(baa) + float(ba)
        ba = format(ba, '.3f')
        sa = (int(sbh) + 2 * int(dbh) + 3 * int(tbh) + 4 * int(hr)) / int(ab)
        saa = float(saa) + float(sa)
        sa = format(sa, '.3f')
        print('%s: %s %s' % (a, ba, sa))    # The main writing part of the loops
        DATA12.write('%s: %s %s\n' % (a, ba, sa))
    t_baa = float(baa) / t
    t_baa = format(t_baa, '.3f')
    t_saa = float(saa) / t
    t_saa = format(t_saa, '.3f')
    print('====================')
    DATA12.write('====================\n')
    if len(team) == 10:
        print('Big 10 Av: %s %s' % (t_baa, t_saa))
        DATA12.write('Big 10 Av: %s %s' % (t_baa, t_saa))
    else:
        print('The %s Av: %s %s' % (len(team), t_baa, t_saa))
        DATA12.write('The %s Av: %s %s' % (len(team), t_baa, t_saa))

    DATA12.close()
