from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "add_product_button is absent"
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()

        #return LoginPage(browser=self.browser, url=self.browser.current_url)

