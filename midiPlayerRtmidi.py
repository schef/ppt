from threading import Timer

from rtmidi.midiconstants import NOTE_ON, NOTE_OFF, CONTROLLER_CHANGE, ALL_NOTES_OFF
from rtmidi.midiutil import open_midioutput

import pitchParser

class MidiPlayer():
    NOTE_DURATION = 1
    CLIENT_NAME = "ppt"
    PORT_NAME = "Output"

    def __init__(self):
        self.midiout_notes, self.port_name = open_midioutput(use_virtual=True, client_name=self.CLIENT_NAME,
                                                             port_name=self.PORT_NAME)
        self.pp = pitchParser.PitchParser()

    def noteOn(self, note):
        # print("noteOn", note)
        self.midiout_notes.send_message([NOTE_ON, note, 100])

    def noteOff(self, note):
        # print("noteOff", note)
        self.midiout_notes.send_message([NOTE_OFF, note, 0])

    def playMultipleNotesMelodicly(self, pitchList):
        # print("playMultipleNotesMelodicly", notes)
        pitchListCopy = list(pitchList)
        pitch = pitchListCopy.pop(0)
        midi = self.pp.get_midi_from_pitch(pitch)
        self.noteOn(midi)
        Timer(self.NOTE_DURATION, self.noteOff, [midi]).start()
        if len(pitchListCopy) > 0:
            Timer(self.NOTE_DURATION, self.playMultipleNotesMelodicly, [pitchListCopy]).start()

    def playMultipleNotesHarmonicly(self, pitchList):
        # print("playMultipleNotesHarmonicly", notes)
        for pitch in pitchList:
            midi = self.pp.get_midi_from_pitch(pitch)
            self.noteOn(midi)
            Timer(self.NOTE_DURATION, self.noteOff, [midi]).start()

    def allNotesOff(self):
        self.midiout_notes.send_message([CONTROLLER_CHANGE, ALL_NOTES_OFF, 0])
