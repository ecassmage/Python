import json


def openStg():
    file = open("settings.json")
    jsonFile = json.load(file)
    file.close()
    return jsonFile
