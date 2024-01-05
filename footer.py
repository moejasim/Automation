from BrainBucketTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

class Footer:
    def __init__(self, browser):
        self.about_us_btn = Element(browser, By.XPATH,"/html/body/footer/div/div/div[1]/ul/li[1]/a")
        self.delivery_information_btn = Element(browser, By.XPATH,"/html/body/footer/div/div/div[1]/ul/li[2]/a")
        self.privacy_policy_btn = Element(browser, By.XPATH,"/html/body/footer/div/div/div[1]/ul/li[3]/a")
        self.contact_us_btn = Element(browser, By.XPATH,"/html/body/footer/div/div/div[2]/ul/li[1]/a")

    def click_about_us(self):
        self.about_us_btn.click()

    def click_delivery_information(self):
        self.delivery_information_btn.click()

    def click_privacy_policy(self):
        self.privacy_policy_btn.click()

    def click_contact_us(self):
        self.about_us_btn.click()