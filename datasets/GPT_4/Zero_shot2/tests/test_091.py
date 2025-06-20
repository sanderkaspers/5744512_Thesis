import unittest
from datasets.GPT_4.Zero_shot2.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_pair_1(self):
        self.assertEqual(find_even_pair([2, 4, 6]), 3)

    def test_pair_2(self):
        self.assertEqual(find_even_pair([1, 3, 5]), 3)

    def test_pair_3(self):
        self.assertEqual(find_even_pair([1, 2, 3, 4]), 2)

    def test_pair_4(self):
        self.assertEqual(find_even_pair([1]), 0)

    def test_pair_5(self):
        self.assertEqual(find_even_pair([2, 2]), 1)

    def test_pair_6(self):
        self.assertEqual(find_even_pair([1, 2]), 0)

    def test_pair_7(self):
        self.assertEqual(find_even_pair([]), 0)

    def test_pair_8(self):
        self.assertEqual(find_even_pair([1, 1, 1, 1]), 6)

    def test_pair_9(self):
        self.assertEqual(find_even_pair([-2, 2, -3, 3]), 2)

    def test_pair_10(self):
        self.assertEqual(find_even_pair(list(range(1, 21))), 50)

