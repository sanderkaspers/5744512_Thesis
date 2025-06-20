import unittest
from datasets.GPT_4.Zero_shot2.programs.program_059 import *

class TestVersion(unittest.TestCase):
    def test_empty_1(self):
        self.assertTrue(empty_dit([{}, {}, {}]))

    def test_empty_2(self):
        self.assertFalse(empty_dit([{}, {"a":1}]))

    def test_empty_3(self):
        self.assertFalse(empty_dit([{"x": 1}, {}]))

    def test_empty_4(self):
        self.assertTrue(empty_dit([]))

