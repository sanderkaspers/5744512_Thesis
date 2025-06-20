import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_normal_range(self): self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 9)

    def test_full_range(self): self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 4), 15)

    def test_single_element(self): self.assertEqual(sum_range_list([10, 20, 30, 40], 2, 2), 30)

    def test_negative_values(self): self.assertEqual(sum_range_list([-1, -2, -3, -4], 1, 3), -9)

    def test_zeros(self): self.assertEqual(sum_range_list([0, 0, 0], 0, 2), 0)

    def test_m_greater_than_n(self): self.assertEqual(sum_range_list([1, 2, 3], 2, 1), 0)

    def test_negative_index(self): self.assertEqual(sum_range_list([10, 20, 30], -1, -1), 30)

    def test_boolean_elements(self): self.assertEqual(sum_range_list([True, False, True], 0, 2), 2)

