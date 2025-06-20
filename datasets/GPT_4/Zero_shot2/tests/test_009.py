import unittest
from datasets.GPT_4.Zero_shot2.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_rev_1(self):
        self.assertEqual(rev(123), 321)

    def test_rev_2(self):
        self.assertEqual(rev(100), 1)

    def test_rev_3(self):
        self.assertEqual(rev(7), 7)

    def test_rev_4(self):
        self.assertEqual(rev(0), 0)

    def test_rev_5(self):
        self.assertEqual(rev(121), 121)

    def test_rev_6(self):
        self.assertEqual(rev(-123), 0)

