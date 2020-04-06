import unittest

import test


class TestTest(unittest.TestCase):

    def test_something(self):
        self.assertEqual(test.gcd(4, 2), 2)

