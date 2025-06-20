import unittest
from datasets.GPT_4.Zero_shot1.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_occurance("xxstdxxstd"), 2)

    def test_2(self):
        self.assertEqual(count_occurance("ststd"), 1)

    def test_3(self):
        self.assertEqual(count_occurance("student"), 0)

    def test_4(self):
        self.assertEqual(count_occurance("StdstdSTD"), 1)

    def test_5(self):
        self.assertEqual(count_occurance(""), 0)

    def test_6(self):
        self.assertEqual(count_occurance("st"), 0)

    def test_7(self):
        self.assertEqual(count_occurance("stdbegin"), 1)

    def test_8(self):
        self.assertEqual(count_occurance("endstd"), 1)

    def test_9(self):
        self.assertEqual(count_occurance("a"*100 + "std" + "b"*100 + "std"), 2)

    def test_10(self):
        self.assertIsInstance(count_occurance("stdstd"), int)

