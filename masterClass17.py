import random
import time

import midiPlayer
import pitchParser


class Practice1701:
    GROUP = "Masterclass 17"
    PRACTICE = "01"
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
        self.randomNotes.sort()

    def main(self):

        while self.hits < self.MAX_HITS:

            self.playChord()
            self.playNotes()

            guessNote = input("note: ")
            if (guessNote == "?"):
                print("Notes are:", self.parser.get_pitch_from_midi(self.randomNotes[0]),
                      self.parser.get_pitch_from_midi(self.randomNotes[1]))
            elif (guessNote == "q"):
                break
            elif (guessNote == "r"):
                pass
            else:
                notes = guessNote.split()
                if (len(notes) != 2):
                    print("Syntax error: write two pitches")
                elif (notes[0] not in list(self.parser.pitchMidiBase.keys()) or notes[1] not in list(self.parser.pitchMidiBase.keys())):
                    print("Syntax error: written pitch does not exist")
                elif (self.parser.get_midi_from_pitch(notes[0]) % 12 == self.randomNotes[0] % 12 and
                      self.parser.get_midi_from_pitch(notes[1]) % 12 == self.randomNotes[1] % 12):
                    self.hits += 1
                    print("Good, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                    self.generateNewChallenge()
                else:
                    self.hits = 0
                    print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))

        print("Finish successfully")
        return (self.hits)


class Practice1702:
    GROUP = "Masterclass 17"
    PRACTICE = "02"
    DESCRIPTION = "Three white tones and one black tone. "
    UUID = "808e2272-29bc-49d4-a1c2-bcb5569a699f"
    MAX_HITS = 3 * 20
    CURRENT_HITS = 0
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()

    pitchListWhite = ["c'", "d'", "e'", "f'", "g'", "a'", "h'", "c''"]
    pitchListBlack = ["cis'", "es'", "fis'", "as'", "b'"]

    hits = 0
    randomNote = 0
    whiteCounter = 0

    def __init__(self):
        self.generateNewChallenge()

    def playNote(self):
        self.player.playSingleNote(self.randomNote)
        time.sleep(self.player.NOTE_DURATION)

    def generateNewChallenge(self):
        self.randomNote = 0
        if self.whiteCounter < 3:
            self.whiteCounter += 1
            self.randomNote = self.parser.get_midi_from_pitch(random.choice(self.pitchListWhite))
        else:
            self.whiteCounter = 0
            self.randomNote = self.parser.get_midi_from_pitch(random.choice(self.pitchListBlack))

    def main(self):

        while self.hits < self.MAX_HITS:

            self.playNote()

            guessNote = input("note: ")
            if (guessNote == "?"):
                print("Note is:", self.parser.get_pitch_from_midi(self.randomNote))
            elif (guessNote == "q"):
                break
            elif (guessNote == "r"):
                pass
            else:
                if (guessNote not in list(self.parser.pitchMidiBase.keys())):
                    print("Syntax error: written pitch not in list")
                elif (self.parser.get_midi_from_pitch(guessNote) % 12 == self.randomNote % 12):
                    self.hits += 1
                    print("Good, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                    self.generateNewChallenge()
                else:
                    self.hits = 0
                    print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))

        print("Finish successfully")
        return (self.hits)


