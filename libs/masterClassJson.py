import random
import time
import json

import midiPlayer
import pitchParser

def recursive_len(item):
    if type(item) == list:
        return sum(recursive_len(subitem) for subitem in item)
    else:
        return 1

class Practice:
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()
    hits = 0
    question = []
    anwser = []

    def __init__(self, jsonFileName):
        self.jsonFileName = jsonFileName
        with open(jsonFileName, 'r') as f:
            self.jsonData = json.load(f)
        self.GROUP = self.jsonData['group']
        self.PRACTICE = self.jsonData['practice']
        self.DESCRIPTION = self.jsonData['description']
        self.UUID = self.jsonData['uuid']
        self.MAX_HITS = self.jsonData['maxHits']
        self.PRACTICE_TYP = self.jsonData['practiceTyp']
        self.CURRENT_HITS = 0
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
        randomPractice = random.choice(self.jsonData['practiceBatch'])
        self.id = randomPractice['id']
        self.question = randomPractice['question']
        self.anwser = randomPractice['anwser']

    def executeNewChallenge(self):
        if (self.PRACTICE_TYP == "PITCH_NAMING_DRILL"):
            self.playHarmonicly()
        elif (self.PRACTICE_TYP == "PITCH_IDENTIFY_DRILL"):
            self.playHarmonicly()
        elif (self.PRACTICE_TYP == "MEDITATION"):
            self.showQuestion()

    def main(self):

        self.executeNewChallenge()

        while self.hits < self.MAX_HITS:

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
                self.executeNewChallenge()
            elif (inputString == "r"):
                self.hits = 0
                print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                self.generateNewChallenge()
                self.executeNewChallenge()
            elif (inputString == "q"):
                break
            else:
                if (self.PRACTICE_TYP == "PITCH_NAMING_DRILL"):
                    self.checkPitchNamingDrill(inputString)
                elif (self.PRACTICE_TYP == "PITCH_IDENTIFY_DRILL"):
                    self.checkPitchIdentifyDrill(inputString)
                elif (self.PRACTICE_TYP == "MEDITATION"):
                    pass

        print("Finish successfully")
        return (self.hits)

    def checkPitchIdentifyDrill(self, inputString):
        print("Input not recognized: <" + inputString +
              ">, use <pa> to check if you sang wright and <n> for next or <?> for more help.")

    def checkPitchNamingDrill(self, inputString):
        anwserGroup = self.anwser
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
                self.hits += 1
                print("Good, hits = ", str(self.hits) +
                      "/" + str(self.MAX_HITS))
                self.generateNewChallenge()
                self.executeNewChallenge()
            else:
                self.hits = 0
                print("Bad, hits = ", str(self.hits) +
                      "/" + str(self.MAX_HITS))
                self.executeNewChallenge()
