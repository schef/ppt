#!/usr/bin/env python3

import pickle
import sys
from pathlib import Path
import colors

import practiceTest
import masterClass17_01

practices = [practiceTest.PracticeTest(),
             masterClass17_01.Practice()]

statusFile = Path('ppt.pickle')

def saveStatus(practices):
    with open(statusFile, 'wb') as handle:
        statusList = []
        for practice in practices:
            statusList.append([practice.UUID, practice.CURRENT_HITS])
        pickle.dump(statusList, handle, protocol=pickle.HIGHEST_PROTOCOL)


def loadStatus(practices):
    if statusFile.is_file():
        with open(statusFile, 'rb') as handle:
            statusList = pickle.load(handle)
            for status in statusList:
                for practice in practices:
                    if status[0] == practice.UUID:
                        practice.CURRENT_HITS = status[1]

if __name__ == "__main__":
    print("Welcome")
    loadStatus(practices)
    while True:
        for enum, practice in enumerate(practices):
            string = str(enum)
            string += " : "
            string += colors.preColor + colors.colorsForeground["RTT_CTRL_TEXT_BRIGHT_GREEN"]
            string += practice.NAME
            string += colors.preColor + colors.colorsCommands["RTT_CTRL_RESET"]
            string += " - "
            string += colors.preColor + colors.colorsForeground["RTT_CTRL_TEXT_BRIGHT_MAGENTA"]
            string += practice.DESCRIPTION
            string += colors.preColor + colors.colorsCommands["RTT_CTRL_RESET"]
            string += " - "
            string += colors.preColor + colors.colorsForeground["RTT_CTRL_TEXT_BRIGHT_BLUE"]
            string += str(practice.CURRENT_HITS) + "/" + str(practice.MAX_HITS)
            string += colors.preColor + colors.colorsCommands["RTT_CTRL_RESET"]
            print(string)
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
