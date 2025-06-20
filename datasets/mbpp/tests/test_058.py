import unittest
from datasets.mbpp.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_check_integer_with__python__expect_False(self):
        self.assertEqual(check_integer("python"), False)

    def test_check_integer_with__1__expect_True(self):
        self.assertEqual(check_integer("1"), True)

    def test_check_integer_with__12345__expect_True(self):
        self.assertEqual(check_integer("12345"), True)

