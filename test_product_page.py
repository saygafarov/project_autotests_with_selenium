from .pages.main_page import MainPage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_to_page()
	page.solve_quiz_and_get_code()
	page.go_to_basket_page()
	page.should_be_same_name_product_that_was_added_and_product_in_basket()
	page.should_be_same_price_product_and_price_in_basket()
