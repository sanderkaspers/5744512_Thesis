import unittest
from datasets.mbpp.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_python_programming(self):
        self.assertEqual(string_to_list("python programming"), ['python', 'programming'])

    def test_lists_tuples_strings(self):
        self.assertEqual(string_to_list("lists tuples strings"), ["lists", "tuples", "strings"])

    def test_write_a_program(self):
        self.assertEqual(string_to_list("write a program"), ["write", "a", "program"])

