import unittest
from datasets.GPT_4.Zero_shot1.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_2(self):
        self.assertEqual(tuple_to_int((5,)), 5)

    def test_3(self):
        self.assertEqual(tuple_to_int((0, 1, 2)), 12)

    def test_4(self):
        self.assertEqual(tuple_to_int((0, 0, 3)), 3)

    def test_5(self):
        self.assertEqual(tuple_to_int(("1", "2")), 12)

    def test_6(self):
        self.assertEqual(tuple_to_int((1, "2", 3)), 123)

    def test_7(self):
        self.assertIsInstance(tuple_to_int((4, 5)), int)

