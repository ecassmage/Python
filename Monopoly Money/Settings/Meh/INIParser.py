class FormatError(Exception):
    def __init__(self, message="Formatting Error"):
        self.message = message
        super().__init__(self.message)


class INI:
    def __init__(self, file, openType):
        self.file = open(file, openType)

    def readlines(self):
        for line in self.file.readlines():
            string = ""
            line = line.replace("\n", "")
            for character in line:
                if character == ';':
                    break
                else:
                    string += character
            if len(string) == 0:
                continue
            if string[0] == '[':
                if string[len(string) - 1] == ']':
                    yield string
                else:
                    raise FormatError
            else:
                yield string

    def parseToList(self):
        lis = []
        listNest = ""
        for line in self.readlines():
            if line[0] == '[' and line[len(line) - 1] == ']':
                lis.append(str(line[1:len(line)-1]))
            else:
                lis.append(line)

    def parseToDict(self):
        lis = {}
        listNest = ""
        for line in self.readlines():
            if line[0] == '[' and line[len(line) - 1] == ']':
                lis.update({str(line[1:len(line)-1]): {}})
                listNest = str(line[1:len(line)-1])
            else:
                lis.update(line)


