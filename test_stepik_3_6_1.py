import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture
def browser():
    print("\nStart driver for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    print("\nQuit driver..")
    driver.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))

    answer = str(math.log(int(time.time())))

    browser.find_element_by_css_selector("textarea").send_keys(answer)

    time.sleep(1)
    browser.find_element_by_css_selector(".submit-submission").click()

    #time.sleep(2)
    message = browser.find_element_by_css_selector(".smart-hints__hint").text

    assert message == "Correct!", f"EXPECTED: 'Correct!' BUT ACTUAL: {message}"