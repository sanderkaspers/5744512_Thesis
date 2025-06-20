import unittest
import unittest
import unittest
from datasets.pynguin.programs import program_020 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
                dict_0 = {}
                var_0 = module_0.is_Monotonic(dict_0)
                assert var_0 is True
    
    
    
            def test_case_1(self):
                bytes_0 = b'\xeaW>\x00\xf9\xcf\xa0HQ\x07\xae"N\x06i'
                var_0 = module_0.is_Monotonic(bytes_0)
    
    
    
            def test_case_2(self):
                bytes_0 = b'\xa7d%'
                var_0 = module_0.is_Monotonic(bytes_0)
                assert var_0 is True
                set_0 = {var_0, var_0, var_0}
                var_1 = module_0.is_Monotonic(set_0)
                assert var_1 is True
                set_1 = {var_0, var_0, var_0}
                var_2 = module_0.is_Monotonic(set_1)
                assert var_2 is True
    
    

