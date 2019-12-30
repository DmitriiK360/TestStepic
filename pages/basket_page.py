from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "Item is presented, but should not be"

    def should_see_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message should be presented"