#from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                 # открываем страницу
    page.add_to_basket()                # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    time.sleep(50)


    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()
    #login_page = page.go_to_login_page()
    #login_page.should_be_login_page()
