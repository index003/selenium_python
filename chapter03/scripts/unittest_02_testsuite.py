import unittest

from chapter03.scripts.unittest_01_testcase import Test01

suite = unittest.TestSuite()
# suite.addTest(Test01("test_add01"))
# suite.addTest(Test01("test_add02"))
suite.addTest(unittest.makeSuite(Test01))

runner = unittest.TextTestRunner()
runner.run(suite)
