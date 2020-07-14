#!/usr/bin/env python3

import glob
import json
import sys
sys.path.insert(0, './libs')
import masterClassJson


class bcolors:
    ENDC = '\033[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'


def readJsonToDict(FILENAME):
    data = None
    try:
        with open(FILENAME) as json_file:
            data = json.load(json_file)
    except:
        print("%s%sERROR:%s Can't open file %s" % (bcolors.CBOLD, bcolors.CRED, bcolors.ENDC, FILENAME))
        sys.exit(1)
    return data


def getWelcomeMessage():
    return("%s%s===== Welcome =====%s" % (bcolors.CBOLD, bcolors.CGREEN, bcolors.ENDC))


def getEndMessage():
    return("%s%s== Good day sir! ==%s" % (bcolors.CBOLD, bcolors.CGREEN, bcolors.ENDC))


def getFileNamePath(FILENAME):
    files = glob.glob('./**/*.json', recursive=True)
    for f in files:
        if FILENAME in f:
            return f
    return ""


def getDescription(data, TAB=""):
    string = ""
    for line in data["description"]:
        string += "%s%s%s%s\n" % (TAB, bcolors.CITALIC, line, bcolors.ENDC)
    return string[:-1]


def getNameList(data):
    nameList = []
    for name in data["masterclasses"]:
        nameList.append(name["name"])
    return nameList


def getMasterclassInfoByName(name, data):
    for line in data["masterclasses"]:
        if (name in line["name"]):
            return line
    return None


def selectMasterclass(data):
    nameList = getNameList(data)
    for e, name in enumerate(nameList):
        print("  [%s%s%s] %s" % (bcolors.CVIOLET, "{:0>2}".format(e), bcolors.ENDC, name))
    try:
        selection = int(input("%sSELECT:%s " % (bcolors.CBOLD, bcolors.ENDC)))
        name = nameList[selection]
        return getMasterclassInfoByName(name, data)
    except:
        print("%s%sERROR:%s Could not parse" % (bcolors.CBOLD, bcolors.CRED, bcolors.ENDC))
        return None


def selectPractice(data):
    for filename in data['filenames']:
        practice = readJsonToDict(getFileNamePath(filename))
        print("  [%s%s%s]" % (bcolors.CVIOLET, "{:0>2}".format(practice["practice"]), bcolors.ENDC))
        print(getDescription(practice, "    "))
    try:
        selection = int(input("%sSELECT:%s " % (bcolors.CBOLD, bcolors.ENDC)))
        filename = data['filenames'][selection]
        return filename
    except:
        print("%s%sERROR:%s Could not parse" % (bcolors.CBOLD, bcolors.CRED, bcolors.ENDC))
        return None


def getPracticeType(data):
    return data["practiceType"]


if __name__ == "__main__":
    print(getWelcomeMessage())

    data = readJsonToDict(getFileNamePath("masterclasses.json"))
    print(getDescription(data))
    masterclass = selectMasterclass(data)

    if (masterclass):
        practiceFilename = selectPractice(masterclass)
        practice = readJsonToDict(getFileNamePath(practiceFilename))
        if practice["practiceType"] == "PITCH_NAMING_DRILL":
            masterClassJson.Practice(getFileNamePath(practiceFilename)).main()
        elif practice["practiceType"] == "PITCH_IDENTIFY_DRILL":
            masterClassJson.Practice(getFileNamePath(practiceFilename)).main()
        elif practice["practiceType"] == "MEDITATION":
            masterClassJson.Practice(getFileNamePath(practiceFilename)).main()
        else:
            print("%s%sERROR:%s practiceType %s not implemented" % (bcolors.CBOLD, bcolors.CRED, bcolors.ENDC, practiceType))

    print(getEndMessage())
