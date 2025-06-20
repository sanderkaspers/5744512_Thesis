import unittest
from datasets.mbpp.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_bell_number_with_2_expect_2(self):
        self.assertEqual(bell_number(2), 2)

    def test_bell_number_with_10_expect_115975(self):
        self.assertEqual(bell_number(10), 115975)

    def test_bell_number_with_56_expect_677568532064582432258148306837141974597905321626(self):
        self.assertEqual(bell_number(56), 6775685320645824322581483068371419745979053216268760300)

