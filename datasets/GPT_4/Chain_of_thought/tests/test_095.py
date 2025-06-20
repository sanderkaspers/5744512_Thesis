import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_zero_length(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            perimeter_pentagon(-5)

    def test_floating_point_length(self):
        self.assertEqual(perimeter_pentagon(5.5), 27.5)

    def test_very_small_length(self):
        self.assertEqual(perimeter_pentagon(0.0001), 0.0005)

    def test_very_large_length(self):
        self.assertEqual(perimeter_pentagon(1e6), 5e6)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon('5')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(None)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon([5])

    def test_mixed_data_type(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon({5})

