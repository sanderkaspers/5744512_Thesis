import unittest
import unittest
from datasets.pynguin.programs import program_058 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
            str_0 = '+lvZ`'
            var_0 = module_0.check_integer(str_0)
            assert var_0 is False
    
    
    
        def test_case_1(self):
            str_0 = 'cznbqX'
            var_0 = module_0.check_integer(str_0)
            assert var_0 is False
    

