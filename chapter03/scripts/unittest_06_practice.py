import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    # 定义初始化方法
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://user-p2p-test.itheima.net")
        self.driver.maximize_window()
        self.driver.implicitly_wait(300)

    # 定义tearDown
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()

    # 测试方法
    def test_login_code_null(self):
        driver = self.driver
        driver.find_element(By.PARTIAL_LINK_TEXT, "登录").click()
        driver.find_element(By.CSS_SELECTOR, "#keywords").send_keys("")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("")
        driver.find_element(By.CLASS_NAME, "login-btn").click()
        result = driver.find_element(By.CSS_SELECTOR, "#err").text
        print(result)
        expect_result = "用户名或密码不能为空"
        # expect_result = "用户名或密码不能为空!"
        try:
            self.assertIn(expect_result, result)
        except AssertionError:
            driver.get_screenshot_as_file("../img/err.png")
            raise


