import platform

if "arm" in platform.machine() or "aarch64" in platform.machine():
    import midiPlayerAndroid
    class MidiPlayer(midiPlayerAndroid.MidiPlayer):
        pass
else:
    import midiPlayerRtmidi
    class MidiPlayer(midiPlayerRtmidi.MidiPlayer):
        pass
