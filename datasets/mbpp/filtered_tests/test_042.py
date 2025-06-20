import unittest
from datasets.mbpp.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_case(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

    def test_case(self):
        self.assertEqual(index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]), 'Dawood')

    def test_case(self):
        self.assertEqual(index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]), 'Ayesha')

