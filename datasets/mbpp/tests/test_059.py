import unittest
from datasets.mbpp.programs.program_059 import *

class TestVersion(unittest.TestCase):
    def test_empty_dit_with_______expect_True(self):
        self.assertEqual(empty_dit([{},{},{}]), True)

    def test_empty_dit_with__1_2______expect_False(self):
        self.assertEqual(empty_dit([{1,2},{},{}]), False)

    def test_empty_dit_with___expect_True(self):
        self.assertEqual(empty_dit({}), True)

