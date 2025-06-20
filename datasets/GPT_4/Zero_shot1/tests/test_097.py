import unittest
from datasets.GPT_4.Zero_shot1.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertTrue(check_type(("a", "b", "c")))

    def test_2(self):
        self.assertTrue(check_type((1.1, 2.2, 3.3)))

    def test_3(self):
        self.assertFalse(check_type((1, "2", 3)))

    def test_4(self):
        self.assertFalse(check_type((1, 2.0, 3)))

    def test_5(self):
        self.assertTrue(check_type(()))

    def test_6(self):
        self.assertTrue(check_type((42,)))

    def test_7(self):
        self.assertTrue(check_type((True, False, True)))

    def test_8(self):
        self.assertFalse(check_type((True, 1, False)))

    def test_9(self):
        self.assertFalse(check_type(([1], [2], (3,))))

    def test_10(self):
        self.assertTrue(check_type(([1], [2], [3])))

    def test_11(self):
        class A: pass
        class B: pass
        self.assertFalse(check_type((A(), B())))

    def test_12(self):
        self.assertFalse(check_type((None, 1)))

    def test_13(self):
        self.assertIsInstance(check_type((1, 2, 3)), bool)

