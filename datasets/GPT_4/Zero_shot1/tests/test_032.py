import unittest
from datasets.GPT_4.Zero_shot1.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sequence(2), 1)

    def test_2(self):
        self.assertEqual(sequence(3), 2)

    def test_3(self):
        self.assertEqual(sequence(4), 3)

    def test_4(self):
        self.assertEqual(sequence(5), 5)

    def test_5(self):
        self.assertEqual(sequence(6), 8)

    def test_6(self):
        self.assertEqual(sequence(7), 13)

    def test_7(self):
        self.assertEqual(sequence(10), 55)

    def test_8(self):
        self.assertEqual(sequence(20), 6765)

