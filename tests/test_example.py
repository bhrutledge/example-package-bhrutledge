import unittest

from example_pkg import example


class TestExample(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(example.add_one(5), 6)
