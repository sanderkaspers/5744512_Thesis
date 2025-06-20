import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_multiple_occurrences(self):
        self.assertEqual(count_occurance('stdstd'), 2)

    def test_no_occurrences(self):
        self.assertEqual(count_occurance('abc'), 0)

    def test_single_occurrence(self):
        self.assertEqual(count_occurance('thestdstring'), 1)

    def test_empty_string(self):
        self.assertEqual(count_occurance(''), 0)

    def test_std_at_start(self):
        self.assertEqual(count_occurance('stdstartswith'), 1)

    def test_std_at_end(self):
        self.assertEqual(count_occurance('endswithstd'), 1)

    def test_overlapping_occurrences(self):
        self.assertEqual(count_occurance('stdstdstd'), 3)

    def test_mixed_case(self):
        self.assertEqual(count_occurance('sTdsTD'), 0)

    def test_large_string(self):
        large_string = 'a' * 1000 + 'std' + 'b' * 1000 + 'std'
        self.assertEqual(count_occurance(large_string), 2)

    def test_special_characters(self):
        self.assertEqual(count_occurance('!std!@std#'), 2)

