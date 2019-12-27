from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is missing."

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def should_be_see_messages(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGES), "Messages is missing."

    def is_product_name_equals(self):
        actual = self.browser.find_elements(*ProductPageLocators.MESSAGES)[0].text
        expected = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert actual == expected, f"Product name in the message is wrong. Expected: {expected}, but actual: {actual}."

    def is_price_equals(self):
        actual = self.browser.find_elements(*ProductPageLocators.MESSAGES)[2].text
        expected = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert actual == expected, f"Price in the message is wrong. Expected: {expected}, but actual: {actual}."