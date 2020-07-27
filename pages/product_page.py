from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket is not present"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_PAGE), "Product name is not presented"

    def should_to_be_right_success_message_product_name(self):
        product_name_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_PAGE).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name_in_page == product_name_in_message, "Product name in page != Product name in message"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_PAGE), "Product price is not presented"

    def should_to_be_right_success_message_product_price(self):
        product_price_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_PAGE).text
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert product_price_in_page == product_price_in_message, "Product price in page != Product price in message"
