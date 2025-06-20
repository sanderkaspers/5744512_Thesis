import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_integer_side(self): self.assertEqual(perimeter_pentagon(5), 25)

    def test_zero_side(self): self.assertEqual(perimeter_pentagon(0), 0)

    def test_float_side(self): self.assertEqual(perimeter_pentagon(3.5), 17.5)

    def test_large_input(self): self.assertEqual(perimeter_pentagon(1000000), 5000000)

    def test_small_input(self): self.assertAlmostEqual(perimeter_pentagon(0.0001), 0.0005)

    def test_negative_side(self): self.assertEqual(perimeter_pentagon(-5), -25)

    def test_boolean_input(self): self.assertEqual(perimeter_pentagon(True), 5)

