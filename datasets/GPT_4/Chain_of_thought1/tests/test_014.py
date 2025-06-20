import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_all_positive(self): self.assertEqual(smallest_num([3, 5, 7, 2]), 2)

    def test_mixed_signs(self): self.assertEqual(smallest_num([-4, 0, 3, -1]), -4)

    def test_all_negative(self): self.assertEqual(smallest_num([-1, -9, -3]), -9)

    def test_duplicates(self): self.assertEqual(smallest_num([5, 5, 1, 5]), 1)

    def test_single_element(self): self.assertEqual(smallest_num([42]), 42)

    def test_floats(self): self.assertEqual(smallest_num([2.5, 3.1, 0.9]), 0.9)

    def test_strings(self): self.assertEqual(smallest_num(['cat', 'apple', 'banana']), 'apple')

