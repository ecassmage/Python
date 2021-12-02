import re
import os


class CourseObj:
    class File:
        def __init__(self, file):
            if os.path.isfile(file):
                self.file = open(file, "a")
                self.state = "a"
            else:
                self.file = open(file, "w")
                self.state = "w"

    def __init__(self, FolderPath="", SingleCourse=False, SaveFileName="CalendarFile"):
        self.FolderPath = FolderPath
        self.SingleCourse = SingleCourse
        self.Course = []
        self.SaveFileName = SaveFileName
        self.file = self.File(SaveFileName)
        pass

    def __state(self):
        return self.file.state

    def iterateFolder(self):
        for File in os.listdir(self.FolderPath):
            if File[-5:] != ".html":
                continue
            self.getNewCourse(self.FolderPath + "\\" + File)

    def SaveToFile(self):
        if self.__state == "a":
            self.file.file.write("\n")
        for element in self.Course:
            pass
        pass

    def getNewCourse(self, courseFileName):
        Weeks = "(Monday|Tuesday|Wednesday|Thursday|Friday)"
        CourseArray = []
        title = False
        for line in open(courseFileName, "r").readlines():
            arr = re.findall(f"({Weeks}[a-z-A-Z0-9: <>]+</span>)", line)
            if not title:
                arrTitle = re.findall("[A-Z]{4} [0-9]{4}", line)
                if len(arrTitle) > 0:
                    CourseArray.append(arrTitle)
                    title = True
            if len(arr):
                arr = arr[0][0].replace("</span>", " ").split("<br>")
                arr[0] = arr[0].split(" ")
                arr[1] = arr[1].replace(" ", "").split("to")
                CourseArray.append(arr)
        if len(CourseArray) == 0:
            print(f"No Course Was found in {courseFileName}")
            return None
        self.Course.append(CourseArray)


def GetLabLec(Line):
    values = re.findall("", Line)


def getNewCourse(courseFileName):
    Weeks = "(Monday|Tuesday|Wednesday|Thursday|Friday)"
    CourseArray = []
    title = False
    for line in open(courseFileName, "r").readlines():
        arr = re.findall(f"({Weeks}[a-z-A-Z0-9: <>]+</span>)", line)
        if not title:
            arrTitle = re.findall("[A-Z]{4} [0-9]{4}", line)
            if len(arrTitle) > 0:
                CourseArray.append(arrTitle)
                title = True
        if len(arr):
            arr = arr[0][0].replace("</span>", " ").split("<br>")
            arr[0] = arr[0].split(" ")
            arr[1] = arr[1].replace(" ", "").split("to")
            CourseArray.append(arr)
    if len(CourseArray) == 0:
        print(f"No Course Was found in {courseFileName}")
        return None
    return CourseArray


if __name__ == "__main__":
    NewCourse = getNewCourse("Course Information.html")
    print(NewCourse)

