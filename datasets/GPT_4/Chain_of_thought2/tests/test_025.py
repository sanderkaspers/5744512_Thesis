import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(minimum(10, 5), 5)

    def test_mixed_sign_integers(self): self.assertEqual(minimum(-3, 7), -3)

    def test_equal_integers(self): self.assertEqual(minimum(4, 4), 4)

    def test_floats(self): self.assertEqual(minimum(2.5, 3.5), 2.5)

    def test_int_float_mix(self): self.assertEqual(minimum(5, 4.5), 4.5)

    def test_zero_positive(self): self.assertEqual(minimum(0, 2), 0)

    def test_zero_negative(self): self.assertEqual(minimum(0, -2), -2)

    def test_boolean_values(self): self.assertEqual(minimum(True, False), False)

