import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_regular(self): self.assertEqual(next_smallest_palindrome(123), '131')

    def test_one_digit(self): self.assertEqual(next_smallest_palindrome(7), '8')

    def test_input_is_palindrome(self): self.assertEqual(next_smallest_palindrome(121), '131')

    def test_ending_in_9(self): self.assertEqual(next_smallest_palindrome(149), '151')

    def test_crossing_thousands(self): self.assertEqual(next_smallest_palindrome(999), '1001')

    def test_very_large(self): self.assertEqual(next_smallest_palindrome(123456789), '123484321')

    def test_string_input(self): self.assertEqual(next_smallest_palindrome('345'), '353')

    def test_leading_zeros(self): self.assertEqual(next_smallest_palindrome('007'), '8')

