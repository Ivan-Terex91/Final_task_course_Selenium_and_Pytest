from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket url is not present"

    def should_be_basket_page_header(self):
        assert "Корзина" == self.browser.find_element(
            *BasketPageLocators.BASKET_PAGE_HEADER).text, "Basket header is not present"

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Items is present"

    def should_be_basket_empty_message(self):
        message_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert "Ваша корзина пуста" in message_in_basket, "Should not basket empty message"

