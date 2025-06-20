import unittest
from datasets.o3.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_recursive_sum_flat(self):
        self.assertEqual(recursive_list_sum([1,2,3]), 6)

    def test_recursive_sum_nested(self):
        self.assertEqual(recursive_list_sum([1,[2,[3],4],5]), 15)

    def test_recursive_sum_empty(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_recursive_sum_negative_numbers(self):
        self.assertEqual(recursive_list_sum([-1,[-2,3]]), 0)

    def test_recursive_sum_single_element(self):
        self.assertEqual(recursive_list_sum([[5]]), 5)

    def test_recursive_sum_invalid_element_raises(self):
        with self.assertRaises(TypeError):
            recursive_list_sum([1,'a',2])

