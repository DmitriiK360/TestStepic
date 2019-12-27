from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class ProductPage(BasePage):

    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ADDED_TO_CART_MESSAGE = (By.XPATH, "//div[@class='alertinner ' and contains(text()[2], 'был добавлен в вашу корзину')]")

    def add_to_cart(self):
        element = self.find_element(self.BUTTON_ADD_TO_CART)
        element.click()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True