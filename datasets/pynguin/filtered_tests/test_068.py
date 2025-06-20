import unittest
from datasets.pynguin.programs import program_068 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
        bool_0 = True
        var_0 = module_0.sum(bool_0, bool_0)
        assert var_0 == 0
    
    

    def test_case_1(self):
        float_0 = 598.57
        int_0 = 120
        var_0 = module_0.sum(float_0, int_0)
        assert var_0 == 0

