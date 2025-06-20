import unittest
from datasets.o3.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_no_occurrence(self):
        self.assertEqual(count_occurance("abcdefg"), 0)

    def test_single_occurrence(self):
        self.assertEqual(count_occurance("std"), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(count_occurance("stdxxstdstd"), 3)

    def test_mixed_case(self):
        self.assertEqual(count_occurance("StDstdSTD"), 1)

    def test_short_string(self):
        self.assertEqual(count_occurance("st"), 0)

