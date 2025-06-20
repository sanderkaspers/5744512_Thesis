import unittest
from datasets.GPT_4.Zero_shot1.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertFalse(are_equivalent(220, 284))

    def test_2(self):
        self.assertTrue(are_equivalent(36, 49))

    def test_3(self):
        self.assertTrue(are_equivalent(7, 13))

    def test_4(self):
        self.assertTrue(are_equivalent(12, 12))

    def test_5(self):
        self.assertFalse(are_equivalent(1, 10))

    def test_6(self):
        self.assertFalse(are_equivalent(1000, 1))

    def test_7(self):
        self.assertIsInstance(are_equivalent(12, 18), bool)

    def test_8(self):
        self.assertFalse(are_equivalent(40, 20))

    def test_9(self):
        self.assertFalse(are_equivalent(20, 40))

