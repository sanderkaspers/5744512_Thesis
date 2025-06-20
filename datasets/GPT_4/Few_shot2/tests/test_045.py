import unittest
from datasets.GPT_4.Few_shot2.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_frequency_lists_all_digits_once(self): self.assertEqual(frequency_lists([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [1]*10)

    def test_frequency_lists_multiple_digits(self): self.assertEqual(frequency_lists([1, 2, 2, 3, 3, 3]), [0, 1, 2, 3, 0, 0, 0, 0, 0, 0])

    def test_frequency_lists_out_of_range(self): self.assertEqual(frequency_lists([-1, 10, 100, 0]), [1]+[0]*9)

    def test_frequency_lists_with_non_integers(self): self.assertEqual(frequency_lists([1, 2.0, '3', [4], 5]), [0, 1, 0, 0, 0, 1, 0, 0, 0, 0])

    def test_frequency_lists_empty(self): self.assertEqual(frequency_lists([]), [0]*10)

    def test_frequency_lists_all_invalid(self): self.assertEqual(frequency_lists(['a', {}, [], 10, -5, 20]), [0]*10)

    def test_frequency_lists_all_zeros(self): self.assertEqual(frequency_lists([0, 0, 0]), [3]+[0]*9)

