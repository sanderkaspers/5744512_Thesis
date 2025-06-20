import unittest
from datasets.GPT_4.Zero_shot2.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_float_1(self):
        self.assertEqual(list_to_float([1, 2, 3]), [1.0, 2.0, 3.0])

    def test_float_2(self):
        self.assertEqual(list_to_float(["1.1", "2.2", "3.3"]), [1.1, 2.2, 3.3])

    def test_float_3(self):
        self.assertEqual(list_to_float([1, "2.0", 3.5]), [1.0, 2.0, 3.5])

    def test_float_4(self):
        self.assertEqual(list_to_float([]), [])

    def test_float_5(self):
        self.assertEqual(list_to_float([1.0, 2.5, 3.2]), [1.0, 2.5, 3.2])

    def test_float_6(self):
        self.assertEqual(list_to_float([-1, "-2.5", -3.0]), [-1.0, -2.5, -3.0])

