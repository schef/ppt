#!/usr/bin/env python3

import sys
sys.path.insert(0, './libs')
import masterClassJson
from common import *

def getWelcomeMessage():
    return("%s%s===== Welcome =====%s" % (bcolors.CBOLD, bcolors.CGREEN, bcolors.ENDC))


def getEndMessage():
    return("%s%s== Good day sir! ==%s" % (bcolors.CBOLD, bcolors.CGREEN, bcolors.ENDC))


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
        print(getDescription(getMasterclassInfoByName(name, data), "    "))
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
            masterClassJson.PracticePitchNamingDrill(getFileNamePath(practiceFilename)).main()
        elif practice["practiceType"] == "PITCH_IDENTIFY_DRILL":
            masterClassJson.PracticePitchIdentifyDrill(getFileNamePath(practiceFilename)).main()
        elif practice["practiceType"] == "MEDITATION":
            masterClassJson.PracticeMeditation(getFileNamePath(practiceFilename)).main()
        else:
            print("%s%sERROR:%s practiceType %s not implemented" % (bcolors.CBOLD, bcolors.CRED, bcolors.ENDC, practiceType))

    print(getEndMessage())
