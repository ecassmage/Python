import json
import os


def settingsOpen():
    temp = os.path.abspath(os.curdir) + '\\txtLists\\settings.json'
    temp2 = os.path.dirname(os.path.abspath(os.curdir))
    try:
        return json.load(open(os.path.abspath(os.curdir) + '\\txtLists\\settings.json'))
    except FileNotFoundError:
        return json.load(open(os.path.dirname(os.path.abspath(os.curdir)) + '\\txtLists\\settings.json'))
