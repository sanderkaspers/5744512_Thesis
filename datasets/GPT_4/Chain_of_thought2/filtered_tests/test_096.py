import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_single_occurrence(self): self.assertEqual(count_occurance('hello std world'), 1)

    def test_multiple_occurrences(self): self.assertEqual(count_occurance('this std is std in std'), 3)

    def test_back_to_back_occurrences(self): self.assertEqual(count_occurance('stdstd'), 2)

    def test_no_occurrence(self): self.assertEqual(count_occurance('this is a test'), 0)

    def test_empty_string(self): self.assertEqual(count_occurance(''), 0)

    def test_occurrence_at_start(self): self.assertEqual(count_occurance('stdhello'), 1)

    def test_occurrence_at_end(self): self.assertEqual(count_occurance('hellostd'), 1)

    def test_incomplete_match(self): self.assertEqual(count_occurance('ststdst'), 1)

    def test_case_sensitivity(self): self.assertEqual(count_occurance('StdSTDstd'), 1)

    def test_with_non_letter_chars(self): self.assertEqual(count_occurance('s!t#d std s*t&d'), 1)

