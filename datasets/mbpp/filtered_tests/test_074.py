import unittest
from datasets.mbpp.programs.program_074 import *

class TestVersion(unittest.TestCase):
    def test_tup_string_with__e_x_e_r_c_i_s_e_s__expect__exercises_(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), ("exercises"))

    def test_tup_string_with__p_y_t_h_o_n__expect__python_(self):
        self.assertEqual(tup_string(('p','y','t','h','o','n')), ("python"))

    def test_tup_string_with__p_r_o_g_r_a_m__expect__program_(self):
        self.assertEqual(tup_string(('p','r','o','g','r','a','m')), ("program"))

