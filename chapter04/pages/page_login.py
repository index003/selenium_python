from chapter04.bases.base import Base
from chapter04 import pages


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(pages.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(pages.login_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(pages.login_password, password)

    # 点击确认按钮
    def page_click_login_btn(self):
        self.base_click(pages.login_btn)

    # 获取登录提示信息
    def page_get_error_info(self):
        return self.base_get_text(pages.login_err_info)

    # 截图
    def page_get_screenshot(self):
        self.base_get_image()

    # 组合业务方法
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
