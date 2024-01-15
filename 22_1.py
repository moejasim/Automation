from selenium.webdriver.common.by import By
import time

from BrainBucketTests.webelements.actions import Actions
from BrainBucketTests.webelements.UIElement import UIElement as Element
from BrainBucketTests.webelements.browser import Browser
from selenium.webdriver.support.color import Color
browser = Browser("https://cleveronly.com/practice/")
driver = browser.get_driver()
#Double click (verify that the background color is changed after performing double click)

yellow_btn = Element(browser, By.ID,"card")
yellow_btn.verify_color(color='rgb(255, 238, 153)')
dbl_click = Actions(browser)
dbl_click.double_click(element=yellow_btn)
yellow_btn.verify_color(color='rgb(255, 179, 128)')

#2Press enter in the input field (verify that the message "You pressed the key!" is displayed after you perform the action)

enter_field = Element(browser, By.XPATH,"//*[@id='key_practice']/input")
obj1 = Actions(browser)
obj1.click(element=enter_field)

obj1.send_keys(keys_to_send='\ue007')
hiden = Element(browser, By.ID,"hidden_text")
assert hiden.get_text() == "You pressed the key!"



pur_btn = Element(browser, By.ID,"context_menu")
rt_click = Actions(browser)
rt_click.right_click(element=pur_btn)
color_check = pur_btn.get_element().value_of_css_property("background-color")
converted_color = Color.from_string(color_check)
assert converted_color.rgba == "rgba(204, 204, 255, 0.8)"

chng_clr_btn = Element(browser, By.XPATH, "/html/body/div/ul/li[1]")
clr_btn_click = Actions(browser)
clr_btn_click.click(element=chng_clr_btn)
pur_btn.verify_color(color='rgb(204, 255, 245)')

chng_fnt_btn = Element(browser, By.XPATH, '//*[text()="Change Font"]')
fnt_btn = Actions(browser)
fnt_btn.click(element=chng_fnt_btn)
assert "bold" in chng_fnt_btn.get_attribute(attribute="style")


lnk_click = Element(browser, By.XPATH,"/html/body/div/ul/li[3]/a")
lnk_btn = Actions(browser)
lnk_btn.click(element=lnk_click)

close_tap = Actions(browser)
close_tap.send_keys(keys_to_send='\ue00c')




sorce_target = Element(browser,By.ID,"droplogo123")
drag_target = Element(browser,By.ID,"drag1")
drag_drop = Actions(browser)
drag_drop.drag_and_drop(source=drag_target,target=sorce_target)





