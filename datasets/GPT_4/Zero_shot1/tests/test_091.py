import unittest
from datasets.GPT_4.Zero_shot1.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_even_pair([1, 3, 5]), 3)

    def test_2(self):
        self.assertEqual(find_even_pair([1, 2, 3, 4]), 2)

    def test_3(self):
        self.assertEqual(find_even_pair([]), 0)

    def test_4(self):
        self.assertEqual(find_even_pair([7]), 0)

    def test_5(self):
        self.assertEqual(find_even_pair([1, 1, 1]), 3)

    def test_6(self):
        self.assertEqual(find_even_pair([-2, -4, -6]), 3)

    def test_7(self):
        self.assertIsInstance(find_even_pair([1, 2]), int)

