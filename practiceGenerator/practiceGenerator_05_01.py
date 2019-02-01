#!/usr/bin/env python3

import uuid

TAB1 = '    '
TAB2 = TAB1 * 2

pitchList = ["c,", "d,", "e,", "f,", "g,", "a,", "h,",
             "c", "d", "e", "f", "g", "a", "h",
             "c'", "d'", "e'", "f'", "g'", "a'", "h'",
             "c''", "d''", "e''", "f''", "g''", "a''", "h''",
             "c'''", ]

def printHeader():
    string = ""
    string += '{' + '\n'
    string += TAB1 + '"group": "",' + '\n'
    string += TAB1 + '"practice": "",' + '\n'
    string += TAB1 + '"description": "",' + '\n'
    string += TAB1 + '"uuid": "'
    string += str(uuid.uuid1())
    string += '",' + '\n'
    string += TAB1 + '"maxHits": 20,' + '\n'
    string += TAB1 + '"practiceTyp" : "",' + '\n'
    string += TAB1 + '"practiceBatch" : [' + '\n'
    print(string, end = "")

def printPractices():
    for i in range(len(pitchList) - 2):
        question = [[pitchList[i], pitchList[i + 2]]]
        anwser = question
        string = ""
        string += TAB2 + '{"id" : '
        string += str(i)
        string += ', "question" : '
        string += str(question)
        string += ', '
        string += ', "anwser" : '
        string += str(anwser)
        if (i < (len(pitchList) - 2) - 1):
            string += '},' + '\n'
        else:
            string += '}' + '\n'
        print(string, end = "")

def printEnd():
    string = ""
    string += TAB1 + ']' + '\n'
    string += '}' + '\n'
    print(string, end = "")

if __name__ == "__main__":
    printHeader()
    printPractices()
    printEnd()