import unittest
from datasets.mbpp.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_odd_values_string_with_abcdef_expect_ace(self):
        self.assertEqual(odd_values_string('abcdef'), "ace")

    def test_odd_values_string_with_python_expect_pto(self):
        self.assertEqual(odd_values_string('python'), "pto")

    def test_odd_values_string_with_data_expect_dt(self):
        self.assertEqual(odd_values_string('data'), "dt")

