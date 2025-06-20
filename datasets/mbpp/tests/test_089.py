import unittest
from datasets.mbpp.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_areEquivalent_with_36_57_expect_False(self):
        self.assertEqual(are_equivalent(36,57), False)

    def test_areEquivalent_with_2_4_expect_False(self):
        self.assertEqual(are_equivalent(2,4), False)

    def test_areEquivalent_with_23_47_expect_True(self):
        self.assertEqual(are_equivalent(23,47), True)

