import re

class PitchParser:
    MIDI_BASE = 48
    pitchMidiBase = {
        "c": 0,
        "cis": 1,
        "d": 2,
        "dis": 3,
        "e": 4,
        "f": 5,
        "fis": 6,
        "g": 7,
        "gis": 8,
        "a": 9,
        "ais": 10,
        "h": 11,
        "des": 1,
        "es": 3,
        "ges": 6,
        "as": 8,
        "b": 10,
    }

    def __init__(self):
        pass

    def is_midi_pitch(self, midi, pitch):
        pitch = re.sub('[\',]', '', pitch)
        return midi % 12 == self.pitchMidiBase[pitch]

    def get_octave_from_pitch(self, pitch):
        octave = 0
        for i in pitch:
            if i == "'":
                octave += 1
            elif i == ",":
                octave -= 1
        return self.MIDI_BASE + octave * 12

    def get_midi_from_pitch(self, pitch):
        octave = self.get_octave_from_pitch(pitch)
        pitch = re.sub('[\',]', '', pitch)
        return self.pitchMidiBase[pitch] + octave

    def get_octave_from_midi(self, midi):
        rest = midi % 12
        center = int(self.MIDI_BASE / 12)
        octave = int((midi - rest) / 12)
        centerOctave = (octave - center)
        if centerOctave > 0:
            return "'" * centerOctave
        elif centerOctave < 0:
            return "," * abs(centerOctave)
        else:
            return ""

    def get_pitch_from_midi(self, midi):
        octave = self.get_octave_from_midi(midi)
        for name, midiBase in self.pitchMidiBase.items():
            if midiBase == midi % 12:
                return name + octave
        return ''

    def get_midi_list_from_pitch_list(self, pitchList):
        midiList = []
        for pitch in pitchList:
            midiList.append(self.get_midi_from_pitch(pitch))
        return midiList