import unittest
from datasets.GPT_4.Zero_shot2.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_tuple_1(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_tuple_2(self):
        self.assertEqual(tuple_to_int((0, 4, 5)), 45)

    def test_tuple_3(self):
        self.assertEqual(tuple_to_int((1, '2', 3)), 123)

    def test_tuple_4(self):
        self.assertEqual(tuple_to_int((1.0, 2.0)), 12)

    def test_tuple_5(self):
        self.assertEqual(tuple_to_int((7,)), 7)

