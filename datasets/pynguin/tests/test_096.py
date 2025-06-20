import unittest
import unittest
import unittest
from datasets.pynguin.programs import program_096 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
                bytes_0 = b'\xeaW>\x00\xf9\xcf\xa0HQ\x07\xae"N\x06i'
                var_0 = module_0.count_occurance(bytes_0)
                assert var_0 == 0
    
    
    
            def test_case_1(self):
                dict_0 = {}
                var_0 = module_0.count_occurance(dict_0)
                assert var_0 == 0
    
    
    
            def test_case_2(self):
                str_0 = '6}s[bR{?&bqlR#0k>sR'
                var_0 = module_0.count_occurance(str_0)
                assert var_0 == 0
    
    
    
            def test_case_3(self):
                str_0 = 'niste\x0cQ64YkF4'
                var_0 = module_0.count_occurance(str_0)
                assert var_0 == 0
    
    

