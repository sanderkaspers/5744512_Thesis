import unittest
from datasets.GPT_4.Few_shot1.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_odd_equivalent_basic(self): self.assertEqual(odd_Equivalent("1101", 4), 3)

    def test_odd_equivalent_none(self): self.assertEqual(odd_Equivalent("0000", 4), 0)

    def test_odd_equivalent_all(self): self.assertEqual(odd_Equivalent("1111", 4), 4)

    def test_odd_equivalent_partial(self): self.assertEqual(odd_Equivalent("101010", 3), 2)

    def test_odd_equivalent_n_less_than_length(self): self.assertEqual(odd_Equivalent("11111", 2), 2)

    def test_odd_equivalent_n_equals_zero(self): self.assertEqual(odd_Equivalent("10101", 0), 0)

    def test_odd_equivalent_empty_string(self): self.assertEqual(odd_Equivalent("", 0), 0)

