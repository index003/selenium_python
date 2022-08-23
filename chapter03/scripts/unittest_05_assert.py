import unittest


class Test01(unittest.TestCase):
    def test_01(self):

        # flag = False
        # flag = True
        #
        # self.assertTrue(flag)
        # self.assertFalse(flag)

        origin_str = "ell"
        object_str = "hello"

        self.assertEqual(origin_str, object_str)
        # self.assertIn(origin_str, object_str)

        # content = None
        # self.assertIsNone(content)
        # self.assertIsNotNone(content)
