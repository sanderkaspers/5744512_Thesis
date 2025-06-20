import unittest
from datasets.GPT_4.Zero_shot2.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_type_1(self):
        self.assertTrue(check_type(("a", "b", "c")))

    def test_type_2(self):
        self.assertFalse(check_type(("a", 1, "b")))

    def test_type_3(self):
        self.assertFalse(check_type((1, 2, 3)))

    def test_type_4(self):
        self.assertTrue(check_type(()))

    def test_type_5(self):
        self.assertTrue(check_type(("only",)))

    def test_type_6(self):
        self.assertFalse(check_type((42,)))

    def test_type_7(self):
        self.assertFalse(check_type(("text", (1, 2))))

    def test_type_8(self):
        self.assertTrue(check_type(("123", "456")))

    def test_type_9(self):
        self.assertTrue(check_type(("α", "β", "γ")))

    def test_type_10(self):
        self.assertTrue(check_type(("A", "a", "Aa")))

    def test_type_11(self):
        self.assertTrue(check_type(tuple("a" * 1000)))

