from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://user-p2p-test.itheima.net")
        self.driver.maximize_window()

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图
    def base_get_image(self):
        return self.driver.get_screenshot_as_file("../image/fail.png")
