from selenium.webdriver.common.by import By
from swlwnium import webdriver

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
	LOGIN_URL = webdriver.current_url
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTR_FORM = (By.CSS_SELECTOR, '#register_form')
