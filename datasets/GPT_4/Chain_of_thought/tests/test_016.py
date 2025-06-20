import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(subject_marks([('English', 88), ('Maths', 97), ('Science', 90)]), [('English', 88), ('Science', 90), ('Maths', 97)])

    def test_single_tuple(self):
        self.assertEqual(subject_marks([('English', 88)]), [('English', 88)])

    def test_all_identical_second_values(self):
        self.assertEqual(subject_marks([('English', 90), ('Maths', 90), ('Science', 90)]), [('English', 90), ('Maths', 90), ('Science', 90)])

    def test_negative_second_values(self):
        self.assertEqual(subject_marks([('English', -88), ('Maths', -97), ('Science', -90)]), [('Maths', -97), ('Science', -90), ('English', -88)])

    def test_mixed_positive_negative(self):
        self.assertEqual(subject_marks([('English', -88), ('Maths', 97), ('Science', 0)]), [('English', -88), ('Science', 0), ('Maths', 97)])

    def test_zero_second_value(self):
        self.assertEqual(subject_marks([('English', 0), ('Maths', 97), ('Science', 0)]), [('English', 0), ('Science', 0), ('Maths', 97)])

    def test_large_second_values(self):
        self.assertEqual(subject_marks([('English', 1000000), ('Maths', 5000000), ('Science', 100000)]), [('Science', 100000), ('English', 1000000), ('Maths', 5000000)])

    def test_small_second_values(self):
        self.assertEqual(subject_marks([('English', 0.0001), ('Maths', 0.0002), ('Science', 0.0003)]), [('English', 0.0001), ('Maths', 0.0002), ('Science', 0.0003)])

    def test_empty_list(self):
        self.assertEqual(subject_marks([]), [])

    def test_floating_point_second_values(self):
        self.assertEqual(subject_marks([('English', 88.5), ('Maths', 97.1), ('Science', 90.2)]), [('English', 88.5), ('Science', 90.2), ('Maths', 97.1)])

    def test_non_numeric_second_values(self):
        with self.assertRaises(TypeError):
            subject_marks([('English', 'A'), ('Maths', 'B'), ('Science', 'C')])

    def test_max_min_integers(self):
        self.assertEqual(subject_marks([('English', 2147483647), ('Maths', -2147483648), ('Science', 0)]), [('Maths', -2147483648), ('Science', 0), ('English', 2147483647)])

