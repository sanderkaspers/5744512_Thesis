import unittest
from datasets.GPT_4.Few_shot1.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_is_monotonic_increasing(self): self.assertEqual(is_Monotonic([1, 2, 3, 4]), True)

    def test_is_monotonic_decreasing(self): self.assertEqual(is_Monotonic([4, 3, 2, 1]), True)

    def test_is_monotonic_constant(self): self.assertEqual(is_Monotonic([5, 5, 5, 5]), True)

    def test_is_monotonic_single_element(self): self.assertEqual(is_Monotonic([10]), True)

    def test_is_monotonic_empty_list(self): self.assertEqual(is_Monotonic([]), True)

    def test_is_monotonic_not_monotonic(self): self.assertEqual(is_Monotonic([1, 3, 2]), False)

    def test_is_monotonic_valley_shape(self): self.assertEqual(is_Monotonic([1, 2, 1]), False)

    def test_is_monotonic_peak_shape(self): self.assertEqual(is_Monotonic([3, 2, 3]), False)

    def test_is_monotonic_mixed_types(self): self.assertEqual(is_Monotonic([1.0, 2, 3.5]), True)

    def test_is_monotonic_with_duplicates(self): self.assertEqual(is_Monotonic([3, 3, 2, 2, 1]), True)

