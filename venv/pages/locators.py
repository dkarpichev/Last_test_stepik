from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password')
    REGISTR_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTR_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTR_CONF_PASS = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '#login_form .btn')
    BUTTON_REGISTER = (By.CSS_SELECTOR, '#register_form .btn')
    SEARCH_AREF = (By.CSS_SELECTOR, '#id_q')