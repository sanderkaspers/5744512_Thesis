import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_some_elements_removed(self): self.assertEqual(remove_elements([1, 2, 3, 4], [2, 4]), [1, 3])

    def test_no_elements_common(self): self.assertEqual(remove_elements([1, 2, 3], [4, 5]), [1, 2, 3])

    def test_all_elements_removed(self): self.assertEqual(remove_elements([1, 2], [1, 2]), [])

    def test_empty_list1(self): self.assertEqual(remove_elements([], [1, 2]), [])

    def test_empty_list2(self): self.assertEqual(remove_elements([1, 2], []), [1, 2])

    def test_duplicates_in_list1(self): self.assertEqual(remove_elements([1, 1, 2, 3], [1]), [2, 3])

    def test_duplicates_in_list2(self): self.assertEqual(remove_elements([1, 2, 3], [2, 2]), [1, 3])

    def test_case_sensitive_strings(self): self.assertEqual(remove_elements(['A', 'a', 'B'], ['a']), ['A', 'B'])

    def test_mixed_types(self): self.assertEqual(remove_elements([1, '1', 2.0], ['1', 2]), [1, 2.0])

    def test_large_input(self): self.assertEqual(remove_elements(list(range(1000)), list(range(500))), list(range(500, 1000)))

