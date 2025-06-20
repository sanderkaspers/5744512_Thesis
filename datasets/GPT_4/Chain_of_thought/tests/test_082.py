import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 4, 3], [1, 2, 3]), 2)

    def test_no_identical_elements(self):
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)

    def test_all_identical_elements(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_different_length_lists(self):
        self.assertEqual(count_samepair([1, 2, 3, 4], [1, 2, 3], [1, 2]), 2)

    def test_single_element_lists(self):
        self.assertEqual(count_samepair([1], [1], [1]), 1)

    def test_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_mixed_data_types(self):
        self.assertEqual(count_samepair([1, '2', 3.0], [1, '2', 3.0], [1, '2', 3.0]), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_samepair([-1, -2, -3], [-1, -2, -3], [-1, -2, -3]), 3)

    def test_floating_point_numbers(self):
        self.assertEqual(count_samepair([1.1, 2.2, 3.3], [1.1, 2.2, 3.3], [1.1, 2.2, 3.3]), 3)

    def test_repeated_values(self):
        self.assertEqual(count_samepair([1, 2, 1], [1, 2, 1], [1, 2, 1]), 3)

