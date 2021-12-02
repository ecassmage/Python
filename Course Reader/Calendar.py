import ScrapeClass
import GUI
import json
import time
import os


class Calendar:
    def __init__(self, CalendarFile="CalendarFile", CourseDropFolder="Courses"):
        self.CalendarFile = CalendarFile
        self.CourseDropFolder = CourseDropFolder

        self.CourseList = {}
        self.loadFile()

        self.GUI = GUI.GUI()

    def loadFile(self):
        if os.path.isfile(self.CalendarFile + ".json"):
            self.CourseList = json.load(open(self.CalendarFile + ".json"))

    def saveFile(self):
        file = open(self.CalendarFile + ".json", "w")
        json.dump(self.CourseList, file)
        file.close()

    def addToCalendar(self, newCourse):
        for key in newCourse:
            if key not in self.CourseList and len(key) == 9:
                self.CourseList.update({key: newCourse[key]})

    def addScrape(self, scrapeObj):
        self.addToCalendar({scrapeObj.Title: scrapeObj.Lectures})

    def deleteCourse(self, courseName):
        if courseName in self.CourseList:
            del(self.CourseList, courseName)

    def FolderDrop(self):
        if os.path.isdir(self.CourseDropFolder):
            for file in os.listdir(self.CourseDropFolder):
                if os.path.isdir(self.CourseDropFolder + "\\" + file):
                    continue
                self.addScrape(ScrapeClass.Scrape(self.CourseDropFolder + "\\" + file))
            pass

    def update(self):
        self.GUI.update()

    def mainloop(self):
        self.GUI.mainloop()


def click(event, calendar):
    ID = calendar.GUI.window.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1)
    print(ID)


def main():
    calendar = Calendar()
    calendar.FolderDrop()
    calendar.saveFile()
    calendar.GUI.Courses(calendar.CourseList)
    calendar.GUI.window.bind("<Button-1>", lambda event: click(event, calendar))
    while True:

        calendar.update()
        time.sleep(1/60)
    pass


if __name__ == "__main__":
    main()
