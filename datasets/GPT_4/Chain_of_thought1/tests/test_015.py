import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(max_difference([1, 2, 3, 10]), 9)

    def test_mixed_signs(self): self.assertEqual(max_difference([-5, 0, 5]), 10)

    def test_all_negative(self): self.assertEqual(max_difference([-10, -3, -1]), 9)

    def test_two_elements(self): self.assertEqual(max_difference([4, 9]), 5)

    def test_repeated_values(self): self.assertEqual(max_difference([7, 7, 7]), 0)

    def test_single_element(self): self.assertEqual(max_difference([42]), 0)

    def test_floats(self): self.assertEqual(max_difference([1.5, 3.2, 7.8]), 6.3)

