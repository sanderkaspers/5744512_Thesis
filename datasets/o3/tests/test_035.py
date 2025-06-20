import unittest
from datasets.o3.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_merge_no_overlap(self):
        d1={'a':1}; d2={'b':2}; d3={'c':3}
        expected={'a':1,'b':2,'c':3}
        self.assertEqual(merge_dictionaries_three(d1,d2,d3), expected)

    def test_merge_overlap_precedence(self):
        d1={'a':1}; d2={'a':2}; d3={'a':3}
        self.assertEqual(merge_dictionaries_three(d1,d2,d3)['a'], 1)

    def test_merge_partial_overlap(self):
        d1={'a':1}; d2={'b':2}; d3={'a':3}
        merged=merge_dictionaries_three(d1,d2,d3)
        self.assertEqual(merged['a'],1)
        self.assertEqual(merged['b'],2)

    def test_merge_empty_dicts(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_merge_mutation_safe(self):
        d1={'a':1}; d2={'b':2}; d3={}
        merged=merge_dictionaries_three(d1,d2,d3)
        d1['c']=3
        self.assertNotIn('c', merged)

