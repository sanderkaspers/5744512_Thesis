import unittest
import unittest
from datasets.pynguin.programs import program_050 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
            str_0 = 'Yt-'
            var_0 = module_0.snake_to_camel(str_0)
            assert var_0 == 'Yt-'
    

