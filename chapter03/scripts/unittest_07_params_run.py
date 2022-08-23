import unittest

from parameterized import parameterized


def add(x, y):
    return x + y


def get_data():
    return [(1, 2, 3), (2, 3, 5), (3, 4, 7)]


class Test01(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_add(self, a, b, expect):
        result = add(a, b)
        assert result == expect



