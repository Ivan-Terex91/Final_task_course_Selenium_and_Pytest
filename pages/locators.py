from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group >a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_IN_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_PRICE_IN_PAGE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')


class BasketPageLocators:
    BASKET_PAGE_HEADER = (By.CSS_SELECTOR, '.page-header h1')
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner >p')
