# Imports
from tkinter import *
from PIL import ImageTk, Image
import os

# You can add to the DATA11.txt file with more teams
# if you want and the program will take the extra team
# into account next time it is run.
#
# This is why there are so many extra steps to this
# Program

# List Initializer's
team = {}
terms = ['gp', 'ab', 'r', 'ht', '2bh', '3bh', 'hr']
teams = {}
dataList = []
length = []
# Canvas tk
tk = Tk()
# Initial Variables
y = 0
s = 0
switch = 0
# Centralized Folder location
input_folder = 'E:\\ECOO\\Sluggers\\Input\\DATA11.txt'
output_folder = 'E:\\ECOO\\Sluggers\\Output\\DATA12.txt'
output2_folder = 'E:\\ECOO\\Sluggers\\Output\\DATA13.txt'
images_folder = 'E:\\ECOO\\Sluggers\\Images'
# Computing Program


def program():

    global s
    global y
    with open("%s" % input_folder, "r") as theFile:
        theFile.readline()
        for line in theFile:
            print(line)
            dataList.append(line)
            words = line.split()
            name = line.split()
            del name[1:8]
            team[y] = words[0]
            y = y + 1

            if len(words) == 8:  # Turning the two lists into a dictionary, also checking for sufficient information
                teams[words[0]] = {terms[0]: words[2], terms[1]: words[2], terms[2]: words[3],  # per team so as to not
                                   terms[3]: words[4], terms[4]: words[5],  # cause any errors
                                   terms[5]: words[6], terms[6]: words[7]}
                with open("%s" % output_folder, 'w') as DATA12:
                    DATA12.write('')
                    DATA12.close()
            else:
                with open("%s" % output_folder, 'w') as DATA12:    # adding onto any team that
                    s = len(words)  # does not meet the appropriate amount of information
                    if len(words) == 7:
                        print('You are missing %s statistic from '
                              '%s, please fix this.\n\n' % (8 - len(words), words[0]))
                        DATA12.write('You are missing %s statistic from %s, please fix this. \n\n'
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
        y = 0
    baa = 0
    saa = 0
    print('2011 Regular Season')
    print('====================')
    with open("%s" % output_folder, 'a') as DATA12:    # The new file being created DATA12 /
        count = 2 + len(team)
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
            ba = ba.replace('0.', '.')
            sa = (int(sbh) + 2 * int(dbh) + 3 * int(tbh) + 4 * int(hr)) / int(ab)
            saa = float(saa) + float(sa)
            sa = format(sa, '.3f')
            sa = sa.replace('0.', '.')
            print('%s: %s %s' % (a, ba, sa))    # The main writing part of the loops
            DATA12.write('%s: %s %s\n' % (a, ba, sa))

        t_baa = float(baa) / t
        t_baa = format(t_baa, '.3f')
        t_baa = t_baa.replace('0.', '.')
        t_saa = float(saa) / t
        t_saa = format(t_saa, '.3f')
        t_saa = t_saa.replace('0.', '.')
        print('====================')
        DATA12.write('====================\n')
        if len(team) == 10:
            print('Big 10 Av: %s %s' % (t_baa, t_saa))
            DATA12.write('Big 10 Av: %s %s' % (t_baa, t_saa))
        else:
            print('The %s Av: %s %s' % (len(team), t_baa, t_saa))
            DATA12.write('The %s Av: %s %s' % (len(team), t_baa, t_saa))

        DATA12.close()
        button_start.after(0, mainframe)

# Hub where the defined programs flip back and forth.
# The delay would not show up between lines in the
# listbox as the program lagged?
# this allowed the writing in the canvas listbox to become independent
# of the main program and the constant flipping meant that there wouldn't
# be any delay between the addition of each new line on canvas


def mainframe():
    global lts
    global switch
    if switch == 0:
        switch = 1
        button_start.after(0, program)

    elif switch == 1:
        switch = 2
        button_start.after(50, del_loop0)

    elif switch == 2:
        lts = list_team.size()
        list_team.after(75, del_loop1)

    elif switch == 3:
        switch = 1
        list_team.delete(0, 'end')
        lts = 0
        print('')
        list_team.after(0, program)
# del_loop0 creates a new file DATA13 which is a copy of DATA12
# it then prints the first line in list_team and closes DATA12 flipping process to mainframe


def del_loop0():
    global list_team
    list_team = Listbox(tk, bg='grey', height=lts)
    list_team.place(x=400, y=80, width=200)
    with open("%s" % output_folder, "r") as copy:
        lines = copy.readlines()
        copy.close()
    DATA13 = open("%s" % output2_folder, 'w')
    for line in lines:
        DATA13.write(line)
    list_team.insert(0, '%s' % lines[0])
    DATA13.close()
    list_team.after(0, mainframe)
# del_loop1 opens DATA13 reads the lines and saves them to "lines"
# it then closes DATA13, deletes first line from "lines"
# it then opens DATA13 back up and overwrites the text inside with "lines"
# it then inserts the lines[0] or the first line into list_team and closes DATA13
# it then jumps to the mainframe function, mainframe will then send it back
# the try, except part is to catch the DATA13 file once it has had all of its lines deleted
# once the program catches the 'IndexError' it will then close the DATA13 file to make sure
# it is closed, delete the DATA13 file from the OS if it still exists, flip the switch to 3
# and finish the program where it can then be run again by clicking the Calculate button


def del_loop1():

    global DATA13
    try:
        with open("%s" % output2_folder, "r") as copy:
            lines = copy.readlines()
            copy.close()

        del lines[0]

        DATA13 = open("%s" % output2_folder, 'w')

        for line in lines:
            DATA13.write(line)
        list_team.insert('end', '%s' % lines[0])
        DATA13.close()
        list_team.after(0, mainframe)
    except IndexError:
        DATA13.close()
        if os.path.exists("%s" % output2_folder):
            os.remove("%s" % output2_folder)
        else:
            pass
        global switch
        switch = 3
        pass


canvas = Canvas(tk, width=1000, height=750, bg='white')
canvas.pack()
sample_output = Label(tk, text='Output here',
                      width=10,
                      height=40,
                      anchor=N,
                      bg='white',
                      font=('Times New Roman', 24)
                      )
sample_output.place(x=400, y=30)
image = Image.open('%s\\Bat.jpg' % images_folder)
image2 = Image.open('%s\\Bat_Flip.jpg' % images_folder)
image = image.resize((236, 151))
image2 = image2.resize((236, 151))
bat = ImageTk.PhotoImage(image)
bat2 = ImageTk.PhotoImage(image2)
canvas.create_image(118, 76, image=bat)
canvas.create_image(882, 76, image=bat2)
button_start = Button(tk, text='Calculate', command=mainframe)
button_start.place(x=450, width=100)
list_team = Listbox()
lts = list_team.size()


with open('%s' % input_folder, 'r') as scan:
    lines = scan.readlines()
    scan.close()
    for comp in range(0, len(lines)):
        length.insert(comp, len(lines[comp]))
    list_initial = Listbox(tk,
                           bg='grey',
                           font='times',
                           height=len(lines) + 1,
                           width=max(length))
    list_initial.place(x=0, y=195)
    sample_input = Label(tk, text='             Input here',
                         width=max(length),
                         height=40,
                         anchor=W,
                         bg='white',
                         font=('Times New Roman', 24))
    sample_input.place(x=0, y=155, height=40)
    while True:
        try:
            list_initial.insert('end', lines[0])
            del lines[0]
        except IndexError:
            break


mainloop()
