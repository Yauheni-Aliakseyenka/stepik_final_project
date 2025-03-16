from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        product_link.click()

