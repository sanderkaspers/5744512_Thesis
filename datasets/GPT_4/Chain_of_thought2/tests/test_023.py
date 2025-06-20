import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(absolute(5), 5)

    def test_negative_integer(self): self.assertEqual(absolute(-5), 5)

    def test_zero(self): self.assertEqual(absolute(0), 0)

    def test_positive_float(self): self.assertEqual(absolute(3.5), 3.5)

    def test_negative_float(self): self.assertEqual(absolute(-2.7), 2.7)

    def test_boolean_true(self): self.assertEqual(absolute(True), 1)

    def test_boolean_false(self): self.assertEqual(absolute(False), 0)

