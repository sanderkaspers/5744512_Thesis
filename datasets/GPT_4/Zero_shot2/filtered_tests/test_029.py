import unittest
from datasets.GPT_4.Zero_shot2.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_tetra_1(self):
        self.assertEqual(tetrahedral_number(0), 0)

    def test_tetra_2(self):
        self.assertEqual(tetrahedral_number(1), 1)

    def test_tetra_3(self):
        self.assertEqual(tetrahedral_number(2), 4)

    def test_tetra_4(self):
        self.assertEqual(tetrahedral_number(3), 10)

    def test_tetra_5(self):
        self.assertEqual(tetrahedral_number(10), 220)

    def test_tetra_6(self):
        self.assertEqual(tetrahedral_number(-1), 0)

