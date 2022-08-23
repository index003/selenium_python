import unittest


def add(x, y):
    return x + y


class Test01(unittest.TestCase):

    def test_add01(self):
        test_result = add(1, 1)
        print("result = ", test_result)

    def test_add02(self):
        test_result = add(1, 2)
        print("result = ", test_result)

    def test_add03(self):
        test_result = add(1, 3)
        print("result = ", test_result)

# if __name__ == '__main__':
#     unittest.main()
