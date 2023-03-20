from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTR_FORM = (By.CSS_SELECTOR, '#register_form')
	EMAIL_FORM = (By.CSS_SELECTOR, '[name=registration-email]')
	PASSWORD_FORM_FIRST = (By.CSS_SELECTOR, '[name=registration-password1]')
	PASSWORD_FORM_SECOND = (By.CSS_SELECTOR, '[name=registration-password2]')
	BUTTON_REGISTR = (By.CSS_SELECTOR, '[name=registration_submit]')

class BasketPageLocators():
	BOOK_NAME_ON_BASKET = (By.CSS_SELECTOR, 'h3 > a[href]')
	BOOK_PRICE_ON_BASKET = (By.CSS_SELECTOR, '.price_color.align-right')
	PRODUCT_ON_BASKET = (By.CSS_SELECTOR, '.basket_summary')
	EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner :first-child')
	BASKET_BUTTON = (By.CSS_SELECTOR, 'span > a[href]')
	
class ProductPageLocators():
	ADD_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
	BOOK_NAME_ON_PAGE = (By.CSS_SELECTOR, 'div > h1')
	BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
	BOOK_NAME_ON_PAGE_ADDED_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong')
	BOOK_PRICE_ON_PAGE_ADDED_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong')
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner')

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
	USER_ICON = (By.CSS_SELECTOR, '.icon-user')

