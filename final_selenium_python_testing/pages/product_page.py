from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_basket.click()