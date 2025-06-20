import unittest
from datasets.GPT_4.Zero_shot2.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_seq_1(self):
        self.assertEqual(sequence(1), 1)

    def test_seq_2(self):
        self.assertEqual(sequence(2), 1)

    def test_seq_3(self):
        self.assertEqual(sequence(3), 2)

    def test_seq_4(self):
        self.assertEqual(sequence(5), 5)

    def test_seq_5(self):
        self.assertEqual(sequence(10), 55)

