import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_positive_multiple(self): self.assertTrue(multiple_of_five(25))

    def test_positive_non_multiple(self): self.assertFalse(multiple_of_five(23))

    def test_zero(self): self.assertTrue(multiple_of_five(0))

    def test_negative_multiple(self): self.assertTrue(multiple_of_five(-15))

    def test_negative_non_multiple(self): self.assertFalse(multiple_of_five(-14))

    def test_large_multiple(self): self.assertTrue(multiple_of_five(10**10))

    def test_float_multiple(self): self.assertTrue(multiple_of_five(20.0))

    def test_float_non_multiple(self): self.assertFalse(multiple_of_five(20.1))

    def test_boolean_true(self): self.assertFalse(multiple_of_five(True))

    def test_boolean_false(self): self.assertTrue(multiple_of_five(False))

