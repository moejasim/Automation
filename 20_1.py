from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
from BrainBucketTests.webelements.browser import Browser

from BrainBucketTests.webelements.UIElement import UIElement as Element

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

firstname_field = Element(browser, By.XPATH,"//fieldset/div[2]")
assert "required" in firstname_field.get_attribute("class")
Element(browser, By.ID, "input-firstname").enter_text("Moe")

#last name

lastname_field = Element(browser, By.XPATH, "//fieldset/div[3]")
assert "required" in lastname_field.get_attribute("class")
Element(browser, By.ID, "input-lastname").enter_text("Jasim")
#email

email_field = Element(browser, By.XPATH, "//fieldset/div[4]")
assert "required" in email_field.get_attribute("class")
Element(browser, By.ID, "input-email").enter_text("test@test.com")

#phone


telephone_field = Element(browser, By.XPATH, "//fieldset/div[5]")
assert "required" in telephone_field.get_attribute("class")
Element(browser, By.ID, "input-telephone").enter_text("00000000")

#FAX


fax_field = Element(browser, By.XPATH, "//fieldset/div[6]")
assert "required" not in fax_field.get_attribute("class")
Element(browser, By.ID, "input-fax").enter_text("00000000")

#company

company_field = Element(browser, By.XPATH, "//fieldset[2]/div[1]")
assert "required" not in company_field.get_attribute("class")
Element(browser, By.ID, "input-company").enter_text("tex company")

#address

address_1_field = Element(browser, By.XPATH, "//fieldset[2]/div[2]")
assert "required" in address_1_field.get_attribute("class")
Element(browser, By.ID, "input-address-1").enter_text("575 W madison st")

address_2_field = Element(browser, By.XPATH, "//fieldset[2]/div[3]")
assert "required" not in address_2_field.get_attribute("class")
Element(browser, By.ID, "input-address-2").enter_text("APT 4304")

city_field = Element(browser, By.XPATH, "//fieldset[2]/div[4]")
assert "required" in city_field.get_attribute("class")
Element(browser, By.ID, "input-city").enter_text("Chicago")

postcode_field = Element(browser, By.XPATH, "//fieldset[2]/div[5]")
assert "required" not in postcode_field.get_attribute("class")
Element(browser, By.ID, "input-postcode").enter_text("60661")

#password

password_field = Element(browser, By.XPATH, "//fieldset[2]/div[6]")
assert "required" in password_field.get_attribute("class")
Element(browser, By.ID, "input-password").enter_text("Password123")

confirm_field = Element(browser, By.XPATH, "//fieldset[2]/div[7]")
assert "required" in confirm_field.get_attribute("class")
Element(browser, By.ID, "input-confirm").enter_text("Password123")


#select country


country_dropdown = Element(browser, By.ID, "input-country").get_element()
country_dropdown_select = Select(country_dropdown)
country_dropdown_select.select_by_visible_text("United States")


# Selecting State from Region/State dropdown
state_dropdown= Element(browser, By.ID,"input-zone" ).get_element()
state_dropdown_select = Select(state_dropdown)
state_dropdown_select.select_by_visible_text("Illinois")



#subscribe to newsletter

subscribe_btn = Element(browser,By.XPATH, "//input[@name='newsletter' and @value='1']").get_element()
if not subscribe_btn.is_selected():
    subscribe_btn.click()
#privacy policy checkbox

privacy_policy_checkbox = Element(browser,By.XPATH, "//input[@name='agree' and @value='1']").get_element()
if not privacy_policy_checkbox.is_selected():
    privacy_policy_checkbox.click()

#click back on login
Element(browser,By.XPATH,"//a[@title='My Account']").click()
Element(browser,By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']").wait_until_visible()
Element(browser,By.XPATH,"//*[@class='dropdown-menu dropdown-menu-right']/li[2]").click()


shutdown = browser.shutdown()
