import unittest
from datasets.o3.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_alpha_and_numeric(self):
        input_data = [('a','1'), ('b','2.5')]
        expected = [('a',1.0), ('b',2.5)]
        self.assertEqual(list_to_float(input_data), expected)

    def test_negative_number(self):
        input_data = [('x','-4')]
        expected = [('x', -4.0)]
        self.assertEqual(list_to_float(input_data), expected)

    def test_multiple_numeric_types(self):
        input_data = [('c','3.14'),('d','1e3')]
        expected = [('c',3.14),('d',1000.0)]
        self.assertEqual(list_to_float(input_data), expected)

    def test_truncates_extra_elements(self):
        input_data = [('z','7','ignored')]
        expected = [('z',7.0)]
        self.assertEqual(list_to_float(input_data), expected)

    def test_all_numeric(self):
        input_data = [('1','2')]
        expected = [('1',2.0)]  # note: first element remains string '1'
        self.assertEqual(list_to_float(input_data), expected)

    def test_empty_list(self):
        self.assertEqual(list_to_float([]), [])

