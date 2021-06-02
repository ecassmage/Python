import json


def settingsFileReader():
    return json.load(open('configFiles/settings.json', 'r'))


def modifierFileReader():
    return json.load(open('configFiles/modifiers.json', 'r'))


def rulesFileReader():
    return json.load(open('configFiles/simulationSettings.json', 'r'))
