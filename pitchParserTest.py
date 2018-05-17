import unittest

import pitchParser

pp = pitchParser.PitchParser()

class PitchParserTest(unittest.TestCase):
    def test_is_midi_pitch(self):
        self.assertTrue(pp.is_midi_pitch(60, "c"))
        self.assertTrue(pp.is_midi_pitch(61, "cis"))
        self.assertTrue(pp.is_midi_pitch(62, "d"))
        self.assertTrue(pp.is_midi_pitch(63, "dis"))
        self.assertTrue(pp.is_midi_pitch(64, "e"))
        self.assertTrue(pp.is_midi_pitch(65, "f"))
        self.assertTrue(pp.is_midi_pitch(66, "fis"))
        self.assertTrue(pp.is_midi_pitch(67, "g"))
        self.assertTrue(pp.is_midi_pitch(68, "gis"))
        self.assertTrue(pp.is_midi_pitch(69, "a"))
        self.assertTrue(pp.is_midi_pitch(70, "ais"))
        self.assertTrue(pp.is_midi_pitch(71, "h"))

        self.assertTrue(pp.is_midi_pitch(61, "des"))
        self.assertTrue(pp.is_midi_pitch(63, "es"))
        self.assertTrue(pp.is_midi_pitch(66, "ges"))
        self.assertTrue(pp.is_midi_pitch(68, "as"))
        self.assertTrue(pp.is_midi_pitch(70, "b"))

        self.assertFalse(pp.is_midi_pitch(61, "c"))

        self.assertTrue(pp.is_midi_pitch(60, "c''"))
        self.assertTrue(pp.is_midi_pitch(60, "c,"))

    def test_get_octave_from_pitch(self):
        self.assertEqual(pp.get_octave_from_pitch("c"), pp.MIDI_BASE)
        self.assertEqual(pp.get_octave_from_pitch("c'"), pp.MIDI_BASE + 12 * 1)
        self.assertEqual(pp.get_octave_from_pitch("c''"), pp.MIDI_BASE + 12 * 2)
        self.assertEqual(pp.get_octave_from_pitch("c'''"), pp.MIDI_BASE + 12 * 3)
        self.assertEqual(pp.get_octave_from_pitch("c,"), pp.MIDI_BASE - 12 * 1)
        self.assertEqual(pp.get_octave_from_pitch("c,,"), pp.MIDI_BASE - 12 * 2)
        self.assertEqual(pp.get_octave_from_pitch("c,,,"), pp.MIDI_BASE - 12 * 3)

    def test_get_midi_from_pitch(self):
        self.assertEqual(pp.get_midi_from_pitch("c"), pp.MIDI_BASE)
        self.assertEqual(pp.get_midi_from_pitch("cis"), pp.MIDI_BASE + 1)
        self.assertEqual(pp.get_midi_from_pitch("d"), pp.MIDI_BASE + 2)
        self.assertEqual(pp.get_midi_from_pitch("dis"), pp.MIDI_BASE + 3)

    def test_get_octave_from_midi(self):
        self.assertEqual(pp.get_octave_from_midi(pp.MIDI_BASE), "")
        self.assertEqual(pp.get_octave_from_midi(pp.MIDI_BASE + 12 * 1), "'")
        self.assertEqual(pp.get_octave_from_midi(pp.MIDI_BASE + 12 * 2), "''")
        self.assertEqual(pp.get_octave_from_midi(pp.MIDI_BASE + 12 * 3), "'''")
        self.assertEqual(pp.get_octave_from_midi(pp.MIDI_BASE - 12 * 1), ",")
        self.assertEqual(pp.get_octave_from_midi(pp.MIDI_BASE - 12 * 2), ",,")
        self.assertEqual(pp.get_octave_from_midi(pp.MIDI_BASE - 12 * 3), ",,,")

    def test_get_pitch_from_midi(self):
        self.assertEqual(pp.get_pitch_from_midi(pp.MIDI_BASE), "c")
        self.assertEqual(pp.get_pitch_from_midi(pp.MIDI_BASE + 1 + 12 * 1), "cis'")
        self.assertEqual(pp.get_pitch_from_midi(pp.MIDI_BASE - 1 - 12 * 1), "h,,")

if __name__ == '__main__':
    unittest.main()
