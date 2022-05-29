import pytest
from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()


def test_guest_check_message_product_in_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.check_message_product_in_basket()
    product_page.check_message_product_price_in_basket()


if __name__ == '__main__':
    pytest.main()
