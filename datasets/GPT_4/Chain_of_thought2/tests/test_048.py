import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_simple_case(self): self.assertEqual(next_smallest_palindrome(123), 131)

    def test_input_is_palindrome(self): self.assertEqual(next_smallest_palindrome(121), 131)

    def test_input_ends_in_nines(self): self.assertEqual(next_smallest_palindrome(99), 101)

    def test_input_just_below_palindrome(self): self.assertEqual(next_smallest_palindrome(130), 131)

    def test_single_digit(self): self.assertEqual(next_smallest_palindrome(7), 8)

    def test_single_digit_nine(self): self.assertEqual(next_smallest_palindrome(9), 11)

    def test_zero_input(self): self.assertEqual(next_smallest_palindrome(0), 1)

    def test_even_digit_length_input(self): self.assertEqual(next_smallest_palindrome(1221), 1331)

    def test_large_number(self): self.assertEqual(next_smallest_palindrome(99899), 99999)

    def test_negative_number(self): self.assertEqual(next_smallest_palindrome(-5), 1)

    def test_input_palindrome_with_odd_middle(self): self.assertEqual(next_smallest_palindrome(999), 1001)

