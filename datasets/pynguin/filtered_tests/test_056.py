import unittest
from datasets.pynguin.programs import program_056 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
        bytes_0 = b'\x82'
        bool_0 = True
        var_0 = module_0.odd_Equivalent(bytes_0, bool_0)
        assert var_0 == 0

