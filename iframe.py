from BrainBucketTests.webelements.browser import Browser
from BrainBucketTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
browser = Browser("https://cleveronly.com/practice/")
driver = browser.get_driver()
class IFrame:
    def __init__(self, browser):
        self.driver = browser.get_driver()
        self.iframe_element = Element(browser, By.TAG_NAME, 'iframe')
        self.logo = Element(browser, By.XPATH,"//*[@class='logo__title']")


    def switch_to_iframe(self):
        return self.driver.switch_to.frame(self.iframe_element.get_element())

    def switch_to_default_content(self):
        return self.driver.switch_to.default_content()

