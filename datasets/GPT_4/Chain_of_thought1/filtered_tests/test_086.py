import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_overlap(self): self.assertEqual(remove_elements([1, 2, 3], [2, 4]), [1, 3])

    def test_no_overlap(self): self.assertEqual(remove_elements([1, 2], [3, 4]), [1, 2])

    def test_all_removed(self): self.assertEqual(remove_elements([1, 2], [1, 2]), [])

    def test_empty_list2(self): self.assertEqual(remove_elements([1, 2], []), [1, 2])

    def test_empty_list1(self): self.assertEqual(remove_elements([], [1, 2]), [])

    def test_both_empty(self): self.assertEqual(remove_elements([], []), [])

    def test_duplicates(self): self.assertEqual(remove_elements([1, 1, 2], [1]), [2])

    def test_unmatched_types(self): self.assertEqual(remove_elements([1, 2], ['a', 'b']), [1, 2])

    def test_type_equality(self): self.assertEqual(remove_elements([1, '1', True], [1]), ['1'])

    def test_nested_lists(self): self.assertEqual(remove_elements([[1], [2]], [[1]]), [[2]])

    def test_unhashable_in_list2(self): self.assertEqual(remove_elements([[1], [2]], [[2]]), [[1]])

