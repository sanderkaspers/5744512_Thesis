import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self): self.assertEqual(sort_sublists([["dog", "apple", "cat"]]), [["apple", "cat", "dog"]])

    def test_multiple_sublists(self): self.assertEqual(sort_sublists([["zebra", "ant"], ["kite", "bat"]]), [["ant", "zebra"], ["bat", "kite"]])

    def test_same_first_letter(self): self.assertEqual(sort_sublists([["apple", "anchor", "ant"]]), [["apple", "anchor", "ant"]])

    def test_single_element_sublists(self): self.assertEqual(sort_sublists([["banana"], ["apple"]]), [["banana"], ["apple"]])

    def test_empty_outer_list(self): self.assertEqual(sort_sublists([]), [])

    def test_empty_inner_sublists(self): self.assertEqual(sort_sublists([[], ["dog", "cat"]]), [[], ["cat", "dog"]])

    def test_case_sensitivity(self): self.assertEqual(sort_sublists([["apple", "Banana", "cherry"]]), [["Banana", "apple", "cherry"]])

    def test_non_alpha_start(self): self.assertEqual(sort_sublists([["1fish", "@home", "zebra"]]), [["1fish", "@home", "zebra"]])

