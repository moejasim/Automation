from selenium import webdriver

driver = webdriver.Chrome(executable_path="../drivers/chromedriver")

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver.maximize_window()

logo = driver.find_element_by_xpath("//img['Brainbucket']")

new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(),'Continue')]")
new_registrant_btn.click()

# register_account
# firstname

firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("MOE")
# lastname

lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("JASIM")
# Email
email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("test.test.com")
# Telephone

telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("847-777-7777")

# fax
fax_field = driver.find_element_by_xpath("//fieldset/div[6]")
fax_field_class = fax_field.get_attribute("class")
assert "required" not in fax_field_class

fax_input = driver.find_element_by_id("input-fax")
fax_input.clear()
fax_input.send_keys("000-000-0001")