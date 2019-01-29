import random
import time
import json

import midiPlayer
import pitchParser

with open('masterclass_05_01.json', 'r') as f:
    jsonData = json.load(f)

class Practice0501:
    GROUP = jsonData['group']
    PRACTICE = jsonData['practice']
    DESCRIPTION = jsonData['description']
    UUID = jsonData['uuid']
    MAX_HITS = jsonData['maxHits']
    CURRENT_HITS = 0
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()
    hits = 0
    question = []
    anwser = []

    def __init__(self):
        self.generateNewChallenge()

    def playHarmonicly(self):
        for item in self.question:
            self.player.playMultipleNotesHarmonicly(item)
            time.sleep(self.player.NOTE_DURATION)

    def playMelodicly(self):
        for item in self.question:
            self.player.playMultipleNotesMelodicly(item)
            time.sleep(self.player.NOTE_DURATION * len(item))

    def playAnwser(self):
        for item in self.anwser:
            self.player.playMultipleNotesMelodicly(item)
            time.sleep(self.player.NOTE_DURATION * len(item))

    def showQuestion(self):
        print("showQuestion id " + str(self.id) + ":", self.question)

    def showAnwser(self):
        print("showAnwser id " + str(self.id) + ":", self.anwser)

    def generateNewChallenge(self):
        randomPractice = random.choice(jsonData['practiceBatchAuto'])
        self.id = randomPractice['id']
        self.question = randomPractice['question']
        self.anwser = randomPractice['anwser']

    def main(self):

        self.playHarmonicly()
        while self.hits < self.MAX_HITS:

            inputString = input("command: ")
            if (inputString == "?"): #help
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
                self.playHarmonicly()
            elif (inputString == "pm"):
                self.playMelodicly()
            elif (inputString == "ph"):
                self.playHarmonicly()
            elif (inputString == "pa"):
                self.playAnwser()
            elif (inputString == "sq"):
                self.showQuestion()
            elif (inputString == "sa"):
                self.showAnwser()
            elif (inputString == "n"):
                self.hits += 1
                print("Good, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                self.generateNewChallenge()
                self.playHarmonicly()
            elif (inputString == "r"):
                self.hits = 0
                print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                self.generateNewChallenge()
                self.playHarmonicly()
            elif (inputString == "q"):
                break

        print("Finish successfully")
        return (self.hits)