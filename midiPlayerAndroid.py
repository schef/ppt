from threading import Timer
from androidhelper import Android

class MidiPlayer():
    NOTE_DURATION = 1
    CLIENT_NAME = "ppt"
    PORT_NAME = "Output"
    PRENAME = "/mnt/sdcard/rar/ppt/ppt/ogg/"
    POSTNAME = ".ogg"

    def __init__(self):
        self.midiout_notes = Android()

    def noteOn(self, note):
        # print("noteOn", note)
        self.midiout_notes.mediaPlay(self.PRENAME + str(note) + self.POSTNAME, str(note))

    def noteOff(self, note):
        # print("noteOff", note)
        self.midiout_notes.mediaPlayClose(str(note))

    def playSingleNote(self, note):
        # print("playSingleNote", note)
        self.noteOn(note)
        Timer(self.NOTE_DURATION, self.noteOff, [note]).start()

    def playMultipleNotesMelodicly(self, originalNotes):
        # print("playMultipleNotesMelodicly", notes)
        notes = list(originalNotes)
        note = notes.pop(0)
        self.noteOn(note)
        Timer(self.NOTE_DURATION, self.noteOff, [note]).start()
        if len(notes) > 0:
            Timer(self.NOTE_DURATION, self.playMultipleNotesMelodicly, [notes]).start()

    def playMultipleNotesHarmonicly(self, notes):
        # print("playMultipleNotesHarmonicly", notes)
        for note in notes:
            self.noteOn(note)
            Timer(self.NOTE_DURATION, self.noteOff, [note]).start()

    def allNotesOff(self):
        for i in self.midiout_notes.mediaPlayList():
            self.midiout_notes.mediaPlayClose(i)
