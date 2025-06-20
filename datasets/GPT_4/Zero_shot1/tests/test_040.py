import unittest
from datasets.GPT_4.Zero_shot1.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_undulating(121))

    def test_2(self):
        self.assertTrue(is_undulating(2323))

    def test_3(self):
        self.assertFalse(is_undulating(12))

    def test_4(self):
        self.assertFalse(is_undulating(111))

    def test_5(self):
        self.assertFalse(is_undulating(123))

    def test_6(self):
        self.assertTrue(is_undulating(898))

    def test_7(self):
        self.assertTrue(is_undulating(76767676))

    def test_8(self):
        self.assertFalse(is_undulating(55555))

    def test_9(self):
        self.assertTrue(is_undulating(12121))

    def test_10(self):
        self.assertFalse(is_undulating(99999))

    def test_11(self):
        self.assertTrue(is_undulating("434343"))

    def test_12(self):
        self.assertTrue(is_undulating(-12121))

    def test_13(self):
        self.assertTrue(is_undulating(1010101010101010))

    def test_14(self):
        self.assertFalse(is_undulating(12112))

    def test_15(self):
        self.assertFalse(is_undulating(212))

    def test_16(self):
        self.assertFalse(is_undulating(4543))

    def test_17(self):
        self.assertFalse(is_undulating(123123))

