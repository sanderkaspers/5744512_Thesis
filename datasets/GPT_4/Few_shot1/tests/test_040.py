import unittest
from datasets.GPT_4.Few_shot1.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_is_undulating_true(self): self.assertEqual(is_undulating(121), True)

    def test_is_undulating_false_same_digit(self): self.assertEqual(is_undulating(111), False)

    def test_is_undulating_false_three_digits(self): self.assertEqual(is_undulating(123), False)

    def test_is_undulating_true_long(self): self.assertEqual(is_undulating(121212), True)

    def test_is_undulating_false_pattern_break(self): self.assertEqual(is_undulating(121221), False)

    def test_is_undulating_too_short_1digit(self): self.assertEqual(is_undulating(1), False)

    def test_is_undulating_too_short_2digits(self): self.assertEqual(is_undulating(12), False)

    def test_is_undulating_starts_wrong(self): self.assertEqual(is_undulating(212121), True)

