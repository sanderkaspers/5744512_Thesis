import unittest
from datasets.o3.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_no_common_elements(self):
        self.assertEqual(remove_elements([1, 2, 3], [4, 5]), [1, 2, 3])

    def test_some_common_elements(self):
        self.assertEqual(remove_elements([1, 2, 3], [2, 4]), [1, 3])

    def test_all_elements_removed(self):
        self.assertEqual(remove_elements([1, 1], [1]), [])

    def test_list1_empty(self):
        self.assertEqual(remove_elements([], [1, 2]), [])

    def test_list2_empty(self):
        self.assertEqual(remove_elements([1, 2], []), [1, 2])

    def test_duplicates_in_list1(self):
        self.assertEqual(remove_elements([1, 1, 2, 3], [1]), [2, 3])

    def test_duplicates_in_list2(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 1, 2]), [3])

    def test_mixed_types(self):
        self.assertEqual(remove_elements([1, 'a', 2], ['a', 3]), [1, 2])

