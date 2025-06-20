import unittest
import unittest
from datasets.pynguin.programs import program_097 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
            bytes_0 = b'\xeaW>\x00\xf9\xcf\xa0HQ\x07\xae"N\x06i'
            var_0 = module_0.check_type(bytes_0)
            assert var_0 is True
    
    
    
        def test_case_1(self):
            dict_0 = {}
            var_0 = module_0.check_type(dict_0)
    
    
    
        def test_case_2(self):
            int_0 = 2951
            float_0 = -30.603
            str_0 = 'Q\tkR_+\n'
            dict_0 = {int_0: int_0, float_0: str_0, float_0: int_0, int_0: str_0}
            tuple_0 = float_0, str_0, dict_0
            str_1 = '\x0cB\\{Q/--yrD2yZMpm'
            tuple_1 = int_0, tuple_0, str_1, dict_0
            var_0 = module_0.check_type(tuple_1)
            assert var_0 is False
    

