import unittest

FLAG = 30


# @unittest.skip("skip Test01")
class Test01(unittest.TestCase):

    # @unittest.skip("skip test01")
    def test_01(self):
        print("test01 is running ...")

    def test_02(self):
        print("test02 is running ...")

    @unittest.skipIf(FLAG > 25, "skip test03")
    def test_03(self):
        print("test03 is running ...")
