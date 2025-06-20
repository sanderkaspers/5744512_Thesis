import unittest
from datasets.o3.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(next_power_of_2(0), 1)

    def test_exact_power_of_two(self):
        self.assertEqual(next_power_of_2(16), 16)

    def test_one(self):
        self.assertEqual(next_power_of_2(1), 1)

    def test_non_power_small(self):
        self.assertEqual(next_power_of_2(3), 4)

    def test_non_power_medium(self):
        self.assertEqual(next_power_of_2(5), 8)

    def test_non_power_large(self):
        self.assertEqual(next_power_of_2(31), 32)

    def test_large_number(self):
        self.assertEqual(next_power_of_2(1025), 2048)

