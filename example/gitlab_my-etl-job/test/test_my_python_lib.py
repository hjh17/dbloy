from unittest import TestCase

from my_python_lib import main_function


class TestFlaskApi(TestCase):

    def test_add(self):
        res = main_function.add(1, 2)
        self.assertEqual(3, res)
