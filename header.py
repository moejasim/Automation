from BrainBucketTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Header:
    def __init__(self, browser):
        self.my_account_btn = Element(browser, By.XPATH, "//a[@title='My Account']")
        self.my_acccount_dropdown = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")
        self.register_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
        self.login_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
        self.wish_list_btn = Element(browser, By.ID, "wishlist-total")
        self.shopping_list_btn = Element(browser, By.XPATH, "//a[@title='Shopping Cart']")
        self.checkout_btn = Element(browser, By.XPATH, "//a[@title='Checkout']")
        self.currency_btn = Element(browser, By.ID, "form-currency")
        self.logo = Element(browser, By.ID, "logo")
        self.search = Element(browser, By.NAME, "search")
        self.currency_btn_dropdown = Element(browser, By.XPATH,"//form[@id='form-currency']/div/ul")
        self.currency_euro = Element(browser, By.NAME, "EUR")
        self.currency_pound = Element(browser, By.NAME, "GBP")
        self.currency_dollar = Element(browser, By.NAME, "USD")
        self.search_btn = Element(browser, By.XPATH, "//*[@class='input-group-btn']")


    def verify_logo_is_visible(self):
        return self.logo.wait_until_visible()

    def open_registration_form(self):
        self.my_account_btn.click()
        self.my_acccount_dropdown.wait_until_visible()
        self.register_btn.click()

    def open_login_page(self):
        self.my_account_btn.click()
        self.my_acccount_dropdown.wait_until_visible()
        self.login_btn.click()

    def change_currency(self, new_currency):
        self.currency_btn.click()
        self.currency_btn_dropdown.wait_until_visible()

        if new_currency == "ERO":
            self.currency_euro.click()
        elif new_currency == "GBP":
            self.currency_pound.click()
        else:
            self.currency_dollar.click()

    def open_wishlist(self):
        self.wish_list_btn.click()
        self.wish_list_btn.wait_until_visible()
        self.wish_list_btn.click()

    def search_for(self, word):
        self.search.enter_text(word)
        self.search_btn.click()
