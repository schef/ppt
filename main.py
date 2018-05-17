#!/usr/bin/env python3

import pickle
import sys
from pathlib import Path
import practiceTest

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
    practices = [practiceTest.PracticeTest()]
    loadStatus(practices)
    while True:
        for enum, practice in enumerate(practices):
            print(str(enum) + ":", practice.NAME, str(practice.CURRENT_HITS) + "/" + str(practice.MAX_HITS))
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
