import unittest
import unittest
from datasets.pynguin.programs import program_070 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
            bool_0 = False
            str_0 = 'wTR+,HMT5K~\nOK'
            var_0 = module_0.long_words(bool_0, str_0)
            assert var_0 == ['wTR+,HMT5K~\nOK']
    

