import random
import time

import midiPlayer
import pitchParser


class PracticeTest:
    GROUP = "Practice test"
    PRACTICE = "test"
    DESCRIPTION = "This is only a example"
    UUID = "dc9c215d-586f-492f-8f1f-3ecda45c56da"
    MAX_HITS = 5
    CURRENT_HITS = 0
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()

    chordsList = [["c'", "e'", "g'"],
                  ["d'", "f'", "a'"],
                  ["e'", "g'", "h'"],
                  ["f'", "a'", "c''"],
                  ["g'", "h'", "d''"],
                  ["a'", "c''", "e''"],
                  ["h'", "d''", "f''"],
                  ]

    pitchList = ["c'", "d'", "e'", "f'", "g'", "a'", "h'", "c''"]

    hits = 0
    randomChord = []
    randomNote = ""

    def __init__(self):
        self.generateNewChallenge()

    def playChords(self):
        self.player.playMultipleNotesHarmonicly(self.randomChord)
        time.sleep(self.player.NOTE_DURATION)

    def playNote(self):
        self.player.playSingleNote(self.randomNote)
        time.sleep(self.player.NOTE_DURATION)

    def generateNewChallenge(self):
        self.randomChord = self.parser.get_midi_list_from_pitch_list(random.choice(self.chordsList))
        self.randomNote = self.parser.get_midi_from_pitch(random.choice(self.pitchList))

    def main(self):

        while self.hits < self.MAX_HITS:

            self.playChords()
            self.playNote()

            guessNote = input("note: ")
            if (guessNote == "?"):
                print("Note is:", self.parser.get_pitch_from_midi(self.randomNote))
            elif (guessNote == "q"):
                break
            elif (guessNote == "r"):
                pass
            elif (self.parser.get_midi_from_pitch(guessNote) % 12 == self.randomNote % 12):
                self.hits += 1
                print("Good, hits = ", self.hits)
                self.generateNewChallenge()
            else:
                self.hits = 0
                print("Bad, hits = ", self.hits)
        print("Finish successfully")
        return (self.hits)
