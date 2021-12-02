import json
import os


def AIOpen():
    try:
        return AICleanDict(json.load(open(os.path.abspath(os.curdir) + '\\Settings\\ArtificialIntelligence.json')))
    except FileNotFoundError:
        try:
            return AICleanDict(json.load(open(os.path.dirname(os.path.abspath(os.curdir)) + '\\Settings\\ArtificialIntelligence.json')))
        except FileNotFoundError:
            print("AI Specifications was not able to be located")
            raise FileNotFoundError


def AICleanDict(Dict: dict):
    listTemp = list(Dict.keys())
    for Key in listTemp:
        if type(Dict[Key]) == dict:
            Dict[Key] = AICleanDict(Dict[Key])

        elif type(Dict[Key]) == list:
            AICleanList(Dict[Key])

        else:
            if type(Key) == str and Key[0:2] == "//":
                Dict.pop(Key)
    return Dict


def AICleanList(List: list):
    listTemp = List.copy()
    for Element in listTemp:
        if type(Element) == dict:
            List[List.index(Element)] = AICleanDict(Element)

        elif type(Element) == list:
            List[List.index(Element)] = AICleanList(Element)

        else:
            if Element == str and Element[0:2] == "//":
                List.pop(List.index(Element))

    return List
