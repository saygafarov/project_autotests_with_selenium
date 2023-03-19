from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_not_be_product_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ON_BASKET),\
			"Product in basket, but should not be"

	def should_be_basket_is_empty(self):
		empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
		assert "Ваша корзина пуста Продолжить покупки" == empty_basket_message, \
			"No empty basket message, but should be"