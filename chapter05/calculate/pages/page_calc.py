from selenium.webdriver.common.by import By

from chapter05.calculate.bases.base import Base
from chapter05.calculate import pages


class PageCalc(Base):

    def page_click_num(self, num):
        for n in str(num):
            loc = (By.CSS_SELECTOR, "#simple{}".format(n))
            self.base_click(loc)

    def page_click_add(self):
        self.base_click(pages.calc_add)

    def page_click_eq(self):
        self.base_click(pages.calc_eq)

    def page_get_value(self):
        return self.base_get_value(pages.calc_result)

    def page_click_clear(self):
        self.base_click(pages.calc_clear)

    def page_get_image(self):
        return self.base_get_image()

    def page_is_login_success(self):
        return self.base_element_exist(pages.calc_add)

    def page_calc_add(self, a, b):
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()
