import json
import os


def JOpen(PathName):
    try:
        return __CommentDict(json.load(open(os.path.abspath(os.curdir) + "\\Settings\\" + PathName)))
    except FileNotFoundError:
        try:
            return __CommentDict(json.load(open(os.path.dirname(os.path.abspath(os.curdir)) + "\\Settings\\" + PathName)))
        except FileNotFoundError:
            print("Json File Was not found")
            raise FileNotFoundError


def __CommentDict(Dict: dict):
    listTemp = list(Dict.keys())
    for Key in listTemp:
        if type(Dict[Key]) == dict:
            Dict[Key] = __CommentDict(Dict[Key])

        elif type(Dict[Key]) == list:
            __CommentList(Dict[Key])

        else:
            if type(Key) == str and Key[0:2] == "//":
                Dict.pop(Key)
    return Dict


def __CommentList(List: list):
    listTemp = List.copy()
    for Element in listTemp:
        if type(Element) == dict:
            List[List.index(Element)] = __CommentDict(Element)

        elif type(Element) == list:
            List[List.index(Element)] = __CommentList(Element)

        else:
            if Element == str and Element[0:2] == "//":
                List.pop(List.index(Element))

    return List