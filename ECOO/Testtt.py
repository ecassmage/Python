# 2011 Regular Season
# Boston 162 5710 875 1600 352 35 203
# NY_Yankees 162 5518 867 1452 267 33 222
# Texas 162 5659 855 1599 310 32 210
# Detroit 162 5563 787 1540 297 34 169
# St.Louis 162 5532 762 1513 308 22 162
# Toronto 162 5559 743 1384 285 34 186
# Cincinnati 162 5612 735 1438 264 19 183
# Colorado 162 5544 735 1429 274 40 163
# Arizona 162 5421 731 1357 293 37 172
# Kansas_City 162 5672 730 1560 325 41 129

from tkinter import *
team = {}
terms = ['gp', 'ab', 'r', 'ht', '2bh', '3bh', 'hr']
teams = {}
dataList = []
y = 0
with open("E:\\Scripting\\Python\\ecoo\\data11.txt", "r") as theFile:
    first_line = theFile.readline()
    for line in theFile:
        dataList.append(line)
        words = line.split()
        name = line.split()
        del name[1:8]
        team[y] = words[0]
        y = y + 1

        teams[words[0]] = {terms[0]: words[2], terms[1]: words[2], terms[2]: words[3],
                           terms[3]: words[4], terms[4]: words[5],
                           terms[5]: words[6], terms[6]: words[7]}


def OnButtonClick(button_id):
    print('2011 Regular Season')
    print('====================')
    t = len(team)
    for x in range(0, t):
        a = team[x]
        gp = (teams[a]['gp'])
        ab = (teams[a]['ab'])
        r = (teams[a]['r'])
        ht = (teams[a]['ht'])
        dbh = (teams[a]['2bh'])
        tbh = (teams[a]['3bh'])
        hr = (teams[a]['hr'])
        sbh = int(ht) - int(dbh) - int(tbh) - int(hr)
        ba = int(ht) / int(ab)
        ba = format(ba, '.3f')
        sa = (int(sbh) + 2 * int(dbh) + 3 * int(tbh) + 4 * int(hr)) / int(ab)
        sa = format(sa, '.3f')
        print('%s: %s %s' % (a, ba, sa))

    if button_id == 1:
        a = team[button_id - 1]
        gp = (teams[a]['gp'])
        ab = (teams[a]['ab'])
        r = (teams[a]['r'])
        ht = (teams[a]['ht'])
        dbh = (teams[a]['2bh'])
        tbh = (teams[a]['3bh'])
        hr = (teams[a]['hr'])
        sbh = int(ht) - int(dbh) - int(tbh) - int(hr)
        ba = int(ht) / int(ab)
        ba = format(ba, '.3f')
        sa = (int(sbh) + 2 * int(dbh) + 3 * int(tbh) + 4 * int(hr)) / int(ab)
        sa = format(sa, '.3f')
        answer = Message(tk, text='%s: '
                                  'SA: %s '
                                  'BA: %s' % (a, ba, sa), font=('times', 36))
        answer.place(x=1000, y=0, width=500)






tk = Tk()

canvas = Canvas(tk, width=1440, height=720)
canvas.pack()


boston_b = Button(tk, text='Boston', command=lambda: OnButtonClick(1))
boston_b.place(x=0, y=0, width=75)

NY_Yankees_b = Button(tk, text='NY Yankees', command=lambda: OnButtonClick(2))
NY_Yankees_b.place(x=0, y=25, width=75)

Texas_b = Button(tk, text='Texas', command=lambda: OnButtonClick(3))
Texas_b.place(x=0, y=50, width=75)

Detroit_b = Button(tk, text='Detroit', command=lambda: OnButtonClick(4))
Detroit_b.place(x=0, y=75, width=75)

St_Louis_b = Button(tk, text='St Louis', command=lambda: OnButtonClick(5))
St_Louis_b.place(x=0, y=100, width=75)

Toronto_b = Button(tk, text='Toronto', command=lambda: OnButtonClick(6))
Toronto_b.place(x=0, y=125, width=75)

Cincinnati_b = Button(tk, text='Cincinnati', command=lambda: OnButtonClick(7))
Cincinnati_b.place(x=0, y=150, width=75)

Colorado_b = Button(tk, text='Colorado', command=lambda: OnButtonClick(8))
Colorado_b.place(x=0, y=175, width=75)

Arizona_b = Button(tk, text='Arizona', command=lambda: OnButtonClick(9))
Arizona_b.place(x=0, y=200, width=75)

Kansas_City_b = Button(tk, text='Kansas City', command=lambda: OnButtonClick(10))
Kansas_City_b.place(x=0, y=225, width=75)

exit_button = Button(tk, text='Press to Exit', command=exit)
exit_button.place(x=200, y=200, width=150, height=45)


mainloop()
