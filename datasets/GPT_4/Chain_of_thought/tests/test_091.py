import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_even_pair([1, 2, 3, 4]), 2)

    def test_all_even_numbers(self):
        self.assertEqual(find_even_pair([2, 4, 6, 8]), 6)

    def test_all_odd_numbers(self):
        self.assertEqual(find_even_pair([1, 3, 5, 7]), 6)

    def test_single_element_list(self):
        self.assertEqual(find_even_pair([1]), 0)

    def test_empty_list(self):
        self.assertEqual(find_even_pair([]), 0)

    def test_mixed_even_odd_numbers(self):
        self.assertEqual(find_even_pair([2, 3, 4, 5, 6]), 3)

    def test_duplicate_numbers(self):
        self.assertEqual(find_even_pair([1, 2, 2, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_even_pair([-2, -4, -3, -1]), 3)

    def test_large_list(self):
        large_list = list(range(1000))
        self.assertEqual(find_even_pair(large_list), 124750)

    def test_list_with_zero(self):
        self.assertEqual(find_even_pair([0, 1, 2, 3]), 2)

