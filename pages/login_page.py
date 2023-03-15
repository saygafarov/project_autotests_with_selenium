from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in LoginPageLocators.LOGIN_URL, "URL has not login"

    def should_be_login_form(self):
        assert LoginPageLocators.LOGIN_FORM, "Login form is not presented"

    def should_be_register_form(self):
        assert LoginPageLocators.REGISTR_FORM, "Registration form is not presented"