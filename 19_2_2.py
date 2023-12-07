from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.get("https://techskillacademy.net/brainbucket/index.php")

driver.maximize_window()

wd_wait = WebDriverWait(driver, 10) # creating a new object that can be reused in the script

logo = wd_wait.until(
    EC.visibility_of_element_located((By.XPATH, "//img[@title='Brainbucket']")))

#activating My Account dropdown
account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()

#Selecting Resgister from dropdown
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")))

register_option = driver.find_element_by_xpath("//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
register_option.click()

#Register Account
#Personal Details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Lana")

time.sleep(2)
#select country
country_dropdown = driver.find_element_by_id("input-country")
country_dropdown_select = Select(country_dropdown)
country_dropdown_select.select_by_index("30") # that will select Brazil

# Selecting State from Region/State dropdown
state_dropdown = driver.find_element_by_id("input-zone")
state_dropdown_select = Select(state_dropdown)
state_dropdown_select.select_by_visible_text("Illinois")

privacy_policy_checkbox = driver.find_element_by_xpath("//input[@name='agree' and @value='1']")
if not privacy_policy_checkbox.is_selected():
    privacy_policy_checkbox.click()
# Checking "I have read and agree to the Privacy Policy" checkbox
privacy_checkbox = driver.find_element_by_name("agree")
if not privacy_checkbox.is_selected():
    privacy_checkbox.click()
##subscribe to newsletter
subscribe_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='1']")
if not subscribe_btn.is_selected():
    subscribe_btn.click()

#Exercise #2
#Verify that you are able to land on the Registration form after selecting the ‘Register’ option.
wd_wait.until(EC.visibility_of_element_located(By.XPATH,"//*[@class='dropdown-menu dropdown-menu-right']")))

register_option = driver.find_element_by_xpath("//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
register_option.click()
# Selecting Login option
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")))
login_option = driver.find_element_by_xpath("//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
login_option.click()


time.sleep(5)
driver.quit()
