import unittest
from datasets.o3.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_property_true_small(self):
        self.assertTrue(check(1))

    def test_property_true_mid(self):
        self.assertTrue(check(73))

    def test_property_true_large(self):
        self.assertTrue(check(793))

    def test_property_false(self):
        self.assertFalse(check(12))

    def test_property_false_single_digit(self):
        self.assertFalse(check(3))

    def test_property_false_zero(self):
        self.assertFalse(check(0))

