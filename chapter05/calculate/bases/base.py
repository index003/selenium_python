from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=0.5).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 获取结果
    def base_get_value(self, loc):
        return self.base_find_element(loc).get_attribute("value")

    # 截图
    def base_get_image(self):
        return self.driver.get_screenshot_as_file("../image/fail.png")

    # 判断元素是否找到
    def base_element_exist(self, loc):
        try:
            self.base_find_element(loc)
            return True
        except:
            return False
