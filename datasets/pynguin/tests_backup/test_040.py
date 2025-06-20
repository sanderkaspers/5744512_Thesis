import unittest
import unittest
from datasets.pynguin.programs import program_040 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
            dict_0 = {}
            var_0 = module_0.is_undulating(dict_0)
            assert var_0 is False
    
    
    
        def test_case_1(self):
            bytes_0 = b'\xeaW>\x00\xf9\xcf\xa0HQ\x07\xae"N\x06i'
            var_0 = module_0.is_undulating(bytes_0)
            assert var_0 is False
    
    
    
        def test_case_2(self):
            int_0 = 848
            bool_0 = True
            var_0 = module_0.is_undulating(bool_0)
            assert var_0 is False
            var_1 = module_0.is_undulating(int_0)
            assert var_1 is True
    

