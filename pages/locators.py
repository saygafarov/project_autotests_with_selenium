from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTR_FORM = (By.CSS_SELECTOR, '#register_form')

class BasketPageLocators():
	BOOK_NAME_ON_BASKET = (By.CSS_SELECTOR, 'h3 > a[href]')
	BOOK_PRICE_ON_BASKET = (By.CSS_SELECTOR, '.price_color.align-right')
	
class ProductPageLocators():
	ADD_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
	BASKET_BUTTON = (By.CSS_SELECTOR, 'span > a[href]')
	BOOK_NAME_ON_PAGE = (By.CSS_SELECTOR, 'div > h1')
	BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
	BOOK_NAME_ON_PAGE_ADDED_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong')
	BOOK_PRICE_ON_PAGE_ADDED_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong')
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner')

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

