from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.page_links import PageLinks
import pytest
import time

@pytest.mark.user_registr
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = PageLinks.MAIN_PAGE
		page = MainPage(browser, link)
		page.open()
		page.go_to_login_page()
		email = str(time.time()) + '@fakemail.org'
		password = email
		login_page = LoginPage(browser, browser.current_url)
		login_page.regist_new_user(email, password)
		browser.implicitly_wait(10)
		login_page.should_be_authorized_user()

	def test_user_cant_see_success_message(self, browser):
		link = PageLinks.PRODUCT_PAGE_CODERS_AT_WORK
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()
		page.should_be_add_to_page()
		page.solve_quiz_and_get_code()
		page.should_be_same_product_name_on_main_page()
		page.should_be_same_product_price_on_main_page()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()
	page.should_be_add_to_page()
	page.solve_quiz_and_get_code()
	page.should_be_same_product_name_on_main_page()
	page.should_be_same_product_price_on_main_page()

@pytest.mark.xfail(reason="guest can see message")	
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = PageLinks.PRODUCT_PAGE_CODERS_AT_WORK
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_to_page()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	link = PageLinks.PRODUCT_PAGE_CODERS_AT_WORK
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.xfail(reason="message don't disappeared")	
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = PageLinks.PRODUCT_PAGE_CODERS_AT_WORK
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_to_page()
	page.should_be_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
	link = PageLinks.PRODUCT_PAGE_CITY_AND_STARS
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = PageLinks.PRODUCT_PAGE_CITY_AND_STARS
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = PageLinks.MAIN_PAGE
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket_page()
	page.should_not_be_product_in_basket()
	page.should_be_basket_is_empty()
