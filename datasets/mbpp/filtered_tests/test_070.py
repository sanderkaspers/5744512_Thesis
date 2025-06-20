import unittest
from datasets.mbpp.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_long_words_with_3__pythonisaprogramminglanguage__expect__python(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

    def test_long_words_with_2__writingaprogram__expect__writing(self):
        self.assertEqual(long_words(2, "writing a program"), ["writing", "program"])

    def test_long_words_with_5__sortinglist__expect__sorting(self):
        self.assertEqual(long_words(5, "sorting list"), ["sorting"])

