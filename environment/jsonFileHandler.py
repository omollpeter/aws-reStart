import json


def readJsonFile(fileName):
    """
    Reads a JSON file
    """
    data = ""

    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError as e:
        print("Could not read file")
    return data
