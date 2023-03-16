from .base_page import BasePage
from .locators import BasketPageLocators

class ProductPage(BasePage):

	def go_to_basket_page(self):
		basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
		self.browser.implicitly_wait(1)
		basket_button.click()

	def should_be_add_to_page(self):
		add_to_basket_button = self.browser.find_element(*BasketPageLocators.ADD_TO_BUTTON)
		add_to_basket_button.click()

	def should_be_return_product_name_on_page(self):
		return self.browser.find_element(*BasketPageLocators.BOOK_NAME_ON_PAGE).text

	def should_be_return_product_price_on_page(self):
		return self.browser.find_element(*BasketPageLocators.BOOK_PRICE_ON_PAGE).text

	def should_be_same_product_name_in_basket_and(self, book_name_on_page):
		book_name_on_basket = self.browser.find_element(*BasketPageLocators.BOOK_NAME_ON_BASKET).text
		assert book_name_on_page == book_name_on_basket, "Book name on page is different book name on basket"

	def should_be_same_product_price_in_basket_and(self, book_price_on_page):
		book_price_on_basket = self.browser.find_element(*BasketPageLocators.BOOK_PRICE_ON_BASKET).text
		assert book_price_on_page == book_price_on_basket, "Book price on page is different book price on basket"