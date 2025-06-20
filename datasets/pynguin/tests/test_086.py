import unittest
import unittest
import unittest
from datasets.pynguin.programs import program_086 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
                str_0 = 'UH^-f$'
                list_0 = [str_0]
                var_0 = module_0.remove_elements(str_0, list_0)
                assert var_0 == ['U', 'H', '^', '-', 'f', '$']
    
    

