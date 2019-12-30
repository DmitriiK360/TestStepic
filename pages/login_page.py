from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Invalid Login page url."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_INPUT), "Username input is missing on the Login form."
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), "Password input is missing on the Login form."
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is missing on the Login form."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME_INPUT), "Username input is missing on the Registration form."
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT), "Password input is missing on the Registration form."
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_INPUT), "Confirm password input is missing on the Registration form."
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is missing on the Registration form."
