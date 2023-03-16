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

	def should_be_same_name_product_that_was_added_and_product_in_basket(self):
		book_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME_ON_BASKET).text
		assert "The shellcoder's handbook" == book_name, "Book name on page is different book name on basket"

	def should_be_same_price_product_and_price_in_basket(self):
		book_price = self.browser.find_element(*BasketPageLocators.BOOK_PRICE_ON_BASKET).text
		assert "£9.99" == book_price, "Book price on page is different book price on basket"