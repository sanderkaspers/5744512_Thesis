import unittest
from datasets.GPT_4.Few_shot2.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_list_to_float_basic(self): self.assertEqual(list_to_float([1, 2, 3]), [1.0, 2.0, 3.0])

    def test_list_to_float_string_numbers(self): self.assertEqual(list_to_float(['1', '2.5', '3']), [1.0, 2.5, 3.0])

    def test_list_to_float_mixed_numeric_types(self): self.assertEqual(list_to_float([1, '2', 3.5]), [1.0, 2.0, 3.5])

    def test_list_to_float_empty_list(self): self.assertEqual(list_to_float([]), [])

    def test_list_to_float_negative_values(self): self.assertEqual(list_to_float([-1, '-2.0', -3.5]), [-1.0, -2.0, -3.5])

