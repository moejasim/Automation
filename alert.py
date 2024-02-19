import time
from BrainBucketTests.webelements.browser import Browser
from BrainBucketTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
URL = "http://techskillacademy.net/practice/"

class Alert:
    def __init__(self, browser):
        self.driver = browser.get_driver()
        self.alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()']")
        self.confirm_brn = Element(browser, By.XPATH, "//button[@onclick='openConfirmationAlert()']")
        self.prompt_btn = Element(browser, By.XPATH, "//button[@onclick='openPrompt()']")
        self.msg = Element(browser, By.ID, 'msg')
        self.prompt_msg = Element(browser, By.ID, 'demo')
        time.sleep(3)

    def test_simple_alert(self):
        alert = self.driver.switch_to.alert
        self.alert_btn.click()
        time.sleep(2)
        alert.accept()
        time.sleep(2)

    def test_confirmation_alert(self):
        confirm_alert = self.driver.switch_to.alert
        self.confirm_brn.click()
        time.sleep(2)
        confirm_alert.dismiss()

        time.sleep(2)
        assert self.msg.get_text() == "You pressed CANCEL!"

        self.confirm_brn.click()
        confirm_alert.accept()

        assert self.msg.get_text() == "You pressed OK!"

    def test_prompt_alert(self):
        prompt_alert = self.driver.switch_to.alert
        self.prompt_btn.click()
        name = "MOE"

        time.sleep(2)
        prompt_alert.send_keys(name)

        prompt_alert.accept()
        msg = "Hello {}! How are you today?".format(name)
        assert self.prompt_msg.get_text() == msg
