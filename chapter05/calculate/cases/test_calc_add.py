import unittest
from parameterized import parameterized
from chapter05.calculate.bases.get_driver import GetDriver
from chapter05.calculate.pages.page_calc import PageCalc
from chapter05.calculate.tools.read_json import read_json


def get_data():
    datas = read_json("calc.json")
    print(datas)
    print(type(datas))
    arrs = []
    for data in datas.values():
        print(data)
        print(type(data))
        arrs.append((data['a'], data['b'], data['expect']))

    return arrs


class TestCalcAdd(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.calc = PageCalc(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_driver()

    def tearDown(self) -> None:
        self.calc.page_click_clear()

    @parameterized.expand(get_data())
    def test_calc_add(self, a, b, expect_result):
        self.calc.page_calc_add(a, b)
        result = self.calc.page_get_value()
        # 断言
        try:
            self.assertEqual(str(expect_result), result)
        except AssertionError:
            self.calc.base_get_image()
            raise

