import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(add(3, 4), 7)

    def test_mixed_sign_integers(self): self.assertEqual(add(10, -3), 7)

    def test_float_addition(self): self.assertEqual(add(2.5, 3.5), 6.0)

    def test_int_float_mix(self): self.assertEqual(add(3, 2.5), 5.5)

    def test_zero_addition(self): self.assertEqual(add(0, 0), 0)

    def test_large_and_small(self): self.assertEqual(add(1e6, 1e-6), 1e6 + 1e-6)

    def test_boolean_values(self): self.assertEqual(add(True, False), 1)

    def test_string_concatenation(self): self.assertEqual(add("hello", "world"), "helloworld")

    def test_list_concatenation(self): self.assertEqual(add([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_complex_addition(self): self.assertEqual(add(1 + 2j, 3 + 4j), 4 + 6j)

