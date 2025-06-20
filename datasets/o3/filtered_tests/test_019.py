import unittest
from datasets.o3.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_bell_zero(self):
        self.assertEqual(bell_number(0), 1)

    def test_bell_one(self):
        self.assertEqual(bell_number(1), 1)

    def test_bell_two(self):
        self.assertEqual(bell_number(2), 2)

    def test_bell_five(self):
        self.assertEqual(bell_number(5), 52)

