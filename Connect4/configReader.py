import json


def readSettings():
    return json.load(open("settings.json"))
