import random
import time

import midiPlayer
import pitchParser


class Practice:
    NAME = "Masterclass 17-01"
    DESCRIPTION = "A C major chord and than two harmonic black tones."
    UUID = "4312e48e-438c-47aa-96ed-ebee24c690bc"
    MAX_HITS = 20
    CURRENT_HITS = 0
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()

    chord = ["c'", "e'", "g'"]

    pitchList = ["cis'", "es'", "fis'", "as'", "b'"]

    hits = 0
    randomNotes = []

    def __init__(self):
        self.generateNewChallenge()
        time.sleep(1)

    def playChord(self):
        self.player.playMultipleNotesHarmonicly(self.parser.get_midi_list_from_pitch_list(self.chord))
        time.sleep(self.player.NOTE_DURATION)

    def playNotes(self):
        self.player.playMultipleNotesHarmonicly(self.randomNotes)
        time.sleep(self.player.NOTE_DURATION)

    def generateNewChallenge(self):
        self.randomNotes = []
        while True:
            randomNote = self.parser.get_midi_from_pitch(random.choice(self.pitchList))
            if (randomNote not in self.randomNotes):
                self.randomNotes.append(randomNote)
            if (len(self.randomNotes) >= 2):
                break
        self.randomNotes.sort();

    def main(self):

        while self.hits < self.MAX_HITS:

            self.playChord()
            self.playNotes()

            guessNote = input("note: ")
            if (guessNote == "?"):
                print("Notes are:", self.parser.get_pitch_from_midi(self.randomNotes[0]), self.parser.get_pitch_from_midi(self.randomNotes[1]))
            elif (guessNote == "q"):
                break
            elif (guessNote == "r"):
                pass
            else:
                notes = guessNote.split()
                if (self.parser.get_midi_from_pitch(notes[0]) % 12 == self.randomNotes[0] % 12 and
                        self.parser.get_midi_from_pitch(notes[1]) % 12 == self.randomNotes[1] % 12):
                    self.hits += 1
                    print("Good, hits = ", self.hits)
                    self.generateNewChallenge()
                else:
                    self.hits = 0
                    print("Bad, hits = ", self.hits)

        print("Finish successfully")
        return (self.hits)
