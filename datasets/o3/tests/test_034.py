import unittest
from datasets.o3.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_centered_hexagonal_n1(self):
        self.assertEqual(centered_hexagonal_number(1), 1)

    def test_centered_hexagonal_n2(self):
        self.assertEqual(centered_hexagonal_number(2), 7)

    def test_centered_hexagonal_n3(self):
        self.assertEqual(centered_hexagonal_number(3), 19)

    def test_centered_hexagonal_large(self):
        self.assertEqual(centered_hexagonal_number(1000), 3*1000*(999)+1)

    def test_centered_hexagonal_zero_negative(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(-1), 3 * -1 * (-2) + 1)

