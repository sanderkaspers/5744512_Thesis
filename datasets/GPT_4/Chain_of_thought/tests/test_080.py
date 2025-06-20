import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_singly([[1, 2], [3, 4], [5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_duplicates_across_sublists(self):
        self.assertEqual(extract_singly([[1, 2], [2, 3], [3, 4]]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(extract_singly([]), [])

    def test_single_sublist_with_duplicates(self):
        self.assertEqual(extract_singly([[1, 2, 2, 3]]), [1, 2, 3])

    def test_single_element_sublists(self):
        self.assertEqual(extract_singly([[1], [2], [3]]), [1, 2, 3])

    def test_mixed_data_types(self):
        self.assertEqual(extract_singly([[1, '2', 3.0], [4, '5', 6.0]]), [1, '2', 3.0, 4, '5', 6.0])

    def test_nested_empty_sublists(self):
        self.assertEqual(extract_singly([[], [], [1, 2]]), [1, 2])

    def test_large_nested_list(self):
        large_list = [[i] for i in range(1000)]
        self.assertEqual(extract_singly(large_list), list(range(1000)))

    def test_all_identical_sublists(self):
        self.assertEqual(extract_singly([[1, 2], [1, 2], [1, 2]]), [1, 2])

    def test_negative_numbers(self):
        self.assertEqual(extract_singly([[1, -2], [-3, 4], [-2, 5]]), [1, -2, -3, 4, 5])

