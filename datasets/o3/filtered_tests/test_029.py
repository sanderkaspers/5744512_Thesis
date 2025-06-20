import unittest
from datasets.o3.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(tetrahedral_number(0), 0)

    def test_one(self):
        self.assertEqual(tetrahedral_number(1), 1)

    def test_two(self):
        self.assertEqual(tetrahedral_number(2), 4)

    def test_five(self):
        self.assertEqual(tetrahedral_number(5), 35)

    def test_ten(self):
        self.assertEqual(tetrahedral_number(10), 220)

