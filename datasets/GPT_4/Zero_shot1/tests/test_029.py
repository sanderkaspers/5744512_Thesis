import unittest
from datasets.GPT_4.Zero_shot1.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(tetrahedral_number(1), 1)

    def test_2(self):
        self.assertEqual(tetrahedral_number(2), 4)

    def test_3(self):
        self.assertEqual(tetrahedral_number(3), 10)

    def test_4(self):
        self.assertEqual(tetrahedral_number(4), 20)

    def test_5(self):
        self.assertEqual(tetrahedral_number(5), 35)

    def test_6(self):
        self.assertEqual(tetrahedral_number(50), 22100)

