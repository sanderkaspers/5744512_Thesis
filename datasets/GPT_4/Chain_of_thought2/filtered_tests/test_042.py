import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_distinct_second_values(self): self.assertEqual(index_minimum([('a', 5), ('b', 2), ('c', 8)]), 'b')

    def test_duplicate_minimums(self): self.assertEqual(index_minimum([('x', 3), ('y', 1), ('z', 1)]), 'y')

    def test_negative_second_values(self): self.assertEqual(index_minimum([('neg', -10), ('zero', 0), ('pos', 5)]), 'neg')

    def test_float_second_values(self): self.assertEqual(index_minimum([('apple', 2.5), ('banana', 1.2), ('cherry', 3.8)]), 'banana')

    def test_mixed_first_elements(self): self.assertEqual(index_minimum([(1, 100), ('a', 50), (3.14, 30)]), 3.14)

    def test_single_tuple(self): self.assertEqual(index_minimum([('only', 42)]), 'only')

    def test_all_same_second_value(self): self.assertEqual(index_minimum([('x', 5), ('y', 5), ('z', 5)]), 'x')

