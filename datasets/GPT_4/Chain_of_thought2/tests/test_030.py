import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(average([2, 4, 6]), 4.0)

    def test_negative_integers(self): self.assertEqual(average([-3, -6, -9]), -6.0)

    def test_mixed_integers(self): self.assertEqual(average([-1, 0, 1]), 0.0)

    def test_float_values(self): self.assertAlmostEqual(average([1.5, 2.5, 3.0]), 2.333333333)

    def test_boolean_values(self): self.assertEqual(average([True, False, True]), 2/3)

    def test_single_element(self): self.assertEqual(average([42]), 42.0)

    def test_large_list(self): self.assertEqual(average(list(range(100))), 49.5)

