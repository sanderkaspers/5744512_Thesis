import unittest
from datasets.o3.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_sequence_base_cases(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_sequence_small_n(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 2)
        self.assertEqual(sequence(5), 3)

    def test_sequence_larger_n(self):
        self.assertEqual(sequence(10), 9)

    def test_sequence_negative(self):
        with self.assertRaises(RecursionError):
            sequence(-1)

    def test_sequence_zero(self):
        with self.assertRaises(RecursionError):
            sequence(0)

