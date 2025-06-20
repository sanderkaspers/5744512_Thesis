import unittest
from datasets.GPT_4.Zero_shot1.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_octagonal(2), 10)

    def test_2(self):
        self.assertEqual(is_octagonal(3), 24)

    def test_3(self):
        self.assertEqual(is_octagonal(4), 43)

    def test_4(self):
        self.assertEqual(is_octagonal(0), 0)

    def test_5(self):
        self.assertEqual(is_octagonal(5), 67)

    def test_6(self):
        self.assertEqual(is_octagonal(-1), 5)

