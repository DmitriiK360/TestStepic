import time
import pytest

from archive.pages.product_page import ProductPage

@pytest.mark.parametrize('offer', ["0","1","2","3","4","5","6","7","8","9"])
def test_login_mail(browser, offer):
    # link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link3 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"

    product_page = ProductPage(browser, link3)
    product_page.open()

    product_page.add_to_cart()
    #
    product_page.solve_quiz_and_get_code()
    time.sleep(10)