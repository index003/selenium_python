import unittest

from parameterized import parameterized


def get_data():
    return [(1, 2, 3), (2, 3, 5), (3, 4, 7)]


class Test01(unittest.TestCase):
    # @parameterized.expand(['1', '2', '3'])
    # def test_add_one(self, num):
    #     print(num)

    # @parameterized.expand([(1, 2, 3), (2, 3, 5), (3, 4, 7)])
    # def test_add_one(self, a, b, result):
    #     print("{} + {} = {}".format(a, b, result))

    # data = [(1, 2, 3), (2, 3, 5), (3, 4, 7)]
    #
    # @parameterized.expand(data)
    # def test_add_one(self, a, b, result):
    #     print("{} + {} = {}".format(a, b, result))

    @parameterized.expand(get_data())
    def test_add_one(self, a, b, result):
        print("{} + {} = {}".format(a, b, result))
