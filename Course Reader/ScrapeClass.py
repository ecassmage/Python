import re
from datetime import datetime


class Scrape:
    def __init__(self, FilePath, autoRead=True):
        self.FilePath = FilePath
        self.Title = ""
        self.Lectures = []
        if autoRead:
            self.ReadFile()

    def getTitle(self, line):
        Title = re.findall("[A-Z]{4} [0-9]{4}", line)
        if len(Title) > 0:
            return self.Title if self.Title != "" else Title[0]
        return self.Title

    @staticmethod
    def getLecLab(line):
        labLec = re.findall("((LEC|LAB) - )", line)
        if len(labLec) > 0:
            return labLec[0][0].replace(" - ", "")
        return ""

    @staticmethod
    def getTimes(line):
        arr = re.findall("((Monday|Tuesday|Wednesday|Thursday|Friday)[a-z-A-Z0-9: <>]+</span>)", line)
        if len(arr):
            arr = arr[0][0].replace("</span>", " ").split("<br>")
            arr[0] = arr[0].split(" ")
            arr[1] = arr[1].replace(" ", "").split("to")
            arr[1][0] = datetime.strftime(datetime.strptime(arr[1][0], "%I:%M%p"), "%H:%M")
            arr[1][1] = datetime.strftime(datetime.strptime(arr[1][1], "%I:%M%p"), "%H:%M")
        return arr

    def ReadFile(self):
        newSlot = {}
        numberOfTypes = [0, 0]
        for line in open(self.FilePath, "r").readlines():
            self.Title = self.getTitle(line)

            LecLab = self.getLecLab(line)
            if LecLab != "":
                newSlot.update({numberOfTypes[1]: [LecLab]})
                numberOfTypes[1] += 1

            Times = self.getTimes(line)
            if len(Times) > 0:
                newSlot[numberOfTypes[0]].append(Times)
                numberOfTypes[0] += 1

            if numberOfTypes != [0, 0] and numberOfTypes[0] == numberOfTypes[1]:
                numberOfTypes = [0, 0]
                self.Lectures.append(newSlot)
                newSlot = {}


if __name__ == "__main__":
    scrape = Scrape("Courses\\COMP2140.html")
    scrape.ReadFile()
    print(scrape.Lectures)
    pass
