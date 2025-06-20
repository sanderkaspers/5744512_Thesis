import unittest
from datasets.GPT_4.Few_shot1.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_list_to_float_basic(self): self.assertEqual(list_to_float([('A', '1')]), [('A', 1.0)])

    def test_list_to_float_all_strings(self): self.assertEqual(list_to_float([('X', 'Y')]), [('X', 'Y')])

    def test_list_to_float_all_numbers(self): self.assertEqual(list_to_float([('2', '3.5')]), [(2.0, 3.5)])

    def test_list_to_float_mixed_cases(self): self.assertEqual(list_to_float([('z', '10'), ('Y', '20.0')]), [('z', 10.0), ('Y', 20.0)])

    def test_list_to_float_multiple_tuples(self): self.assertEqual(list_to_float([('A', '1'), ('B', '2.2')]), [('A', 1.0), ('B', 2.2)])

    def test_list_to_float_single_tuple(self): self.assertEqual(list_to_float([('M', '0')]), [('M', 0.0)])

    def test_list_to_float_empty_list(self): self.assertEqual(list_to_float([]), [])

