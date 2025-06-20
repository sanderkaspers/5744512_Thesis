import unittest
from datasets.GPT_4.Zero_shot2.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_octagonal_1(self):
        self.assertEqual(is_octagonal(1), 1)

    def test_octagonal_2(self):
        self.assertEqual(is_octagonal(2), 10)

    def test_octagonal_3(self):
        self.assertEqual(is_octagonal(3), 24)

    def test_octagonal_4(self):
        self.assertEqual(is_octagonal(0), 0)

    def test_octagonal_5(self):
        self.assertEqual(is_octagonal(-1), 5)

