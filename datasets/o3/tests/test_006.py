import unittest
from datasets.o3.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_remove_some_chars(self):
        self.assertEqual(remove_dirty_chars("They are students", "aeiou"), "Thy r stdnts")

    def test_remove_all_chars(self):
        self.assertEqual(remove_dirty_chars("hello", "helo"), "")

    def test_no_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("Sample", ""), "Sample")

    def test_case_sensitive(self):
        self.assertEqual(remove_dirty_chars("AaBb", "ab"), "AB")

    def test_first_string_empty(self):
        self.assertEqual(remove_dirty_chars("", "abc"), "")

