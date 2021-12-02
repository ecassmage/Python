import json
import os


def getSetting(filePath):
    try:
        return json.load(open(os.path.abspath(os.curdir) + '\\Settings\\' + filePath))
    except FileNotFoundError:
        return json.load(open(os.path.dirname(os.path.abspath(os.curdir)) + '\\Settings\\' + filePath))


def getInit():
    return getSetting("initial.json")


def getSetup():
    return getSetting("setup.json")


if __name__ == '__main__':
    pass
