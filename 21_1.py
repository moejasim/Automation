from BrainBucketTests.webelements.UIElement import UIElement as Element
from BrainBucketTests.webelements.browser import Browser
from BrainBucketTests.webelements.dropdown import Dropdown
from BrainBucketTests.webelements.Radiobutton import Radiobutton
from BrainBucketTests.components.header import Header
from selenium.webdriver.common.by import By
from BrainBucketTests.components.footer import Footer


#opening the website

browser = Browser("https://cleveronly.com/brainbucket/")
driver = browser.get_driver()


currency = Header(browser)
currency.change_currency(new_currency="GBP")

wishlist = Header(browser)
wishlist.wish_list_btn.click()

enter_text1 = Header(browser)
enter_text1.search_for(word='Hello')

aboutus = Footer(browser)
aboutus.about_us_btn.click()


