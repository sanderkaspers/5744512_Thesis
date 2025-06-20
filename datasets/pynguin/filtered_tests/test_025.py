import unittest
from datasets.pynguin.programs import program_025 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
        str_0 = 'UH^-f$'
        list_0 = [str_0]
        var_0 = module_0.is_samepatterns(str_0, list_0)
        assert var_0 is False
    
    

    def test_case_1(self):
        set_0 = set()
        str_0 = 'Fp?Ob6?'
        var_0 = module_0.is_samepatterns(set_0, str_0)
        assert var_0 is False
        str_1 = '382sW'
        str_2 = 'l5\\!'
        var_1 = module_0.is_samepatterns(str_1, str_2)
        assert var_1 is False
        str_3 = '{Z~7~\x0bE\tJeB\\I>L'
        str_4 = '\tiT-RY%UZj<+T.D'
        var_2 = module_0.is_samepatterns(str_3, str_4)
        assert var_2 is False
    
    

    def test_case_2(self):
        set_0 = set()
        bytes_0 = b'\xda\xaa\xd0\xea\xa5n\xca\xff\xa8\xa8\xd4\x83'
        int_0 = -400
        list_0 = [bytes_0, int_0, bytes_0]
        tuple_0 = bytes_0, bytes_0, int_0, list_0
        var_0 = module_0.is_samepatterns(tuple_0, set_0)
        assert var_0 is False
        str_0 = 'Fp?Ob6?'
        var_1 = module_0.is_samepatterns(set_0, str_0)
        assert var_1 is False
        str_1 = '382sW'
        str_2 = 'l5\\!'
        var_2 = module_0.is_samepatterns(str_1, str_2)
        assert var_2 is False
        var_3 = module_0.is_samepatterns(set_0, set_0)
        assert var_3 is True
        var_4 = module_0.is_samepatterns(list_0, list_0)
        assert var_4 is True

