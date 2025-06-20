import unittest
from datasets.GPT_4.Zero_shot2.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_patterns_1(self):
        self.assertTrue(is_samepatterns(["red", "blue"], ["a", "b"]))

    def test_patterns_2(self):
        self.assertFalse(is_samepatterns(["red", "red"], ["a", "b"]))

    def test_patterns_3(self):
        self.assertFalse(is_samepatterns(["red", "blue"], ["a", "a"]))

    def test_patterns_4(self):
        self.assertTrue(is_samepatterns(["red", "red"], ["a", "a"]))

    def test_patterns_5(self):
        self.assertFalse(is_samepatterns(["red", "blue", "green"], ["a", "b"]))

    def test_patterns_6(self):
        self.assertTrue(is_samepatterns([], []))

    def test_patterns_7(self):
        self.assertTrue(is_samepatterns(["red"], ["a"]))

    def test_patterns_8(self):
        colors = [str(i) for i in range(1000)]
        patterns = [chr(65 + (i % 26)) + str(i // 26) for i in range(1000)]
        self.assertFalse(is_samepatterns(colors, patterns))

