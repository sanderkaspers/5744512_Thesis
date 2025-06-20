import unittest
from datasets.o3.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_even_pair([]), 0)

    def test_single_element(self):
        self.assertEqual(find_even_pair([2]), 0)

    def test_all_even_xor(self):
        self.assertEqual(find_even_pair([1,3,5]), 3)

    def test_mixed_even_odd(self):
        self.assertEqual(find_even_pair([1,2,3]), 1)

    def test_all_zeros(self):
        self.assertEqual(find_even_pair([0,0,0]), 3)

    def test_large_input(self):
        arr = list(range(100))
        self.assertTrue(find_even_pair(arr) >= 0)

