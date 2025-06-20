import unittest
from datasets.GPT_4.Zero_shot2.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_text_1(self):
        self.assertEqual(text_lowercase_underscore("Hello World"), "hello_world")

    def test_text_2(self):
        self.assertEqual(text_lowercase_underscore("Python_is_fun"), "python_is_fun")

    def test_text_3(self):
        self.assertEqual(text_lowercase_underscore("unit-test-example"), "unit_test_example")

    def test_text_4(self):
        self.assertEqual(text_lowercase_underscore("Mix_ed -Format String"), "mix_ed_format_string")

    def test_text_5(self):
        self.assertEqual(text_lowercase_underscore("  Leading -and__trailing-- "), "_leading_and_trailing_")

    def test_text_6(self):
        self.assertEqual(text_lowercase_underscore("JustAPlainString"), "justaplainstring")

    def test_text_7(self):
        self.assertEqual(text_lowercase_underscore(""), "")

