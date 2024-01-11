from BrainBucketTests.components.header import Header
from BrainBucketTests.components.right_menu import RightMenu
from BrainBucketTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.email_input = Element(browser, By.XPATH, "//input[@name='email']")
        self.password_input = Element(browser, By.XPATH, "//input[@name='password']")
        self.login_btn = Element(browser, By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/input")
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def enter_field(self, email, password):
        self.email_input.enter_text(email)
        self.password_input.enter_text(password)

    def click_login_button(self):
        self.login_btn.click()

    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()
