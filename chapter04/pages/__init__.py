from selenium.webdriver.common.by import By

login_link = (By.PARTIAL_LINK_TEXT, "登录")
login_username = (By.CSS_SELECTOR, "#keywords")
login_password = (By.CSS_SELECTOR, "#password")
login_btn = (By.CLASS_NAME, "login-btn")
login_err_info = (By.CSS_SELECTOR, "#err")
