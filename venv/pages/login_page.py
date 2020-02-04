from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        text = "login"
        assert text in url, f'Don\'t have a text \"{text}\" in url:{url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "We don\'t have email input in log in form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "We don\'t have password input in log in form"
        assert self.is_element_present(*LoginPageLocators.BUTTON_LOGIN), "We don\'t have Submit button in log in form"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_EMAIL), "We don\'t have email input in register form"
        assert self.is_element_present(*LoginPageLocators.REGISTR_PASS), "We don\'t have password input in register form"
        assert self.is_element_present(*LoginPageLocators.REGISTR_CONF_PASS), "We don\'t have confirm password input in register form"
        assert self.is_element_present(*LoginPageLocators.BUTTON_REGISTER), "We don\'t have Submit button input in register form"