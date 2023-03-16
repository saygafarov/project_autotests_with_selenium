from .pages.main_page import MainPage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open()

	book_name_on_page = page.should_be_return_product_name_on_page()
	book_price_on_page = page.should_be_return_product_price_on_page()

	page.should_be_add_to_page()
	page.solve_quiz_and_get_code()
	page.go_to_basket_page()
	page.should_be_same_product_name_in_basket_and(book_name_on_page)
	page.should_be_same_product_price_in_basket_and(book_price_on_page)
