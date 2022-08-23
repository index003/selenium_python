import unittest


def setUpModule():
    print("setUpModule() is running ...")


def tearDownModule():
    print("tearDownModule() is running ...")


class Test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass() is running ...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass() is running ...")

    def setUp(self) -> None:
        print("setUp() is running ...")

    def tearDown(self) -> None:
        print("tearDown() is running ...")

    def test01(self):
        print("test01 is running ...")

    def test02(self):
        print("test02 is running ...")


class Test02(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass() is running ...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass() is running ...")

    def setUp(self) -> None:
        print("setUp() is running ...")

    def tearDown(self) -> None:
        print("tearDown() is running ...")

    def test01(self):
        print("test01 is running ...")

    def test02(self):
        print("test02 is running ...")
