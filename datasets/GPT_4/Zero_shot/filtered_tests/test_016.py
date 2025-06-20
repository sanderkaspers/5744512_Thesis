import unittest
from datasets.GPT_4.Zero_shot.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        expected_output = [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
        assert subject_marks(subjectmarks) == expected_output

    def test_multiple_spaces_2(self):
        subjectmarks = [('English', 85), ('Science', 85), ('Maths', 85)]
        expected_output = [('English', 85), ('Science', 85), ('Maths', 85)]
        assert subject_marks(subjectmarks) == expected_output

    def test_multiple_spaces_3(self):
        subjectmarks = [('English', 92)]
        expected_output = [('English', 92)]
        assert subject_marks(subjectmarks) == expected_output

    def test_multiple_spaces_4(self):
        subjectmarks = []
        expected_output = []
        assert subject_marks(subjectmarks) == expected_output

    def test_multiple_spaces_5(self):
        subjectmarks = [('English', 88.5), ('Science', 90), ('Maths', 97.3), ('Social sciences', 82)]
        expected_output = [('Social sciences', 82), ('English', 88.5), ('Science', 90), ('Maths', 97.3)]
        assert subject_marks(subjectmarks) == expected_output

    def test_multiple_spaces_6(self):
        subjectmarks = [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
        expected_output = [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
        assert subject_marks(subjectmarks) == expected_output

    def test_multiple_spaces_7(self):
        subjectmarks = [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]
        expected_output = [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
        assert subject_marks(subjectmarks) == expected_output

