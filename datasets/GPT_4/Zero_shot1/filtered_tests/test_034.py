import unittest
from datasets.GPT_4.Zero_shot1.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(centered_hexagonal_number(1), 1)

    def test_2(self):
        self.assertEqual(centered_hexagonal_number(2), 7)

    def test_3(self):
        self.assertEqual(centered_hexagonal_number(3), 19)

    def test_4(self):
        self.assertEqual(centered_hexagonal_number(4), 37)

    def test_5(self):
        self.assertEqual(centered_hexagonal_number(5), 61)

    def test_6(self):
        self.assertEqual(centered_hexagonal_number(50), 7351)

    def test_7(self):
        self.assertEqual(centered_hexagonal_number(1e3), 2997001.0)

    def test_8(self):
        self.assertEqual(centered_hexagonal_number(10), centered_hexagonal_number(10))

