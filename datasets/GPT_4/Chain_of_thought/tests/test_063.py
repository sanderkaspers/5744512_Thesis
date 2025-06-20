import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(search([1, 1, 2, 2, 3]), 3)

    def test_single_element_array(self):
        self.assertEqual(search([1]), 1)

    def test_all_identical_elements(self):
        self.assertEqual(search([1, 1, 1, 1]), 0)

    def test_multiple_pairs_one_unique(self):
        self.assertEqual(search([4, 4, 5, 5, 6, 6, 7]), 7)

    def test_large_array(self):
        large_array = list(range(1, 10001)) + [10001] + list(range(1, 10001))
        self.assertEqual(search(large_array), 10001)

    def test_negative_numbers(self):
        self.assertEqual(search([-1, -1, -2, -2, -3]), -3)

    def test_mixed_positive_negative_numbers(self):
        self.assertEqual(search([-1, 1, -1, 2, 2]), 1)

    def test_array_with_zero(self):
        self.assertEqual(search([0, 1, 1, 2, 2]), 0)

    def test_empty_array(self):
        self.assertEqual(search([]), 0)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            search([1, 2, 'three', 2, 1])

