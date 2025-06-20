import unittest
from datasets.mbpp.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_is_undulating_with__1212121__expect_True(self):
        self.assertEqual(is_undulating("1212121"), True)

    def test_is_undulating_with__1991__expect_False(self):
        self.assertEqual(is_undulating("1991"), False)

    def test_is_undulating_with__121__expect_True(self):
        self.assertEqual(is_undulating("121"), True)

