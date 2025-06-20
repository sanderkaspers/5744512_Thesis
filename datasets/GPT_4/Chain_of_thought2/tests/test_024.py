import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(maximum(10, 5), 10)

    def test_mixed_sign_integers(self): self.assertEqual(maximum(-3, 7), 7)

    def test_equal_integers(self): self.assertEqual(maximum(4, 4), 4)

    def test_floats(self): self.assertEqual(maximum(2.5, 3.5), 3.5)

    def test_int_float_mix(self): self.assertEqual(maximum(5, 5.5), 5.5)

    def test_zero_positive(self): self.assertEqual(maximum(0, 2), 2)

    def test_zero_negative(self): self.assertEqual(maximum(0, -2), 0)

    def test_boolean_values(self): self.assertEqual(maximum(True, False), True)

