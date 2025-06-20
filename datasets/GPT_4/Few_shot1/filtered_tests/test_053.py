import unittest
from datasets.GPT_4.Few_shot1.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_count_positive(self): self.assertEqual(count([1, 2, 3]), 6)

    def test_count_empty(self): self.assertEqual(count([]), 0)

    def test_count_single(self): self.assertEqual(count([5]), 5)

    def test_count_negative(self): self.assertEqual(count([-1, -2, -3]), -6)

    def test_count_mixed(self): self.assertEqual(count([1, -2, 3]), 2)

    def test_count_zeros(self): self.assertEqual(count([0, 0, 0]), 0)

