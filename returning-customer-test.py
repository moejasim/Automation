from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/moejasim/PycharmProjects/pythonProject/drivers/chromedriver')

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver.maximize_window()


email_input = driver.find_element_by_xpath("//input[@name='email']")
email_input.send_keys("your_email@example.com")

password_input = driver.find_element_by_xpath("//input[@name='password']")
password_input.send_keys("123456789")

new_registrant_btn = driver.find_element_by_xpath("//input[contains(text(),'Login')]")
new_registrant_btn.click()