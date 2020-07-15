#!/usr/bin/env python3

import random
import time
import json

import midiPlayer
import pitchParser
from common import *


def recursive_len(item):
    if type(item) == list:
        return sum(recursive_len(subitem) for subitem in item)
    else:
        return 1


class PracticeBase:
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()

    def playHarmonicly(self, noteList):
        for note in noteList:
            self.player.playMultipleNotesHarmonicly(note)
            time.sleep(self.player.NOTE_DURATION)

    def playMelodicly(self, noteList):
        for note in noteList:
            self.player.playMultipleNotesMelodicly(note)
            time.sleep(self.player.NOTE_DURATION * len(note))

    def showQuestion(self, challange):
        print("showQuestion id " + str(challange["id"]) + ":", challange["question"])

    def showAnwser(self, challange):
        print("showAnwser id " + str(challange["id"]) + ":", challange["anwser"])

    def generateNewChallenge(self, practiceBatch):
        return random.choice(practiceBatch)


class PracticePitchNamingDrill(PracticeBase):
    def __init__(self, filename):
        print("PracticePitchNamingDrill")
        self.practice = readJsonToDict(getFileNamePath(filename))

    def executeNewChallenge(self, noteList):
        self.playHarmonicly(noteList)

    def main(self):
        print("Practice start")
        hits = 0
        challenge = self.generateNewChallenge(self.practice["practiceBatch"])
        self.executeNewChallenge(challenge["question"])

        while hits < self.practice["maxHits"]:

            inputString = input("command: ")
            if (inputString == "?"):  # help
                helpString = " ?: this help message" + "\n"
                helpString += "pr: play repeat" + "\n"
                helpString += "pm: play melodicly" + "\n"
                helpString += "ph: play harmonicly" + "\n"
                helpString += "pa: play anwser" + "\n"
                helpString += "sq: show question" + "\n"
                helpString += "sa: show anwser" + "\n"
                helpString += " n: next" + "\n"
                helpString += " r: reset session" + "\n"
                helpString += " q: quit" + "\n"
                print(helpString)
            elif (inputString == "pr"):
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "pm"):
                self.playMelodicly(challenge["question"])
            elif (inputString == "ph"):
                self.playHarmonicly(challenge["question"])
            elif (inputString == "pa"):
                self.playMelodicly(challenge["anwser"])
            elif (inputString == "sq"):
                self.showQuestion(challenge)
            elif (inputString == "sa"):
                self.showAnwser(challenge)
            elif (inputString == "n"):
                hits += 1
                print("Good, hits = ", str(hits) + "/" + str(self.practice["maxHits"]))
                challenge = self.generateNewChallenge(self.practice["practiceBatch"])
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "r"):
                hits = 0
                print("Bad, hits = ", str(hits) + "/" + str(self.practice["maxHits"]))
                challenge = self.generateNewChallenge(self.practice["practiceBatch"])
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "q"):
                break
            else:
                anwserGroup = challenge["anwser"]
                anwserGroupLen = len(anwserGroup)
                inputGroup = [inputString.split(' ')]
                if (anwserGroupLen > 1):
                    for i in anwserGroupLen - 1:
                        inputGroup.append(input(">: ").split(' '))
                if (recursive_len(anwserGroup) != recursive_len(inputGroup)):
                    print("Wrong number of pitches", inputGroup, anwserGroup)
                else:
                    guess = True
                    for i in range(anwserGroupLen):
                        for y in range(len(anwserGroup[i])):
                            if (self.parser.get_midi_base_from_pitch(anwserGroup[i][y]) != self.parser.get_midi_base_from_pitch(inputGroup[i][y])):
                                guess = False
                    if (guess):
                        hits += 1
                        print("Good, hits = ", str(hits) + "/" + str(self.practice["maxHits"]))
                        challenge = self.generateNewChallenge(self.practice["practiceBatch"])
                        self.executeNewChallenge(challenge["question"])
                    else:
                        hits = 0
                        print("Bad, hits = ", str(hits) + "/" + str(self.practice["maxHits"]))
                        self.executeNewChallenge(challenge["question"])

        print("Practice end")
        return (hits)


