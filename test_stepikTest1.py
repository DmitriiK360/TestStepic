from selenium import webdriver
import time
import pytest

@pytest.fixture
def browser():
    print("\nStart driver for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    print("\nQuit driver..")
    driver.quit()


def test_test1(browser):
    link = "http://suninjuly.github.io/registration1.html"
    #browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    first_name = browser.find_element_by_xpath("//div[@class = 'first_block']//input[contains(@class, 'first')]")
    second_name = browser.find_element_by_xpath("//div[@class = 'first_block']//input[contains(@class, 'second')]")
    email = browser.find_element_by_xpath("//div[@class = 'first_block']//input[contains(@class, 'third')]")

    first_name.send_keys("First name")
    second_name.send_keys("Second name")
    email.send_keys("usernsme@usermail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    #self.assertEquals("Congratulations! You have successfully registered!", welcome_text)

def test_test2(browser):
    link = "http://suninjuly.github.io/registration2.html"
    #browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    first_name = browser.find_element_by_xpath("//div[@class = 'first_block']//input[contains(@class, 'first')]")
    second_name = browser.find_element_by_xpath("//div[@class = 'first_block']//input[contains(@class, 'second')]")
    email = browser.find_element_by_xpath("//div[@class = 'first_block']//input[contains(@class, 'third')]")

    first_name.send_keys("First name")
    second_name.send_keys("Second name")
    email.send_keys("usernsme@usermail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    #self.assertEquals("Congratulations! You have successfully registered!", welcome_text)