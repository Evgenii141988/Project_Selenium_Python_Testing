from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_basket.click()

    def check_message_product_in_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert name_product.text == name_product_in_basket.text, 'Product name is not in basket'

    def check_message_product_price_in_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert price_product.text == price_product_in_basket.text, 'Product price is not in basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not disappeared"