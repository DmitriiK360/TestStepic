import time
import pytest
from archive.pages.product_page import ProductPage

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_to_cart()
    #time.sleep(5)
    assert product_page.is_not_element_present(*product_page.ADDED_TO_CART_MESSAGE)
    #time.sleep(2)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    #time.sleep(5)
    assert product_page.is_not_element_present(*product_page.ADDED_TO_CART_MESSAGE)

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    #time.sleep(5)
    assert product_page.is_disappeared(*product_page.ADDED_TO_CART_MESSAGE)