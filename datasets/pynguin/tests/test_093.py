import unittest
import unittest
import unittest
from datasets.pynguin.programs import program_093 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
                str_0 = 'UH^-f$'
                list_0 = [str_0]
                var_0 = module_0.frequency(str_0, list_0)
                assert var_0 == 0
    
    
    
            def test_case_1(self):
                str_0 = 'fJzn3ZP\x0b|M{"%8DPF)'
                str_1 = 'B'
                list_0 = [str_0, str_1]
                str_2 = 'h?M&%:'
                set_0 = None
                var_0 = module_0.frequency(list_0, set_0)
                assert var_0 == 0
                bool_0 = False
                bytes_0 = b'\xd0\xc0`\x93\x00\x81G\xa7\x84:y\xab%\xfa\xd9'
                float_0 = -1264.1119
                str_3 = 'K\x0cYu6oNzE'
                bytes_1 = b'\xb2z|\xd5\x12\xfe\xba\xccad\xe1y\xa5\x9f=%\xc03'
                tuple_0 = float_0, str_3, bytes_1
                bool_1 = True
                tuple_1 = bool_0, bytes_0, tuple_0, bool_1
                str_4 = 'D'
                var_1 = module_0.frequency(tuple_1, str_4)
                assert var_1 == 0
                float_1 = None
                tuple_2 = list_0, str_2, set_0, float_1
                var_2 = module_0.frequency(tuple_2, set_0)
                assert var_2 == 2
                var_3 = module_0.frequency(str_0, str_1)
                assert var_3 == 0
    
    

