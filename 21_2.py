from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from BrainBucketTests.webelements.browser import Browser
from BrainBucketTests.pages.login_page import LoginPage
from BrainBucketTests.pages.registration_page import RegistrationPage
from BrainBucketTests.webelements.UIElement import UIElement as Element
from BrainBucketTests.webelements.dropdown import Dropdown
from BrainBucketTests.webelements.Radiobutton import Radiobutton
#opening the website
browser = Browser("https://cleveronly.com/brainbucket/")
driver = browser.get_driver()


#checking if logo is visible
Element(browser,By.XPATH,"//img[@title='Brainbucket']").wait_until_visible()


#activating My Account dropdown and Selecting Register from dropdown
Element(browser, By.XPATH,"//a[@title='My Account']").click()
Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']").wait_until_visible()
Element(browser, By.XPATH,"//*[@class='dropdown-menu dropdown-menu-right']/li[1]").click()


#Personal Details
#first name
registration_page = RegistrationPage(browser)
registration_page.enter_first_name("Moe")
registration_page.enter_last_name("Jasim")
registration_page.enter_email("test@test.com")
registration_page.enter_telephone("00000000")
registration_page.enter_fax("00000000")
registration_page.enter_company("tex company")
registration_page.enter_first_line_address("575 W madison st")
registration_page.enter_city("Chicago")
registration_page.enter_postcode("60661")
registration_page.enter_password("Password123")
registration_page.confirm_password("Password123")

# Select country and state
registration_page.select_country("United States")
registration_page.select_state("Illinois")

# Subscribe to newsletter and agree to privacy policy
registration_page.subscribe_to_newsletters()
registration_page.agree_to_privacy_policy()

#click back on login
Element(browser,By.XPATH,"//a[@title='My Account']").click()

Element(browser,By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']").wait_until_visible()
Element(browser,By.XPATH,"//*[@class='dropdown-menu dropdown-menu-right']/li[2]").click()
login_page = LoginPage(browser)
login_page.enter_field("test@test.com","Password123")
login_page.click_login_button()
