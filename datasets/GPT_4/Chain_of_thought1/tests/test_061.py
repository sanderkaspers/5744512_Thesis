import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_integer_strings(self): self.assertEqual(list_to_float(['1', '2', '3']), [1.0, 2.0, 3.0])

    def test_float_strings(self): self.assertEqual(list_to_float(['1.1', '2.2']), [1.1, 2.2])

    def test_mixed_types(self): self.assertEqual(list_to_float(['3', 4.5, 6]), [3.0, 4.5, 6.0])

    def test_floats(self): self.assertEqual(list_to_float([1.0, 2.0]), [1.0, 2.0])

    def test_negatives(self): self.assertEqual(list_to_float(['-1', -2.5]), [-1.0, -2.5])

    def test_zeros(self): self.assertEqual(list_to_float(['0', 0]), [0.0, 0.0])

    def test_scientific_notation(self): self.assertEqual(list_to_float(['1e10', '2.5e-5']), [1e10, 2.5e-5])

    def test_empty_list(self): self.assertEqual(list_to_float([]), [])

    def test_boolean_values(self): self.assertEqual(list_to_float([True, False]), [1.0, 0.0])

    def test_special_strings(self): result = list_to_float(['NaN', 'inf']); self.assertTrue(math.isnan(result[0])); self.assertTrue(math.isinf(result[1]))

