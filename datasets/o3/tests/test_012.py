import unittest
from datasets.o3.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_octagonal_first(self):
        self.assertEqual(is_octagonal(1), 1)

    def test_octagonal_small(self):
        self.assertEqual(is_octagonal(5), 65)

    def test_octagonal_zero(self):
        self.assertEqual(is_octagonal(0), 0)

    def test_octagonal_negative(self):
        self.assertEqual(is_octagonal(-3), 3 * (-3) * (-3) - 2 * (-3))

