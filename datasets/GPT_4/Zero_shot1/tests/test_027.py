import unittest
from datasets.GPT_4.Zero_shot1.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_Diff(22), True)

    def test_2(self):
        self.assertEqual(is_Diff(10), False)

    def test_3(self):
        self.assertEqual(is_Diff(0), True)

    def test_4(self):
        self.assertEqual(is_Diff(-11), True)

    def test_5(self):
        self.assertEqual(is_Diff(-10), False)

    def test_6(self):
        self.assertEqual(is_Diff(121), True)

    def test_7(self):
        self.assertEqual(is_Diff(123), False)

