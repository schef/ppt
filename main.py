#!/usr/bin/env python3

import pickle
import sys
import os
import colors
import time

import practiceTest
import masterClassJson

practices = [practiceTest.PracticeTest(),
             masterClassJson.Practice('masterclass_00_01.json')
             ]

nameWidthGroup = 0
nameWidthPractice = 0
nameWidthDescription = 0

statusFile = os.path.dirname(os.path.realpath(__file__)) + 'ppt.pickle'
def saveStatus(practices):
    with open(statusFile, 'wb') as handle:
        statusList = []
        for practice in practices:
            statusList.append([practice.UUID, practice.CURRENT_HITS])
        pickle.dump(statusList, handle, protocol=pickle.HIGHEST_PROTOCOL)


def loadStatus(practices):
    if os.path.isfile(statusFile):
        with open(statusFile, 'rb') as handle:
            statusList = pickle.load(handle)
            for status in statusList:
                for practice in practices:
                    if status[0] == practice.UUID:
                        practice.CURRENT_HITS = status[1]

def getColoredText(text, colorText, colorBg=""):
    string = colors.preColor + colors.colorsForeground[colorText]
    if colorBg:
        string += colors.preColor + colors.colorsBackground[colorBg]
    string += text
    string += colors.preColor + colors.colorsCommands["RESET"]
    return string


def printPractice(enum, practice):
    string = str(enum)
    string += " : "
    nameGroup = practice.GROUP
    if len(nameGroup) < nameWidthGroup:
        nameGroup += (nameWidthGroup - len(nameGroup)) * " "
    string += getColoredText(nameGroup, "GREEN")
    string += " : "
    namePractice = practice.PRACTICE
    if len(namePractice) < nameWidthPractice:
        namePractice += (nameWidthPractice - len(namePractice)) * " "
    string += getColoredText(namePractice, "MAGENTA")
    string += " : "
    nameDescription = practice.DESCRIPTION
    if len(nameDescription) < nameWidthDescription:
        nameDescription += (nameWidthDescription - len(nameDescription)) * " "
    string += getColoredText(nameDescription, "CYAN")
    string += " : "
    hitsString = str(practice.CURRENT_HITS) + "/" + str(practice.MAX_HITS)
    if (practice.CURRENT_HITS == 0):
        string += getColoredText(hitsString, "BRIGHT_BLUE")
    elif (practice.CURRENT_HITS / practice.MAX_HITS) < 0.5:
        string += getColoredText(hitsString, "BRIGHT_CYAN")
    elif (practice.CURRENT_HITS / practice.MAX_HITS) >= 0.5 and (practice.CURRENT_HITS / practice.MAX_HITS) < 1.0:
        string += getColoredText(hitsString, "BRIGHT_YELLOW")
    else:
        string += getColoredText(hitsString, "BRIGHT_GREEN")
    print(string)

def getNameWidth():
    for practice in practices:
        global nameWidthGroup, nameWidthPractice, nameWidthDescription
        if len(practice.GROUP) > nameWidthGroup:
            nameWidthGroup = len(practice.GROUP)
        if len(practice.PRACTICE) > nameWidthPractice:
            nameWidthPractice = len(practice.PRACTICE)
        if len(practice.DESCRIPTION) > nameWidthDescription:
            nameWidthDescription = len(practice.DESCRIPTION)

def init():
    loadStatus(practices)
    getNameWidth()

if __name__ == "__main__":
    print("Welcome")
    init()
    while True:
        for enum, practice in enumerate(practices):
            printPractice(enum, practice)
        practice = input("Select practice: ")
        if practice == "q":
            break
        else:
            hits = int(practices[int(practice)].main())
            if hits > practices[int(practice)].CURRENT_HITS:
                practices[int(practice)].CURRENT_HITS = hits
            saveStatus(practices)
    print("Good day sir!")
    sys.exit(0)
