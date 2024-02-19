from BrainBucketTests.webelements.browser import Browser

from BrainBucketTests.alert_practice.alert import Alert
from BrainBucketTests.alert_practice.iframe import IFrame

browser = Browser("https://cleveronly.com/practice/")
driver = browser.get_driver()


test_simple = Alert(browser)
test_simple.test_simple_alert()

test_confirm = Alert(browser)
test_confirm.test_confirmation_alert()

test_prompt = Alert(browser)
test_prompt.test_prompt_alert()

switch_to_iframe_test = IFrame(browser)
switch_to_iframe_test.switch_to_iframe()

switch_to_default_content_test = IFrame(browser)
switch_to_default_content_test.switch_to_iframe()




