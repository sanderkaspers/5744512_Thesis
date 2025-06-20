import unittest
from datasets.GPT_4.Zero_shot2.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_eqtuple_1(self):
        self.assertEqual(find_equal_tuple([(1, 2), (1, 2)]), (True, True))

    def test_eqtuple_2(self):
        self.assertEqual(find_equal_tuple([(1, 2), (1, 3)]), (True, False))

    def test_eqtuple_3(self):
        self.assertEqual(find_equal_tuple([(1, 2), (3, 4)]), (False, False))

    def test_eqtuple_4(self):
        self.assertEqual(find_equal_tuple([]), ())

    def test_eqtuple_5(self):
        self.assertEqual(find_equal_tuple([(5,), (5,), (5,)]), (True,))

    def test_eqtuple_6(self):
        self.assertEqual(find_equal_tuple([(1, 2, 3), (1, 5, 3), (1, 6, 3)]), (True, False, True))

    def test_eqtuple_7(self):
        self.assertEqual(find_equal_tuple([(7, 8)]), (True, True))

