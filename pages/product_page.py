from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def should_be_add_to_page(self):
		add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
		add_to_basket_button.click()

	def should_be_return_product_name_on_page(self):
		return self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_PAGE).text

	def should_be_return_product_price_on_page(self):
		return self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE).text

	def should_be_same_product_name_in_basket_and(self, book_name_on_page):
		book_name_on_basket = self.browser.find_element(*BasketPageLocators.BOOK_NAME_ON_BASKET).text
		assert book_name_on_page == book_name_on_basket, \
			"Book name on page is different book name on basket"

	def should_be_same_product_price_in_basket_and(self, book_price_on_page):
		book_price_on_basket = self.browser.find_element(*BasketPageLocators.BOOK_PRICE_ON_BASKET).text
		assert book_price_on_page == book_price_on_basket, \
			"Book price on page is different book price on basket"

	def should_be_same_product_name_on_main_page(self):
		book_name_on_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_PAGE).text
		book_name_on_page_added_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_PAGE_ADDED_IN_BASKET).text
		current_url = self.browser.current_url
		assert book_name_on_page == book_name_on_page_added_in_basket, \
			f"Book name on page is different book name on basket{current_url}"

	def should_be_same_product_price_on_main_page(self):
		book_price_on_page = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE).text
		book_price_on_page_added_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE_ADDED_IN_BASKET).text
		current_url = self.browser.current_url
		assert book_price_on_page == book_price_on_page_added_in_basket, \
			f"Book price on page is different book price on basket{current_url}"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
			"Success message is presented, but should not be"

	def should_be_disappeared_message(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should be disappeared"