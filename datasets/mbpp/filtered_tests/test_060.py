import unittest
from datasets.mbpp.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_tuple_to_int_with__1_2_3__expect_123(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

    def test_tuple_to_int_with__4_5_6__expect_456(self):
        self.assertEqual(tuple_to_int((4,5,6)), 456)

    def test_tuple_to_int_with__5_6_7__expect_567(self):
        self.assertEqual(tuple_to_int((5,6,7)), 567)

