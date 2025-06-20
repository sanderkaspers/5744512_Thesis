import unittest
from datasets.GPT_4.Few_shot.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(snake_to_camel("snake_case"), "SnakeCase") # Normal case)

    def test_case_2(self):
        self.assertEqual(snake_to_camel("this_is_snake_case"), "ThisIsSnakeCase") # Multiple underscores)

    def test_case_3(self):
        self.assertEqual(snake_to_camel("alreadycamelcase"), "Alreadycamelcase") # No underscores)

    def test_case_4(self):
        self.assertEqual(snake_to_camel(""), "") # Empty string)

    def test_case_5(self):
        self.assertEqual(snake_to_camel("one_two_three"), "OneTwoThree") # All lowercase)

    def test_case_6(self):
        self.assertEqual(snake_to_camel("oneTwo_Three"), "OnetwoThree") # Mixed case)

    def test_case_7(self):
        self.assertEqual(snake_to_camel("snake__case"), "SnakeCase") # Double underscore)

    def test_case_8(self):
        self.assertEqual(snake_to_camel("_leadingunderscore"), "Leadingunderscore") # Leading underscore)

