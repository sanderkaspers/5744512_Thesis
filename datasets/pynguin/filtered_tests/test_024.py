import unittest
from datasets.pynguin.programs import program_024 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
        int_0 = 854
        bool_0 = True
        var_0 = module_0.dif_Square(bool_0)
        assert var_0 is True
        var_1 = module_0.dif_Square(int_0)
        assert var_1 is False

