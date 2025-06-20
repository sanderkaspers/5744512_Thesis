import unittest
from datasets.pynguin.programs import program_004 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
        str_0 = "'CH\x0c,9O*{"
        var_0 = module_0.text_lowercase_underscore(str_0)
        assert var_0 is False
    
    

    def test_case_1(self):
        str_0 = 'fy_bg'
        var_0 = module_0.text_lowercase_underscore(str_0)
        assert var_0 is True