class PracticePitchIdentifyDrill(PracticeBase):
    def __init__(self, filename):
        print("PracticePitchIdentifyDrill")
        self.practice = readJsonToDict(getFileNamePath(filename))

    def executeNewChallenge(self, noteList):
        self.playHarmonicly(noteList)

    def main(self):
        print("Practice start")
        hits = 0
        challenge = self.generateNewChallenge(self.practice["practiceBatch"])
        self.executeNewChallenge(challenge["question"])

        while hits < self.practice["maxHits"]:

            inputString = input("command: ")
            if (inputString == "?"):  # help
                helpString = " ?: this help message" + "\n"
                helpString += "pr: play repeat" + "\n"
                helpString += "pm: play melodicly" + "\n"
                helpString += "ph: play harmonicly" + "\n"
                helpString += "pa: play anwser" + "\n"
                helpString += "sq: show question" + "\n"
                helpString += "sa: show anwser" + "\n"
                helpString += " n: next" + "\n"
                helpString += " r: reset session" + "\n"
                helpString += " q: quit" + "\n"
                print(helpString)
            elif (inputString == "pr"):
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "pm"):
                self.playMelodicly(challenge["question"])
            elif (inputString == "ph"):
                self.playHarmonicly(challenge["question"])
            elif (inputString == "pa"):
                self.playMelodicly(challenge["anwser"])
            elif (inputString == "sq"):
                self.showQuestion(challenge)
            elif (inputString == "sa"):
                self.showAnwser(challenge)
            elif (inputString == "n"):
                hits += 1
                print("Good, hits = ", str(hits) + "/" + str(self.practice["maxHits"]))
                challenge = self.generateNewChallenge(self.practice["practiceBatch"])
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "r"):
                hits = 0
                print("Bad, hits = ", str(hits) + "/" + str(self.practice["maxHits"]))
                challenge = self.generateNewChallenge(self.practice["practiceBatch"])
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "q"):
                break
            else:
                print("Input not recognized: <" + inputString +
                    ">, use <pa> to check if you sang wright and <n> for next or <?> for more help.")

        print("Practice end")
        return (hits)


class PracticeMeditation(PracticeBase):
    def __init__(self, filename):
        print("PracticeMeditation")
        self.practice = readJsonToDict(getFileNamePath(filename))

    def executeNewChallenge(self, noteList):
        self.showQuestion(noteList)

    def main(self):
        print("Practice start")
        hits = 0
        challenge = self.generateNewChallenge(self.practice["practiceBatch"])
        self.executeNewChallenge(challenge["question"])

        while hits < self.practice["maxHits"]:

            inputString = input("command: ")
            if (inputString == "?"):  # help
                helpString = " ?: this help message" + "\n"
                helpString += "pr: play repeat" + "\n"
                helpString += "pm: play melodicly" + "\n"
                helpString += "ph: play harmonicly" + "\n"
                helpString += "pa: play anwser" + "\n"
                helpString += "sq: show question" + "\n"
                helpString += "sa: show anwser" + "\n"
                helpString += " n: next" + "\n"
                helpString += " r: reset session" + "\n"
                helpString += " q: quit" + "\n"
                print(helpString)
            elif (inputString == "pr"):
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "pm"):
                self.playMelodicly(challenge["question"])
            elif (inputString == "ph"):
                self.playHarmonicly(challenge["question"])
            elif (inputString == "pa"):
                self.playMelodicly(challenge["anwser"])
            elif (inputString == "sq"):
                self.showQuestion(challenge)
            elif (inputString == "sa"):
                self.showAnwser(challenge)
            elif (inputString == "n"):
                hits += 1
                print("Good, hits = ", str(hits) + "/" + str(self.practice["maxHits"]))
                challenge = self.generateNewChallenge(self.practice["practiceBatch"])
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "r"):
                hits = 0
                print("Bad, hits = ", str(hits) + "/" + str(self.practice["maxHits"]))
                challenge = self.generateNewChallenge(self.practice["practiceBatch"])
                self.executeNewChallenge(challenge["question"])
            elif (inputString == "q"):
                break

        print("Practice end")
        return (hits)