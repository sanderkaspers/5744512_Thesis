import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(next_smallest_palindrome(123), 131)

    def test_single_digit(self):
        self.assertEqual(next_smallest_palindrome(7), 8)

    def test_number_ending_in_9(self):
        self.assertEqual(next_smallest_palindrome(29), 33)

    def test_large_number(self):
        self.assertEqual(next_smallest_palindrome(999999), 1000001)

    def test_palindrome_number(self):
        self.assertEqual(next_smallest_palindrome(121), 131)

    def test_all_same_digits(self):
        self.assertEqual(next_smallest_palindrome(111), 121)

    def test_close_to_palindrome(self):
        self.assertEqual(next_smallest_palindrome(122), 131)

    def test_minimum_integer(self):
        self.assertEqual(next_smallest_palindrome(0), 1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            next_smallest_palindrome('123')

    def test_boundary_condition(self):
        self.assertTrue(next_smallest_palindrome(sys.maxsize) > sys.maxsize)

