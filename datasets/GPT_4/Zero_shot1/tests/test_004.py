import unittest
from datasets.GPT_4.Zero_shot1.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(text_lowercase_underscore("Python3 is Great!"), "python3_is_great")

    def test_2(self):
        self.assertEqual(text_lowercase_underscore(""), "")

    def test_3(self):
        self.assertEqual(text_lowercase_underscore("SOME MIXED case TEXT"), "some_mixed_case_text")

    def test_4(self):
        self.assertEqual(text_lowercase_underscore("123 456 789"), "123_456_789")

    def test_5(self):
        self.assertEqual(text_lowercase_underscore("___"), "")

    def test_6(self):
        self.assertEqual(text_lowercase_underscore("Hello_World_again"), "hello_world_again")

    def test_7(self):
        self.assertEqual(text_lowercase_underscore("Well... this is awkward."), "well_this_is_awkward")

    def test_8(self):
        self.assertEqual(text_lowercase_underscore("e-mail address: test@example.com"), "e_mail_address_test_example_com")

    def test_9(self):
        self.assertEqual(text_lowercase_underscore("A B C D E"), "a_b_c_d_e")

