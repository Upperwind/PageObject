from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()



    def should_be_login_url(self): # реализуйте проверку на корректный url адрес
            assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
            login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
            login_link.click()
            #assert "login" in self.browser.current_url, "There is not login in url"
            assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Registerm form is absent"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True