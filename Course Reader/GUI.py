
"""
Name: CourseReader (GUI)
Developer: Evan Morrison
Version: 1.0.0
Since 1.0.0


IDK this isn't organised.
"""

import tkinter as tk
import FindCollisions
import tkinter.font as tkfont
import json


class CourseBox:
    """
    Class CourseBox
    Holds a Box for each course appointment slot.
    """
    def __init__(self, CourseText, ListOfDays, ListOfTimes, color):
        """
        Defines the CourseBox variables
        :param CourseText: Takes the text for the label
        :param ListOfDays: Takes the List of days that this appointment needs to be shown for
        :param ListOfTimes: Takes the List of times for each day. This will later be used to determine the position of the appointments.
        :param color: Color of the appointment. Universal across all appointments for each course
        """
        self.idBox = []; self.Label = []
        self.Text = CourseText
        self.Days = ListOfDays
        self.Times = ListOfTimes
        self.color = color
        pass

    def equals(self, course2):
        """
        checks if these two are equal.
        :param course2: takes the CourseBox wanted wanted to compare against this one.
        :return: returns True if equal, False if not equal.
        """
        if self.Text != course2.Text or len(self.Days) != len(course2.Days) or self.color != course2.color:
            return False
        for Day in self.Days:
            if Day not in course2.Days:
                return False
        for Time in self.Times:
            if Time not in course2.Times:
                return False
        return True

    def collectCoordinates(self, window, Day):
        """

        :param window:
        :param Day:
        :return:
        """
        DaysOfWeek = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
        xNotPad = window.columnDimensions[0] / 10
        yNotPad = window.columnDimensions[1] / 3
        graceX = window.settings["Window"]["columnGrace"]
        graceY = window.settings["Window"]["rowGrace"]
        TimeSplit1 = self.Times[0].split(":")
        TimeSplit2 = self.Times[1].split(":")
        x1 = graceX + window.columnDimensions[0] * DaysOfWeek[Day] + xNotPad
        y1 = graceY + window.columnDimensions[1] * (int(TimeSplit1[0]) * 2 + (int(TimeSplit1[1]) / 30)) + yNotPad
        x2 = graceX + window.columnDimensions[0] * (DaysOfWeek[Day] + 1) - xNotPad
        y2 = graceY + window.columnDimensions[1] * (int(TimeSplit2[0]) * 2 + (int(TimeSplit2[1]) / 30))
        return [x1, y1, x2, y2]

    @staticmethod
    def SetCoordinates(Coord, ConflictNumber, NumberOfConflicts):
        x1 = Coord[0] + ((ConflictNumber - 1) * ((Coord[2] - Coord[0]) / NumberOfConflicts)) + 1
        x2 = Coord[0] + (ConflictNumber * ((Coord[2] - Coord[0]) / NumberOfConflicts)) - 1
        return [x1, Coord[1], x2, Coord[3]]

    def findOverlap(self, window):

        def CollectingCollisions(ID, listItems: list):
            Collected = getCollisionList(ID)
            if len(Collected) == 1:
                return listItems
            for CollectedID in Collected:
                if CollectedID[0] not in InfoAdded:
                    listItems.append(FindCollisions.CollectInfo(CollectedID, window))
                    InfoAdded.append(CollectedID[0])
                    CollectingCollisions(CollectedID[0], listItems)
            return listItems

        def getCollisionList(numberID):
            coordCollisions = window.window.coords(numberID)
            listOfIdCollisions = window.window.find_overlapping(coordCollisions[0], coordCollisions[1], coordCollisions[2], coordCollisions[3])
            listOfCollisions = []
            for CourseCollision in window.CourseBoxes:
                for CourseIDNumCollision in range(len(CourseCollision.idBox)):
                    if CourseCollision.idBox[CourseIDNumCollision] in listOfIdCollisions:
                        listOfCollisions.append([CourseCollision.idBox[CourseIDNumCollision], CourseCollision.Label[CourseIDNumCollision], CourseCollision])
            return listOfCollisions

        for number in range(len(self.idBox)):
            InfoAdded = []
            ListOfCollisions = CollectingCollisions(self.idBox[number], [])
            if len(ListOfCollisions) <= 1:
                return False
            ListOfOrder = FindCollisions.FindFitNext(ListOfCollisions)
            TotalNum = len(ListOfOrder)
            for pos, listOfElements in enumerate(ListOfOrder):
                for element in listOfElements:
                    currentNode = element['id']
                    coordNew = currentNode[2].SetCoordinates(currentNode[2].collectCoordinates(window, self.Days[number]), (pos + 1), TotalNum)
                    window.window.coords(currentNode[0], coordNew[0], coordNew[1], coordNew[2], coordNew[3])
                    currentNode[1].place(x=coordNew[0] + 1, y=coordNew[1] + 1)
        return True


class GUI:

    def __init__(self):
        self.Open = True
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

    def update(self):
        if self.Open:
            self.tk.update()

    def mainloop(self):
        if self.Open:
            self.tk.mainloop()

    def getColumns(self):
        return self.settings[self.Mode]["columns"]

    def getRows(self):
        return self.settings[self.Mode]["rows"]

    def Courses(self, CourseList):
        colors = ["red", "green", "orange", "pink", "cyan", "purple", "blue"]
        for number, CourseName in enumerate(CourseList):
            for ListDict in CourseList[CourseName]:
                for Iteration in ListDict:
                    CourseBoxTemp = CourseBox(ListDict[Iteration][0] + " " + CourseName, ListDict[Iteration][1][0], ListDict[Iteration][1][1], colors[number])
                    for Course in self.CourseBoxes:
                        if CourseBoxTemp.equals(Course):
                            break
                    else:
                        self.CourseBoxes.append(CourseBoxTemp)
                pass
            pass
        self.__CourseAdd__()
        for Course in self.CourseBoxes:
            Course.findOverlap(self)

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
            text.place(x=(self.settings["Window"]["columnGrace"] - (x + self.font.measure(time) + 2)), y=(self.currentCoord+2))

            self.currentCoord += self.columnDimensions[1]
            self.Labels.append(text)
        pass

    def __CourseAdd__(self):
        DaysOfWeek = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
        xNotPad = self.columnDimensions[0] / 10
        yNotPad = self.columnDimensions[1] / 3
        grace = self.settings["Window"]["columnGrace"]
        for Course in self.CourseBoxes:
            for day in Course.Days:
                Coord = Course.collectCoordinates(self, day)
                if self.settings['stipple']:
                    Course.idBox.append(self.window.create_rectangle(Coord[0], Coord[1], Coord[2], Coord[3], fill=Course.color, stipple="gray50"))
                else:
                    Course.idBox.append(self.window.create_rectangle(Coord[0], Coord[1], Coord[2], Coord[3], fill=Course.color))

                labelTemp = tk.Label(self.window, text=Course.Text, bg=Course.color)
                labelTemp.place(
                    x=grace + self.columnDimensions[0] * DaysOfWeek[day] + xNotPad,
                    y=Coord[1]
                )
                Course.Label.append(labelTemp)
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
