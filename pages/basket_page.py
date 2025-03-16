from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket have products"

    def should_be_empty_screen_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), \
            "Basket is not empty"


