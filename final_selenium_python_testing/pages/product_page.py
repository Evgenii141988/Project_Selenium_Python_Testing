from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)