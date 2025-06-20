import unittest
from datasets.GPT_4.Zero_shot2.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_freq_1(self):
        self.assertEqual(frequency_lists(['a', 'b', 'a']), {'a': 2, 'b': 1})

    def test_freq_2(self):
        self.assertEqual(frequency_lists(['a', '', 'b', '', 'a']), {'a': 2, 'b': 1})

    def test_freq_3(self):
        self.assertEqual(frequency_lists(['', '', '']), {})

    def test_freq_4(self):
        self.assertEqual(frequency_lists(['x']), {'x': 1})

    def test_freq_5(self):
        self.assertEqual(frequency_lists(['z', 'z', 'z']), {'z': 3})

    def test_freq_6(self):
        self.assertEqual(frequency_lists([]), {})

    def test_freq_7(self):
        self.assertEqual(frequency_lists(['a', 'A', 'a']), {'a': 2, 'A': 1})

    def test_freq_8(self):
        self.assertEqual(frequency_lists([' ', ' ', '\t']), {' ': 2, '\t': 1})

    def test_freq_9(self):
        self.assertEqual(frequency_lists(['1', '2', '1']), {'1': 2, '2': 1})

    def test_freq_10(self):
        self.assertEqual(frequency_lists(['!', '@', '!']), {'!': 2, '@': 1})

    def test_freq_11(self):
        self.assertEqual(frequency_lists(['a'] * 1000), {'a': 1000})

    def test_freq_12(self):
        self.assertEqual(frequency_lists(['1', 1, '']), {'1': 1, 1: 1})

    def test_freq_13(self):
        self.assertEqual(frequency_lists(['x', 'y', 'z']), {'x': 1, 'y': 1, 'z': 1})

    def test_freq_14(self):
        self.assertEqual(frequency_lists(['', 'a', '', 'a']), {'a': 2})

    def test_freq_15(self):
        self.assertEqual(frequency_lists(['test', 'test', 'TEST']), {'test': 2, 'TEST': 1})

