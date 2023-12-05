
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='drivers/chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver.maximize_window()

# Wait for the logo to be visible
wd_wait = WebDriverWait(driver, 10)
logo = wd_wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//img[@title='Brainbucket']")
))

# Click on the "Continue" button with WebDriverWait
continue_button = wd_wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(text(), 'Continue')]")
))
continue_button.click()

# Wait for the "Register Account" title to be visible on the Registration page
register_account_title = wd_wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//h1[contains(text(), 'Register Account')]")
))

# Rest of the code for interacting with the Registration page
# ...

# Example: Interacting with the first name input field
firstname_input = wd_wait.until(EC.visibility_of_element_located(
    (By.ID, "input-firstname")
))
firstname_input.clear()
firstname_input.send_keys("Lana")

# Close the browser
driver.quit()
