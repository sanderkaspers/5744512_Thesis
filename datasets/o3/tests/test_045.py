import unittest
from datasets.o3.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_basic_frequency(self):
        self.assertEqual(frequency_flattened([[1,2,2],[3]]), {1:1,2:2,3:1})

    def test_empty_inner_lists(self):
        self.assertEqual(frequency_flattened([[] , [1]]), {1:1})

    def test_all_empty(self):
        self.assertEqual(frequency_flattened([[],[]]), {})

    def test_strings(self):
        self.assertEqual(frequency_flattened([['a','b'],['a']]), {'a':2,'b':1})

    def test_nested_single_element(self):
        self.assertEqual(frequency_flattened([[42]]), {42:1})

    def test_mixed_types(self):
        self.assertEqual(frequency_flattened([[1,'1'],['1']]), {1:1,'1':2})

