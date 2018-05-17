from threading import Timer

from rtmidi.midiconstants import NOTE_ON, NOTE_OFF, CONTROLLER_CHANGE, ALL_NOTES_OFF
from rtmidi.midiutil import open_midioutput

class MidiPlayer():
    NOTE_DURATION = 1
    CLIENT_NAME = "ppt"
    PORT_NAME = "Output"

    def __init__(self):
        self.midiout_notes, self.port_name = open_midioutput(use_virtual=True, client_name=self.CLIENT_NAME,
                                                             port_name=self.PORT_NAME)

    def noteOn(self, note):
        # print("noteOn", note)
        self.midiout_notes.send_message([NOTE_ON, note, 100])

    def noteOff(self, note):
        # print("noteOff", note)
        self.midiout_notes.send_message([NOTE_OFF, note, 0])

    def playSingleNote(self, note):
        # print("playSingleNote", note)
        self.noteOn(note)
        Timer(self.NOTE_DURATION, self.noteOff, [note]).start()

    def playMultipleNotesMelodicly(self, notes):
        # print("playMultipleNotesMelodicly", notes)
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
        self.midiout_notes.send_message([CONTROLLER_CHANGE, ALL_NOTES_OFF, 0])
