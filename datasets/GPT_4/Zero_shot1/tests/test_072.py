import unittest
from datasets.GPT_4.Zero_shot1.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertIn(max_occurrences([4, 4, 5, 5]), [4, 5])

    def test_2(self):
        self.assertIn(max_occurrences([1, 2, 3]), [1, 2, 3])

    def test_3(self):
        self.assertEqual(max_occurrences([7, 7, 7]), 7)

    def test_4(self):
        self.assertEqual(max_occurrences(["a", "b", "a"]), "a")

    def test_5(self):
        self.assertEqual(max_occurrences(["x", 1, "x", 1, 1]), 1)

    def test_6(self):
        self.assertIn(max_occurrences([9, 8, 9]), [9])

