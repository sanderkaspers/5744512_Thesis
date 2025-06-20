import unittest
from datasets.GPT_4.Zero_shot2.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_bell_1(self):
        self.assertEqual(bell_number(0), 1)

    def test_bell_2(self):
        self.assertEqual(bell_number(1), 1)

    def test_bell_3(self):
        self.assertEqual(bell_number(2), 2)

    def test_bell_4(self):
        self.assertEqual(bell_number(3), 5)

    def test_bell_5(self):
        self.assertEqual(bell_number(5), 52)

