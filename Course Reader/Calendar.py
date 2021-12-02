import ScrapeClass
import GUI
import json
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


if __name__ == "__main__":
    calendar = Calendar()
    calendar.FolderDrop()
    calendar.saveFile()
    calendar.GUI.Courses(calendar.CourseList)
    calendar.GUI.tk.mainloop()
