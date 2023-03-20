from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def regist_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email_form.send_keys(email)
        password_form_first = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_FIRST)
        password_form_first.send_keys(password)
        password_form_second = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_SECOND)
        password_form_second.send_keys(password)
        button_regist = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTR)
        button_regist.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL has not login"

    def should_be_login_form(self):
        assert LoginPageLocators.LOGIN_FORM, "Login form is not presented"

    def should_be_register_form(self):
        assert LoginPageLocators.REGISTR_FORM, "Registration form is not presented"