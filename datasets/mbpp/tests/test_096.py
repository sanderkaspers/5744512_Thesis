import unittest
from datasets.mbpp.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_count_occurance_with__letstdlenstdporstd__expect_3(self):
        self.assertEqual(count_occurance("letstdlenstdporstd"), 3)

    def test_count_occurance_with__truststdsolensporsd__expect_1(self):
        self.assertEqual(count_occurance("truststdsolensporsd"), 1)

    def test_count_occurance_with__makestdsostdworthit__expect_2(self):
        self.assertEqual(count_occurance("makestdsostdworthit"), 2)

