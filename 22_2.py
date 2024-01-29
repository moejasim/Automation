from BrainBucketTests.pages.home_page import HomePage
from BrainBucketTests.webelements.browser import Browser
from BrainBucketTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

browser = Browser("https://cleveronly.com/brainbucket/")




def test_show_pcs():
    home_page = HomePage(browser)
    home_page.show_pcs()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()

    assert section_title == "PC" or section_title == "There are no products to list in this category."




def test_show_mac():
    home_page = HomePage(browser)
    home_page.show_mac_desktops()
    numbers_of_macs = home_page.get_numbers_of_macs_from_dropdown()
    numbers_of_des_products = home_page.get_numbers_of_products()
    assert numbers_of_macs == numbers_of_des_products

def test_windows_laptops():
    home_page = HomePage(browser)
    home_page.show_windows_laptops()
    message_text = home_page.get_no_product_message()
    assert message_text == "There are no products to list in this category."


def test_opening_all_desktops():
    home_page = HomePage(browser)
    home_page.show_all_desktops()
    message_text = home_page.get_no_product_message()
    assert message_text == "There are no products to list in this category."

    test_show_pcs()
    test_show_mac()
    test_opening_all_desktops()
    test_windows_laptops()
