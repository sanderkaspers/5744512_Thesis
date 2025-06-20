import unittest
from datasets.GPT_4.Few_shot1.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_index_minimum_basic(self): self.assertEqual(index_minimum([('a', 2), ('b', 1)]), 'b')

    def test_index_minimum_first_min(self): self.assertEqual(index_minimum([('x', 0), ('y', 5), ('z', 10)]), 'x')

    def test_index_minimum_last_min(self): self.assertEqual(index_minimum([('x', 9), ('y', 5), ('z', -1)]), 'z')

    def test_index_minimum_all_equal(self): self.assertEqual(index_minimum([('a', 3), ('b', 3), ('c', 3)]), 'a')

    def test_index_minimum_negative_values(self): self.assertEqual(index_minimum([('a', -5), ('b', -10), ('c', -3)]), 'b')

    def test_index_minimum_single_tuple(self): self.assertEqual(index_minimum([('solo', 99)]), 'solo')

