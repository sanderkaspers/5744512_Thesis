import unittest
from datasets.GPT_4.Zero_shot1.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bell_number(1), 1)

    def test_2(self):
        self.assertEqual(bell_number(2), 2)

    def test_3(self):
        self.assertEqual(bell_number(3), 5)

    def test_4(self):
        self.assertEqual(bell_number(4), 15)

    def test_5(self):
        self.assertEqual(bell_number(5), 52)

    def test_6(self):
        self.assertEqual(bell_number(6), 203)

    def test_7(self):
        self.assertEqual(bell_number(10), 115975)

