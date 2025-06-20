import unittest
from datasets.GPT_4.Zero_shot2.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_freq_1(self):
        self.assertEqual(frequency([1, 2, 3, 2, 2], 2), 3)

    def test_freq_2(self):
        self.assertEqual(frequency([1, 2, 3], 3), 1)

    def test_freq_3(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)

    def test_freq_4(self):
        self.assertEqual(frequency([], 1), 0)

    def test_freq_5(self):
        self.assertEqual(frequency([5, 5, 5, 5], 5), 4)

    def test_freq_6(self):
        self.assertEqual(frequency(['a', 1, '1', 1], 1), 2)

    def test_freq_7(self):
        self.assertEqual(frequency([[1], 1, [1]], [1]), 2)

    def test_freq_8(self):
        self.assertEqual(frequency(['A', 'a', 'A'], 'a'), 1)

    def test_freq_9(self):
        self.assertEqual(frequency([-1, -1, 1], -1), 2)

    def test_freq_10(self):
        self.assertEqual(frequency([1.0, 1, '1'], 1), 2)

    def test_freq_11(self):
        self.assertEqual(frequency(list(range(10000)) + [5]*10, 5), 11)

