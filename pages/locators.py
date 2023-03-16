from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTR_FORM = (By.CSS_SELECTOR, '#register_form')

class BasketPageLocators():
	ADD_TO_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
	BASKET_BUTTON = (By.CSS_SELECTOR, 'span > a[href]')
	BOOK_NAME_ON_BASKET = (By.CSS_SELECTOR, 'h3 > a[href]')
	BOOK_PRICE_ON_BASKET = (By.CSS_SELECTOR, '.price_color.align-right')