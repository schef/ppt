from threading import Timer

import rtmidi

import pitchParser

CHANNEL = 0x90

class MidiPlayer():
    NOTE_DURATION = 1
    CLIENT_NAME = "ppt"
    PORT_NAME = "Output"

    def __init__(self):
        self.midi = rtmidi.MidiOut()
        self.midi.open_virtual_port("ppt")
        self.pp = pitchParser.PitchParser()

    def noteOn(self, note):
        # print("noteOn", note)
        self.midi.send_message([CHANNEL, note, 100])

    def noteOff(self, note):
        # print("noteOff", note)
        self.midi.send_message([CHANNEL, note, 0])

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
        self.midi.send_message(rtmidi.MidiMessage.allNotesOff())
