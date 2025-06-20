import unittest
from datasets.GPT_4.Few_shot2.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_remove_elements_basic(self): self.assertEqual(remove_elements([1, 2, 3], [2]), [1, 3])

    def test_remove_elements_all_removed(self): self.assertEqual(remove_elements([1, 2], [1, 2]), [])

    def test_remove_elements_none_removed(self): self.assertEqual(remove_elements([1, 2], [3, 4]), [1, 2])

    def test_remove_elements_empty_list1(self): self.assertEqual(remove_elements([], [1, 2]), [])

    def test_remove_elements_empty_list2(self): self.assertEqual(remove_elements([1, 2], []), [1, 2])

    def test_remove_elements_duplicates_in_list1(self): self.assertEqual(remove_elements([1, 2, 2, 3], [2]), [1, 3])

    def test_remove_elements_with_strings(self): self.assertEqual(remove_elements(['a', 'b', 'c'], ['b']), ['a', 'c'])

    def test_remove_elements_with_mixed_types(self): self.assertEqual(remove_elements([1, '1', 2], ['1']), [1, 2])

    def test_remove_elements_identical_lists(self): self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3]), [])

