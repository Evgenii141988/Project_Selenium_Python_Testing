from final_selenium_python_testing.pages.base_page import BasePage
from final_selenium_python_testing.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'There are items in the basket'

    def should_basket_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), 'The basket is not empty'
