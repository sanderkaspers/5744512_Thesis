import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_both_numeric_strings(self): self.assertEqual(list_to_float([['1', '2']]), [(1.0, 2.0)])

    def test_one_alpha_one_numeric(self): self.assertEqual(list_to_float([['a', '3']]), [('a', 3.0)])

    def test_both_alpha(self): self.assertEqual(list_to_float([['x', 'y']]), [('x', 'y')])

    def test_mixed_case_alpha(self): self.assertEqual(list_to_float([['A', 'b']]), [('A', 'b')])

    def test_multiple_pairs(self): self.assertEqual(list_to_float([['1', '2'], ['3.5', 'b'], ['c', '4.2']]), [(1.0, 2.0), (3.5, 'b'), ('c', 4.2)])

    def test_empty_outer_list(self): self.assertEqual(list_to_float([]), [])

    def test_float_and_exponential_notation(self): self.assertEqual(list_to_float([['1.5', '1e3']]), [(1.5, 1000.0)])

    def test_negative_number_string(self): self.assertEqual(list_to_float([['-2', '5']]), [(-2.0, 5.0)])

