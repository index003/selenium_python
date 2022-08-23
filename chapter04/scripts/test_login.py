import unittest
from parameterized import parameterized
from chapter04.pages.page_login import PageLogin


def get_data():
    return [("", "", "用户名或密码不能为空")]


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 实例化 获取页面对象 PageLogin
        self.login = PageLogin()
        # 点击登录链接
        self.login.page_click_login_link()

    def tearDown(self) -> None:
        # 关闭driver对象
        self.login.driver.quit()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, password, expect_result):
        # 调用登录方法
        self.login.page_login(username=username, password=password)

        # 获取登录提示信息
        msg = self.login.page_get_error_info()

        # 断言
        try:
            self.assertIn(expect_result, msg)
        except AssertionError:
            self.login.base_get_image()
            raise
