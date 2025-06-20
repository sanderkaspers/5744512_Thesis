import unittest
from datasets.GPT_4.Zero_shot1.programs.program_074 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(tup_string(()), "")

    def test_2(self):
        self.assertEqual(tup_string(('x',)), "x")

    def test_3(self):
        self.assertEqual(tup_string(('a', ' ', 'b')), "a b")

    def test_4(self):
        self.assertEqual(tup_string(('!', '@', '#')), "!@#")

    def test_5(self):
        self.assertEqual(tup_string(('1', '2', '3')), "123")

    def test_6(self):
        self.assertEqual(tup_string(('a', '', 'b')), "ab")

    def test_7(self):
        self.assertEqual(tup_string(('A', 'b', 'C')), "AbC")

