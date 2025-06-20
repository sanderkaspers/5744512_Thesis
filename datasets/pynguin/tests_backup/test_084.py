import unittest
import unittest
from datasets.pynguin.programs import program_084 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
            bytes_0 = b'\xeaW>\x00\xf9\xcf\xa0HQ\x07\xae"N\x06i'
            var_0 = module_0.max_Abs_Diff(bytes_0)
            assert var_0 == 249
    

