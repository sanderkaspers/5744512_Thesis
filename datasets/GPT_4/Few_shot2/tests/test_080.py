import unittest
from datasets.GPT_4.Few_shot2.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_extract_singly_all_unique(self): self.assertEqual(extract_singly([1, 2, 3]), [1, 2, 3])

    def test_extract_singly_no_unique(self): self.assertEqual(extract_singly([1, 1, 2, 2]), [])

    def test_extract_singly_some_unique(self): self.assertEqual(extract_singly([1, 2, 2, 3, 4, 4]), [1, 3])

    def test_extract_singly_empty(self): self.assertEqual(extract_singly([]), [])

    def test_extract_singly_single_element(self): self.assertEqual(extract_singly([5]), [5])

    def test_extract_singly_all_same(self): self.assertEqual(extract_singly([9, 9, 9]), [])

    def test_extract_singly_with_strings(self): self.assertEqual(extract_singly(['a', 'b', 'a', 'c']), ['b', 'c'])

    def test_extract_singly_mixed_types(self): self.assertEqual(extract_singly(['x', 1, 'x', 2]), [1, 2])

    def test_extract_singly_with_nested_lists(self): self.assertRaises(TypeError, extract_singly, [[1], [1]])