class Practice170301:
    GROUP = "Masterclass 17"
    PRACTICE = "0301"
    DESCRIPTION = "Black fours. Unlock and sing them."
    UUID = "9c9027ab-0ace-43cb-bc5f-4a8d24fb76bd"
    MAX_HITS = 20
    CURRENT_HITS = 0
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()

    pitchList = ["cis'", "es'", "fis'", "as'", "b'"]

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
        while (len(self.randomNotes) < 4):
            randomNote = self.parser.get_midi_from_pitch(random.choice(self.pitchList))
            if (randomNote not in self.randomNotes):
                self.randomNotes.append(randomNote)
        self.randomNotes.sort()

    def main(self):

        while self.hits < self.MAX_HITS:

            self.playChord()

            guessNote = input("command: ")
            if (guessNote == "?"):
                self.playNotes()
            elif (guessNote == "q"):
                break
            elif (guessNote == "r"):
                pass
            elif (guessNote == "m"):
                self.hits += 0
                print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                self.generateNewChallenge()
            elif (guessNote == "n"):
                self.hits +=1
                print("Good, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                self.generateNewChallenge()

        print("Finish successfully")
        return (self.hits)


class Practice170302:
    GROUP = "Masterclass 17"
    PRACTICE = "0302"
    DESCRIPTION = "Black fours. Identify them."
    UUID = "ca6f4a2d-43e5-45af-9720-6289e80f264d"
    MAX_HITS = 20
    CURRENT_HITS = 0
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()

    pitchList = ["cis'", "es'", "fis'", "as'", "b'"]

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
        while (len(self.randomNotes) < 4):
            randomNote = self.parser.get_midi_from_pitch(random.choice(self.pitchList))
            if (randomNote not in self.randomNotes):
                self.randomNotes.append(randomNote)
        self.randomNotes.sort()

    def areNotesValids(self, notes):
        validNotes = list(self.parser.pitchMidiBase.keys())
        for note in notes:
            if note not in validNotes:
                return False
        return True

    def main(self):

        while self.hits < self.MAX_HITS:

            self.playChord()

            guessNote = input("command: ")
            if (guessNote == "?"):
                print("Notes are:", [self.parser.get_pitch_from_midi(i) for i in self.randomNotes])
            elif (guessNote == "q"):
                break
            elif (guessNote == "r"):
                pass
            else:
                notes = guessNote.split()
                if (len(notes) != 4):
                    print("Syntax error: write 4 pitches")
                elif (not self.areNotesValids(notes)):
                    print("Syntax error: written pitch does not exist")
                elif (self.parser.get_midi_from_pitch(notes[0]) % 12 == self.randomNotes[0] % 12 and
                      self.parser.get_midi_from_pitch(notes[1]) % 12 == self.randomNotes[1] % 12 and
                      self.parser.get_midi_from_pitch(notes[2]) % 12 == self.randomNotes[2] % 12 and
                      self.parser.get_midi_from_pitch(notes[3]) % 12 == self.randomNotes[3] % 12):
                    self.hits += 1
                    print("Good, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
                    self.generateNewChallenge()
                else:
                    self.hits = 0
                    print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))

        print("Finish successfully")
        return (self.hits)


class Practice1704:
    GROUP = "Masterclass 17"
    PRACTICE = "04"
    DESCRIPTION = "Meditation. C major with As and Fis. Doubles."
    UUID = "a7546fbd-f1ec-4b16-bc68-9e6457380150"
    MAX_HITS = 20
    CURRENT_HITS = 0
    player = midiPlayer.MidiPlayer()
    parser = pitchParser.PitchParser()

    pitchList = ["c'", "d'", "e'", "f'", "g'", "a'", "h'", "c''",
                     "fis'", "as'"]
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
        while (len(self.randomNotes) < 2):
            randomNote = self.parser.get_midi_from_pitch(random.choice(self.pitchList))
            if (randomNote not in self.randomNotes):
                self.randomNotes.append(randomNote)
        self.randomNotes.sort()

    def main(self):

        while self.hits < self.MAX_HITS:

            print("Sing", self.parser.get_pitch_from_midi(self.randomNotes[0]), self.parser.get_pitch_from_midi(self.randomNotes[1]))

            guessNote = input("command: ")
            if (guessNote == "?"):
                self.playNotes()
                self.hits = 0
                print("Bad, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))
            elif (guessNote == "q"):
                break
            elif (guessNote == "p"):
                self.playChord()
            elif (guessNote == "n"):
                print("Next.")
                self.generateNewChallenge()
                self.hits += 1
                print("Good, hits = ", str(self.hits) + "/" + str(self.MAX_HITS))

        print("Finish successfully")
        return (self.hits)
