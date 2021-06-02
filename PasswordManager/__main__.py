from tkinter import *
from threading import Thread
import String_Generator
import json
testCases = json.load(open("testcases.json", 'r'))

tk = Tk()
canvas = Canvas(tk, width=1000, height=1000, bg='orange')
canvas.pack()
LoginFrame = Frame(tk, bg='orange')
SignupFrame = Frame(tk, bg='orange')
SiteVar, UserVar, PassVar, PassVar_2 = StringVar(), StringVar(), StringVar(), StringVar()
Done_Thread = False


def Login_GUI():
    """Signup Widget"""

    """Labels"""

    Label_Site = Label(LoginFrame, text="Site", bg='orange', font=('calibre', 25, 'bold'))
    Label_Site.grid(row=0, column=0, rowspan=2, columnspan=2)

    Label_User = Label(LoginFrame, text="Username", bg='orange', font=('calibre', 25, 'bold'))
    Label_User.grid(row=2, column=0, rowspan=2, columnspan=2)

    Label_Pass = Label(LoginFrame, text="Password", bg='orange', font=('calibre', 25, 'bold'))
    Label_Pass.grid(row=4, column=0, rowspan=2, columnspan=2)

    """Entries"""

    Entry_Site = Entry(LoginFrame, textvariable=SiteVar, font=('calibre', 25, 'bold'))
    Entry_Site.grid(row=0, column=2, ipadx=100, ipady=10, rowspan=2)

    Entry_User = Entry(LoginFrame, textvariable=UserVar, font=('calibre', 25, 'bold'))
    Entry_User.grid(row=2, column=2, ipadx=100, ipady=10, rowspan=2)

    Entry_Pass = Entry(LoginFrame, textvariable=PassVar, font=('calibre', 25, 'bold'), show='*')
    Entry_Pass.grid(row=4, column=2, ipadx=100, ipady=10, rowspan=2)

    """Buttons"""

    Button_Check = Button(LoginFrame, text="Submit", command=check_if_valid, width=25, height=5)
    Button_Check.grid(row=6, column=2)

    Login_Check = Button(LoginFrame, text="Login", command=Login_GUI)
    Login_Check.grid(row=0, column=4)

    Signup_Check = Button(LoginFrame, text="Signup", command=Signup_GUI)
    Signup_Check.grid(row=0, column=3)

    """Change Widget"""
    SiteVar.set(""), PassVar.set(""), UserVar.set(""), PassVar_2.set("")
    SignupFrame.place_forget()
    LoginFrame.place(x=25, y=25)
    # lis = [Label_Site, Label_User, Label_Pass, Entry_Site, Entry_User, Entry_Pass]
    # if deletion is False:
    #     return lis


def Signup_GUI():
    """Signup Widget"""

    """Labels"""

    Label_Site = Label(SignupFrame, text="   Site", bg='orange', font=('calibre', 25, 'bold'))
    Label_Site.grid(row=0, column=0, rowspan=2)

    Label_User = Label(SignupFrame, text="   Username", bg='orange', font=('calibre', 25, 'bold'))
    Label_User.grid(row=2, column=0, rowspan=2)

    Label_Pass = Label(SignupFrame, text="   Password", bg='orange', font=('calibre', 25, 'bold'))
    Label_Pass.grid(row=4, column=0, rowspan=2)

    Label_Pass_Confirm = Label(SignupFrame, text="Password Confirm", bg='orange', font=('calibre', 25, 'bold'))
    Label_Pass_Confirm.grid(row=6, column=0, rowspan=2, columnspan=2)

    """Entries"""

    Entry_Site = Entry(SignupFrame, textvariable=SiteVar, font=('calibre', 25, 'bold'))
    Entry_Site.grid(row=0, column=2, ipadx=100, ipady=10, rowspan=2)

    Entry_User = Entry(SignupFrame, textvariable=UserVar, font=('calibre', 25, 'bold'))
    Entry_User.grid(row=2, column=2, ipadx=100, ipady=10, rowspan=2)

    Entry_Pass = Entry(SignupFrame, textvariable=PassVar, font=('calibre', 25, 'bold'), show='*')
    Entry_Pass.grid(row=4, column=2, ipadx=100, ipady=10, rowspan=2)

    Entry_Pass_2 = Entry(SignupFrame, textvariable=PassVar_2, font=('calibre', 25, 'bold'), show='*')
    Entry_Pass_2.grid(row=6, column=2, ipadx=100, ipady=10, rowspan=2)

    """Buttons"""

    Button_Check = Button(SignupFrame, text="Submit", command=check_pass, width=25, height=5)
    Button_Check.grid(row=8, column=2)

    Login_Check = Button(SignupFrame, text="Login", command=Login_GUI)
    Login_Check.grid(row=0, column=4)

    Show_Pass = Button(SignupFrame, text="Show", command=lambda: change_show(Entry_Pass, Entry_Pass_2))
    Show_Pass.grid(row=4, column=3)

    Signup_Check = Button(SignupFrame, text="Signup", command=Signup_GUI)
    Signup_Check.grid(row=0, column=3)

    """Change Widget"""

    SiteVar.set(""), PassVar.set(""), UserVar.set(""), PassVar_2.set("")
    LoginFrame.place_forget()
    SignupFrame.place(x=25, y=25)


def change_show(Entry_Pass, Entry_Pass_2):
    if Entry_Pass.cget('show') == '*':
        Entry_Pass.config(show="")
        Entry_Pass_2.config(show="")
    else:
        Entry_Pass.config(show="*")
        Entry_Pass_2.config(show="*")


def check_if_valid():
    SiteVar_string, UserVar_string = SiteVar.get(), UserVar.get()
    PassVar_string = PassVar.get()
    SiteVar.set(""), PassVar.set(""), UserVar.set("")
    site_cypher = String_Generator.EV_encryption(SiteVar_string)
    user_cypher = String_Generator.EV_encryption(UserVar_string)
    pass_cypher = String_Generator.EV_encryption(PassVar_string)
    if site_cypher in testCases:
        if user_cypher == testCases[site_cypher]['user'] and pass_cypher == testCases[site_cypher]['password']:
            print("we GOOD")
        else:
            print("we BAD")
    else:
        print("we BAD")
    canvas.update()
    return


def process(pass_cypher):
    global Done_Thread
    inp = input("This is the password generated, Do you want to see it?: ")
    if inp == 'yes':
        print(f"This is the Password we made:\n{pass_cypher}")
    Done_Thread = True
    return


def check_pass():
    global Done_Thread
    SiteVar_string, UserVar_string = SiteVar.get(), UserVar.get()
    PassVar_string, PassVar_string_2 = PassVar.get(), PassVar_2.get()
    SiteVar.set(""), PassVar.set(""), UserVar.set(""), PassVar_2.set("")
    if PassVar_string == PassVar_string_2:
        site_cypher = String_Generator.EV_encryption(SiteVar_string)
        user_cypher = String_Generator.EV_encryption(UserVar_string)
        pass_cypher = String_Generator.EV_encryption(PassVar_string)
        testCases.update({site_cypher: {'user': user_cypher, 'password': pass_cypher}})
        p = Thread(target=process, args=(pass_cypher,))
        p.start()
        c = 0
        while True:
            canvas.update()
            if Done_Thread:
                break
        print("Hello")
        Done_Thread = False


def main():
    Login_GUI()
    while True:
        canvas.update()


if __name__ == '__main__':
    word = 'Hello World!'
    b = String_Generator.EV_encryption(word, skey=4, length=1000)
    # print(repr(String_Generator.EV_encryption(b, skey=4, encrypt=False)))
    main()
    tk.mainloop()
