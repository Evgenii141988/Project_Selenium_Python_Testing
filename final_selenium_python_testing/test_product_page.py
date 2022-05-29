import pytest
from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    

if __name__ == '__main__':
    pytest.main()
