import unittest
from datasets.GPT_4.Few_shot1.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_snake_to_camel_basic(self): self.assertEqual(snake_to_camel("hello_world"), "HelloWorld")

    def test_snake_to_camel_single_word(self): self.assertEqual(snake_to_camel("python"), "Python")

    def test_snake_to_camel_multiple_underscores(self): self.assertEqual(snake_to_camel("a__b__c"), "A__B__C")

    def test_snake_to_camel_leading_underscore(self): self.assertEqual(snake_to_camel("_start"), "_Start")

    def test_snake_to_camel_trailing_underscore(self): self.assertEqual(snake_to_camel("end_"), "End_")

    def test_snake_to_camel_all_underscores(self): self.assertEqual(snake_to_camel("___"), "___")

    def test_snake_to_camel_empty(self): self.assertEqual(snake_to_camel(""), "")

