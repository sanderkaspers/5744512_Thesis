import unittest
from datasets.GPT_4.Few_shot1.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_check_integer_valid_positive(self): self.assertEqual(check_integer("123"), True)

    def test_check_integer_valid_negative(self): self.assertEqual(check_integer("-456"), True)

    def test_check_integer_valid_with_plus(self): self.assertEqual(check_integer("+789"), True)

    def test_check_integer_invalid_alpha(self): self.assertEqual(check_integer("12a3"), False)

    def test_check_integer_empty_string(self): self.assertEqual(check_integer(""), None)

    def test_check_integer_only_sign(self): self.assertEqual(check_integer("+"), False)

    def test_check_integer_leading_trailing_spaces(self): self.assertEqual(check_integer("  42 "), True)

    def test_check_integer_space_inside(self): self.assertEqual(check_integer("4 2"), False)

    def test_check_integer_double_sign(self): self.assertEqual(check_integer("--12"), False)

