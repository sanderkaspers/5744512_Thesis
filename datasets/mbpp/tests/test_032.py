import unittest
from datasets.mbpp.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_sequence_with_10_expect_6(self):
        self.assertEqual(sequence(10), 6)

    def test_sequence_with_2_expect_1(self):
        self.assertEqual(sequence(2), 1)

    def test_sequence_with_3_expect_2(self):
        self.assertEqual(sequence(3), 2)

