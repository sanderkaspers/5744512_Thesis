import unittest
from datasets.mbpp.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_len_log_with__python___PHP___bigdata__expect_7(self):
        self.assertEqual(len_log(["python","PHP","bigdata"]), 7)

    def test_len_log_with__a___ab___abc__expect_3(self):
        self.assertEqual(len_log(["a","ab","abc"]), 3)

    def test_len_log_with__small___big___tall__expect_5(self):
        self.assertEqual(len_log(["small","big","tall"]), 5)

