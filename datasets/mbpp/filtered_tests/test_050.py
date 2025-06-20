import unittest
from datasets.mbpp.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_snake_to_camel_with_python_program_expect_PythonProgram(self):
        self.assertEqual(snake_to_camel('python_program'), ('PythonProgram'))

    def test_snake_to_camel_with_python_language_expect__PythonLanguage_(self):
        self.assertEqual(snake_to_camel('python_language'), ('PythonLanguage'))

    def test_snake_to_camel_with_programming_language_expect__ProgrammingLanguage_(self):
        self.assertEqual(snake_to_camel('programming_language'), ('ProgrammingLanguage'))

