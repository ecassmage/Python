import tkinter as tk
import tkinter.font as tkfont
import json


class CourseBox:
    def __init__(self, CourseText, ListOfDays, ListOfTimes, color):
        self.idBox = []
        self.Label = []
        self.Text = CourseText
        self.Days = ListOfDays
        self.Times = ListOfTimes
        self.color = color
        pass


class GUI:

    def __init__(self):
        self.settings = json.load(open("settings.json"))
        self.Mode = "Custom"

        self.tk = tk.Tk()
        self.window = tk.Canvas(self.tk, width=self.settings["Window"]["width"], height=self.settings["Window"]["height"], bg="peach puff")

        self.Lines = []
        self.Labels = []
        self.CourseBoxes = []

        self.font = tkfont.Font(family="Ariel", size=200, weight="normal")

        self.columnDimensions = [
            (self.settings["Window"]["width"] - self.settings["Window"]["columnGrace"]) // self.getColumns(),
            (self.settings["Window"]["height"] - self.settings["Window"]["rowGrace"]) // self.getRows()
        ]

        if int((self.settings["Window"]["columnGrace"] / (longestStr(self.font, self.getRows()) / (8 / 10))) * self.font['size']) > self.columnDimensions[1]/2:
            self.font.config(size=int(self.columnDimensions[1] / 2) - 2)
        else:
            self.font.config(size=int((self.settings["Window"]["columnGrace"] / (longestStr(self.font, self.getRows()) / (8 / 10))) * self.font['size']))

        self.window.pack()
        self.__boardDecals__()
        self.__LabelsDecalsDay__()
        pass

    def getColumns(self):
        return self.settings[self.Mode]["columns"]

    def getRows(self):
        return self.settings[self.Mode]["rows"]

    def Courses(self, CourseList):
        colors = ["red", "green", "orange", "blue", "pink", "purple", "cyan"]
        for number, CourseName in enumerate(CourseList):
            for ListDict in CourseList[CourseName]:
                for Iteration in ListDict:
                    self.CourseBoxes.append(CourseBox(ListDict[Iteration][0] + " " + CourseName, ListDict[Iteration][1][0], ListDict[Iteration][1][1], colors[number]))
                pass
            pass
        self.__CourseAdd__()

    def __boardDecals__(self):
        lineMover = self.settings["Window"]["columnGrace"]
        for _ in range(self.getColumns()):  # Going from Top to Bottom, new Lines from left to Right
            self.Lines.append(self.window.create_line(lineMover, 0, lineMover, self.settings["Window"]['height'], fill='black', width=4))
            lineMover += self.columnDimensions[0]

        lineMover = self.settings["Window"]["rowGrace"]
        for _ in range(self.getRows()):  # Going from Left to Right, new Lines from Top to Bottom
            self.Lines.append(self.window.create_line(0, lineMover, self.settings["Window"]["width"], lineMover, fill='black', width=3))
            lineMover += self.columnDimensions[1]

    def __LabelsDecalsDay__(self):
        self.currentCoord = self.settings["Window"]["rowGrace"]
        x = int(self.settings["Window"]["columnGrace"] - longestStr(self.font, self.getRows())) // 2
        y = int(self.columnDimensions[1] - (self.font['size']*2)) // 2
        z = self.font['size']
        for time in timeGenerator(self.getRows()):
            text = tk.Label(self.window, text=time, bg="peach puff", font=self.font, padx=0, pady=0)
            text.place(x=(self.settings["Window"]["columnGrace"] - (x + self.font.measure(time) + 2)), y=(self.currentCoord + y + 2))

            self.currentCoord += self.columnDimensions[1]
            self.Labels.append(text)
        pass

    def __CourseAdd__(self):
        DaysOfWeek = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
        xNotPad = self.columnDimensions[0] / 10
        yNotPad = self.columnDimensions[1] / 3
        grace = self.settings["Window"]["columnGrace"]
        times = []
        for Course in self.CourseBoxes:
            for day in Course.Days:
                TimeSplit1 = Course.Times[0].split(":")
                TimeSplit2 = Course.Times[1].split(":")
                Course.idBox.append(
                    self.window.create_rectangle(
                        grace + self.columnDimensions[0] * DaysOfWeek[day] + xNotPad,
                        self.columnDimensions[1]*(int(TimeSplit1[0])*2 + (int(TimeSplit1[1])/30)) + yNotPad,
                        grace + self.columnDimensions[0] * (DaysOfWeek[day] + 1) - xNotPad,
                        self.columnDimensions[1]*(int(TimeSplit2[0])*2 + (int(TimeSplit2[1])/30)) - yNotPad,
                        fill=Course.color
                    )
                )
                labelTemp = tk.Label(self.window, text=Course.Text, bg=Course.color)
                labelTemp.place(
                    x=grace + self.columnDimensions[0] * DaysOfWeek[day] + xNotPad,
                    y=self.columnDimensions[1]*(int(TimeSplit1[0])*2 + (int(TimeSplit1[1])/30)) + yNotPad
                )
                # Course.Label.append(
                #
                # )
            pass


def timeGenerator(rows):
    if rows >= 48:
        for i in range(int(rows/2)):
            if i == 25:
                yield str(0) + ":00"
                yield str(0) + ":30"
            else:
                yield str(i) + ":00"
                yield str(i) + ":30"
    else:
        for i in range(rows):
            if i == 25:
                yield str(0) + ":00"
            else:
                yield str(i) + ":00"


def longestStr(fontSize, rows, option=None):
    font = tkfont.Font(family=option['family'], size=fontSize, weight=option['family']) if type(fontSize) == int else fontSize
    number = 0
    for numberInGen in timeGenerator(rows):
        if font.measure(numberInGen) > number:
            number = font.measure(numberInGen)
    return number


if __name__ == '__main__':
    gui = GUI()
    gui.tk.mainloop()
