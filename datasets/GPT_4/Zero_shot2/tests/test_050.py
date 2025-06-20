import unittest
from datasets.GPT_4.Zero_shot2.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_snake_1(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_snake_2(self):
        self.assertEqual(snake_to_camel('_hello_world'), '_HelloWorld')

    def test_snake_3(self):
        self.assertEqual(snake_to_camel('hello_world_'), 'HelloWorld_')

    def test_snake_4(self):
        self.assertEqual(snake_to_camel('hello__world'), 'Hello_World')

    def test_snake_5(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_snake_6(self):
        self.assertEqual(snake_to_camel('hello'), 'Hello')

    def test_snake_7(self):
        self.assertEqual(snake_to_camel('___'), '___')

    def test_snake_8(self):
        self.assertEqual(snake_to_camel('a1_b2'), 'A1B2')

    def test_snake_9(self):
        self.assertEqual(snake_to_camel('HELLO_WORLD'), 'HelloWorld')

    def test_snake_10(self):
        self.assertEqual(snake_to_camel('HeLLo_WorLD'), 'HelloWorld')

