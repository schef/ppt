import random
import time
import json

import midiPlayer
import pitchParser



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
            else:
                if (self.PRACTICE_TYP == "SOLO_KEYBOARD"):
                    pitches = inputString.split(' ')
                    if (len(pitches) != len(self.anwser)):
                        print("Wrong number of pitches", pitches, self.anwser)
                    else:
                        guess = True
                        for i in range(len(pitches)):
                            if (self.parser.get_midi_base_from_pitch(pitches[i]) != self.parser.get_midi_base_from_pitch(self.anwser[i])):
                                guess = False
                        if (guess):
                            self.hits += 1
                            print("Good, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                            self.generateNewChallenge()
                            self.playHarmonicly()
                        else:
                            self.hits = 0
                            print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                            self.playHarmonicly()
                elif (self.PRACTICE_TYP == "TEAM_PLAYER"):
                    pass
                elif (self.PRACTICE_TYP == "MEDITATION"):
                    pass
                else:
                    print("Input not recognized", inputString)                    

        print("Finish successfully")
        return (self.hits)