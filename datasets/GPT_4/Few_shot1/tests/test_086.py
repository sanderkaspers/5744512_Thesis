import unittest
from datasets.GPT_4.Few_shot1.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_remove_elements_basic(self): self.assertEqual(remove_elements([1, 2, 3], [2]), [1, 3])

    def test_remove_elements_no_common(self): self.assertEqual(remove_elements([1, 2, 3], [4, 5]), [1, 2, 3])

    def test_remove_elements_all_common(self): self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3]), [])

    def test_remove_elements_empty_list1(self): self.assertEqual(remove_elements([], [1, 2, 3]), [])

    def test_remove_elements_empty_list2(self): self.assertEqual(remove_elements([1, 2, 3], []), [1, 2, 3])

    def test_remove_elements_both_empty(self): self.assertEqual(remove_elements([], []), [])

    def test_remove_elements_duplicates_in_list1(self): self.assertEqual(remove_elements([1, 1, 2], [1]), [2])

    def test_remove_elements_duplicates_in_list2(self): self.assertEqual(remove_elements([1, 2, 3], [2, 2]), [1, 3])

    def test_remove_elements_strings(self): self.assertEqual(remove_elements(["a", "b", "c"], ["b"]), ["a", "c"])

    def test_remove_elements_mixed_types(self): self.assertEqual(remove_elements([1, "1", 2], ["1"]), [1, 2])

    def test_remove_elements_nested_lists(self): self.assertEqual(remove_elements([[1], [2]], [[2]]), [[1], [2]])

    def test_remove_elements_case_sensitive(self): self.assertEqual(remove_elements(["A", "a"], ["a"]), ["A"])

    def test_remove_elements_large_input(self): self.assertEqual(remove_elements(list(range(1000)), list(range(500))), list(range(500, 1000)))

    def test_remove_elements_none_values(self): self.assertEqual(remove_elements([None, 1], [1]), [None])

    def test_remove_elements_boolean_values(self): self.assertEqual(remove_elements([True, False, 1], [1]), [False])

