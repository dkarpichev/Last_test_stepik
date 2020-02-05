from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_bsket (self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()
        assert True
    def assert_text(self):
        main_name = self.browser.find_element(*ProductPageLocators.PRODUCTS_NAME)
        message = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_MESSAGE)
        assert main_name.text in message.text, f'Don\'t have a text \"{main_name.text}\" in message:{message.text}'

    def is_message_present(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BENEFIT), "Meassage \"Deferred benefit offer\" is not presented"

    def compare_price (self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCTS_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert price.text == basket_price.text, f'Don\'t have a price = \"{price}\" in basket_price'

