import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_sublists([['apple', 'banana', 'cherry'], ['dog', 'cat']]), [['apple', 'banana', 'cherry'], ['cat', 'dog']])

    def test_empty_list_of_lists(self):
        self.assertEqual(sort_sublists([]), [])

    def test_empty_sublists(self):
        self.assertEqual(sort_sublists([[], ['apple'], []]), [[], ['apple'], []])

    def test_single_element_sublists(self):
        self.assertEqual(sort_sublists([['apple'], ['banana'], ['cherry']]), [['apple'], ['banana'], ['cherry']])

    def test_strings_with_different_cases(self):
        self.assertEqual(sort_sublists([['Apple', 'banana', 'Cherry']]), [['Apple', 'Cherry', 'banana']])

    def test_strings_with_special_characters(self):
        self.assertEqual(sort_sublists([['@home', '#hashtag', '!bang']]), [['!bang', '#hashtag', '@home']])

    def test_strings_with_numeric_values(self):
        self.assertEqual(sort_sublists([['1apple', '2banana', '3cherry']]), [['1apple', '2banana', '3cherry']])

    def test_identical_strings_in_sublists(self):
        self.assertEqual(sort_sublists([['apple', 'apple'], ['banana', 'banana']]), [['apple', 'apple'], ['banana', 'banana']])

    def test_strings_of_different_lengths(self):
        self.assertEqual(sort_sublists([['short', 'longer', 'longest']]), [['longer', 'longest', 'short']])

    def test_non_string_inputs_in_sublists(self):
        with self.assertRaises(TypeError):
            sort_sublists([['apple', 2, 'banana']])

