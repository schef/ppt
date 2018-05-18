import random
import time

import midiPlayer
import pitchParser


class Practice0501:
    GROUP = "Masterclass 05"
    PRACTICE = "01"
    DESCRIPTION = "Any two white tones separated by one. Listen and Sing."
    UUID = "f90c6b33-9238-436d-bbcf-6bdae3a7d1bb"
    MAX_HITS = 20
    CURRENT_HITS = 0
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()

    pitchList = ["c,", "d,", "e,", "f,", "g,", "a,", "h,",
                 "c", "d", "e", "f", "g", "a", "h",
                 "c'", "d'", "e'", "f'", "g'", "a'", "h'",
                 "c''", "d''", "e''", "f''", "g''", "a''", "h''",
                 "c'''",]

    hits = 0
    randomNotes = []

    def __init__(self):
        self.generateNewChallenge()

    def playChord(self):
        self.player.playMultipleNotesHarmonicly(self.randomNotes)
        time.sleep(self.player.NOTE_DURATION)

    def playNotes(self):
        self.player.playMultipleNotesMelodicly(self.randomNotes)
        time.sleep(self.player.NOTE_DURATION * len(self.randomNotes))

    def generateNewChallenge(self):
        self.randomNotes = []
        randomIndex = random.choice(range(len(self.pitchList) - 2))
        self.randomNotes.append(self.parser.get_midi_from_pitch(self.pitchList[randomIndex]))
        self.randomNotes.append(self.parser.get_midi_from_pitch(self.pitchList[randomIndex + 2]))
        self.randomNotes.sort()

    def main(self):

        while self.hits < self.MAX_HITS:

            self.playChord()

            guessNote = input("command: ")
            if (guessNote == "?"):
                self.playNotes()
            elif (guessNote == "a"):
                self.hits = 0
                print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
            elif (guessNote == "q"):
                break
            elif (guessNote == "r"):
                pass
            elif (guessNote == "n"):
                self.hits += 1
                print("Good, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                self.generateNewChallenge()

        print("Finish successfully")
        return (self.hits)