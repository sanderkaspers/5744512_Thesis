import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_single_std(self): self.assertEqual(count_occurance('abcstdxyz'), 1)

    def test_multiple_std(self): self.assertEqual(count_occurance('stdabcstdxyzstd'), 3)

    def test_start_position(self): self.assertEqual(count_occurance('stdabc'), 1)

    def test_end_position(self): self.assertEqual(count_occurance('abcstd'), 1)

    def test_no_occurrence(self): self.assertEqual(count_occurance('abcdefg'), 0)

    def test_adjacent_std(self): self.assertEqual(count_occurance('stdstd'), 2)

    def test_empty_string(self): self.assertEqual(count_occurance(''), 0)

    def test_short_string(self): self.assertEqual(count_occurance('st'), 0)

    def test_case_sensitivity(self): self.assertEqual(count_occurance('STD'), 0)

    def test_special_characters(self): self.assertEqual(count_occurance('s†d'), 0)

    def test_overlapping_pattern(self): self.assertEqual(count_occurance('ststd'), 1)

    def test_long_input(self): self.assertEqual(count_occurance('std'*1000), 1000)

