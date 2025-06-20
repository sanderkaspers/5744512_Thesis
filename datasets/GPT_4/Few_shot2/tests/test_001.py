import unittest
from datasets.GPT_4.Few_shot2.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_remove_Occ_basic_removal(self): self.assertEqual(remove_Occ('hello', 'l'), 'heo')

    def test_remove_Occ_single_occurrence(self): self.assertEqual(remove_Occ('abc', 'a'), 'bc')

    def test_remove_Occ_no_occurrence(self): self.assertEqual(remove_Occ('abc', 'x'), 'abc')

    def test_remove_Occ_all_same_chars(self): self.assertEqual(remove_Occ('aaa', 'a'), 'a')

    def test_remove_Occ_first_and_last_same(self): self.assertEqual(remove_Occ('abacada', 'a'), 'bacad')

    def test_remove_Occ_empty_string(self): self.assertEqual(remove_Occ('', 'a'), '')

    def test_remove_Occ_string_of_one_char(self): self.assertEqual(remove_Occ('a', 'a'), '')

    def test_remove_Occ_string_of_two_same_chars(self): self.assertEqual(remove_Occ('aa', 'a'), '')

    def test_remove_Occ_case_sensitivity(self): self.assertEqual(remove_Occ('AbcaC', 'c'), 'AbcaC')

    def test_remove_Occ_remove_middle_only(self): self.assertEqual(remove_Occ('xaxax', 'a'), 'xaxx')

