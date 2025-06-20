import unittest
from datasets.GPT_4.Zero_shot1.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(list_to_float([1, 2, 3]), [1.0, 2.0, 3.0])

    def test_2(self):
        self.assertEqual(list_to_float(["4", "5.5"]), [4.0, 5.5])

    def test_3(self):
        self.assertEqual(list_to_float([1.1, 2.2]), [1.1, 2.2])

    def test_4(self):
        self.assertEqual(list_to_float([1, "2.0"]), [1.0, 2.0])

    def test_5(self):
        self.assertEqual(list_to_float([]), [])

    def test_6(self):
        self.assertEqual(list_to_float([True, False]), [1.0, 0.0])

    def test_7(self):
        result = list_to_float(["1.23"])
        self.assertIsInstance(result[0], float)

